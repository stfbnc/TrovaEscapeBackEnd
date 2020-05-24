import Room
import Constants as c


class E14_R1(Room.Room):

    def __init__(self):
        super().__init__('Asylum - La Cinica degli Orrori', 'https://www.escaperoomroma.it/asylum-clinica-degli-orrori/', 'E14_R1')

    def get_prices(self):
        p = ['4 GIOCATORI – € 30,00 a persona',
             '5 GIOCATORI – € 30,00 a persona',
             '6 GIOCATORI – € 25,00 a persona',
             '7 GIOCATORI – € 25,00 a persona',
             '8 GIOCATORI – € 25,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
