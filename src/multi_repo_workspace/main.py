import pathlib
import click
from multi_repo_workspace.commands.mrw_create import CreateWorkspace


def main():
    cli()


# region command: > mrw


@click.group(invoke_without_command=True)
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
@click.pass_context
def cli(ctx, verbose):
    """Default command. mrw """
    ctx.ensure_object(dict)

    if ctx.invoked_subcommand is None:
        output_text = click.style("Welcome to Multi-Repo Workspace (MRW)!",
                                  fg='green')
        click.echo(f"{output_text}\n")

    else:
        click.echo("I am about to invoke %s" % ctx.invoked_subcommand)


# endregion

# region > mrw create


@cli.command()
@click.argument("name", type=str, required=False)
@click.option("-d",
              "--directory",
              required=False,
              help="Where to create workspace folder.",
              type=click.Path(exists=True,
                              file_okay=False,
                              dir_okay=True,
                              path_type=pathlib.Path))
def create(name: str, directory: click.Path):
    CreateWorkspace({
        "workspace_name": name,
        "workspace_directory": directory
    })()


# endregion
