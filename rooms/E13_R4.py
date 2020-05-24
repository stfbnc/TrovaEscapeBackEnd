import Room
import Constants as c


class E13_R4(Room.Room):

    def __init__(self):
        super().__init__('Alcatraz', 'https://www.adventurerooms.it/roma/services/alcatraz/', 'E13_R4')

    def get_prices(self):
        p = ['3 GIOCATORI – € 23,00 a persona',
             '4-12 GIOCATORI – € 20,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
