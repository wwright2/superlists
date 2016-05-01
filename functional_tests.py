#/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        pass #self.browser.quit()

        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes 
        # to check out its homepage
        try:
            self.browser.get('http://localhost:8000')
            self.assertIn('To-Do',self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do',header_text)

            #She is invited to enter a to-do item straight away
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )
                
            #She types "Buy peacock feathers" into a text box (Ediths's hobby
            # is tying fly-fishin lures)
            # When she hits enter, the page updates, and now the page lists
            # "1: Buy peacock feathers" as an item in a to-do list
            # "2: Use peacock feathers to make fly" as an item in a to-do list
            
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Buy peacock feathers')
            inputbox.send_keys(Keys.ENTER)
            time.sleep(3)
            self.check_for_row_in_list_table('1: Buy peacock feathers')

            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Use peacock feathers to make a fly')
            inputbox.send_keys(Keys.ENTER)
            time.sleep(3)
            self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
            
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows),
                    "New to-do item did not appear in table -- its text was:\n%s" % (table.text,
                    )
                )
        except Exception as x:
            print (repr(x))
            

        self.fail('Finish the test!')




        # There is still a text box inviting her to add another item.  She
        # enters " Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list
        # Edith
        # that the
        # explanatory text

        # She visits that URL

        # Satisfied
        

if __name__ == '__main__' :
    unittest.main(warnings='ignore')
        

#assert 'Django' in browser.title
