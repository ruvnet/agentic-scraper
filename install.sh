#!/bin/bash

# install.sh

# Check if Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found, installing now..."
    curl -sSL https://install.python-poetry.org | python3 -
else
    echo "Poetry is already installed."
fi

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Install FastAPI project dependencies
echo "Installing FastAPI project dependencies..."
cd fastapi
poetry install
cd ..

# Install Web Scraper CLI project dependencies
echo "Installing Web Scraper CLI project dependencies..."
cd web_scraper
poetry install

# Install Playwright browsers
echo "Installing Playwright browsers..."
poetry run playwright install chromium

cd ..

echo "Installation complete!"
