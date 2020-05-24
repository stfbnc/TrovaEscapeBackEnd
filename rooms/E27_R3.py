import Room
import Constants as c


class E27_R3(Room.Room):

    def __init__(self):
        super().__init__('Creature Magiche', 'https://magicescape.it/le-stanze/creature-magiche/', 'E27_R3')

    def get_prices(self):
        p = ['1 GIOCATORE – € 30,00',
             '2 GIOCATORI – € 60,00',
             '3 GIOCATORI – € 75,00',
             '4 GIOCATORI – € 80,00',
             '5 GIOCATORI – € 100,00',
             '6 GIOCATORI – € 120,00',
             '7 GIOCATORI – € 140,00',
             'FAMIGLIE: (2 ADULTI e 2 BAMBINI) – € 160,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
