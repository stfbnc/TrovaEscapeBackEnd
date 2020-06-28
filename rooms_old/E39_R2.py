import Room
import Constants as c


class E39_R2(Room.Room):

    def __init__(self):
        super().__init__('La Casa di Julie', 'http://www.fugacity.it/services/la-casa-di-julie/', 'E39_R2')

    def get_prices(self):
        return ''

    def get_availabilities(self):
        return ""
