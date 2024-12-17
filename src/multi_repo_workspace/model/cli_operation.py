import pathlib

import click


class Operation:

    def __init__(self, *, name, description, function):
        self.name = name
        self.description = description  # verbose
        self.function = function
        self.has_tried = False
        self.has_succeeded = False

    def __call__(self):
        self.has_tried = True
        try:
            self.function()
            self.has_succeeded = True
        except Exception as e:
            self.has_succeeded = False
            print(e)


class CreateOrUseDirectory(Operation):

    def __init__(self, directory: pathlib.Path):

        def create_or_use_directory():
            click.echo(
                click.style(f"Creating or using directory: {directory}",
                            fg='blue',
                            bold=True))
            click.echo(f"Creating or using directory: {directory}")
            if not directory.exists():
                directory.mkdir()

        super().__init__(name="CreateOrUseDirectory",
                         description="description",
                         function=create_or_use_directory)


class CreateFile(Operation):

    def __init__(self, file: pathlib.Path):

        def create_file():
            click.echo(
                click.style(f"Creating file: {file}", fg='blue', bold=True))
            if not file.exists():
                file.touch()
            else:
                raise FileExistsError(f"File {file} already exists.")

        super().__init__(name="CreateFile",
                         description="description",
                         function=create_file)


class WriteToFile(Operation):

    def __init__(self, file: pathlib.Path, content: str):

        def write_to_file():
            click.echo(
                click.style(f"Writing to file: {file}", fg='blue', bold=True))
            click.echo(click.style(content, fg='green'))
            file.write_text(content)

        super().__init__(name="WriteToFile",
                         description="description",
                         function=write_to_file)
