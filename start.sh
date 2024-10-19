#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Run the web scraper with all provided arguments
poetry run web-scraper "$@"
