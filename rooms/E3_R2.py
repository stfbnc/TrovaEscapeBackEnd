import Room
import Constants as c


class E3_R2(Room.Room):

    def __init__(self):
        super().__init__('La piccola Emily', 'https://magicescape.it/le-stanze/la-piccola-emily/', 'E3_R2')

    def get_prices(self):
        p = ['1 persona: 25,00 €',
             '2 persone: 50,00 €',
             '3 persone: 60,00 €',
             '4 persone: 60,00 €']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
