# Tutorial from: https://pynative.com/python-object-oriented-programming-oop-exercise/

# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(160,0)
print(modelX.max_speed, modelX.mileage)

# magic functions in Pyhton: https://www.tutorialsteacher.com/python/magic-methods-in-python
