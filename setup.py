import codecs
from os.path import abspath, dirname, join

from setuptools import find_packages, setup


CURRENT_DIR = dirname(abspath(__file__))


def readme():
    with codecs.open(join(CURRENT_DIR, 'README.rst'), encoding='utf-8') as f:
        return f.read()


def requirements():
    with open(join(CURRENT_DIR, 'requirements.txt')) as f:
        return f.read().splitlines()


setup(
    name='django_tqdm',
    version='0.0.3',
    url='https://github.com/desecho/django-tqdm',
    license='MIT',
    author='Anton Samarchyan',
    author_email='desecho@gmail.com',
    description='Fast, Extensible Progress Meter (tqdm) For Django',
    long_description=readme(),
    install_requires=requirements(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Monitoring',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
    ],
    keywords='progressbar progressmeter progress bar meter rate eta console terminal time',
    tests_require=[
        'pytest',
    ],
)
