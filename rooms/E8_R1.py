import Room
import Constants as c


class E8_R1(Room.Room):

    def __init__(self):
        super().__init__('I misteri della terra di mezzo', 'http://www.escaperoomrealgame.it/room/i-misteri-della-terra-di-mezzo/', 'E8_R1')

    def get_prices(self):
        p = ['2 giocatori : €25,00 a persona',
             '3 giocatori : €20,00 a persona',
             '4 giocatori : €17,50 a persona',
             '5 giocatori : €15,00 a persona',
             '6 giocatori : €15,00 a persona',
             '7 giocatori : €15,00 a persona',
             '8 giocatori : €15,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
