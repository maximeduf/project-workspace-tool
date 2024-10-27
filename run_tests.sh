#!/bin/bash

# Function to check if the virtual environment is activated
function check_venv() {
    if [[ -z "$VIRTUAL_ENV" ]]; then
        echo "Virtual environment is not activated. Please activate it before running the tests."
        echo "For full information, see docs/setup-python-venv.md"
        exit 1
    fi
}

# Check and activate virtual environment if needed
check_venv

# Set PYTHONPATH and run tests
export PYTHONPATH=src
pytest --cov-config .coveragerc --cov-report term-missing --cov=multi_repo_workspace tests
