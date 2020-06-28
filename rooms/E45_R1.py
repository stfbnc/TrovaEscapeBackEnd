import Room
import Constants as c


class E45_R1(Room.Room):

    def __init__(self):
        super().__init__('', '', 'E45_R1')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
