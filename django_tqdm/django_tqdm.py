"""Fast, Extensible Progress Meter (tqdm) For Django."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.core.management.base import BaseCommand as BaseCommandOriginal
from django.core.management.color import color_style
from tqdm import tqdm as tqdm_original


# Fix for python3
try:
    unicode
except NameError:
    unicode = lambda s: str(s)  # pylint: disable=redefined-builtin


class OutputBase(object):
    def error(self, text, ending='\n', fatal=False):
        self.write(text, ending=ending, fatal=fatal, error=True)

    def info(self, text, ending='\n', fatal=False):
        self.write(text, ending=ending, fatal=fatal)


class BaseCommand(BaseCommandOriginal, OutputBase):  # pylint: disable=no-member,abstract-method
    def write(self, text, ending='\n', fatal=False, error=False):
        text = unicode(text)
        if error:
            output = self.stderr
        else:
            output = self.stdout
        output.write(text, ending=ending)
        if fatal:
            sys.exit()

    def tqdm(self, *args, **kwargs):
        return tqdm(command=self, *args, **kwargs)


class tqdm(tqdm_original, OutputBase):  # pylint: disable=no-member
    def __init__(self, *args, **kwargs):
        self.command = kwargs.pop('command')
        self.isatty = self.command.stdout.isatty()
        # Disable output by default. It means the console won't wind up in stderr if in pipe mode and will be still
        # visible in console.
        if 'disable' not in kwargs:
            kwargs['disable'] = None
        # Don't show traces of progress bar by default. We will still see them if error occurs so that is good.
        if 'leave' not in kwargs:
            kwargs['leave'] = False
        super(tqdm, self).__init__(*args, **kwargs)

    def write(self, text, file=sys.stdout, ending='\n', fatal=False, error=False):  # pylint: disable=redefined-builtin
        if self.isatty:
            if error:
                text = unicode(text)
                text = color_style().ERROR(text)
            super(tqdm, self).write(text, file=file, end=ending)
            if fatal:
                sys.exit()
        else:
            self.command.write(text, ending=ending, fatal=fatal, error=error)
