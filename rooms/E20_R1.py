import Room
import Constants as c


class E20_R1(Room.Room):

    def __init__(self):
        super().__init__('I Segreti d\'Egitto', 'https://www.fugacemente.it/roma-san-lorenzo/escape-room/segreti-egitto/', 'E20_R1')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
