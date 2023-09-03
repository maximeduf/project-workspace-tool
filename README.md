# Multi Repo Workspace (mrw) 
This is mainly work in progress.


## Run
for python prerequisites see [setup-python-venv.md](setup-python-venv.md)
### Cli
```
python -m main
```
### Tests
```
pytest --cov-config .coveragerc  --cov-report term-missing --cov=main tests/
```

## Vision
The multi-repo workspace tool will help
- manage projects composed of multiple git repositories in a single workspace 
- provide a way to automatically configure a development environment for the project

### About Workspaces
Workspaces are configurable and can be initialized with a config file or command line arguments.
