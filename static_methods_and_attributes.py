# Une methode statique ne prend aucun parametre d'instance , mais uniquement des parametres classiques
# Elle permet d'effectuer des operations independamment des instances et de sstructurer le code
# Elle permet egalement plus de flexibilite lors de certaines operations
# Une methode statique peut etre appelee sur une instance ou sur la classe elle-meme

class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)


s1 = Student("John", [80, 85, 100, 65])
s2 = Student("Paul", [65, 70, 75, 65])

# Methode statique appelee sur la classe elle-meme
# On veut calculer la moyenne que sur les 2 premieres notes uniquement pour l'etudiant s2
average = Student.average_from_grades(s2.grades[:2])
average_all_students = Student.average_from_grades(s1.grades + s2.grades)
print(average)
print(average_all_students)