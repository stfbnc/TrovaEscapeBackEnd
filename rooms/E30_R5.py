import Room
import Constants as c


class E30_R5(Room.Room):

    def __init__(self):
        super().__init__('Jack lo Squartatore', 'https://roma.escapegameover.it/rooms/jack-the-ripper.html', 'E30_R5')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4 GIOCATORI – € 19,00 a persona',
             '5 GIOCATORI – € 17,00 a persona',
             '6 GIOCATORI – € 16,00 a persona',
             '7 GIOCATORI – € 16,00 a persona',
             '8 GIOCATORI – € 16,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
