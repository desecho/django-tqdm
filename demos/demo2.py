"""Demo 2 - tqdm usage."""

from time import sleep
from typing import Any

from django_tqdm import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        def demo() -> None:
            t = self.tqdm(total=50)
            for x in range(50):
                sleep(0.02)
                t.update(1)
                if x == 10:
                    t.info("info")
                if x == 40:
                    t.error("error")

        demo()


demo2 = Command()
demo2.handle()
