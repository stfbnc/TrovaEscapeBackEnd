import Room
import Constants as c


class E9_R1(Room.Room):

    def __init__(self):
        super().__init__('Black Mirror - Fuga dal sogno', 'https://www.nox-escape.com/black-mirror/', 'E9_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 60,00',
             '3 GIOCATORI – € 60,00',
             '4 GIOCATORI – € 70,00',
             '5 GIOCATORI – € 75,00',
             '6 GIOCATORI – € 90,00',
             '6 GIOCATORI (UNDER 18) – € 72,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
