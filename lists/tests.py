from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request_content(self):
        response = self.client.post('/', data={'item_text': "A new item"})
        self.assertIn("A new item", response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
