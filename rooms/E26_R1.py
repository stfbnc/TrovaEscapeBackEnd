import Room
import Constants as c


class E26_R1(Room.Room):

    def __init__(self):
        super().__init__('La Monaca di Valkenburg', 'https://getoutroma.it/la-monaca-di-valkenburg/', 'E26_R1')

    def get_prices(self):
        p = ['2-3 GIOCATORI – € 30,00 a persona',
             '4 GIOCATORI – € 25,00 a persona',
             '5-7 GIOCATORI – € 20,00 a persona',
             '8+ GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
