import Room
import Constants as c


class E30_R11(Room.Room):

    def __init__(self):
        super().__init__('La Casa di Carta', 'https://roma.escapegameover.it/rooms/la-mision-del-profesor.html', 'E30_R11')

    def get_prices(self):
        p = ['4 GIOCATORI – € 22,50 a persona',
             '5 GIOCATORI – € 20,00 a persona',
             '6 GIOCATORI – € 20,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
