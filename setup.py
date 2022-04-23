from os.path import abspath, dirname, join

from setuptools import setup

CURRENT_DIR = dirname(abspath(__file__))


def requirements():
    with open(join(CURRENT_DIR, "requirements.txt")) as f:
        return f.read().splitlines()


setup(
    install_requires=requirements(),
)
