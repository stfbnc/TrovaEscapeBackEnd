import Room
import Constants as c


class E18_R1(Room.Room):

    def __init__(self):
        super().__init__('Accademia delle Streghe', 'https://www.fugacemente.it/roma-colle-prenestino/escape-room/accademia-delle-streghe/', 'E18_R1')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
