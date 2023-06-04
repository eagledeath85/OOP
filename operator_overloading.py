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
#################### OVERLOADING __eq__, __neq__, __gt__ methods ####################
#################### OVERLOADING __ge__, __lt__, __le__ methods ####################

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

    # __eq__ allows to check equality between objects
    def __eq__(self, other):
        # We first check if the 2 objects are of the same type
        if not isinstance(other, Line):
            return False
        # If yes, then we check whether their attributes are identical
        return self.point1 == other.point1 and self.point2 == other.point2

    # __eq__ checks the non-equality between objects
    def __ne__(self, other):
        return not self.__eq__(other)

    # __gt__ evaluates "strictly greater than" and returns True or False
    def __gt__(self, other):
        return len(self) > len(other)

    # __gte__ evaluates "greater than or equal to" and returns True or False
    def __ge__(self, other):
        return len(self) >= len(other)

    # __gt__ evaluates "strictly smaller than" and returns True or False
    def __lt__(self, other):
        return len(self) < len(other)

    # __gte__ evaluates "smaller than or equal to" and returns True or False
    def __le__(self, other):
        return len(self) <= len(other)


line1 = Line((10, 5), (20, 9))
newline = line1 // 2
print(newline.point1, newline.point2)
print(len(line1))
line2 = Line((10, 5), (20, 9))
print(line1 == line2)


#################### OVERLOADING __eq__, __neq__, __gt__ methods ####################

class BookPage:
    def __init__(self, text, page_number):
        self.text = text
        self.page_number = page_number

    def __len__(self):
        return len(self.text)

    # returns a human-readable representation of the object, meaning
    # the text itself instead of the string representation of the instance at its memory location
    def __str__(self):
        return self.text

    # __repr__ is more for debugging purpose.
    # It gives all the important information about the object we need when debugging or looking at the internal representation of it
    def __repr__(self):
        return self.__str__()

class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number

    def __len__(self):
        return len(self.pages)

    def __str__(self):
        return f"Book(title = {self.title}, author = {self.author}, pages = {self.pages}, id_number = {self.id_number}"

    def __repr__(self):
        return f"Book(id_number={self.id_number})"


book_page1 = BookPage("Page 1", 1)
book_page2 = BookPage("Page 2", 2)
book = Book("My First Book", "John Doe", [str(book_page1), str(book_page2)], 1)
print(len(book))
print(book_page1)
print(book)
print(book.__repr__())