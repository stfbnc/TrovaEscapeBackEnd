import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options


class E2_R2(Room.Room):

    def __init__(self):
        super().__init__('L\'Esorcista - Parte 1', 'https://www.escaperoomroma.it/esorcista-le-origini-del-male/', 'E2_R2')

    def get_prices(self):
        p = ['FINO A 4 GIOCATORI – € 90,00 totali',
             '5 GIOCATORI – € 20,00 a persona',
             '6 GIOCATORI – € 20,00 a persona',
             '7 GIOCATORI – € 20,00 a persona',
             '8+ GIOCATORI – € 20,00 a persona']

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
            iframe_element = wait.until(
                presence_of_element_located((By.XPATH, '//*[@class="et_pb_code_inner"]//iframe')))
            driver.switch_to.frame(iframe_element)

            wait.until(presence_of_element_located((By.XPATH, '//*[@id="sb_time_slots_container"]/div')))
            all_time_elems = driver.find_elements_by_xpath('//*[@id="sb_time_slots_container"]/div')

            for elem in all_time_elems:
                avails.append(elem.find_element_by_tag_name('a').text)
        except:
            print('Page timed out after {} secs'.format(wait_time))

        driver.quit()

        return c.SEPARATOR.join(avails)
