# Cli Philosophy of mrw
The wish I have with this command-line interface tool is to have the ability to either get prompted for all the options and have mrw ask for required information, as well as being able to provide all the information through command arguments, options and flags for non-interactive usability.

A user should be able to enter `mrw` without anything else and be prompted with different options, for example:
```bash
mrw

Welcome to multi-repo workspace!
What do you want to do?
(a) List all workspaces
(b) Create a workspace
(x) Exit

# enter a
Select a workspace.
(digit) workspace_name directory
(1) project-one-workspace /home/max/c/
(2) super-thing-workspace /home/max/c/
(x) Back to multi-repo workspace

# enter x
Welcome to multi-repo workspace!
What do you want to do?
(a) List all workspaces
(b) Create a workspace
(x) Exit

# enter b
Creating new workspace
Enter a workspace name: new-project-workspace #entered by user
Where to create workspace directory 'new-project-workspace'? [.]: #default entered by user

Creating new workspace 'new-project-workspace' at /home/max/c/
Creating folder /home/max/c/new-project-workspace
Creating new-project-workspace/workspace.yml with content
    -------------------------------------------
    name: new-project-workspace
    -------------------------------------------

Workspace Created
What do you want to do?
(a) List all workspaces
(b) Create a workspace
(x) Exit

# enter x
```

The aspect of being able to "navigate" through what mrw has to offer should depend on the specificity of command arguments.
Are they all there? Are some left behind that should be prompted for? The vision is to be as user friendly as possible but also be able to be trusted when used from a script.
