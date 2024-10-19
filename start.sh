#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Print current directory
echo "Current directory: $(pwd)"

# Add the project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd)"

# Print updated Python path
echo "Updated PYTHONPATH: $PYTHONPATH"

# Print Poetry environment info
poetry env info

# Run the web_scraper CLI with quiet mode
cd web_scraper
echo "Running web_scraper CLI..."
poetry run python -m web_scraper.cli --quiet "$@"
