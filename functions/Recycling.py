from functions import ParentRecycling

class Recycling:
    def __int__(self, form_id, date, type, weight, description, image):
        self.form_id = form_id
        self._date = date
        self._type = type
        self._weight = weight
        self._description = description
        self._image = image

    def set_id(self, form_id):
        self.form_id = form_id

    def get_id(self): return self.form_id

    def set_date(self, date):
        self._date = date

    def get_date(self): return self._date

    def set_type(self, type):
        self._type = type

    def get_type(self): return self._type

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self): return self._weight

    def set_description(self, description):
        self._description = description

    def get_description(self): return self._description

    def set_image(self, image):
        self._image = image

    def get_image(self): return self._image
