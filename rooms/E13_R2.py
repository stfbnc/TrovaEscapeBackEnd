import Room
import Constants as c


class E13_R2(Room.Room):

    def __init__(self):
        super().__init__('Fuga dal Manicomio', 'https://www.adventurerooms.it/roma/services/fuga-dal-manicomio/', 'E13_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4-5 GIOCATORI – € 17,50 a persona',
             '6-12 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
