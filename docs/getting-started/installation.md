# Install multi-repo-workspace 
For development, look further down.

## Python, pip and dependencies
`sudo apt-get install build-essential`
`sudo add-apt-repository ppa:deadsnakes/ppa`
`sudo apt-get install python3.13`
`sudo apt-get install python3.13-dev`
**Installs PIP globally**
`curl https://bootstrap.pypa.io/get-pip.py | python3.13`

## Install multi-repo-workspace
`pip install multi-repo-workspace`

## Use mrw
`mrw -v`

## Next
See [Quick Start Guide](quick-start.md).

# Install for development
## Python, pip and dependencies
`sudo add-apt-repository ppa:deadsnakes/ppa`
`sudo apt-get install python3.13`
`sudo apt-get install python3.13-dev`
`sudo apt-get install build-essential`
`sudo apt-get install python3.13-venv`
**Installs PIP globally**
`curl https://bootstrap.pypa.io/get-pip.py | python3.13`

## Virtual environment

### creates a virtualenv
`python3.13 -m venv venv`

### activates the virtualenv
`source venv/bin/activate`
**to deactivate**
`deactivate`

## Install multi-repo-workspace
in venv activated, editable install of the code with testing dependencies
`python -m pip install -e ."[test]"`

## Use mrw
`mrw -v`

## Next
See [Quick Start Guide](quick-start.md).
See [Contributing](../development/contributing.md).
