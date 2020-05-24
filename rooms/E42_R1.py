import Room
import Constants as c


class E42_R1(Room.Room):

    def __init__(self):
        super().__init__('Atto I - Le Sorelle', 'https://www.lacasadelmale.it/rooms/le-sorelle/', 'E42_R1')

    def get_prices(self):
        p = ['TURNO VERDE:',
             '1-4 GIOCATORI – € 140,00 totali',
             '6-12 GIOCATORI – € 35,00 a persona',
             'TURNO GIALLO:',
             '1 GIOCATORE – € 70,00 totali',
             '2-12 GIOCATORI – € 35,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
