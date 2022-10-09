from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.test import TestCase

from lists.models import Item, List


class ListAndItemModelSaveTest(TestCase):

    def test_save_and_get_items(self):
        list_ = List()
        list_.save()

        item1 = Item()
        item1.text = "I am item1"
        item1.list = list_
        item1.save()

        item2 = Item()
        item2.text = "I am item2"
        item2.list = list_
        item2.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items: QuerySet = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "I am item1")
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, "I am item2")
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_list(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')

        with self.assertRaises(ValidationError):
            item.save()
            # SQLite doesn't support enforcing emptiness constraints on text columns,
            # and so our save method is letting this invalid value through silently.
            # Hence, full_clean to check validation
            item.full_clean()