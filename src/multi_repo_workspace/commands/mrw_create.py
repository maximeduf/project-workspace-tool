import pathlib
import click
from multi_repo_workspace.model.cli_args import CommandArgs, LineArgument
from multi_repo_workspace.model.cli_command import Command
import os

from multi_repo_workspace.model.cli_operation import CreateFile, CreateOrUseDirectory, Operation, WriteToFile
from multi_repo_workspace.model.workspace import Workspace
from pathlib import Path
from typing import Any, Callable, List
from typing import TypeVar


class CreateWorkspace(Command[CommandArgs, None]):
    """
    MrwCreate creates a new workspace.

    The 2 arguments are workspace_name and workspace_directory. They are optional.
    If they are not provided, the user will be prompted to enter them.

    If the user enters a workspace name that is the same as an existing
    directory, the user will be prompted to confirm that they want to
    use that directory.
    """

    def __init__(self, args: dict):
        super().__init__()
        self.ops: List[Operation] = []
        self.args = CommandArgs(
            LineArgument("workspace_name", args["workspace_name"],
                         self.prompt_name, self.confirm_name),
            LineArgument("workspace_directory", args["workspace_directory"],
                         self.prompt_path, self.confirm_path))

    def echo_welcome(self):
        return click.echo("Hello! inside the create use case\n")

    def prompt_name(self) -> str:
        return click.prompt("Enter workspace name", type=str)

    def confirm_name(self, name: str) -> bool:
        output_text = f"'{name}' will be used for the workspace directory.\n"
        output_text += f"A worspace file named '{name}.yml' will be created.\n"
        output_text += f"Do you want to use '{name}' as workspace name?"

        return click.confirm(
            output_text,
            abort=False,
        )

    def prompt_path(self) -> click.Path:
        workspace_path: click.Path = click.prompt(
            "Enter workspace path",
            type=click.Path(exists=False,
                            dir_okay=True,
                            file_okay=False,
                            path_type=pathlib.Path),
            default=".",
            show_default=True,
            prompt_suffix=": ",
        )
        return workspace_path.expanduser() if str(workspace_path).startswith(
            "~") else workspace_path

    def confirm_path(self, path: pathlib.Path) -> bool:
        name = self.args["workspace_name"].value
        work_dir = path.joinpath(name)
        create_or_use = "create" if not work_dir.exists() else "use"
        confirmation = click.confirm(
            f"Do you want to {create_or_use} workspace folder at '{work_dir.absolute()}'?"
        )
        if confirmation:
            self.ops.append(CreateOrUseDirectory(work_dir))
            self.ops.append(CreateFile(work_dir.joinpath(f"{name}.yml")))
        else:
            self.args["workspace_name"].is_confirmed = False
        return confirmation

    def __call__(self):
        self.echo_welcome()

        click.echo(self.args)

        # confirm arguments
        while not self.args.is_confirmed():
            argsToConfirm = [
                arg for arg in self.args.arg_values() if not arg.is_confirmed
            ]
            for arg in argsToConfirm:
                # confirm param
                if not arg.value:
                    arg.value = arg.prompt()
                if not arg.is_confirmed:
                    arg.is_confirmed = arg.confirm(arg.value)
                arg.value = None if not arg.is_confirmed else arg.value
                if not arg.is_confirmed:
                    break

        workspace = Workspace(self.args["workspace_name"].value,
                              self.args["workspace_directory"].value, None)
        file = workspace.get_file_path(f"{workspace.name}.yml")
        self.ops.append(CreateFile(file))
        self.ops.append(WriteToFile(file, str(workspace)))
        # execute operations
        for op in self.ops:
            op()

        if all(op.has_succeeded for op in self.ops):
            click.echo(
                click.style(f"Created workspace \n{workspace}",
                            fg='green',
                            bold=True))
        else:
            click.echo(click.style("Failed to create workspace.", fg='red'))
            click.echo("Exiting...")
            os._exit(1)
