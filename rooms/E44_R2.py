import Room
import Constants as c


class E44_R2(Room.Room):

    def __init__(self):
        super().__init__('Lo Studio di Leonardo da Vinci', 'https://escapeoddityroma.simplybook.it/v2/?widget-type=iframe&theme=tender&theme=tender&timeline=modern&datepicker=top_calendar#book/service/2/count/1/provider/1/', 'E44_R2')

    def get_prices(self):
        p = ['2 GIOCATORI – € 20,00 (lun-gio) / € 25,00 (ven-dom) a persona',
             '3 GIOCATORI – € 19,00 (lun-gio) / € 24,00 (ven-dom) a persona',
             '4 GIOCATORI – € 16,50 (lun-gio) / € 22,00 (ven-dom) a persona',
             '5 GIOCATORI – € 15,00 (lun-gio) / € 20,00 (ven-dom) a persona',
             '6+ GIOCATORI – € 13,50 (lun-gio) / € 18,00 (ven-dom) a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
