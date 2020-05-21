import Room
import Constants as c


class E3_R1(Room.Room):

    def __init__(self):
        super().__init__('Lo studio di Harry Houdini', 'https://magicescape.it/le-stanze/lo-studio-di-harry-houdini/', 'E3_R1')

    def get_prices(self):
        p = ['1 persona: 25,00 €',
             '2 persone: 50,00 €',
             '3 persone: 75,00 €',
             '4 persone: 80,00 €',
             '5 persone: 90,00 €',
             '6 persone: 90,00 €',
             '7 persone: 105,00 €',
             '8 persone: 120,00 €',
             'Famiglie: (2 adulti e 2 bambini) 60,00€']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
