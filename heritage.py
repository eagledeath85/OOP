# ------------ IMPLEMENTATION DE LA CLASSE ------------

class HumanBeing:   # Classe Parent
    HUMAN_BEING = "(Unknown human being)"

    def display_info_human_being(self):
        print(f"Human Being info: {self.HUMAN_BEING}")


class Cat(HumanBeing):   # Classe Enfant
    # La variable de classe de la classe parent est ecrasee
    HUMAN_BEING = "Cat (mamal cat)"

    # La methode display_info_human_being est heritee de la classe parent

class Person(HumanBeing):   # Classe Enfant
    # La variable de classe de la classe parent est ecrasee
    HUMAN_BEING = "Human (mamal Homo Sapiens)"

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

class Student(Person):
    def __init__(self, name: str, age: int, studies: str):
        # Les variables du constructeur parent sont appelees grace a la syntaxe suivante
        super().__init__(name, age)
        self.studies = studies

    # La methode self_presentation de Student est la meme que celle de Person, avec un ajout specifique a sa classe
    # Pour appeler la methode de la classe parent on utilise la syntaxe super().<nom_methode_classe_parent>
    def self_presentation(self):
        # La methode de la classe parent est ecrasee
        super().self_presentation()
        print(f"I'm studying {self.studies}")


# ------------ UTILISATION ------------
persons_list = [
                Person("Jean", 26),
                Person("Paul", 12),
                Person("Zoe", 21),
                ]

for person in persons_list:
    person.self_presentation()          # Appel de fonction d'instance sur l'instance person
    person.display_info_human_being()   # Appel de fonction statique sur la classe Person
    print()

cat1 = Cat()
cat1.display_info_human_being()
print()
humanBeing = HumanBeing()
humanBeing.display_info_human_being()
print()
student = Student("Gordon", 23, "Informatics")
student.self_presentation()
student.display_info_human_being()  # student herite egalement de la classe HumanBeing