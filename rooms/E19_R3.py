import Room
import Constants as c


class E19_R3(Room.Room):

    def __init__(self):
        super().__init__('Assalto alla Zecca', 'https://www.fugacemente.it/roma-tor-vergata/escape-room/assalto-alla-zecca/', 'E19_R3')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
