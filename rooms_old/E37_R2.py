import Room
import Constants as c


class E37_R2(Room.Room):

    def __init__(self):
        super().__init__('Ufficio del Serial Killer', 'https://www.fugacemente.it/castelgandolfo/room/ufficio-del-serial-killer/', 'E37_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 50,00',
             '3 GIOCATORI – € 60,00',
             '4 GIOCATORI – € 72,00',
             '5 GIOCATORI – € 90,00',
             '6 GIOCATORI – € 108,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
