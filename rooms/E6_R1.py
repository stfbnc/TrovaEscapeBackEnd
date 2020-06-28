import Room
import Constants as c


class E6_R1(Room.Room):

    def __init__(self):
        super().__init__('Hostel - Capitolo 1', 'https://www.thefearescaperoom.it/hostel-capitolo-1/', 'E6_R1')

    def get_prices(self):
        p = ['3 persone 100€',
             '4 persone 120€',
             '5 persone 125€',
             '6 persone 130€',
             '7 persone 140€',
             '8 persone 160€',
             '9 persone 180€',
             '10 persone 200€',
             '11 persone 220€',
             '12 persone 240€']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
