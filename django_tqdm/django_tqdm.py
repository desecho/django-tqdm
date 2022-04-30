"""Fast, Extensible Progress Meter (tqdm) For Django."""

import sys
from typing import Any, TextIO

from django.core.management.base import BaseCommand as BaseCommandOriginal
from django.core.management.color import color_style
from tqdm import tqdm


class OutputBase:
    def error(self, text: str, ending: str = "\n", fatal: bool = False) -> None:
        self.write(text, ending=ending, fatal=fatal, error=True)  # type: ignore

    def info(self, text: str, ending: str = "\n", fatal: bool = False) -> None:
        self.write(text, ending=ending, fatal=fatal)  # type: ignore


class Tqdm(tqdm, OutputBase):
    def __init__(self, *args: Any, **kwargs: Any):
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
        if self.isatty:
            if error:
                text = color_style().ERROR(text)
            super().write(text, file=file, end=ending)
            if fatal:
                sys.exit()
        else:
            self.command.write(text, ending=ending, fatal=fatal, error=error)


class BaseCommand(BaseCommandOriginal, OutputBase):
    def write(self, text: str, ending: str = "\n", fatal: bool = False, error: bool = False) -> None:
        if error:
            output = self.stderr
        else:
            output = self.stdout
        output.write(text, ending=ending)
        if fatal:
            sys.exit()

    def tqdm(self, *args: Any, **kwargs: Any) -> Tqdm:
        return Tqdm(command=self, *args, **kwargs)
