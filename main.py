
# ------------ IMPLEMENTATION DE LA CLASSE ------------
class Person:

    # Constructeur de la classe Person
    # On cree toujours les variables d'instance au niveau du constructeur
    def __init__(self, name: str = "", age: int = 0):
        # Le mot-cle self se rapporte a l'instance creee.
        # Toutes les variables d'instance sont appelees par la syntaxe self.<nom_variable_instance>
        self.name = name        # cree une variable d'instance nom (une variable par instance)
        self.age = age
        if name == "":
            self.ask_user_name()
        print(f"Constructor of {self.name}")

    def self_presentation(self):    # instance method
        if self.age == 0:
            print(f"My name is {self.name}")
        else:
            print(f"My name is {self.name} and I have {self.age}")
            if self.is_major():     # syntaxe pour acceder a une methode depuis une autre methode
                print("I am major")
            else:
                print("I am minor")

    def is_major(self) -> bool:
        return self.age >= 18

    def ask_user_name(self):
        self.name = input("What is your name? ")


    def other_function():   # static method
        print("Other Function")


# ------------ APPEL DE LA CLASSE ------------
# person1 = Person("jack", 15)    # creation d'une personne
# person2 = Person("john", 43)    # creation d'une personne

persons_tuple = [Person("Jean", 26), Person("Paul", 12), Person()]

for person in persons_tuple:
    person.self_presentation()

# person3 = Person()
person4 = persons_tuple.append(Person(age=46))

# person1.self_presentation() # methode d'instance
# person3.self_presentation()
# person4.self_presentation()
# if person1.is_major():
#     print(f"{person1.name} is major")
# else:
#     print(f"{person1.name} is minor")


# Person.other_function()     # methode de classe (statique)