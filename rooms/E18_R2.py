import Room
import Constants as c


class E18_R2(Room.Room):

    def __init__(self):
        super().__init__('Zombie Lab', 'https://www.fugacemente.it/roma-colle-prenestino/escape-room/zombie-lab/', 'E18_R2')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
