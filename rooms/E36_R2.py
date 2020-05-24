import Room
import Constants as c


class E36_R2(Room.Room):

    def __init__(self):
        super().__init__('L\'Inferno Dantesco', 'https://www.experienceescaperoom.it/inferno-dantesco/', 'E36_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4-6 GIOCATORI – € 18,00 a persona',
             '7 GIOCATORI – € 17,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
