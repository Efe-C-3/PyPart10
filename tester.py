class Car:
    """Represents a wheeled motor vehicle used for transportation."""


my_car = Car()
my_car.make = 'chevy'
my_car.model = 'camaro'
my_car.transmission = 'manual'


def print_car_details(car):
    print("Car make: %s" % car.make)
    print("Car model: %s" % car.model)
    print("Transmission: %s" % car.transmission)


print_car_details(my_car)
