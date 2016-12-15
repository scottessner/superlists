from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Scott goes to the home page and accidentally tries to submit
        # an empty list item. He hits enter on the empty input box
        self.browser.get(self.server_url)
        inputbox =  self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        # The home page refreshes and there is an error message saying 
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # He tries again with some text for the item, which now works.
        inputbox =  self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, he now decides to submit a second blank list item
        inputbox =  self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)
        
        # He receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And he can correct it by filling some text in
        inputbox =  self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
