
# When we want to access/change a private attribute with the syntax instance.attribute, but still want to perform checks
# on it, we can use the @property decorator. Then, We first declare the getter of the attribute (without get_), then the setter
# The name of the getter is the name of the property

##### THIS ONLY WORKS WITH PRIVATE ATTRIBUTES #####
class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0    # Putting a _ before the attribute indicates this attribute should be private

    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("This value is not valid")
        self._salary = salary

##########################################################################3

class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        print("run")    # just to check it's working fine
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid value")
        self._second = second

t = Time(54)
t.second = 34
print(t.second)