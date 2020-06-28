import Room
import Constants as c


class E38_R2(Room.Room):

    def __init__(self):
        super().__init__('Il Vecchio Luna Park', 'http://www.mentalmenteescaperoom.it/room/escape-room-roma-2/', 'E38_R2')

    def get_prices(self):
        p = ['2-6 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
