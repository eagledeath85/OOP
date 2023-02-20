# La fonction isinstance permet de verifier et valider que les parametres qu'on lui passe sont des instances voulues

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        # Si le parametre age n'est pas une instance de type int alors on execute le code
        if not isinstance(age, int):
            print("ERROR, the age must be of type integer")
            self.age = 0
    def display_info(self):
        print(f"My name is {self.name}")
        if self.age > 0 :
            print(f"Next year I'll be {self.age + 1}")


person = Person("Jean", 20.0)
person.display_info()