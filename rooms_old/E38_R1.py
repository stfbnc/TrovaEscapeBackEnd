import Room
import Constants as c


class E38_R1(Room.Room):

    def __init__(self):
        super().__init__('La Piramide di Zafira', 'http://www.mentalmenteescaperoom.it/room/escape-room-roma-1/', 'E38_R1')

    def get_prices(self):
        p = ['2-6 GIOCATORI – € 15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
