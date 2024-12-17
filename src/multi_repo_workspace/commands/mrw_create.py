import pathlib
import click
from multi_repo_workspace.core.logging import get_logger
from multi_repo_workspace.model.cli_args import CommandArgs, LineArgument
from multi_repo_workspace.core.cli_command import Command
import os

from multi_repo_workspace.model.cli_operation import CreateFile, CreateOrUseDirectory, Operation, WriteToFile
from multi_repo_workspace.model.workspace import Workspace
from typing import List


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
        else:
            self.args["workspace_name"].is_confirmed = False
        return confirmation

    def __call__(self):
        log = get_logger()
        log.info("Starting CreateWorkspace command")

        # confirm arguments
        log.debug(f"Confirming {self.args}")
        while not self.args.is_confirmed():

            log.debug("Prompting user for arguments")
            argsToConfirm = [
                arg for arg in self.args.arg_values() if not arg.is_confirmed
            ]
            for arg in argsToConfirm:
                # if value is not set, prompt user
                if not arg.value:
                    log.debug(f"Prompting user for {arg}")
                    arg.value = arg.prompt()
                # if value is set, confirm it
                if not arg.is_confirmed:
                    log.debug(f"Confirming {arg.name}")
                    arg.is_confirmed = arg.confirm(arg.value)
                # if value was not confirmed, set value to None
                if not arg.is_confirmed:
                    log.debug(f"{arg} was not confirmed")
                    arg.value = None
                    break  # break out of for loop
                else:
                    log.debug(f"{arg.name} is {arg.is_confirmed_str()}")

        # create workspace
        log.debug("Creating workspace object")
        workspace = Workspace(
            self.args["workspace_name"].value,
            self.args["workspace_directory"].value.absolute(), None)
        log.debug(f"Workspace object created: {workspace}")
        file = workspace.get_file_path(f"{workspace.name}.yml").absolute()
        log.warning(f"File path: {file}")
        self.ops.append(CreateFile(file))
        self.ops.append(WriteToFile(file, str(workspace)))
        log.debug(f"Operations queued : {self.ops}")

        # execute operations
        for op in self.ops:
            log.debug(f"Executing operation: {op.name}")
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
