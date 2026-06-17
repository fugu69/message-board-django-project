from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(post_content="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.post_content, "This is a test!")

    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')
        self.assertContains(response, "This is a test!")


