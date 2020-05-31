import Room
import Constants as c


class E28_R3(Room.Room):

    def __init__(self):
        super().__init__('L''Inferno di Dante', 'https://roma.cronos.house/linferno-di-dante/', 'E28_R3')

    def get_prices(self):
        p = ['2-3 GIOCATORI – € 25,00 a persona',
             '4-6 GIOCATORI – € 20,00 a persona',
             '7-8 GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
