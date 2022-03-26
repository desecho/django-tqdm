"""Fast, Extensible Progress Meter (tqdm) For Django."""

from __future__ import unicode_literals

import sys

from django.core.management.base import BaseCommand as BaseCommandOriginal
from django.core.management.color import color_style
from tqdm import tqdm


class OutputBase:  # pylint: disable=bad-option-value
    def error(self, text, ending="\n", fatal=False):
        self.write(text, ending=ending, fatal=fatal, error=True)

    def info(self, text, ending="\n", fatal=False):
        self.write(text, ending=ending, fatal=fatal)


class BaseCommand(BaseCommandOriginal, OutputBase):  # pylint: disable=no-member,abstract-method
    def write(self, text, ending="\n", fatal=False, error=False):
        if error:
            output = self.stderr
        else:
            output = self.stdout
        output.write(text, ending=ending)
        if fatal:
            sys.exit()

    def tqdm(self, *args, **kwargs):
        return Tqdm(command=self, *args, **kwargs)


class Tqdm(tqdm, OutputBase):  # pylint: disable=no-member
    def __init__(self, *args, **kwargs):
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

    def write(
        self, text, file=sys.stdout, ending="\n", fatal=False, error=False
    ):  # pylint: disable=redefined-builtin,arguments-renamed
        if self.isatty:
            if error:
                text = color_style().ERROR(text)
            super().write(text, file=file, end=ending)
            if fatal:
                sys.exit()
        else:
            self.command.write(text, ending=ending, fatal=fatal, error=error)
