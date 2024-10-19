#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Print current directory
echo "Current directory: $(pwd)"

# Print Python path
echo "PYTHONPATH: $PYTHONPATH"

# Print Poetry environment info
poetry env info

# Run the web_scraper CLI with verbose Python
cd web_scraper
poetry run python -v -m web_scraper.cli "$@"
