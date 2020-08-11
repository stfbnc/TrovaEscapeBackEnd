import Room
import Constants as c


class E40_R2(Room.Room):

    def __init__(self):
        super().__init__('Il Nuovo Incubo 2 - Il Risveglio di Amanda', 'http://www.luciferescaperoom.it/prenota-il-risveglio-di-amanda/', 'E40_R2')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
