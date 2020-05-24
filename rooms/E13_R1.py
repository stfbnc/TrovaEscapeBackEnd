import Room
import Constants as c


class E13_R1(Room.Room):

    def __init__(self):
        super().__init__('Lo Scienziato Pazzo', 'https://www.adventurerooms.it/roma/services/lo-scienziato-pazzo/', 'E13_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4-5 GIOCATORI – € 17,50 a persona',
             '6-12 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
