#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Run the web_scraper CLI
poetry run python -m web_scraper.cli "$@"
