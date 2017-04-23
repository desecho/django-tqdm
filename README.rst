django-tqdm
==============

|PyPI-Status| |PyPI-Versions| |Travis| |Codecov| |Codacy| |Requirements|

*Use tqdm in django management commands seamlessly.*

It uses tqdm_ and it is meant to be used with Django_.
It provides simple universal commands for Django management command to output text using standard command functions and tqdm.

Usage
-----

.. code:: python

    from django_tqdm import BaseCommand
    from time import sleep

    class Command(BaseCommand):
        def handle(self, *args, **options):
            # Output directly
            self.error('Error')
            self.info('Info')

            # Output through tqdm
            t = self.tqdm(total=50)
            for x in range(50):
                sleep(0.03)
                t.update(1)

                if x == 10:
                    t.info('X = 10')
                if x == 20:
                    t.error('X = 20')

Advanced:

.. code:: python

    info(text, ending='\n', fatal=False)
    error(text, ending='\n', fatal=False)
    write(text, ending='\n', fatal=False, error=False)

If you set *fatal* to *True* it will terminate the command after printing the message.

For documentation on tqdm see tqdm_.

Comparison
------------

In django-tqdm:

.. code:: python

    self.info('info')
    self.error('error')

In vanilla Django:

.. code:: python

    self.stdout.write('info')
    self.stderr.write('error')


Demos
------------

Demo 1
------------

.. code:: python

    self.info('info')
    self.error('error')

|Demo1|

Demo 2
------------

.. code:: python

    t = self.tqdm(total=50)
    for x in range(50):
        sleep(0.02)
        t.update(1)
        if x == 10:
            t.info('info')
        if x == 40:
            t.error('error')

|Demo2|

Demo 3 - Vanilla tqdm with default settings for comparison
------------------------------------------------------------------

.. code:: python

    t = tqdm(total=50)
    for x in range(50):
        sleep(0.02)
        t.update(1)
        if x == 25:
            t.write('info')
        if x == 40:
            t.write('error', file=sys.stderr)

|Demo3|


.. |Demo1| image:: https://desecho.org/django-tqdm/demo1.gif
.. |Demo2| image:: https://desecho.org/django-tqdm/demo2.gif
.. |Demo3| image:: https://desecho.org/django-tqdm/demo3.gif

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/django-tqdm.svg
   :target: https://pypi.python.org/pypi/django-tqdm

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/django-tqdm.svg
   :target: https://pypi.python.org/pypi/django-tqdm

.. |Travis| image:: https://travis-ci.org/desecho/django-tqdm.svg?branch=master
    :target: https://travis-ci.org/desecho/django-tqdm

.. |Codecov| image:: https://codecov.io/gh/desecho/django-tqdm/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/desecho/django-tqdm

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/fd1d71750ca8434199778c80e19b5136
    :target: https://www.codacy.com/app/desecho/django-tqdm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=desecho/django-tqdm&amp;utm_campaign=Badge_Grade

.. |Requirements| image:: https://requires.io/github/desecho/django-tqdm/requirements.svg?branch=master
     :target: https://requires.io/github/desecho/django-tqdm/requirements/?branch=master
     :alt: Requirements Status

.. _tqdm: https://github.com/tqdm/tqdm
.. _Django: https://www.djangoproject.com
