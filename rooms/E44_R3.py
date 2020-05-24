import Room
import Constants as c


class E44_R3(Room.Room):

    def __init__(self):
        super().__init__('La Stanza del Mese', 'https://escapeoddityroma.simplybook.it/v2/?widget-type=iframe&theme=tender&theme=tender&timeline=modern&datepicker=top_calendar#book/service/6/count/1/provider/1/', 'E44_R3')

    def get_prices(self):
        p = ['€ 12,00 a persona']

        return c.SEPARATOR.join(p)

    def get_availabilities(self):
        return ""
