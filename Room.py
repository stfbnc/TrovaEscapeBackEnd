import Constants as C


class Room:

    def __init__(self,
                 name,
                 website,
                 code):
        self.name = name
        self.website = website
        self.code = code
        self.prices = ""
        self.avails = ""

    def get_prices(self):
        return ""

    def get_availabilities(self):
        return ""

    def get_room_object(self):
        room = {C.ROOMS_NAME_TAG: self.name,
                C.ROOMS_WEBSITE_TAG: self.website,
                C.ROOMS_PRICES_TAG: self.get_prices(),
                C.ROOMS_AVAIL_TAG: self.get_availabilities(),
                C.ROOMS_CODE_TAG: self.code}
        return room
