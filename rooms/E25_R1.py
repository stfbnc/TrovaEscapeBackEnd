import Room
import Constants as c


class E25_R1(Room.Room):

    def __init__(self):
        super().__init__('Nightmare', 'https://roma.secret-rooms.it/negozio/prenotazioni/prenotazione-stanza-nightmare-roma/', 'E25_R1')

    def get_prices(self):
        p = ['2 GIOCATORI – € 50,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
