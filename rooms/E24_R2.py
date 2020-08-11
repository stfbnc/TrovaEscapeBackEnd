import Room
import Constants as c


class E24_R2(Room.Room):

    def __init__(self):
        super().__init__('Amnesia Totale', 'https://escaperoomromaexitus.com/quest/amnesiatotale/', 'E24_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4-8 GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
