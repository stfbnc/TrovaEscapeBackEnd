import Room
import Constants as c


class E30_R1(Room.Room):

    def __init__(self):
        super().__init__('Scuola di Magia', 'https://roma.escapegameover.it/rooms/philosophers-stone.html', 'E30_R1')

    def get_prices(self):
        p = ['4 GIOCATORI – € 22,50 a persona',
             '5 GIOCATORI – € 20,00 a persona',
             '6 GIOCATORI – € 20,00 a persona',
             '7 GIOCATORI – € 20,00 a persona',
             '8 GIOCATORI – € 20,00 a persona',
             '9 GIOCATORI – € 20,00 a persona',
             '10 GIOCATORI – € 20,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
