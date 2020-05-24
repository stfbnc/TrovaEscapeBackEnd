import Room
import Constants as c


class E27_R2(Room.Room):

    def __init__(self):
        super().__init__('Vendetta', 'https://magicescape.it/vendetta/', 'E27_R2')

    def get_prices(self):
        p = ['1 GIOCATORE – € 30,00',
             '2 GIOCATORI – € 60,00',
             '3 GIOCATORI – € 75,00',
             '4 GIOCATORI – € 80,00',
             '5 GIOCATORI – € 100,00',
             '6 GIOCATORI – € 120,00',
             '7 GIOCATORI – € 140,00',
             '8 GIOCATORI – € 160,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
