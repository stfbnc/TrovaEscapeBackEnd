import Room
import Constants as c


class E32_R2(Room.Room):

    def __init__(self):
        super().__init__('Il Segreto del Vaticano', 'http://www.thedoor.it/roma/prenotazioni.php?s=2', 'E32_R2')

    def get_prices(self):
        p = ['2-6 GIOCATORI – A PARTIRE DA € 45,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
