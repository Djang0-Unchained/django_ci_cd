from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from posts.models import Posts


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--number', action='store', type=int,
                            default=100, help='Number of posts')

    def handle(self, *args, **options):
        number = options.get('number', 100)
        posts_obj = [Posts(title=get_random_string(length=36)) for _ in range(number)]
        Posts.objects.bulk_create(posts_obj)

