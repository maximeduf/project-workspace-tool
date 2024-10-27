# Multi-repo Workspace (mrw)
An alternative to monorepos for managing projects composed of multiple git repositories without using git submodules.

This also aims to provide a way to automatically configure a development environment for the project.

## Run
for python prerequisites see [setup-python-venv.md](setup-python-venv.md)

### CLI
```
python -m main
```

### Tests
```
pytest --cov-config .coveragerc  --cov-report term-missing --cov=main tests/
```

## Docs
for documentation see [mrw documentation](mrw-doc.md)
