import Room
import Constants as c


class E17_R3(Room.Room):

    def __init__(self):
        super().__init__('Dexter - Destino di Sangue', 'https://www.fugacemente.it/roma-anagnina/escape-room/dexter-destino-di-sangue/', 'E17_R3')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
