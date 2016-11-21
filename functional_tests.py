from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Scott has heard about a new online to-do app. He goes to check it out
        self.browser.get('http://localhost:8000')

        #He notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is invited to create an item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        
        #He types "Charge heli batteries" as an item in a to-do list
        inputbox.send_keys('Charge heli batteries')

        #When he hits enter, the page updates, and now the page lists
        # "1: Charge heli batteries" as an item in the to-do table
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Charge heli batteries', [row.text for row in rows])
        
        #There is still a textbox inviting him to add another item.
        #He enters "Charge headset batteries"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Charge headset batteries')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again, and now shows both items on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Charge heli batteries', [row.text for row in rows])
        self.assertIn('2: Charge headset batteries', [row.text for row in rows])

        #Scott wonders if the site will remember his list.
        #He sees the site created a unique URL for him.
        #There is some explanatory text to that effect.
        self.fail('Finish the test!')
        
        #He visits that URL.  The list is still there.
        
        #Satisfied, he leaves.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
