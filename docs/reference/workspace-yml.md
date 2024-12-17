# Workspace
## Workspace properties
workspace.yml without repos
```(yml)
name: cool-project-workspace
```
workspace.yml with repos
```(yml)
name: cool-project-workspace

repos:
  - url: https://github.com/user/cool-project-frontend
    folder_name: frontend
    initial_branch: develop
  - url: https://github.com/user/cool-project-backend
    folder_name: backend
    initial_branch: develop

```
