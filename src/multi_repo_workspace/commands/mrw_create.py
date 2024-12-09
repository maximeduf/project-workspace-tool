import click
from multi_repo_workspace.model.use_case import UseCase
import os

from multi_repo_workspace.model.workspace import Workspace
from pathlib import Path


class ProgramArguments:
    """
    ProgramArguments will have arguments passed from command line
    """

    def __init__(self, workspace_name: str, workspace_path: Path):
        self.workspace_name = workspace_name
        self.workspace_path = workspace_path


class MrwCreate(UseCase[ProgramArguments, None]):
    """
    MrwCreate is a use case that creates a new workspace.

    The 2 arguments are workspace_name and workspace_path. They are optional.
    If they are not provided, the user will be prompted to enter them.

    If the user enters a workspace name that is the same as an existing
    directory, the user will be prompted to confirm that they want to
    use that directory.
    """
    def __init__(self, params: ProgramArguments):
        super().__init__()
        self.params = params

    def __call__(self):
        workspace_name_arg: str = self.params.workspace_name
        workspace_path_arg: Path = self.params.workspace_path

        click.echo("Hello! inside the create use case")
        click.echo(f"workspace_name: {workspace_name_arg}")
        click.echo(f"directory: {workspace_path_arg}")

        # TODO: not be so quick and dirty, create some services for readablity
        # are the arguments valid?
        # begin with workspace_name

        path_confirmed = workspace_path_arg is not None
        name_confirmed = workspace_name_arg is not None
        if name_confirmed:
            workspace_name = workspace_name_arg
        if path_confirmed:
            workspace_path = workspace_path_arg

        click.echo(f"name_confirmed: {name_confirmed}")
        while not name_confirmed:
            if not workspace_name_arg:
                workspace_name = click.prompt("Enter workspace name", type=str)

                # are you sure you want to use workspace_name?
                name_confirmed = click.confirm(
                    f"Are you sure you want to use '{
                        workspace_name}' as workspace name?",
                    abort=False,
                )

        click.echo("name confirmed!")
        # ask for workspace path
        while not path_confirmed:
            if not workspace_path_arg:
                workspace_path = Path(click.prompt(
                    "Enter workspace path",
                    type=click.Path(exists=False, dir_okay=True,
                                    file_okay=False),
                    default=".",
                    show_default=True,
                    prompt_suffix=": ",
                ))
                click.echo(f"workspace_path: {
                           str(workspace_path.absolute()).split("/")[-1]}")
                if (workspace_path.is_dir() and
                        str(workspace_path.absolute()).split("/")[-1] ==
                        workspace_name):
                    workspace_path = Path(workspace_path)
                    click.echo(
                        "workspace_path is a directory with"
                        "the same name as workspace_name")
                else:
                    workspace_path = Path(workspace_path, workspace_name)
                    click.echo(
                        "workspace_path is a directory with"
                        "a different name than workspace_name")

                path_confirmed = click.confirm(
                    f"Are you sure you want to use '{
                        workspace_path.absolute()}' as workspace folder?",
                    abort=False)
                click.echo(f"path_confirmed: {path_confirmed}")
            else:
                workspace_path = Path(workspace_path_arg)

        # operations to be done
        folder_exists = os.path.exists(workspace_path)
        file_exists = os.path.exists(
            os.path.join(workspace_path, f"{workspace_name}.yml"))

        # folder prompt
        folder_prompt = f"\nWill create folder at {workspace_path.absolute()}"
        if folder_exists:
            folder_prompt = f"\nWill use existing folder at {
                workspace_path.absolute()}"

        # file prompt
        file_prompt = f"\nWill create workspace file at {
            os.path.join(workspace_path.absolute(), f'{workspace_name}.yml')}"
        if file_exists:
            file_prompt = "\nWill use and override existing workspace" + \
                f"file at {workspace_path}"

        # confirm operations
        click.confirm(f"These operations will be executed.\n"
                      f"Do you accept? If not mrw will exit."
                      f"{folder_prompt}"
                      f"{file_prompt}", abort=True)

        click.echo("Creating workspace...")

        # create/use workspace folder
        if not os.path.exists(workspace_path):
            os.makedirs(workspace_path)
            click.echo(f"Created new directory at {workspace_path.absolute()}")
        else:
            output_text = click.style(workspace_path.absolute(), fg='green')
            click.echo(f"Using existing directory at {output_text}")

        # create/use workspace file
        workspace_file = Path(os.path.join(
            workspace_path, f"{workspace_name}.yml"))
        if not os.path.exists(workspace_file):
            # create workspace file
            with open(workspace_file, 'w') as config_file:
                config_file.write(f"workspace_name={workspace_name}\n")
            click.echo(f"Created new workspace config file at {
                       workspace_file.absolute()}")
        else:
            click.echo(f"Using existing workspace config file at {
                       workspace_file.absolute()}")

        # create Workspace model
        workspace = Workspace(workspace_name, workspace_path, None)

        click.echo(f"Created workspace \n{workspace}")
        click.echo("-----------------------------------------")
        # read from workspace_file and output it to the console
        with open(workspace_file, 'r') as config_file:
            click.echo(config_file.read())
