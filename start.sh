#!/bin/bash

# start.sh

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Run the FastAPI web scraper
poetry run uvicorn fastapi.main:app --reload
