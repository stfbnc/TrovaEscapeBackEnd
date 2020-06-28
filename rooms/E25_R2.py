import Room
import Constants as c


class E25_R2(Room.Room):

    def __init__(self):
        super().__init__('Sabotage', 'https://roma.secret-rooms.it/negozio/prenotazioni/prenotazione-stanza-sabotage-roma/', 'E25_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 50,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
