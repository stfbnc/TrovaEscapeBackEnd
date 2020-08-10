import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
#from selenium.webdriver.firefox.options import Options


class E3_R1(Room.Room):

    def __init__(self):
        super().__init__('Lo studio di Harry Houdini', 'https://magicescape.it/le-stanze/lo-studio-di-harry-houdini/', 'E3_R1')

    def get_prices(self):
        p = ['1 persona: 25,00 €',
             '2 persone: 50,00 €',
             '3 persone: 75,00 €',
             '4 persone: 80,00 €',
             '5 persone: 90,00 €',
             '6 persone: 90,00 €',
             '7 persone: 105,00 €',
             '8 persone: 120,00 €',
             'Famiglie: (2 adulti e 2 bambini) 60,00€']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        wait_time = 10
        # options = Options()
        # options.headless = True
        driver = webdriver.Firefox()  # options=options)
        driver.get(self.website)
        avails = []

        print(self.code)

        try:
            wait = WebDriverWait(driver, wait_time)
            iframe_element = wait.until(presence_of_element_located((By.XPATH, '//*[@id="prenota"]//iframe')))
            driver.switch_to.frame(iframe_element)

            wait.until(presence_of_element_located((By.XPATH, '//*[@id="sb_time_slots_container"]/div')))
            all_time_elems = driver.find_elements_by_xpath('//*[@id="sb_time_slots_container"]/div')

            for elem in all_time_elems:
                avails.append(elem.find_element_by_tag_name('a').text)
        except:
            print('Page timed out after {} secs'.format(wait_time))

        driver.quit()

        return c.SEPARATOR.join(avails)
