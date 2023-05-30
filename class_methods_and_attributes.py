# In a class method we can only access class attributes

class Car:

    # Class attribute. Here this attribute will contain the number of instances of the class Car we created
    number_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.number_of_cars += 1 # The class attribute is incremented by 1 each time a new instance is created

    @classmethod
    def update_number_of_cars(cls, cars):
        # update the number of cars by passing the parameter cars
        cls.number_of_cars = cars   # cls is mandatory and stands for the name of the class
        print("Run")


c1 = Car("Ford", "Edge")
c2 = Car("Peugeot", "3008")
Car.update_number_of_cars(10)

print(f"c1: {c1.number_of_cars}")
print(f"c2: {c2.number_of_cars}")
print(f"Car: {Car.number_of_cars}")

#################################################################################

class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)

print(Circle.get_area_and_perimeter(3))