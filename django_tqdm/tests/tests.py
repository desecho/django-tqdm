"""Tests for django-tqdm"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import sleep

import pytest
from django_tqdm import BaseCommand


class Command(BaseCommand):
    def handle(self, name, *args, **options):
        def basic():
            self.error('error')
            self.info('info')

        def tqdm():
            t = self.tqdm(total=50)
            for x in range(50):
                sleep(0.02)
                t.update(1)
                if x == 25:
                    t.info('info')
                if x == 40:
                    t.error('error')

        def fatal():
            self.error('error', fatal=True)

        # pylint gives errors when it is used
        # locals()[name]()
        if name == 'basic':
            basic()
        elif name == 'tqdm':
            tqdm()
        elif name == 'fatal':
            fatal()


def test_basic(capsys):
    command = Command()
    command.handle('basic')
    out, err = capsys.readouterr()
    assert err == 'error\n'
    assert out == 'info\n'


def test_tqdm(capsys):
    command = Command()
    command.handle('tqdm')
    out, err = capsys.readouterr()
    assert err == 'error\n'
    assert out == 'info\n'


def test_fatal(capsys):
    command = Command()
    with pytest.raises(SystemExit):
        command.handle('fatal')
    _, err = capsys.readouterr()
    assert err == 'error\n'
