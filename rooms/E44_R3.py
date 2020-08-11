import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options


class E44_R3(Room.Room):

    def __init__(self):
        super().__init__('La Stanza del Mese', 'https://escapeoddityroma.simplybook.it/v2/?widget-type=iframe&theme=tender&theme=tender&timeline=modern&datepicker=top_calendar#book/service/6/count/1/provider/1/', 'E44_R3')

    def get_prices(self):
        p = ['€ 12,00 a persona']

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

            wait.until(presence_of_element_located((By.XPATH, '//*[@id="sb_time_slots_container"]/div/a')))
            all_time_elems = driver.find_elements_by_xpath('//*[@id="sb_time_slots_container"]/div/a')

            for elem in all_time_elems:
                if elem.get_attribute('class') == 'sb-cell free ':
                    avails.append(elem.text)
        except:
            print('Page timed out after {} secs'.format(wait_time))

        driver.quit()

        return c.SEPARATOR.join(avails)
