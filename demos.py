# coding: utf-8
from __future__ import unicode_literals

import sys
from time import sleep

from django_tqdm import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):
    def handle(self, *args, **options):
        def demo1():
            self.error('error')
            self.info('info')

        def demo2():
            t = self.tqdm(total=123)
            for x in range(123):
                sleep(0.02)
                t.update(1)
                if x == 5:
                    t.info('info')
                if x == 50:
                    t.error('error')

        def demo3():
            t = tqdm(total=123)

            for x in range(123):
                sleep(0.02)
                t.update(1)
                if x == 5:
                    t.write('1')
                if x == 50:
                    t.write('3', file=sys.stderr)

        def demo4():
            # works fine, no color
            t = tqdm(total=123, disable=True)

            for x in range(123):
                sleep(0.02)
                t.update(1)
                if x == 5:
                    t.write('1')
                if x == 50:
                    t.write('3', file=sys.stderr)

        def demo5():
            # still broken
            t = tqdm(total=123, leave=False)

            for x in range(123):
                sleep(0.02)
                t.update(1)
                if x == 5:
                    t.write('1')
                if x == 50:
                    t.write('3', file=sys.stderr)

        demo1()
        demo2()
        demo3()
        demo4()
        demo5()


demo = Command()
demo.handle()
