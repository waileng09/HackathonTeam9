import shelve


class Recycling:
    def __int__(self, id, date, type, weight, description, image):
        self.__id = id
        self.__date = date
        self.__type = type
        self.__weight = weight
        self.__description = description
        self.__image = image

    def get_id(self): return self.__id

    def set_date(self, date):
        self.__date = date

    def get_date(self): return self.__date

    def set_type(self, type):
        self.__type = type

    def get_type(self): return self.__type

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self): return self.__weight

    def set_description(self, description):
        self.__description = description

    def get_description(self): return self.__description

    def set_image(self, image):
        self.__image = image

    def get_image(self): return self.__image
