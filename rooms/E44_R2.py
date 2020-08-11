import Room
import Constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options


class E44_R2(Room.Room):

    def __init__(self):
        super().__init__('Lo Studio di Leonardo da Vinci', 'https://escapeoddityroma.simplybook.it/v2/?widget-type=iframe&theme=tender&theme=tender&timeline=modern&datepicker=top_calendar#book/service/2/count/1/provider/1/', 'E44_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 20,00 (lun-gio) / € 25,00 (ven-dom) a persona',
             '3 GIOCATORI – € 19,00 (lun-gio) / € 24,00 (ven-dom) a persona',
             '4 GIOCATORI – € 16,50 (lun-gio) / € 22,00 (ven-dom) a persona',
             '5 GIOCATORI – € 15,00 (lun-gio) / € 20,00 (ven-dom) a persona',
             '6+ GIOCATORI – € 13,50 (lun-gio) / € 18,00 (ven-dom) a persona']

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
