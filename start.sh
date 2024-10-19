#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Run the web scraper with provided command line arguments
poetry run web-scraper "$@"
