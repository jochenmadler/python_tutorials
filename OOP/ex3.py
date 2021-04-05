# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

# Vehicle Name: School Volvo Speed: 180 Mileage: 12
bus1 = Bus("School Volvo", 180, 12)
print("Vehicle Name: " + bus1.name + " Speed: " + str(bus1.max_speed) + " Mileage: " + str(bus1.mileage)) 

