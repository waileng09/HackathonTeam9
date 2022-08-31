class User:
    count_id = 0
    def __init__(self, first_name, last_name, email_address, password, password2, type):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__password = password
        self.__password2 = password2
        self.__type = type

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_email_address(self):
        return self.__email_address

    def set_password(self,password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password2(self,password2):
        self.__password2 = password2

    def get_password2(self):
        return self.__password2

    def set_type(self,type):
        self.__type = type

    def get_type(self):
        return self.__type

    def confirm(self):
        if self.get_password() == self.get_password2():
            return True

        else:
            return False



