import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # this is for mac, no need for windows
import page
import HtmlTestRunner
import time

PATH = "/Users/cuicuiyuan/Documents/DemoGoogleSearch/chromedriver"
baseURL = "https://www.google.com/"
options = webdriver.ChromeOptions()

class MendelAiSearch(unittest.TestCase):
    # """A sample test class to show how page object works"""
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(PATH), options = options) # initialize chrome driver
        self.driver.get(baseURL)
        self.driver.implicitly_wait(5) #  wait for 10 sec.
        self.driver.maximize_window() #  maximize the browser window

    def test_01_search_in_google_returns_suggestion(self):
        # """Tests google.com search feature. Searches for the word "google" then
        # verified that some results show up.  Note that it does not look for
        # any particular text in search results page. This test verifies that
        # the results were not empty."""


        #Load the main page. In this case the home page of Google.com.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Google" is in title
        self.assertTrue(main_page.is_title_matches(), "Google.com title doesn't match.")
        #Sets the text of search textbox to "test"
        main_page.search_text_element = "test"

        auto_count = main_page.result_count()
        #Verifies that the auto suggested result(s) would  display
        self.assertIsNotNone(auto_count, "There is no auto suggestions.")
    
    def test_02_search_in_google_match_the_suggestions(self):
        # """Tests google.org search feature. Searches for the word "test" then
        # verified that some results show up.  Note any auto result suggestionss should contain "test". This test verifies that
        # the results include the keyword "test" """

        #Load the main page. In this case the home page of Google.com.
        main_page = page.MainPage(self.driver)

        #Sets the text of search textbox to "test"
        keyword = main_page.search_text_element = "test"

        time.sleep(2)

        results = main_page.main_results()

        #Declar an array that holds all the result text
        all_results = []

        for ele in results:
            # print("Suggestions are:", main_page.main_resultText(ele))
            all_results.append(main_page.main_resultText(ele))
        
        #Verifies that the entered keyword is in the auto suggessted results
        self.assertIn(keyword, all_results, "The keyword is not in the auto suggested result(s)")

    def test_03_search_in_google_click_the_result(self):
        # """Tests google.org search feature. Searches for the word "test" then
        # verified that some results show up. Click the first result text. This test verifies that
        # the keyword on the result page matches the keyword "test" """

        #Load the main page. In this case the home page of Google.com.
        main_page = page.MainPage(self.driver)
        result_page = page.SearchResultsPage(self.driver)

        #Sets the text of search textbox to "test"
        keyword = main_page.search_text_element = "test"

        time.sleep(2)

        main_page.click_the_first_result()

        #Get the keyword in the result page search textbox
        word = result_page.search_text_element
        #Verifies that the keyword on the search result page search textbox matches the keyword entered on the main page
        self.assertEqual(word, keyword, "The result page search textbox keyword is wrong")

    @classmethod 
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/Users/cuicuiyuan/Documents/DemoGoogleSearch/Reports"))