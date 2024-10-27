import click


def main():
    cli()


@click.group(invoke_without_command=True)
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
@click.pass_context
def cli(ctx, verbose):
    """Default command invoked as a command."""
    ctx.ensure_object(dict)
    # add command groups
    # ctx.obj['group'] = GroupObject()
    # relay args
    # ctx.obj['group'].set_verbose(verbose)
    # ...
    click.echo("cli init sups ups ups")
