import Room
import Constants as c


class E15_R3(Room.Room):

    def __init__(self):
        super().__init__('Hannibal', 'https://www.fugacemente.it/cinecitta/room/hannibal/', 'E15_R3')

    def get_prices(self):
        p = ['2 GIOCATORI – € 50,00',
             '3 GIOCATORI – € 60,00',
             '4 GIOCATORI – € 72,00',
             '5 GIOCATORI – € 90,00',
             '6 GIOCATORI – € 108,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
