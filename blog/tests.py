from django.test import TestCase

from .models import Post


class PostModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title="Django",
                                        author="Ramesh", slug="Dj")

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), "Django")
