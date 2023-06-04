


class Student:
    # Write your code here.
    all_students = []
    def __init__(self, name: str, grade: int):
        # Write your code here.
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    # Write your code here.
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade: int):
        MIN_GRADE = 0
        MAX_GRADE = 100
        if not MIN_GRADE < new_grade < MAX_GRADE:
            raise ValueError(f"New grade not in the accepted range of [{MIN_GRADE}-{MAX_GRADE}].")
        self._grade = new_grade

    @staticmethod
    def calculate_average_grade(students_list: list):
        if not students_list:
            return -1
        grades = 0
        for student in students_list:
            grades += student.grade
        average_grade = grades / len(students_list)
        return round(average_grade, 2)

    @classmethod
    def get_average_grade(cls, students):
         return cls.calculate_average_grade(cls.all_students)


    @classmethod
    def get_best_student(cls, students):
        best_student = None
        for student in cls.all_students:
            if best_student == None or best_student.grade < student.grade:
                best_student = student
        return best_student




stud1 = Student('Will', 80)
stud2 = Student('Josie', 95)
average = stud1.calculate_average_grade([stud1, stud2])
print(average)