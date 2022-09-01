import shelve
import User


class Customer (User.User):
    count_id = 0
    def __init__(self, first_name, Last_name, email_address, password, password2, type, birthday):
        super().__init__(first_name, Last_name, email_address, password, password2, type)
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__birthday = birthday
        self.__points = 50

    #for rewards
    def set_points(self,points):
        self.__points = points

    #for rewards
    def get_points(self):
        return self.__points

    def set_customer_id(self, customer_id):
        self.__customer_id =  customer_id

    def get_customer_id(self):
        return self.__customer_id

    def set_birthday(self, birthday):
        self.__birthday = birthday

    def get_birthday(self):
        return self.__birthday

    def __str__(self):
        print("A Customer with id {} is created".format(self.get_customer_id()))

    def confirm(self):
        if self.get_password() == self.get_password2():
            return True

        else:
            return False

