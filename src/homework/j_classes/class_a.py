import random

class Die:
    def roll(self):
        self.__roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return self.__roll_value

    def __str__(self):
        return "The rolled value is " + str(self.__roll_value)
