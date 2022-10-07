from django.test import TestCase


class SmokeTest(TestCase):

    def test_trigger_failure(self):
        self.assertEquals(1 / 2, 0.49999)
