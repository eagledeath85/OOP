class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hello my name is {self.first_name} {self.last_name}")


# Class Employee inherits from class Person
# An Employee instance will then have access to all the methods of the Person class
class Employee(Person):
    # When we want to use the constructor of the parent class, we override it using the super() keyword
    # The child constructor needs AT LEAST to require the same parameters as the parent constructor
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary


    # If we want to use a parent method but modify it a little bit, we override it.
    # say_hello() method from Person class is overridden with the one below.
    # To get access to the parent method, we'll use the keyword super()
    def say_hello(self):
        print("-----------")
        super().say_hello()
        print("-----------")

    def test(self):
        print("test")


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department


class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth


o = Owner("John", "Doe", 300000)
o.say_hello()

m = Manager("Peter", "North", 80000, "Sales")

############ isinstance() #################

# When manipulating inheritance, we can check if an object is an instance of a specific class with the isinstance() method
# We check whether the object o is an instance of Person
print(isinstance(o, Person))
print(isinstance(m, Person))

############# Multiple Inheritances #############

# A class can inherit from multiple classes.
# In that case, we'll look for methods primarily in the first class declared in parentheses.
# If the method doesn't exist in the first parent class, we'll look in the second parent class
class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A, B):
    pass

c = C()
