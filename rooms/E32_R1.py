import Room
import Constants as c


class E32_R1(Room.Room):

    def __init__(self):
        super().__init__('CSI', 'http://www.thedoor.it/roma/prenotazioni.php?s=1', 'E32_R1')

    def get_prices(self):
        p = ['2-6 GIOCATORI – A PARTIRE DA € 45,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
