# multi-repo-workspace (mrw)
`mrw` is a tool for managing multiple Git repositories in one workspace. It uses `workspace.yml` to define repository configurations, allowing developers to clone and manage all repos with a single command. New contributors can start quickly by cloning the workspace and running mrw apply."

## Docs
For full documentation see [mrw documentation](https://github.com/maximeduf/multi-repo-workspace/blob/master/docs/README.md)

## Prerequisites
for python prerequisites see [installation documentation](https://github.com/maximeduf/multi-repo-workspace/blob/master/docs/development/installation.md).

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

## Usage
for usage, look at [quick-start.md](https://github.com/maximeduf/multi-repo-workspace/blob/master/docs/getting-started/quick-start.md).

