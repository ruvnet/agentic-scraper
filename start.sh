#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Add the project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd)"

# Run the web_scraper CLI with quiet mode
cd web_scraper
poetry run python cli.py --quiet "$@"
