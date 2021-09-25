import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_mentors(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return f'Оценка {grade} по курсу {course} лектору {lecturer} добавлена'
        else:
            return 'Ошибка'

    def mid_grade(self):
        grades = self.grades.values()
        grades_list = sum(grades, [])
        middle_grade = statistics.mean(grades_list)
        return middle_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mid_grade} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("f'{other} - не является студентом")
            return
        return self.mid_grade < other.mid_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses = []

    def mid_grade(self):
        grades = self.grades.values()
        grades_list = sum(grades, [])
        middle_grade = statistics.mean(grades_list)
        return middle_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mid_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("f'{other} - не является лектором")
            return
        return self.mid_grade < other.mid_grade

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


Ivan_Petrov = Student("Ivan", "Petrov", "male")
Ivan_Petrov.courses_in_progress += ["python"]
Ivan_Petrov.finished_courses += ["java"]

Petr_Ivanov = Student("Petr", "Ivanov", "male")
Petr_Ivanov.courses_in_progress += ["java"]
Petr_Ivanov.finished_courses += ["python"]

Sergey_Semenov = Mentor("Sergey", "Semenov")
Sergey_Semenov.courses_attached += ["python", "java"]

Semen_Sergeev = Mentor("Semen", "Sergeev")
Semen_Sergeev.courses_attached += ["python", "java"]

Andrey_Stepanov = Lecturer("Andrey", "Stepanov")
Andrey_Stepanov.courses += ["python", "java"]

Stepan_Andreev = Lecturer("Stepan", "Andreev")
Stepan_Andreev.courses += ["python", "java"]

Denis_Nikitin = Reviewer("Denis", "Nikitin")
Denis_Nikitin.courses_attached += ["python", "java"]
Nikita_Denisov = Reviewer("Nikita", "Denisov")
Nikita_Denisov.courses_attached += ["python", "java"]


Ivan_Petrov.rate_mentors(Andrey_Stepanov, "python", 5)
Petr_Ivanov.rate_mentors(Stepan_Andreev, "java", 7)

Denis_Nikitin.rate_hw(Ivan_Petrov, "python", 10)
Nikita_Denisov.rate_hw(Petr_Ivanov, "java", 8)


students_list = [Ivan_Petrov, Petr_Ivanov]
lecturer_list = [Andrey_Stepanov, Stepan_Andreev]

def mid_students_grades(students_list, course_name):
    amount_grades = 0
    sum_grades = 0
    for student in students_list:
        if course_name in student.grades:
            amount_grades += len(student.grades[course_name])
            sum_grades += sum(student.grades[course_name])
    mid_gr = f'"Средняя оценка:" {sum_grades/amount_grades}'
    return mid_gr


def mid_lecturer_grades(lecturer_list, course_name):
    amount_grades = 0
    sum_grades = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.grades:
            amount_grades += len(lecturer.grades[course_name])
            sum_grades += sum(lecturer.grades[course_name])
    mid_gr = f'"Средняя оценка:" {sum_grades / amount_grades}'
    return mid_gr



