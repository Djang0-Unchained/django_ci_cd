from django.test import TestCase
from posts.models import Posts

# Create your tests here.


class AnimalTestCase(TestCase):
    def setUp(self):
        Posts.objects.create(title='title')
        Posts.objects.create(title='title_1')

    def test_titles(self):
        post = Posts.objects.get(title="title")
        post_1 = Posts.objects.get(title="title_1")
        self.assertEqual(post.title, 'title')
        self.assertEqual(post_1.title, 'title_1')

    def test_number_of_posts(self):
        number_of_posts = Posts.objects.count()
        self.assertEqual(number_of_posts, 2)
