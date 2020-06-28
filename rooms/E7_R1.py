import Room
import Constants as c


class E7_R1(Room.Room):

    def __init__(self):
        super().__init__('Rapina alla banca', 'https://www.tribescaperoom.it/avventure/rapina-alla-banca/', 'E7_R1')

    def get_prices(self):
        p = ['2 GIOCATORI: 50€ (25€ a persona)',
             '3 GIOCATORI: 60€ (20€ a persona)',
             '4 GIOCATORI: 76€ (19€ a persona)',
             '5 GIOCATORI: 85€ (17€ a persona)',
             '6 GIOCATORI: 96€ (16€ a persona)',
             '7 GIOCATORI: 112€ (16€ a persona)',
             '8 GIOCATORI: 128€ (16€ a persona)']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
