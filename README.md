# Multi-repo Workspace (mrw)
An alternative to monorepos for managing projects composed of multiple git repositories without using git submodules.

This also aims to provide a way to automatically configure a development environment for the project.

## Prerequisites
for python prerequisites see [setup-python-venv.md](https://github.com/maximeduf/multi-repo-workspace/blob/master/docs/setup-python-venv.md)

## Install and Run for development
in venv activated
```
python -m pip install -e ."[test]"
```

### CLI
```
mrw
```

### Tests
```
PYTHONPATH=src pytest --cov-config .coveragerc --cov-report term-missing --cov=multi_repo_workspace tests
```
or
```
./run_tests.sh
```

## Docs
for documentation see [mrw documentation](https://github.com/maximeduf/multi-repo-workspace/blob/master/docs/mrw-doc.md)
