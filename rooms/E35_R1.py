import Room
import Constants as c


class E35_R1(Room.Room):

    def __init__(self):
        super().__init__('Egyptian', 'http://www.escapecampodeifiori.com/prenota/', 'E35_R1')

    def get_prices(self):
        p = ['2-3 GIOCATORI – € 60,00',
             '4 GIOCATORI – € 80,00',
             '5 GIOCATORI – € 100,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
