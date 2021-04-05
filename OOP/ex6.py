# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
# # If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

