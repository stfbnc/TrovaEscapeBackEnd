import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options


class E3_R2(Room.Room):

    def __init__(self):
        super().__init__('La piccola Emily', 'https://magicescape.it/le-stanze/la-piccola-emily/', 'E3_R2')

    def get_prices(self):
        p = ['1 persona: 25,00 €',
             '2 persone: 50,00 €',
             '3 persone: 60,00 €',
             '4 persone: 60,00 €']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        wait_time = 10
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(self.website)
        avails = []

        try:
            wait = WebDriverWait(driver, wait_time)
            iframe_element = wait.until(presence_of_element_located((By.XPATH, '//*[@id="prenota"]//iframe')))
            driver.switch_to.frame(iframe_element)

            wait.until(presence_of_element_located((By.XPATH, '//*[@id="sb_time_slots_container"]/div')))
            all_time_elems = driver.find_elements_by_xpath('//*[@id="sb_time_slots_container"]/div')

            for elem in all_time_elems:
                avails.append(elem.find_element_by_tag_name('a').text)
        except:
            print('E3_R2: Page timed out after {} secs'.format(wait_time))

        driver.quit()

        return c.SEPARATOR.join(avails)
