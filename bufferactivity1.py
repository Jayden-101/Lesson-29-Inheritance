# Python program to demonstrate
# issubclass()

# Defining Parent Class
class Vehicle:

    # Constructor
    def __init__(vehicleType):
        print("Vehicle is a ", vehicleType)

# Defining Child Class

class Car(Vehicle):

    # Constructor
    def __init__(self):
        Vehicle.__init__("Car")

# Driver's Code

print(issubclass(Car, Vehicle))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicle)))