import Room
import Constants as c


class E9_R2(Room.Room):

    def __init__(self):
        super().__init__('Accademia di Magia e Stregoneria', 'https://www.nox-escape.com/mizar-magia/', 'E9_R2')

    def get_prices(self):
        p = ['3 GIOCATORI – € 69,00',
             '4 GIOCATORI – € 80,00',
             '5 GIOCATORI – € 80,00',
             '6 GIOCATORI – € 90,00',
             'FAMIGLIA (1 O 2 ADULTI + 2 O 3 UNDER 14) – € 60,00']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
