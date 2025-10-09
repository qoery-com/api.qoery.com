#!/usr/bin/env python3
"""
Build script to generate API documentation using temporary files.
This script:
1. Creates temporary files with injected examples
2. Runs Redocly to generate docs.html
3. Cleans up temporary files
"""

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


def read_example_file(file_path):
    """Read content from an example file, preserving content exactly."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: Example file not found: {file_path}")
        return None


def inject_examples_into_yaml(yaml_content, examples_dir):
    """Inject example files into YAML content."""
    
    # Pattern to match individual source lines with INJECT comments
    pattern = r'(\s*source:\s*#\s*INJECT:\s*([^\s]+))'
    
    def replace_source_line(match):
        indent = match.group(1).split('source:')[0]  # Get the indentation
        example_file = match.group(2)  # Get the example file path
        
        example_path = os.path.join(examples_dir, example_file)
        example_content = read_example_file(example_path)
        
        if example_content:
            # Normalize only line endings (CRLF/CR -> LF) during temp build
            # Preserve per-line EOLs to avoid introducing extra blank lines in renderers
            normalized = example_content.replace('\r\n', '\n').replace('\r', '\n')
            # If the example starts with a leading newline, drop just one to avoid
            # rendering an empty first line in the code block.
            if normalized.startswith('\n'):
                normalized = normalized[1:]
            # Always use strip-final-newline chomping to avoid a trailing blank line
            chomp = '|-'
            new_source = f"{indent}source: {chomp}\n"
            for line in normalized.splitlines(False):
                new_source += f"{indent}  {line}"
            return new_source
        else:
            # If file not found, return the original line
            return match.group(1)
    
    return re.sub(pattern, replace_source_line, yaml_content)


def strip_request_bodies(yaml_content):
    """Remove requestBody sections to hide the auto-generated Payload tab in docs.

    Works line-by-line to remove the block starting at a line equal to
    "requestBody:" and all following lines that are more indented than that
    line. Operates only on temporary files during docs build.
    """
    lines = yaml_content.splitlines(True)  # keep line endings
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^([ \t]*)requestBody:\s*\n?$', line)
        if m:
            indent = m.group(1)
            i += 1
            # Consume all lines that are more indented than the requestBody line
            while i < len(lines):
                nxt = lines[i]
                # A more-indented line must start with indent + space or indent + tab
                if nxt.startswith(indent + ' ') or nxt.startswith(indent + '\t'):
                    i += 1
                    continue
                break
            # Skip adding any of the requestBody block
            continue
        else:
            result_lines.append(line)
            i += 1
    return ''.join(result_lines)

def create_temp_api_files(api_dir, examples_dir, temp_dir):
    """Create temporary API files with injected examples."""
    print("Creating temporary API files with injected examples...")
    
    # Create temporary directory structure
    temp_api_dir = temp_dir / 'api'
    temp_paths_dir = temp_api_dir / 'paths'
    temp_schemas_dir = temp_api_dir / 'schemas'
    temp_responses_dir = temp_api_dir / 'responses'
    
    temp_paths_dir.mkdir(parents=True)
    temp_schemas_dir.mkdir(parents=True)
    temp_responses_dir.mkdir(parents=True)
    
    # Copy schemas and responses (no changes needed)
    shutil.copy2(api_dir.parent / 'schemas' / 'schemas.yaml', temp_schemas_dir)
    shutil.copy2(api_dir.parent / 'responses' / 'responses.yaml', temp_responses_dir)
    
    # Process API files and inject examples
    for api_file in api_dir.glob('*.yaml'):
        print(f"  Processing {api_file.name}...")
        
        with open(api_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has placeholder comments
        if '# INJECT:' not in content:
            print(f"    No injection placeholders found in {api_file.name}")
            # Just copy the file as-is
            shutil.copy2(api_file, temp_paths_dir)
            continue
        
        # Inject examples
        new_content = inject_examples_into_yaml(content, examples_dir)

        # Strip request bodies to avoid showing the auto-generated "Payload" tab
        # in the built documentation. We only do this for the temporary build.
        new_content = strip_request_bodies(new_content)
        
        # Write to temporary file
        temp_file = temp_paths_dir / api_file.name
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"    ✓ Examples injected into {api_file.name}")
    
    return temp_api_dir


def create_temp_main_api_file(script_dir, temp_dir):
    """Create temporary main api.yaml file."""
    print("Creating temporary main API file...")
    
    # Read the original api.yaml
    with open(script_dir / 'api.yaml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Write to temporary location
    temp_api_file = temp_dir / 'api.yaml'
    with open(temp_api_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return temp_api_file


def run_redocly_build(temp_api_file, output_file):
    """Run Redocly to generate documentation.

    Resolution order for the CLI:
    1) REDOCLY_BIN env var if provided
    2) Local ./node_modules/.bin/redocly
    3) Global `redocly` on PATH
    4) npx -y @redocly/cli build-docs ... (last resort)

    A timeout is applied to avoid hanging builds.
    """
    print(f"Running Redocly to generate {output_file}...")

    script_dir = Path(__file__).parent
    timeout_seconds = int(os.getenv('REDOCLY_TIMEOUT_SECONDS', '240'))

    # 1) Explicit override
    redocly_bin = os.getenv('REDOCLY_BIN')
    if redocly_bin:
        candidates = [[redocly_bin, 'build-docs']]
    else:
        # 2) Local bin
        local_bin = script_dir / 'node_modules' / '.bin' / 'redocly'
        candidates = []
        if local_bin.exists():
            candidates.append([str(local_bin), 'build-docs'])
        # 3) Global on PATH
        candidates.append(['redocly', 'build-docs'])
        # 4) npx fallback
        candidates.append(['npx', '-y', '@redocly/cli', 'build-docs'])

    last_error = None
    for base_cmd in candidates:
        cmd = base_cmd + [str(temp_api_file), '--output', str(output_file)]
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=timeout_seconds,
            )
            print(f"✓ Documentation generated successfully: {output_file}")
            return True
        except subprocess.TimeoutExpired:
            print(f"Error: Redocly command timed out after {timeout_seconds}s: {' '.join(base_cmd)}")
            last_error = 'timeout'
        except FileNotFoundError:
            # try next candidate
            last_error = 'not found'
        except subprocess.CalledProcessError as e:
            print(f"Redocly failed with exit code {e.returncode} using: {' '.join(base_cmd)}")
            if e.stdout:
                print(f"stdout:\n{e.stdout}")
            if e.stderr:
                print(f"stderr:\n{e.stderr}")
            last_error = 'failed'

    if last_error == 'not found':
        print("Error: Redocly not found. Try: npm i -g @redocly/cli or use npx -y @redocly/cli")
    return False


def main():
    """Main build function."""
    script_dir = Path(__file__).parent
    api_dir = script_dir / 'api' / 'paths'
    examples_dir = script_dir / 'examples'
    output_file = script_dir / 'index.html'
    
    print("Building API documentation with temporary files...")
    print(f"API directory: {api_dir}")
    print(f"Examples directory: {examples_dir}")
    print(f"Output file: {output_file}")
    
    # Create temporary directory (persist if KEEP_TEMP=1)
    keep_temp = os.getenv('KEEP_TEMP') == '1'
    if keep_temp:
        temp_dir = Path(tempfile.mkdtemp(prefix='qoery-docs-'))
        temp_ctx = None
    else:
        temp_ctx = tempfile.TemporaryDirectory()
        temp_dir = Path(temp_ctx.name)
    print(f"Using temporary directory: {temp_dir}")

    try:
            # Create temporary API files with injected examples
            temp_api_dir = create_temp_api_files(api_dir, examples_dir, temp_dir)
            
            # Create temporary main API file
            temp_api_file = create_temp_main_api_file(script_dir, temp_dir)
            
            # Run Redocly to generate documentation
            success = run_redocly_build(temp_api_file, output_file)
            
            if success:
                print(f"\n✓ Build complete! Documentation generated: {output_file}")
            else:
                print("\n✗ Build failed!")
                return 1
                
    except Exception as e:
        print(f"Error during build: {e}")
        return 1
    finally:
        if not keep_temp and temp_ctx is not None:
            temp_ctx.cleanup()
        else:
            print(f"Temporary files kept at: {temp_dir}")

    return 0


if __name__ == '__main__':
    exit(main())
