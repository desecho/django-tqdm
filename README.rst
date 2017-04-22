django-tqdm
==============

.. image:: https://travis-ci.org/desecho/django-tqdm.svg?branch=master
    :target: https://travis-ci.org/desecho/django-tqdm

.. image:: https://codecov.io/gh/desecho/django-tqdm/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/desecho/django-tqdm

.. image:: https://api.codacy.com/project/badge/Grade/fd1d71750ca8434199778c80e19b5136
    :target: https://www.codacy.com/app/desecho/django-tqdm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=desecho/django-tqdm&amp;utm_campaign=Badge_Grade

.. image:: https://requires.io/github/desecho/django-tqdm/requirements.svg?branch=master
     :target: https://requires.io/github/desecho/django-tqdm/requirements/?branch=master
     :alt: Requirements Status

*Use tqdm in django management commands seamlessly.*

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
