import pathlib
import click
from multi_repo_workspace.model.use_case import UseCase
import os

from multi_repo_workspace.model.workspace import Workspace
from pathlib import Path
from typing import Any, Callable
from typing import TypeVar

T = TypeVar('T')


class LineArgument:
    """
    Represents a single program argument. (--path)
    @param name: The name of the argument.  (path)
    @param value: The value of the argument. (~/Documents)
    @param prompt: To be given in the use case's __init__.
    @param confirm: To be given in the use case's __init__.
    """

    def __init__(self,
                 name: str,
                 value: T = None,
                 prompt: Callable[[str], T] = None,
                 confirm: Callable[[T], bool] = None,
                 is_confirmed: bool = False):
        self.name = name
        self.value = value
        self.prompt = prompt
        self.confirm = confirm
        self.is_confirmed = is_confirmed

    def set_prompts(self, *, prompt: Callable[[str], T],
                    confirm: Callable[[T], bool]):
        self.prompt = prompt
        self.confirm = confirm

    def __repr__(self):
        repr = f"{self.name}: {self.value}, "
        repr += f"{'prompt good' if self.prompt else 'prompt missing'}, "
        repr += f"{'confirm good' if self.prompt else 'confirm missing'}, "
        repr += f"{'GO' if self.is_confirmed else 'NO GO'})"
        return repr


class MrwArguments:
    """
    MrwArguments will have arguments passed from command line as a dictionary.
    """

    def __init__(self, *args: LineArgument):
        self.args = {arg.name: arg for arg in args}

    def __getitem__(self, name: str):
        return self.args.get(name)

    def arg_values(self):
        return self.args.values()

    def is_confirmed(self, name: str = None) -> bool:
        """
        Check if a specific argument or all arguments have been confirmed.
        """
        if name:
            return (self.args.get(name).is_confirmed
                    if name in self.args else False)
        return all(arg.is_confirmed for arg in self.args.values())

    def __repr__(self):
        repr = "MrwArguments(\n"
        for arg in self.args.values():
            repr += f"    {arg.__repr__()}\n"
        repr += ")"
        return repr


class MrwCreate(UseCase[MrwArguments, None]):

    @staticmethod
    def prompt_name(_: Any = None) -> str:
        return click.prompt("Enter workspace name", type=str)

    @staticmethod
    def confirm_name(name: str) -> bool:
        return click.confirm(
            f"Are you sure you want to use '{name}' as workspace name?",
            abort=False,
        )

    @staticmethod
    def prompt_path(_: Any = None) -> click.Path:
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

    @staticmethod
    def confirm_path(path: pathlib.Path) -> bool:
        """
        Takes in a pathlib.Path and returns a boolean.
        """
        return click.confirm(
            f"Are you sure you want to create workspace folder at '{path.absolute()}'?"
        )

    """
    MrwCreate creates a new workspace.

    The 2 arguments are workspace_name and workspace_directory. They are optional.
    If they are not provided, the user will be prompted to enter them.

    If the user enters a workspace name that is the same as an existing
    directory, the user will be prompted to confirm that they want to
    use that directory.
    """

    def __init__(self):
        super().__init__()
        self.operations_accepted = False

    def echo_welcome(self):
        return click.echo("Hello! inside the create use case\n")

    def __call__(self, args: dict):
        self.echo_welcome()

        mrw_params = MrwArguments(
            LineArgument("workspace_name", args["workspace_name"],
                            MrwCreate.prompt_name, MrwCreate.confirm_name),
            LineArgument("workspace_directory", args["workspace_directory"],
                            MrwCreate.prompt_path, MrwCreate.confirm_path))

        click.echo(mrw_params)

        while not self.operations_accepted:
            # confirm arguments
            while not mrw_params.is_confirmed():
                paramsToConfirm = [
                    param for param in mrw_params.arg_values()
                    if not param.is_confirmed
                ]
                for param in paramsToConfirm:
                    # confirm param
                    while not param.is_confirmed:
                        if not param.value:
                            param.value = param.prompt()
                        if not param.is_confirmed:
                            param.is_confirmed = param.confirm(param.value)
                        param.value = None if not param.is_confirmed else param.value

            pass
            # operations for creating workspace
            #   create or use folder
            #   create workspace file

            # operations
            #   build a list of operations to be done
            #   confirm the set of operations?
            #   if not operations_accepted
            #       remove confirmations from mrw_params

        # operations to be done
        #folder_exists=os.path.exists(self.params.get_argument('workspace_path'))
        # file_exists=os.path.exists(
        #     os.path.join(workspace_path, f"{workspace_name}.yml"))

        # # folder prompt
        # folder_prompt=f"\nWill create folder at {workspace_path.absolute()}"
        # if folder_exists:
        #     folder_prompt=f"\nWill use existing folder at {
        #         workspace_path.absolute()}"

        # # file prompt
        # file_prompt=f"\nWill create workspace file at {
        #     os.path.join(workspace_path.absolute(), f'{workspace_name}.yml')}"
        # if file_exists:
        #     file_prompt="\nWill use and override existing workspace" + \
        #         f"file at {workspace_path}"

        # # confirm operations
        # click.confirm(f"These operations will be executed.\n"
        #               f"Do you accept? If not mrw will exit."
        #               f"{folder_prompt}"
        #               f"{file_prompt}", abort=True)

        # click.echo("Creating workspace...")

        # # create/use workspace folder
        # if not os.path.exists(workspace_path):
        #     os.makedirs(workspace_path)
        #     click.echo(f"Created new directory at {workspace_path.absolute()}")
        # else:
        #     output_text=click.style(workspace_path.absolute(), fg='green')
        #     click.echo(f"Using existing directory at {output_text}")

        # # create/use workspace file
        # workspace_file=Path(os.path.join(
        #     workspace_path, f"{workspace_name}.yml"))
        # if not os.path.exists(workspace_file):
        #     # create workspace file
        #     with open(workspace_file, 'w') as config_file:
        #         config_file.write(f"workspace_name={workspace_name}\n")
        #     click.echo(f"Created new workspace config file at {
        #                workspace_file.absolute()}")
        # else:
        #     click.echo(f"Using existing workspace config file at {
        #                workspace_file.absolute()}")

        # # create Workspace model
        # workspace=Workspace(workspace_name, workspace_path, None)

        # click.echo(f"Created workspace \n{workspace}")
        # click.echo("-----------------------------------------")
        # # read from workspace_file and output it to the console
        # with open(workspace_file, 'r') as config_file:
        #     click.echo(config_file.read())
