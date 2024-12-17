import logging

import click


def setup_logging(level=logging.DEBUG, log_file=None):
    log_level = level
    console_format = "[%(name)s.%(levelname)s] %(message)s"
    file_format = f"%(asctime)s - {console_format}"

    class ClickEchoHandler(logging.Handler):
        """Custom logging handler that emits log messages using click.echo"""

        def emit(self, record):
            log_entry = self.format(record)
            click.echo(log_entry)

    click_handler = ClickEchoHandler()
    click_handler.setLevel(log_level)
    click_handler.setFormatter(logging.Formatter(console_format))
    logging.getLogger().addHandler(click_handler)
    logging.basicConfig(level=log_level, format=console_format)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(file_format))
        logging.getLogger().addHandler(file_handler)


def get_logger() -> logging.Logger:
    return logging.getLogger("mrw")
