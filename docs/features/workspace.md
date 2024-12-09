# Workspace
A workspace is a folder version controlled that contains a workspace.yml file that define the workspace.

When a developer wants to work on a project with mrw, they clone the workspace repo, install mrw and run `mrw apply` to get all the repositories listed cloned.

Later on, workspaces will have more functionality to add other requirements to be automated from a workspace definition.

The workspace folder is where the folders of the repositories listed in workspace.yml live. These folders are ignored in the workspace's repository

## Creating workspaces
With mrw installed, we can create a workspace with the command `mrw create` to get prompted for the workspace-name and location. The workspace folder and file are created and the git repository initialized.

Without prompt

**TODO: ask if mrw should initialize a git repository?**
**TODO: also ask for git init options like initial-branch, branch-name, if they want to give a remote**

The result is a bare bones workspace, from which we can continue to use mrw commands or edit the workspace definition file.

### Bare bone workspace
```
# workspace.yml
name: workspace
```

### Add a repository
`mrw` does not *create* repositories (at least not now), it adds existing repository to be cloned from a remote url.
To add a repository **to be cloned from an existing remote url**, use, without arguments, the command `mrw repo add` to get prompted for the remote url and, optionaly (default suggested), a pretty_folder_name for the repository.
