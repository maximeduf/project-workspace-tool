# Quick Start Guide
## With the CLI
**create workspace**
```
mrw create
```

**add a repository**
```
mrw repo add
```

**init the workspace** (clone repositories(for now))
```
mrw init
```

## With a workspace.yml file
Example with workspace name "project-workspace" and repos:
- "project-frontend"
- "project-backend"
- "project-e2e-tests"

**create workspace.yml**
```(yml)
name: project-workspace
repos:
  - folder_name: frontend
    remote_url: https://github.com/user/project-frontend.git
    initial_branch: develop
  - folder_name: backend
    remote_url: https://github.com/user/project-backend.git
    initial_branch: develop
  - folder_name: e2e-tests
    remote_url: https://github.com/user/project-e2e-tests.git
    initial_branch: develop

```
**run the init command**
```
mrw init
```

## Next
Read on the [concept of Workspace](../features/workspace.md)
Look at all [commands](../features/commands/command-index.md)
