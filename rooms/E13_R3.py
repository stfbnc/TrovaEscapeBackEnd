import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options


class E13_R3(Room.Room):

    def __init__(self):
        super().__init__('Il Giocattolaio', 'https://www.adventurerooms.it/roma/services/il-giocattolaio/', 'E13_R3')

    def get_prices(self):
        p = ['2 GIOCATORI – € 20,00 a persona',
             '3 GIOCATORI – € 17,50 a persona',
             '4-5 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

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

            wait.until(presence_of_element_located((By.XPATH, '//*[@class="app_timetable_wrapper"]//div')))
            all_time_elems = driver.find_elements_by_xpath('//*[@class="app_timetable_wrapper"]//div')

            title = 0
            for elem in all_time_elems:
                if elem.get_attribute('class') == 'app_timetable_title':
                    title += 1
                if 'free' in elem.get_attribute('class').split():
                    avails.append(elem.text)
                if title == 2:
                    break
        except:
            print('Page timed out after {} secs'.format(wait_time))

        driver.quit()

        return c.SEPARATOR.join(avails)
