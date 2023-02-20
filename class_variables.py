# ------------ IMPLEMENTATION DE LA CLASSE ------------

class Person:
    # Les variables de classe sont appliquees a toutes les instances crees
    # Elles sont declarees avant le constructeur
    HUMAN_BEING = "Human (Homo Sapiens)"

    # Constructeur de la classe Person
    # On cree toujours les variables d'instance au niveau du constructeur
    def __init__(self, name: str = "", age: int = 0):
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

    def display_info_human_being(): # fonction statique
        # Pour appeler une variable de classe dans une fonction on utilise la syntaxe
        # <class_name>.<variable_de_classe>
        print(f"Human Being info: {Person.HUMAN_BEING}")


# ------------ UTILISATION ------------
persons_list = [
                Person("Jean", 26),
                Person("Paul", 12),
                Person("Zoe", 21),
                ]

for person in persons_list:
    person.self_presentation()          # Appel de fonction d'instance sur l'instance person
    Person.display_info_human_being()   # Appel de fonction statique sur la classe Person