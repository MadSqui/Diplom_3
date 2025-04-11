from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_load_element(self,locators):
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(locators))

    def find_element(self,locators):
        return self.driver.find_element(*locators)

    def current_url(self):
        return self.driver.current_url
    def execute_scripts(self,element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_for_element(self,locators):
        return self.driver.find_element(*locators).text

    def drag_and_drop(self,element1,element2):
        element1 = self.driver.find_element(*element1)
        element2 = self.driver.find_element(*element2)
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()

    def wait_for_clickable_element(self,locators):
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(locators))

    def wait_for_invisibility_element(self,locators):
        WebDriverWait(self.driver,20).until(expected_conditions.invisibility_of_element_located(locators))

    def open_url(self, url):
        self.driver.get(url)