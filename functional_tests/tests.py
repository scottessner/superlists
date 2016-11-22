from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Scott has heard about a new online to-do app. He goes to check it out
        self.browser.get(self.live_server_url)

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

        self.wait_for_page_loaded(10)          
        scott_list_url = self.browser.current_url
        #self.browser.get(self.live_server_url)
        self.assertRegex(scott_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Charge heli batteries')
        
        #There is still a textbox inviting him to add another item.
        #He enters "Charge headset batteries"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Charge headset batteries')
        inputbox.send_keys(Keys.ENTER)
 
        #The page updates again, and now shows both items on the list
        #self.browser.get(self.live_server_url)
        time.sleep(3)
        self.wait_for_page_loaded(10)
        self.check_for_row_in_list_table('1: Charge heli batteries')
        self.check_for_row_in_list_table('2: Charge headset batteries')

        #Now a new user, Francis, comes along to the site

        ## We use a new browser session to make sure that no info
        ## of Scott's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There is no sign of Scott's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Charge heli batteries', page_text)
        self.assertNotIn('Charge headset batteries', page_text)

        #Francis starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        

        #Francis gets his own unique URL
        self.wait_for_page_loaded(10)
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, scott_list_url)

        #Again there is no trace of Scott's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Charge heli batteries', page_text)
        self.assertNotIn('Charge headset batteries', page_text)        
        
    def check_for_row_in_list_table(self, row_text):
        self.wait_for_page_loaded(10)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
     
    def wait_for_page_loaded(self, timeout):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.ID, 'id_list_table')))
