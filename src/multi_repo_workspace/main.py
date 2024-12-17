import logging
import pathlib
import sys
import click
from multi_repo_workspace.core.logging import setup_logging, get_logger
from multi_repo_workspace.commands.mrw_create import CreateWorkspace
import re


def set_verbosity(ctx) -> bool:
    full_command = ' '.join(sys.argv)
    if any(opt in full_command for opt in ["-v", "--version"]) or re.search(
            r" -[a-zA-Z]*v[a-zA-Z]*", full_command):
        logging.getLogger("mrw").setLevel(logging.DEBUG)
        get_logger().debug("Verbose logging enabled")
        ctx.obj['verbose'] = True
        return True
    return False


def main():
    setup_logging()
    cli()


# region command: > mrw


@click.group(invoke_without_command=True)
@click.option("--verbose",
              "-v",
              is_flag=True,
              help="Will print verbose messages.")
@click.help_option("-h", "--help")
@click.pass_context
def cli(ctx, verbose):
    """Default command. mrw """

    ctx.ensure_object(dict)
    set_verbosity(ctx)
    log = get_logger()

    log.debug("Starting Multi-Repo Workspace (MRW) CLI")

    if ctx.invoked_subcommand is None:
        default_text = click.style("default", bold=True, italic=True)
        log.debug(f"Invoking {default_text} with params: {ctx.params}")
        log.debug("Exiting...")

    else:
        command_text = click.style(ctx.invoked_subcommand, bold=True)
        log.debug(
            f"Invoking {command_text} subcommand with params: {ctx.params}")


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
@click.option("--verbose",
              "-v",
              is_flag=True,
              help="Will print verbose messages.")
@click.help_option("-h", "--help")
@click.pass_context
def create(ctx, name: str, directory: pathlib.Path, verbose: bool):
    ctx.ensure_object(dict)

    CreateWorkspace({
        "workspace_name": name,
        "workspace_directory": directory
    })()


# endregion
