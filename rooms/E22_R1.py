import Room
import Constants as c


class E22_R1(Room.Room):

    def __init__(self):
        super().__init__('La Stanza di Van Gogh', 'https://www.nox-escape.com/', 'E22_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 40,00',
             '3 GIOCATORI – € 54,00',
             '4 GIOCATORI – € 60,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
