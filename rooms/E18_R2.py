import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options


class E18_R2(Room.Room):

    def __init__(self):
        super().__init__('Zombie Lab', 'https://www.fugacemente.it/roma-colle-prenestino/escape-room/zombie-lab/', 'E18_R2')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        wait_time = 10
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(self.website)
        avails = []

        print(self.code)

        try:
            wait = WebDriverWait(driver, wait_time)
            iframe_element = wait.until(presence_of_element_located((By.XPATH, '//*[@class="container"]//iframe')))
            driver.switch_to.frame(iframe_element)

            wait.until(
                presence_of_element_located((By.XPATH, '//*[@class="bct-room-col j_tab_content_1 j_room_pk_3"]/span')))
            all_time_elems = driver.find_elements_by_xpath(
                '//*[@class="bct-room-col j_tab_content_1 j_room_pk_3"]/span')

            for elem in all_time_elems:
                if elem.get_attribute('class') != 'btn-no':
                    avails.append(elem.text)
        except:
            print('Page timed out after {} secs'.format(wait_time))

        driver.quit()

        return c.SEPARATOR.join(avails)
