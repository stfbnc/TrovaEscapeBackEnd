import Room
import Constants as c


class E3_R3(Room.Room):

    def __init__(self):
        super().__init__('Fuga dalla prigione dei maghi', 'https://magicescape.it/le-stanze/fuga-dalla-prigione-dei-maghi/', 'E3_R3')

    def get_prices(self):
        p = ['1 persona: 30,00 €',
             '2 persone: 60,00 €',
             '3 persone: 75,00 €',
             '4 persone: 80,00 €',
             '5 persone: 100,00 €',
             '6 persone: 120,00 €',
             'Famiglie: (2 adulti e 2 bambini) 60,00€']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
