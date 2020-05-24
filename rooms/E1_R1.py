import Room
import Constants as c


class E1_R1(Room.Room):

    def __init__(self):
        super().__init__('L''Annegatore', 'https://www.escaperoomroma.it/annegatore/', 'E1_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 a persona',
             '3 GIOCATORI – € 20,00 a persona',
             '4 GIOCATORI – € 18,50 a persona',
             '5 GIOCATORI – € 17,50 a persona',
             '6 GIOCATORI – € 16,00 a persona',
             '7 GIOCATORI – € 15,00 a persona',
             '8 GIOCATORI – € 15,00 a persona',
             '9 GIOCATORI – € 15,00 a persona',
             '10 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
