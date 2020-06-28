import Room
import Constants as c


class E23_R3(Room.Room):

    def __init__(self):
        super().__init__('Il Segreto dei Templari', 'http://d.supersaas.it/schedule/La_Casa_Degli_Enigmi/RM_Il%20Segreto%20dei%20Templari', 'E23_R3')

    def get_prices(self):
        p = ['2 GIOCATORI – € 25,00 (lun-gio) / € 30,00 (ven-dom) a persona',
             '3 GIOCATORI – € 20,00 (lun-gio) / € 22,00 (ven-dom) a persona',
             '4 GIOCATORI – € 16,00 (lun-gio) / € 18,00 (ven-dom) a persona',
             '5 GIOCATORI – € 15,00 (lun-gio) / € 16,00 (ven-dom) a persona',
             '6-7 GIOCATORI – € 14,00 (lun-gio) / € 15,00 (ven-dom) a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return c.NO_RETR_AVAILS
