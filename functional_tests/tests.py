import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(
            executable_path=r'C:\Users\YugandharG\REPO\test-driven-development\geckodriver.exe')  # ADD geckodriver path here before testing

    def tearDown(self) -> None:
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mr.X has heard about a cool new online to-do app. They go
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # They notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("To-Do", header_text)

        # they are invited to enter a to-do item straight away
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), "Enter a to-do item")

        # they type "Buy peacock feathers" into a text box (Their hobby is tying fly-fishing lures)
        input_box.send_keys("Buy peacock feathers")

        # When they hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # There is still a text box inviting her to add another item. They
        # enter "Use peacock feathers to make a fly" (They are very methodical)
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        input_box.send_keys("Use peacock feathers to make a fly")
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        # The page updates again, and now shows both items on their list
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # They wonder whether the site will remember her list. Then they see
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail("Complete the test!")

        # They visit that URL - her to-do list is still there.
