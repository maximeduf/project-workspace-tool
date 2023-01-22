Greatly inspired by https://github.com/AnthonyBloomer/python-cli-template

# create python virtual environment
python3 -m venv .venv

# source environment 
source .venv/bin/activate

# install requirements.txt
pip install -r requirements.txt

# run tests
python tests/tests.py

# run app
as a module: python -m cli -h
directly: python cli/cli.py -h

# TODO: 
- write script to 
    - verify (is python installed, which version, look for existing aliases)
    - setup (install python itself, create venv, install dependencies) and 
    - execute python cli
- todo


