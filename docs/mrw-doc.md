# Multi-repo Workspace (mrw)
An alternative to monorepos for managing projects composed of multiple git repositories without using git submodules.
This also aims to provide a way to automatically configure a development environment for the project.
For more info, see the Vision section below.

## Prerequisites
for python prerequisites see [setup-python-venv.md](setup-python-venv.md)
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

## What is done

### commands
- default -> prints `cli init`
### Configs
Config objects modeled:
- AliasConfig
- FunctionConfig
- VarConfig

## Vision
A workspace is effectively a github repository that is the starting point to get up and running on a project.
The main definition is in a yaml file that at least has a list of repositories.

Different ways to handle this is
- begin with a yaml file, use the cli to do the rest
- use the cli to do everything
- either way, use a non-interactive (with commmand arguments) or interactive approach (prompts to get the information)
### Priority
Priority is on **yaml first** and **interactive** approach to create a workspace that can **clone all repositories in one go**, with **only git repository configurations**. Some other configurations are already modeled, but they are not critical for this project to be useful.
### Ultimate goal
The ultimate goal is to be able to have :
- other configurations, like aliases, functions or environment variables, available system wide.
- install dependencies by providing commands to execute after repository cloning
- ensure other configurations, for example a etc/hosts line, presence of environment variables or any other requirement for development of a project.
- have the ability to use yaml first or cli first and interactive or non-interactive.

This was thought with linux in mind but being compatible with windows would be best.

## Brainstormed ideas for interactive workspace creation
### from default
- begin create new worksapce, or
- begin list workspaces to select and go from there
```
mrw
 - create new workspace [x]
 - list workspaces
```
### create workspace use case
```
mrw workspace create
```
Questions for new workspace
- enter a workspace name (ie: mrw. will create workspace folder "mrw-workspace" at path location)
- enter path location for new workspace (default: here)
- add configuration? (Y|n) (repeat until no) (**use case**)
print summary
- all good? (Y|n)
... creating workspace 
... initialising git repository
... creating name-workspace.yml
... done
- apply configurations? (**use case**)

### add workspace configuration use case (incomplete)
```
mrw config add
- from path
- from name
- from list
```
Questions for configuration
