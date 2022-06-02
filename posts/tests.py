from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    """
    This clas is just a test class that will a create a sample database for us to test
    our post model
    """
    def setUp(self):
        """
        When created, it will create a sample entry 
        """
        Post.objects.create(text='just a test!!')

    def test_text_content(self):
        """
        Tests to make sure the same test entry is what it is supposed to be
        """
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test!!')


class HomePageViewTest(TestCase):
    """
    This class is to test if the homepage exists and returns a HTTP 200 response
    If it uses HomePageView as the view, 
    And if it uses home.html as the template
    """
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
