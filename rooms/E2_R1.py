import Room
import Constants as c


class E2_R1(Room.Room):

    def __init__(self):
        super().__init__('The Ring', 'https://www.escaperoomroma.it/the-ring/', 'E2_R1')

    def get_prices(self):
        p = ['FINO A 4 GIOCATORI – € 90,00 totali',
             '5 GIOCATORI – € 20,00 a persona',
             '6 GIOCATORI – € 20,00 a persona',
             '7 GIOCATORI – € 20,00 a persona',
             '8+ GIOCATORI – € 20,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""