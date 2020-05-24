import Room
import Constants as c


class E16_R3(Room.Room):

    def __init__(self):
        super().__init__('Jekyll e Hyde', 'https://www.fugacemente.it/timeadventures/room/jekyll-e-hyde/', 'E16_R3')

    def get_prices(self):
        p = ['2 GIOCATORI – € 50,00',
             '3 GIOCATORI – € 60,00',
             '4 GIOCATORI – € 72,00',
             '5 GIOCATORI – € 90,00',
             '6 GIOCATORI – € 108,00',
             'OLTRE 6 GIOCATORI – € 18,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
