"""Fast, Extensible Progress Meter (tqdm) For Django."""

import sys
from typing import Any, TextIO

from django.core.management.base import BaseCommand as BaseCommandOriginal
from django.core.management.color import color_style
from tqdm import tqdm


class OutputBase:
    """Output Base."""

    def error(self, text: str, ending: str = "\n", fatal: bool = False) -> None:
        """Print error message."""
        self.write(text, ending=ending, fatal=fatal, error=True)  # type: ignore

    def info(self, text: str, ending: str = "\n", fatal: bool = False) -> None:
        """Print message."""
        self.write(text, ending=ending, fatal=fatal)  # type: ignore


class Tqdm(tqdm, OutputBase):
    """Tqdm."""

    command: "BaseCommand"
    isatty: bool

    def __init__(self, *args: Any, **kwargs: Any):
        """Init."""
        self.command = kwargs.pop("command")
        self.isatty = self.command.stdout.isatty()
        # Disable output by default. It means the console won't wind up in stderr if in pipe mode and will be still
        # visible in console.
        if "disable" not in kwargs:
            kwargs["disable"] = None
        # Don't show traces of progress bar by default. We will still see them if error occurs so that is good.
        if "leave" not in kwargs:
            kwargs["leave"] = False
        super().__init__(*args, **kwargs)

    # pylint: disable=arguments-renamed
    def write(
        self, text: str, file: TextIO = sys.stdout, ending: str = "\n", fatal: bool = False, error: bool = False
    ) -> None:
        """Print a message via tqdm (without overlap with bars)."""
        if self.isatty:
            if error:
                text = color_style().ERROR(text)
            super().write(text, file=file, end=ending)
            if fatal:
                sys.exit()
        else:
            self.command.write(text, ending=ending, fatal=fatal, error=error)


class BaseCommand(BaseCommandOriginal, OutputBase):
    """
    The base class from which all management commands ultimately derive.

    Use this class if you want access to all of the mechanisms which
    parse the command-line arguments and work out what code to call in
    response; if you don't need to change any of that behavior,
    consider using one of the subclasses defined in this file.

    If you are interested in overriding/customizing various aspects of
    the command-parsing and -execution behavior, the normal flow works
    as follows:

    1. ``django-admin`` or ``manage.py`` loads the command class
       and calls its ``run_from_argv()`` method.

    2. The ``run_from_argv()`` method calls ``create_parser()`` to get
       an ``ArgumentParser`` for the arguments, parses them, performs
       any environment changes requested by options like
       ``pythonpath``, and then calls the ``execute()`` method,
       passing the parsed arguments.

    3. The ``execute()`` method attempts to carry out the command by
       calling the ``handle()`` method with the parsed arguments; any
       output produced by ``handle()`` will be printed to standard
       output and, if the command is intended to produce a block of
       SQL statements, will be wrapped in ``BEGIN`` and ``COMMIT``.

    4. If ``handle()`` or ``execute()`` raised any exception (e.g.
       ``CommandError``), ``run_from_argv()`` will  instead print an error
       message to ``stderr``.

    Thus, the ``handle()`` method is typically the starting point for
    subclasses; many built-in commands and command types either place
    all of their logic in ``handle()``, or perform some additional
    parsing work in ``handle()`` and then delegate from it to more
    specialized methods as needed.

    Several attributes affect behavior at various steps along the way:

    ``help``
        A short description of the command, which will be printed in
        help messages.

    ``output_transaction``
        A boolean indicating whether the command outputs SQL
        statements; if ``True``, the output will automatically be
        wrapped with ``BEGIN;`` and ``COMMIT;``. Default value is
        ``False``.

    ``requires_migrations_checks``
        A boolean; if ``True``, the command prints a warning if the set of
        migrations on disk don't match the migrations in the database.

    ``requires_system_checks``
        A list or tuple of tags, e.g. [Tags.staticfiles, Tags.models]. System
        checks registered in the chosen tags will be checked for errors prior
        to executing the command. The value '__all__' can be used to specify
        that all system checks should be performed. Default value is '__all__'.

        To validate an individual application's models
        rather than all applications' models, call
        ``self.check(app_configs)`` from ``handle()``, where ``app_configs``
        is the list of application's configuration provided by the
        app registry.

    ``stealth_options``
        A tuple of any options the command uses which aren't defined by the
        argument parser.
    """

    def write(self, text: str, ending: str = "\n", fatal: bool = False, error: bool = False) -> None:
        """Print a message."""
        if error:
            output = self.stderr
        else:
            output = self.stdout
        output.write(text, ending=ending)
        if fatal:
            sys.exit()

    def tqdm(self, *args: Any, **kwargs: Any) -> Tqdm:
        """Return a tqdm instance."""
        return Tqdm(command=self, *args, **kwargs)
