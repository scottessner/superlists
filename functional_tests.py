from selenium import webdriver
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
        self.fail('Finish the test!')
        
        #He is invited to create an item right away
        
        #He types "Charge heli batteries" as an item in a to-do list
        
        #There is still a textbox inviting him to add another item.
        #He enters "Charge headset batteries"
        
        #The page updates again, and now shows both items on the list
        
        #Scott wonders if the site will remember his list.
        #He sees the site created a unique URL for him.
        #There is some explanatory text to that effect.
        
        #He visits that URL.  The list is still there.
        
        #Satisfied, he leaves.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
