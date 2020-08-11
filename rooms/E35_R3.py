import Room
import Constants as c


class E35_R3(Room.Room):

    def __init__(self):
        super().__init__('Armageddon', 'http://www.escapecampodeifiori.com/prenota/', 'E35_R3')

    def get_prices(self):
        p = ['2-3 GIOCATORI – € 60,00',
             '4 GIOCATORI – € 80,00',
             '5 GIOCATORI – € 100,00',
             '6 GIOCATORI – € 120,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
