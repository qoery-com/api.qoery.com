#!/bin/bash

# Generate Python SDK with consistent settings
openapi-generator-cli generate \
  -i api.yaml \
  -g python \
  -o ./sdks/python-sdk \
  --package-name qoery \
  --package-description "qoery's Python SDK" \
  --package-url "https://github.com/qoery/python-sdk" \
  --package-company "qoery" \
  --package-authors "qoery team"

echo "SDK generated successfully!"

# Generate JavaScript SDK with consistent settings
openapi-generator-cli generate \
  -i api.yaml \
  -g javascript \
  -o ./sdks/js \
  --additional-properties npmName=qoery,projectName=qoery

echo "JS SDK generated successfully!"
