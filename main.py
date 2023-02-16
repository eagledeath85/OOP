
# ------------ IMPLEMENTATION DE LA CLASSE ------------
class Person:

    # Constructeur de la classe Person
    # On cree toujours les variables d'instance au niveau du constructeur
    def __init__(self, name: str, age: int):
        self.name = name        # cree une variable d'instance nom (une variable par instance)
        self.age = age
        print(f"Constructor of {name}")

    def self_presentation(self):    # instance method
        print(f"My name is {self.name} and I have {self.age}")
        if self.is_major():     # syntaxe pour acceder a une methode depuis une autre methode
            print("I am major")
        else:
            print("I am minor")

    def is_major(self) -> bool:
        return self.age >= 18

    def other_function():   # static method
        print("Other Function")


# ------------ APPEL DE LA CLASSE ------------
person1 = Person("jack", 15)    # creation d'une personne
person2 = Person("john", 43)    # creation d'une personne

person1.self_presentation() # methode d'instance
if person1.is_major():
    print(f"{person1.name} is major")
else:
    print(f"{person1.name} is minor")


Person.other_function()     # methode de classe (statique)