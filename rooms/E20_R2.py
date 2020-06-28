import Room
import Constants as c


class E20_R2(Room.Room):

    def __init__(self):
        super().__init__('Stanza di 50 Sfumature', 'https://www.fugacemente.it/roma-san-lorenzo/escape-room/stanza-50-sfumature/', 'E20_R2')

    def get_prices(self):
        return c.NO_RETR_PRICES

    def get_availabilities(self):
        return ""
