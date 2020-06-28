import Room
import Constants as c


class E19_R2(Room.Room):

    def __init__(self):
        super().__init__('Monaco Oscuro', 'https://www.fugacemente.it/roma-tor-vergata/escape-room/monaco-oscuro/', 'E19_R2')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
