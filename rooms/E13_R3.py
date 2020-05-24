import Room
import Constants as c


class E13_R3(Room.Room):

    def __init__(self):
        super().__init__('Il Giocattolaio', 'https://www.adventurerooms.it/roma/services/il-giocattolaio/', 'E13_R3')

    def get_prices(self):
        p = ['2 GIOCATORI – € 20,00 a persona',
             '3 GIOCATORI – € 17,50 a persona',
             '4-5 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
