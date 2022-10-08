import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\YugandharG\REPO\test-driven-development\geckodriver.exe')  # ADD geckodriver path here before testing

    def tearDown(self) -> None:
        self.browser.close()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mr.X has heard about a cool new online to-do app. They go
        # to check out its homepage
        self.browser.get("http://localhost:8000")

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
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_element(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inviting her to add another item. They
        # enter "Use peacock feathers to make a fly" (They are very methodical)

        # The page updates again, and now shows both items on their list

        # They wonder whether the site will remember her list. Then they see
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # They visit that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main()
