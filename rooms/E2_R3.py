import Room
import Constants as c


class E2_R3(Room.Room):

    def __init__(self):
        super().__init__('L\'Esorcista - Parte 2', 'https://www.escaperoomroma.it/esorcista-il-cimitero/', 'E2_R3')

    def get_prices(self):
        p = ['FINO A 4 GIOCATORI – € 90,00 totali',
             '5 GIOCATORI – € 20,00 a persona',
             '6 GIOCATORI – € 20,00 a persona',
             '7 GIOCATORI – € 20,00 a persona',
             '8+ GIOCATORI – € 20,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
