import Room
import Constants as c


class E5_R1(Room.Room):

    def __init__(self):
        super().__init__('Ouija - Paranormal experience', 'https://cogitoergoroom.it/services/ouija/', 'E5_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 30,00 a persona',
             '3 GIOCATORI – € 25,00 a persona',
             '4/6 GIOCATORI – € 20,00 a persona',
             '7/8+ GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
