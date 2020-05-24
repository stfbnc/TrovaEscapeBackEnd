import Room
import Constants as c


class E12_R3(Room.Room):

    def __init__(self):
        super().__init__('Ultimatum', 'https://questhouse.it/rooms/ultimatum/', 'E12_R3')

    def get_prices(self):
        p = ['4 GIOCATORI – € 20,00 a persona',
             '5 GIOCATORI – € 18,00 a persona',
             '6 GIOCATORI – € 16,00 a persona',
             '7 GIOCATORI – € 14,00 a persona',
             '8+ GIOCATORI – € 12,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
