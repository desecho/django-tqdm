django-tqdm
==============

|PyPI-Status| |PyPI-Versions| |LICENSE| |Tests| |Codecov| |Requirements| |Downloads|

*Fast, Extensible Progress Meter (tqdm) For Django*.

| Use tqdm_ in Django_ management commands seamlessly.
| It provides simple universal commands for Django management command to output
  text using standard command functions and tqdm.
| Only currently supported versions of Django and Python are supported.

Usage
-----

.. code:: python

    from django_tqdm import BaseCommand
    from time import sleep

    class Command(BaseCommand):
        def handle(self, *args, **options):
            # Output directly
            self.error("Error")
            self.info("Info")

            # Output through tqdm
            t = self.tqdm(total=50)
            for x in range(50):
                sleep(0.03)
                t.update(1)

                if x == 10:
                    t.info("X = 10")
                if x == 20:
                    t.error("X = 20")

Advanced:

.. code:: python

    info(text, ending="\n", fatal=False)
    error(text, ending="\n", fatal=False)
    write(text, ending="\n", fatal=False, error=False)

If you set ``fatal`` to ``True`` it will terminate the command after printing the message.

For documentation on tqdm see tqdm_.

Comparison
------------

In django-tqdm:

.. code:: python

    self.info("info")
    self.error("error")

In vanilla Django:

.. code:: python

    self.stdout.write("info")
    self.stderr.write("error")


Demos
------------

Demo 1 - Simple usage
------------------------

.. code:: python

    self.info("info")
    self.error("error")

|Demo1|

Demo 2 - tqdm usage
-----------------------

.. code:: python

    t = self.tqdm(total=50)
    for x in range(50):
        sleep(0.02)
        t.update(1)
        if x == 10:
            t.info("info")
        if x == 40:
            t.error("error")

|Demo2|

Demo 3 - Vanilla tqdm with default settings for comparison
------------------------------------------------------------------

.. code:: python

    t = tqdm(total=50)
    for x in range(50):
        sleep(0.02)
        t.update(1)
        if x == 25:
            t.write("info")
        if x == 40:
            t.write("error", file=sys.stderr)

|Demo3|


Developer documentation
-------------------------

Read `developer documentation`_.


.. |Demo1| image:: https://asciinema.org/a/117133.png
   :target: https://asciinema.org/a/117133

.. |Demo2| image:: https://asciinema.org/a/117136.png
   :target: https://asciinema.org/a/117136

.. |Demo3| image:: https://asciinema.org/a/117137.png
   :target: https://asciinema.org/a/117137

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/django-tqdm.svg
   :target: https://pypi.python.org/pypi/django-tqdm

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/django-tqdm.svg
   :target: https://pypi.python.org/pypi/django-tqdm

.. |LICENSE| image:: https://img.shields.io/pypi/l/django-tqdm.svg
   :target: https://raw.githubusercontent.com/desecho/django-tqdm/master/LICENSE

.. |Tests| image:: https://github.com/desecho/django-tqdm/actions/workflows/test.yaml/badge.svg?branch=master
    :target: https://github.com/desecho/django-tqdm/actions/workflows/test.yaml

.. |Codecov| image:: https://codecov.io/gh/desecho/django-tqdm/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/desecho/django-tqdm

.. |Requirements| image:: https://requires.io/github/desecho/django-tqdm/requirements.svg?branch=master
     :target: https://requires.io/github/desecho/django-tqdm/requirements/?branch=master
     :alt: Requirements Status

.. |Downloads| image:: https://pepy.tech/badge/django-tqdm
     :target: https://pepy.tech/project/django-tqdm
     :alt: Downloads

.. _tqdm: https://github.com/tqdm/tqdm
.. _Django: https://www.djangoproject.com
.. _developer documentation: https://github.com/desecho/django-tqdm/blob/master/developer_doc.md
