# Operator Overloading is the ability to implement custom operations on our own classes
# We can overload all the __method__() methods to define ourselves their behavior
# We then are able to do all kind of operations on instances of our classes (add, substract, multiply, calculate length, ...)
import math


#################### OVERLOADING __add__ method ####################
class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number

    # self is the first instance, other is the second instance
    def __add__(self, other):
        # Adding the words of the 2 instances together
        new_words = self.words + ", " + other.words

        # Creating the number page number which is one more than the greatest page of the 2 instances
        new_page = max(self.page_number, other.page_number) + 1

        # Returning a new Page object with new_words, new_page as parameters
        return Page(new_words, new_page)


page1 = Page("This is page1", 1)
page2 = Page("This is page2", 2)

# We want to make page1 + page2 -> page3
page3 = page1 + page2
print(page3.words, page3.page_number)


#################### OVERLOADING __sub__, __mul__  methods ####################
class StoreItem:
    TAX = 0.13  # all items have a fix tax, so TAX is a class attribute

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.price_after_tax = 0  # we will set this attribute with the set_price_after_tax() method
        self.set_price_after_tax()

    def set_price_after_tax(self):
        self.price_after_tax = round(self.price * (1 + self.TAX), 2)

    # We apply a discount to the item before adding the tax
    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)


# The overload of the __sub__ method will allow us to perform something like "bread - 2"
bread = StoreItem("bread", 7)
# discounted_bread = bread - 2
discounted_bread = bread * 0.8
print(f"Discounted price: {discounted_bread.price}")
print(f"Discounted price after tax: {discounted_bread.price_after_tax}")


#################### OVERLOADING __truediv__, __floordiv__, __len__, methods ####################

class Line:
    def __init__(self, point1, point2):  # point1 and point2 are tuples containing coordinates
        self.point1 = point1
        self.point2 = point2

    # __truediv__ is the regular division /
    def __truediv__(self, factor):
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)

    # __floordiv__ is the integer division //
    def __floordiv__(self, factor):
        new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
        new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
        return Line(new_point1, new_point2)

    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2  # in case the distance is negative, we square it
        distance_y = (self.point1[1] - self.point2[1]) ** 2  # in case the distance is negative, we square it
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)  # round the distance because len method must return an integer (python rules)

    def __eq__(self, other):
        if not isinstance(other, Line):
            return False
        return self.point1 == other.point1 and self.point2 == other.point2

    def __ne__(self, other):
        return not self.__eq__(other)


line1 = Line((10, 5), (20, 9))
newline = line1 // 2
print(newline.point1, newline.point2)
print(len(line1))
line2 = Line((10, 5), (20, 10))
print(line1 == line2)
