import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_mentors(self, Lecturer, course, grade):
        if isinstance(Lecturer, Lecturer) and course in Lecturer.courses_attached:
            if course in Lecturer.teach_grades:
                Lecturer.teach_grades[course] += [grade]
            else:
                Lecturer.teach_grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self):
        grades = self.grades.values()
        grades_list = sum(grades, [])
        middle_grade = statistics.mean(grades_list)
        return middle_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {mid_grade} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
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

    def mid_grade(self):
        grades = self.grades.values()
        grades_list = sum(grades, [])
        middle_grade = statistics.mean(grades_list)
        return middle_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {mid_grade}'
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

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
