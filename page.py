from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    # """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    # """Base class to initialize the base page that will be called from all
    # pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    # """Home page action methods come here. I.e. Google.com"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        # """Verifies that the hardcoded text "Google" appears in page title"""

        return "Google" in self.driver.title

    def result_count(self):
        # Get the number of suggested results
        return len(self.driver.find_elements(*MainPageLocators.RESULTS))

    def results(self):
        # Get the auto suggested result elements
        return self.driver.find_elements(*MainPageLocators.RESULTS)

    def resultText(self, elem):
        # Get the auto suggested result html text
        return elem.get_attribute("innerHTML")

    def main_results(self):
        # Get the auto suggested nested span result elements
        return self.driver.find_elements(*MainPageLocators.MAIN_RESULTS)

    def main_resultText(self, elem):
        # Get the auto suggested nested span result text
        return elem.text

    def click_the_first_result(self):
        # Click the first suggested result
        self.driver.find_element(*MainPageLocators.FIRST_RESULT).click()


class SearchResultsPage(BasePage):
    # """Search results page action methods come here"""
    # Get the search textbox value
    search_text_element = SearchTextElement()

