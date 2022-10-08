from django.db.models import QuerySet
from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request_content(self):
        response = self.client.post('/', data={'item_text': "A new item"})
        self.assertIn("A new item", response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelSaveTest(TestCase):

    def test_save_and_get_items(self):
        item1 = Item()
        item1.text = "I am item1"
        item1.save()

        item2 = Item()
        item2.text = "I am item2"
        item2.save()

        saved_items: QuerySet = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "I am item1")
        self.assertEqual(second_saved_item.text, "I am item2")
