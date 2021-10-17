"""Tests for django-tqdm."""

import pytest

from django_tqdm import BaseCommand


class Command(BaseCommand):
    def handle(self, name, *args, **options):
        def basic():
            self.error('error')
            self.info('info')

        def tqdm(fatal=False):
            t = self.tqdm(total=25)
            for x in range(25):
                t.update(1)
                if x == 10:
                    t.info('info')
                if x == 20:
                    t.error('error', fatal=fatal)

        def tqdm_params():
            t = self.tqdm(total=25, disable=None, leave=False)
            for x in range(25):
                t.update(1)
                if x == 10:
                    t.info('info')
                if x == 20:
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
        elif name == 'tqdm_fatal':
            tqdm(fatal=True)
        elif name == 'tqdm_params':
            tqdm_params()


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


def test_tqdm_atty(mocker):
    isatty = mocker.patch('django.core.management.base.OutputWrapper.isatty')
    isatty.return_value = True
    command = Command()
    command.handle('tqdm')


def test_tqdm_atty_fatal(mocker):
    isatty = mocker.patch('django.core.management.base.OutputWrapper.isatty')
    isatty.return_value = True
    command = Command()
    with pytest.raises(SystemExit):
        command.handle('tqdm_fatal')


def test_tqdm_additional_params(capsys):
    command = Command()
    command.handle('tqdm_params')
    out, err = capsys.readouterr()
    assert err == 'error\n'
    assert out == 'info\n'
