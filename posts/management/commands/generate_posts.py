from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--number', action='store', type=int,
                            default=100, help='Number of posts')

    def handle(self, *args, **options):
        pass
