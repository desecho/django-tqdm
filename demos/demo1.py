"""Demo 1 - Simple usage."""

from typing import Any

from django_tqdm import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        def demo() -> None:  # pylint: disable=duplicate-code
            self.info("info")
            self.error("error")

        demo()


demo1 = Command()
demo1.handle()
