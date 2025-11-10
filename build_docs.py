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
import yaml
import json
from pathlib import Path


def read_example_file(file_path):
    """Read content from an example file, preserving content exactly."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: Example file not found: {file_path}")
        return None


def resolve_refs_in_spec(spec, base_path):
    """Resolve $ref references in the OpenAPI spec."""
    import yaml
    
    def resolve_ref(obj, base_path):
        if isinstance(obj, dict):
            if '$ref' in obj:
                ref_path = obj['$ref']
                if ref_path.startswith('api/'):
                    # Load the referenced file
                    ref_file = base_path.parent / ref_path
                    if ref_file.exists():
                        try:
                            with open(ref_file, 'r', encoding='utf-8') as f:
                                ref_content = yaml.safe_load(f)
                            
                            # Navigate to the referenced part
                            parts = ref_path.split('#/')
                            if len(parts) > 1:
                                path_parts = parts[1].split('/')
                                for part in path_parts:
                                    if part and ref_content and part in ref_content:
                                        ref_content = ref_content[part]
                                    else:
                                        print(f"Warning: Could not resolve path {part} in {ref_path}")
                                        return obj  # Return original if path not found
                            
                            return ref_content
                        except Exception as e:
                            print(f"Warning: Error loading {ref_file}: {e}")
                            return obj
                else:
                    return obj  # Return original if not a local ref
            else:
                return {k: resolve_ref(v, base_path) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [resolve_ref(item, base_path) for item in obj]
        else:
            return obj
    
    return resolve_ref(spec, base_path)


def generate_markdown_docs(api_spec_path, examples_dir):
    """Generate markdown documentation from OpenAPI spec."""
    print("Generating markdown documentation...")
    
    # Load the OpenAPI spec
    with open(api_spec_path, 'r', encoding='utf-8') as f:
        spec = yaml.safe_load(f)
    
    # Resolve all $ref references to get complete path definitions
    # Load all path files from the temporary API directory
    temp_api_dir = api_spec_path.parent / 'api'
    
    # Load all path files
    all_paths = {}
    if temp_api_dir.exists():
        for path_file in temp_api_dir.glob('paths/*.yaml'):
            with open(path_file, 'r', encoding='utf-8') as f:
                path_spec = yaml.safe_load(f)
                if 'paths' in path_spec:
                    all_paths.update(path_spec['paths'])
    
    # Resolve $ref references from main spec
    resolved_paths = {}
    if 'paths' in spec:
        for path_key, path_value in spec['paths'].items():
            if isinstance(path_value, dict) and '$ref' not in path_value:
                # This is an inline path definition (like /v0/datasets/{job_id})
                resolved_paths[path_key] = path_value
            elif isinstance(path_value, dict) and '$ref' in path_value:
                # Try to resolve the reference
                ref_path = path_value['$ref']
                if ref_path.startswith('api/paths/'):
                    # Extract the file and path
                    parts = ref_path.split('#/')
                    if len(parts) > 1:
                        file_part = parts[0]
                        path_part = parts[1]
                        file_path = api_spec_path.parent / file_part
                        if file_path.exists():
                            with open(file_path, 'r', encoding='utf-8') as f:
                                ref_content = yaml.safe_load(f)
                                # Navigate to the referenced path
                                # path_part format: paths/~1v0~1datasets
                                path_parts = path_part.replace('~1', '/').split('/')
                                current = ref_content
                                for part in path_parts:
                                    if part and isinstance(current, dict) and part in current:
                                        current = current[part]
                                    else:
                                        current = None
                                        break
                                if current:
                                    resolved_paths[path_key] = current
                # Also check if it's already in all_paths
                if path_key not in resolved_paths and path_key in all_paths:
                    resolved_paths[path_key] = all_paths[path_key]
            else:
                # Direct path value
                resolved_paths[path_key] = path_value
    
    # Merge with paths from files
    for path_key, path_value in all_paths.items():
        if path_key not in resolved_paths:
            resolved_paths[path_key] = path_value
    
    # Replace the paths in the main spec with resolved paths
    if resolved_paths:
        spec['paths'] = resolved_paths
    
    markdown_parts = []
    
    # API Info
    info = spec.get('info', {})
    markdown_parts.append(f"# {info.get('title', 'API Documentation')}")
    markdown_parts.append(f"**Version:** {info.get('version', 'N/A')}")
    markdown_parts.append("")
    
    # Description
    if 'description' in info:
        markdown_parts.append(info['description'])
        markdown_parts.append("")
    
    # Contact info
    if 'contact' in info:
        contact = info['contact']
        markdown_parts.append("## Contact")
        if 'name' in contact:
            markdown_parts.append(f"**Name:** {contact['name']}")
        if 'email' in contact:
            markdown_parts.append(f"**Email:** {contact['email']}")
        if 'url' in contact:
            markdown_parts.append(f"**URL:** {contact['url']}")
        markdown_parts.append("")
    
    # Base URL
    if 'servers' in spec and spec['servers']:
        markdown_parts.append("## Base URL")
        markdown_parts.append(f"`{spec['servers'][0]['url']}`")
        markdown_parts.append("")
    
    # Authentication
    if 'security' in spec:
        markdown_parts.append("## Authentication")
        markdown_parts.append("All endpoints require API key authentication via the `X-API-Key` header.")
        markdown_parts.append("")
    
    # Tags/Endpoints
    if 'paths' in spec:
        markdown_parts.append("## Endpoints")
        markdown_parts.append("")
        
        # Group by tags
        endpoints_by_tag = {}
        for path, methods in spec['paths'].items():
            if isinstance(methods, dict):
                for method, details in methods.items():
                    if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
                        if isinstance(details, dict):
                            tags = details.get('tags', ['General'])
                            for tag in tags:
                                if tag not in endpoints_by_tag:
                                    endpoints_by_tag[tag] = []
                                endpoints_by_tag[tag].append((path, method.upper(), details))
                        else:
                            print(f"Warning: Details for {method} {path} is not a dict: {type(details)}")
            else:
                print(f"Warning: Methods for {path} is not a dict: {type(methods)}")
        
        # Process each tag
        for tag, endpoints in endpoints_by_tag.items():
            markdown_parts.append(f"### {tag}")
            markdown_parts.append("")
            
            for path, method, details in endpoints:
                # Endpoint header
                markdown_parts.append(f"#### {method} {path}")
                markdown_parts.append("")
                
                # Description
                if 'description' in details:
                    markdown_parts.append(details['description'])
                    markdown_parts.append("")
                
                # Request body
                if 'requestBody' in details:
                    markdown_parts.append("**Request Body:**")
                    markdown_parts.append("")
                    req_body = details['requestBody']
                    if 'description' in req_body:
                        markdown_parts.append(req_body['description'])
                        markdown_parts.append("")
                    
                    # Schema info
                    if 'content' in req_body and 'application/json' in req_body['content']:
                        schema = req_body['content']['application/json'].get('schema', {})
                        if '$ref' in schema:
                            ref_name = schema['$ref'].split('/')[-1]
                            markdown_parts.append(f"Schema: `{ref_name}`")
                        markdown_parts.append("")
                
                # Parameters
                if 'parameters' in details:
                    markdown_parts.append("**Parameters:**")
                    markdown_parts.append("")
                    for param in details['parameters']:
                        param_name = param.get('name', '')
                        param_type = param.get('schema', {}).get('type', 'string')
                        param_desc = param.get('description', '')
                        required = param.get('required', False)
                        req_text = " (required)" if required else ""
                        markdown_parts.append(f"- `{param_name}` ({param_type}){req_text}: {param_desc}")
                    markdown_parts.append("")
                
                # Code examples
                if 'x-codeSamples' in details:
                    markdown_parts.append("**Examples:**")
                    markdown_parts.append("")
                    
                    for example in details['x-codeSamples']:
                        lang = example.get('lang', '')
                        source = example.get('source', '')
                        
                        # Try to read from example files if source contains INJECT
                        if '# INJECT:' in source:
                            example_file = source.split('# INJECT:')[1].strip()
                            example_path = examples_dir / example_file
                            if example_path.exists():
                                with open(example_path, 'r', encoding='utf-8') as f:
                                    source = f.read()
                        
                        # Determine code block language
                        code_lang = lang.lower()
                        if code_lang == 'curl':
                            code_lang = 'bash'
                        elif code_lang == 'javascript':
                            code_lang = 'javascript'
                        elif code_lang == 'python':
                            code_lang = 'python'
                        
                        markdown_parts.append(f"**{lang}:**")
                        markdown_parts.append(f"```{code_lang}")
                        markdown_parts.append(source.strip())
                        markdown_parts.append("```")
                        markdown_parts.append("")
                
                # Responses
                if 'responses' in details:
                    markdown_parts.append("**Responses:**")
                    markdown_parts.append("")
                    for status_code, response in details['responses'].items():
                        desc = response.get('description', '')
                        markdown_parts.append(f"- `{status_code}`: {desc}")
                    markdown_parts.append("")
                
                markdown_parts.append("---")
                markdown_parts.append("")
    
    return '\n'.join(markdown_parts)


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


def inject_copy_button_into_html(html_file, markdown_content):
    """Inject the copy button and markdown content into the generated HTML."""
    print("Injecting copy button into HTML...")
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Escape the markdown content for JavaScript
    # Use json.dumps to properly escape the content
    escaped_markdown = json.dumps(markdown_content)
    
    # Create a simple copy button HTML
    copy_button_html = '''
    <button id="copy-for-llm-btn" style="
        background: #007bff;
        color: white;
        border: none;
        padding: 8px 16px;
        margin-left: 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    " onclick="copyToClipboard()">
        📋 Copy for LLMs
    </button>
    '''
    
    # JavaScript that waits for Redocly to finish rendering
    copy_script = f'''
    <script>
    function copyToClipboard() {{
        const markdownContent = {escaped_markdown};
        
        // Try modern clipboard API first
        if (navigator.clipboard && window.isSecureContext) {{
            navigator.clipboard.writeText(markdownContent).then(function() {{
                showCopySuccess();
            }}).catch(function() {{
                fallbackCopy(markdownContent);
            }});
        }} else {{
            fallbackCopy(markdownContent);
        }}
    }}
    
    function fallbackCopy(text) {{
        // Create a temporary textarea element
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        textArea.style.top = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        
        try {{
            const successful = document.execCommand('copy');
            if (successful) {{
                showCopySuccess();
            }} else {{
                showCopyError();
            }}
        }} catch (err) {{
            showCopyError();
        }}
        
        document.body.removeChild(textArea);
    }}
    
    function showCopySuccess() {{
        const button = document.getElementById('copy-for-llm-btn');
        if (button) {{
            const originalText = button.innerHTML;
            button.innerHTML = '✅ Copied!';
            button.style.backgroundColor = '#28a745';
            button.style.borderColor = '#28a745';
            button.style.color = 'white';
            
            setTimeout(function() {{
                button.innerHTML = originalText;
                button.style.backgroundColor = 'white';
                button.style.borderColor = '#007bff';
                button.style.color = '#007bff';
            }}, 2000);
        }}
    }}
    
    function showCopyError() {{
        const button = document.getElementById('copy-for-llm-btn');
        if (button) {{
            const originalText = button.innerHTML;
            button.innerHTML = '❌ Failed';
            button.style.backgroundColor = '#dc3545';
            button.style.borderColor = '#dc3545';
            button.style.color = 'white';
            
            setTimeout(function() {{
                button.innerHTML = originalText;
                button.style.backgroundColor = 'white';
                button.style.borderColor = '#007bff';
                button.style.color = '#007bff';
            }}, 2000);
        }}
    }}
    
    // Wait for Redocly to finish rendering, then add the button
    function addCopyButton() {{
        const title = document.querySelector('h1');
        if (title && !document.getElementById('copy-for-llm-btn')) {{
            const button = document.createElement('button');
            button.id = 'copy-for-llm-btn';
            button.innerHTML = '📋 Copy for LLMs';
            button.style.cssText = `
                background: white;
                color: #007bff;
                border: 1px solid #007bff;
                padding: 6px 12px;
                margin-left: 15px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 13px;
                font-weight: 500;
                transition: all 0.2s ease;
                display: inline-block;
                vertical-align: middle;
            `;
            button.onclick = copyToClipboard;
            
            // Add hover effect
            button.onmouseover = function() {{
                this.style.backgroundColor = '#007bff';
                this.style.color = 'white';
            }};
            button.onmouseout = function() {{
                this.style.backgroundColor = 'white';
                this.style.color = '#007bff';
            }};
            
            // Make the title container display inline so the button appears on the same line
            title.style.display = 'inline-block';
            title.style.marginRight = '15px';
            
            // Insert right after the title, on the same line
            title.parentNode.insertBefore(button, title.nextSibling);
        }}
    }}
    
    // Try to add the button after Redocly loads
    document.addEventListener('DOMContentLoaded', function() {{
        setTimeout(addCopyButton, 1000);
    }});
    
    // Also try when the page is fully loaded
    window.addEventListener('load', function() {{
        setTimeout(addCopyButton, 500);
    }});
    </script>
    '''
    
    # No need to inject static button - we'll add it dynamically with JavaScript
    
    # Add the JavaScript at the end
    if '</body>' in html_content:
        html_content = html_content.replace('</body>', copy_script + '</body>')
    else:
        html_content += copy_script
    
    # Write the modified HTML back to the file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✓ Copy button injected successfully")


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
            
            # Generate markdown documentation
            markdown_content = generate_markdown_docs(temp_api_file, examples_dir)
            
            # Run Redocly to generate documentation
            success = run_redocly_build(temp_api_file, output_file)
            
            if success:
                # Inject the copy button into the generated HTML
                inject_copy_button_into_html(output_file, markdown_content)
                print(f"\n✓ Build complete! Documentation generated: {output_file}")
                print("✓ Copy for LLMs button added to documentation")
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
