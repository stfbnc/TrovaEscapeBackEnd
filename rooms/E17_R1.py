import Room
import Constants as c


class E17_R1(Room.Room):

    def __init__(self):
        super().__init__('Ultimo Horcrux', 'https://www.fugacemente.it/roma-anagnina/escape-room/ultimo-horcrux/', 'E17_R1')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
