import codecs
from os.path import abspath, dirname, join

from setuptools import find_packages, setup


def readme():
    with codecs.open(join(dirname(abspath(__file__)), 'README.rst'), encoding='utf-8') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name='django_tqdm',
    version='0.0.1',
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
        'Classifier: Environment :: Console',
        'Classifier: Topic :: Software Development :: Libraries',
        'Classifier: Topic :: Software Development :: Libraries :: Python Modules',
        'Classifier: Topic :: Software Development :: User Interfaces',
        'Classifier: Topic :: System :: Monitoring',
        'Classifier: Topic :: Terminals',
        'Classifier: Topic :: Utilities',
        'Classifier: Intended Audience :: Developers',
    ],
    keywords='progressbar progressmeter progress bar meter rate eta console terminal time',
    tests_require=[
        'pytest',
    ],
)
