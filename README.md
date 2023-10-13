# Multi-repo Workspace
An alternative to monorepos for managing projects composed of multiple git repositories without using git submodules.

Mr. W also aims to provide a way to automatically configure a development environment for the project.

## Run
for python prerequisites see [setup-python-venv.md](setup-python-venv.md)
### Tests
```
pytest --cov-config .coveragerc  --cov-report term-missing --cov=main tests/
```
