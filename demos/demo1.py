from django_tqdm import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        def demo():
            self.info('info')
            self.error('error')

        demo()


demo = Command()
demo.handle()
