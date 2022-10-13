from django.test import TestCase

from lists.forms import ItemForm, EMPTY_ITEM_ERROR


class ItemFromTest(TestCase):

    def test_form_renders_input_box(self):
        item_form = ItemForm()
        self.assertIn('class="form-control input-lg"', item_form.as_p())
        self.assertIn('placeholder="Enter a to-do item"', item_form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])
