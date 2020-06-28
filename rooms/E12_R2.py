import Room
import Constants as c


class E12_R2(Room.Room):

    def __init__(self):
        super().__init__('Infected', 'https://questhouse.it/rooms/infected/', 'E12_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4 GIOCATORI – € 18,00 a persona',
             '5 GIOCATORI – € 16,00 a persona',
             '6 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
