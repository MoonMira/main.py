class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        all_grade = []
        for grade in self.grades.values():
            for all_ in grade:
                all_grade.append(all_)
        aver = sum(all_grade)/len(all_grade)
        return aver

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average()}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        return cool_lecturer.average() < best_student.average()

    def __gt__(self, other):
        return cool_lecturer.average() > best_student.average()

    def __eq__(self, other):
        return cool_lecturer.average() == best_student.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average()}'

    def average(self):
        all_grade = []
        for grade in self.grades.values():
            for all_ in grade:
                all_grade.append(all_)
        aver = sum(all_grade)/len(all_grade)
        return aver

    def __lt__(self, other):
        return cool_lecturer.average() < best_student.average()

    def __gt__(self, other):
        return cool_lecturer.average() > best_student.average()

    def __eq__(self, other):
        return cool_lecturer.average() == best_student.average()

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def student_course_average(students_list, course):
    all_grades_students = []
    all_grade = []
    for student in students_list:
        if course in student.grades:
            all_grades_students.append(student.grades)

    for grade in all_grades_students:
        for el in grade.values():
            all_grade.extend(el)
    aver = sum(all_grade) / len(all_grade)
    return aver


def lector_course_average(lector_list, course):
    all_grades_lector = []
    all_grade = []
    for lector in lector_list:
        if course in lector.grades:
            all_grades_lector.append(lector.grades)

    for grade in all_grades_lector:
        for el in grade.values():
            all_grade.extend(el)
    aver = sum(all_grade) / len(all_grade)
    return aver


some_lecturer = Lecturer('Some', 'Buddy')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

student_two = Student('John', 'Luck', 'your_gender')
student_two.courses_in_progress += ['Python']
student_two.courses_in_progress += ['Git']
student_two.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('Mike', 'Vasovski')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

lecturer_two = Lecturer('Julit', 'Maison')
lecturer_two.courses_attached += ['Python']
lecturer_two.courses_attached += ['Git']

best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 4)
best_student.rate_hw(cool_lecturer, 'Python', 9)

student_two.rate_hw(lecturer_two, 'Git', 5)
student_two.rate_hw(lecturer_two, 'Git', 3)
student_two.rate_hw(lecturer_two, 'Git', 2)

cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 3)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(student_two, 'Git', 4)
cool_reviewer.rate_hw(student_two, 'Git', 7)
cool_reviewer.rate_hw(student_two, 'Git', 8)


print(best_student.grades)
print(student_two.grades)
print(best_student.average())
print(student_two.average())
print(best_student.__str__())
print(student_two.__str__())

print(cool_lecturer < best_student)
print(cool_lecturer > best_student)
print(cool_lecturer == best_student)

print(cool_lecturer.grades)
print(lecturer_two.grades)
print(cool_lecturer.__str__())
print(lecturer_two.__str__())
print(cool_lecturer.average())
print(lecturer_two.average())

print(cool_reviewer.__str__())

print(student_course_average([best_student, student_two], 'Python'))
print(lector_course_average([cool_lecturer, lecturer_two], 'Python'))
