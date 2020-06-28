import Room
import Constants as c


class E28_R4(Room.Room):

    def __init__(self):
        super().__init__('Jurassic World', 'https://roma.cronos.house/jurassic-world/', 'E28_R4')

    def get_prices(self):
        p = ['2-3 GIOCATORI – € 25,00 a persona',
             '4-6 GIOCATORI – € 20,00 a persona',
             '7 GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
