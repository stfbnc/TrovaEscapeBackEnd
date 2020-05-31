import Room
import Constants as c


class E27_R1(Room.Room):

    def __init__(self):
        super().__init__('Indiana Jones e l''oro di Roma', 'https://magicescape.it/indiana-jones-roma/', 'E27_R1')

    def get_prices(self):
        p = ['1 GIOCATORE – € 30,00',
             '2 GIOCATORI – € 60,00',
             '3 GIOCATORI – € 75,00',
             '4 GIOCATORI – € 80,00',
             '5 GIOCATORI – € 100,00',
             '6 GIOCATORI – € 120,00',
             'FAMIGLIE: (2 ADULTI e 2 BAMBINI) – € 60,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
