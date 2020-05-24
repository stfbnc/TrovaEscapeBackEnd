import Room
import Constants as c


class E12_R1(Room.Room):

    def __init__(self):
        super().__init__('Alice', 'https://questhouse.it/rooms/alice/', 'E12_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 30,00 a persona',
             '3 GIOCATORI – € 25,00 a persona',
             '4 GIOCATORI – € 22,00 a persona',
             '5 GIOCATORI – € 20,00 a persona',
             '6 GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
