import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=r'')  # ADD geckodriver path here before testing

    def tearDown(self) -> None:
        self.browser.close()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mr.X has heard about a cool new online to-do app. They go
        # to check out its homepage
        self.browser.get("http://localhost:8000")

        # They notice the page title and header mention to-do lists
        self.assertIn('TO-DO', self.browser.title)

        # they are invited to enter a to-do item straight away

        # they type "Buy peacock feathers" into a text box (Their hobby
        # is tying fly-fishing lures)

        # When they hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. They
        # enter "Use peacock feathers to make a fly" (They are very methodical)

        # The page updates again, and now shows both items on their list

        # They wonder whether the site will remember her list. Then they see
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # They visit that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main()
