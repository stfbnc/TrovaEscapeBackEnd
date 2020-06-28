import Room
import Constants as c


class E19_R1(Room.Room):

    def __init__(self):
        super().__init__('Notte da Leoni', 'https://www.fugacemente.it/roma-tor-vergata/escape-room/notte-da-leoni/', 'E19_R1')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
