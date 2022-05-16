from selenium.webdriver.common.by import By

class MainPageLocators(object):
    # """A class for main page locators. All main page locators should come here"""

    RESULTS = (By.XPATH, "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div[1]/ul[1]/li")
    MAIN_RESULTS = (By.XPATH, "//ul/li[contains(@class,'sbct')]//div[@class='wM6W7d']//span")
    FIRST_RESULT = (By.XPATH, "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div[1]/ul[1]/li[1]")


# class SearchResultsPageLocators(object):
#     # """A class for search results locators. All search results locators should
#     # come here"""

#     pass