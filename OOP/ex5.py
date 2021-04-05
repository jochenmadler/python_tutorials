# efine a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:

    # class attribute, same for every instance
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

