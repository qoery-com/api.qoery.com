#!/bin/bash
set -e

# Release script for qoery packages
# Usage: ./release.sh [patch|minor|major|version]
# Examples:
#   ./release.sh patch     # 0.2.4 -> 0.2.5
#   ./release.sh minor     # 0.2.4 -> 0.3.0
#   ./release.sh major     # 0.2.4 -> 1.0.0
#   ./release.sh 0.2.5     # Set specific version

VERSION_TYPE=$1

if [ -z "$VERSION_TYPE" ]; then
    echo "Usage: ./release.sh [patch|minor|major|version]"
    echo ""
    echo "Examples:"
    echo "  ./release.sh patch     # 0.2.4 -> 0.2.5"
    echo "  ./release.sh minor     # 0.2.4 -> 0.3.0"
    echo "  ./release.sh major     # 0.2.4 -> 1.0.0"
    echo "  ./release.sh 0.2.5     # Set specific version"
    exit 1
fi

# Get current version
CURRENT_VERSION=$(grep -E 'VERSION.*=' sdks/python-sdk/setup.py | sed 's/.*"\(.*\)".*/\1/')
echo "Current version: $CURRENT_VERSION"

# Calculate new version
if [[ "$VERSION_TYPE" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    # Specific version provided
    NEW_VERSION=$VERSION_TYPE
else
    # Semantic versioning
    IFS='.' read -ra VERSION_PARTS <<< "$CURRENT_VERSION"
    MAJOR=${VERSION_PARTS[0]}
    MINOR=${VERSION_PARTS[1]}
    PATCH=${VERSION_PARTS[2]}
    
    case $VERSION_TYPE in
        patch)
            PATCH=$((PATCH + 1))
            ;;
        minor)
            MINOR=$((MINOR + 1))
            PATCH=0
            ;;
        major)
            MAJOR=$((MAJOR + 1))
            MINOR=0
            PATCH=0
            ;;
        *)
            echo "Invalid version type: $VERSION_TYPE"
            echo "Use: patch, minor, major, or a specific version like 0.2.5"
            exit 1
            ;;
    esac
    
    NEW_VERSION="$MAJOR.$MINOR.$PATCH"
fi

echo "New version: $NEW_VERSION"

# Confirm release
read -p "Do you want to release version $NEW_VERSION? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Release cancelled."
    exit 1
fi

# Update versions in both SDKs
echo "📝 Updating versions..."

# Update Python SDK version
sed -i.bak "s/VERSION = \"$CURRENT_VERSION\"/VERSION = \"$NEW_VERSION\"/" sdks/python-sdk/setup.py
rm sdks/python-sdk/setup.py.bak

# Update NPM version
cd sdks/js
npm version $NEW_VERSION --no-git-tag-version
cd ../..

# Update main API version
sed -i.bak "s/version: $CURRENT_VERSION/version: $NEW_VERSION/" api.yaml
rm api.yaml.bak

echo "✅ Versions updated to $NEW_VERSION"

# Commit changes
echo "📝 Committing changes..."
git add .
git commit -m "chore: bump version to $NEW_VERSION

- Updated Python SDK to $NEW_VERSION
- Updated NPM package to $NEW_VERSION  
- Updated API spec to $NEW_VERSION"

# Create and push tag
echo "🏷️  Creating tag v$NEW_VERSION..."
git tag "v$NEW_VERSION"
git push origin main
git push origin "v$NEW_VERSION"

echo ""
echo "🚀 Release $NEW_VERSION initiated!"
echo ""
echo "📋 What happens next:"
echo "1. GitHub Actions will automatically:"
echo "   - Build and publish NPM package"
echo "   - Build and publish PyPI package"
echo "   - Create GitHub release"
echo ""
echo "2. Monitor progress at:"
echo "   https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\([^/]*\/[^/]*\)\.git.*/\1/')/actions"
echo ""
echo "3. Packages will be available at:"
echo "   - NPM: https://www.npmjs.com/package/qoery"
echo "   - PyPI: https://pypi.org/project/qoery/"
echo ""
echo "✨ Happy releasing!"
