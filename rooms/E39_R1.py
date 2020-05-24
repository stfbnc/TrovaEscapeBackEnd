import Room
import Constants as c


class E39_R1(Room.Room):

    def __init__(self):
        super().__init__('The Black Room', 'http://www.fugacity.it/services/the-black-room/', 'E39_R1')

    def get_prices(self):
        return ''

    def get_availabilities(self):
        return ""
