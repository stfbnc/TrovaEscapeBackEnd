import Constants as C


class Escape:

    def __init__(self,
                 name,
                 short_name,
                 address,
                 phone,
                 website,
                 lat,
                 lon,
                 tags,
                 code):
        self.name = name
        self.short_name = short_name
        self.address = address
        self.phone = phone
        self.website = website
        self.lat = lat
        self.lon = lon
        self.tags = tags
        self.code = code
        self.rooms = []

    def set_rooms(self, rooms):
        self.rooms = rooms

    def get_escape_object(self):
        escape = {C.ESCAPE_NAME_TAG: self.name,
                  C.ESCAPE_SHORT_NAME_TAG: self.short_name,
                  C.ESCAPE_ADDRESS_TAG: self.address,
                  C.ESCAPE_PHONE_TAG: self.phone,
                  C.ESCAPE_WEBSITE_TAG: self.website,
                  C.ESCAPE_LAT_TAG: self.lat,
                  C.ESCAPE_LON_TAG: self.lon,
                  C.ESCAPE_TAGS_TAG: self.tags,
                  C.ESCAPE_CODE_TAG: self.code,
                  C.ROOMS_TAG: self.rooms}
        return escape
