class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students.append(self)

    def _average_grade(self, grade):
        sumgrade = 0
        count = 0
        for values in self.grades.values():
            sumgrade += sum(values)
            count += len(values)
        if count != 0:
            return round(sumgrade / count, 2)
        else:
            return "Оценки не выставлялись"

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name} \n' \
                 f'Фамилия: {self.surname} \n' \
                 f'Средняя оценка за домашние задания: {self._average_grade(self.grades)}\n' \
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
                 f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def __lt__(self, other):
        if isinstance(other, Student):
            if self._average_grade(self.grades) > other._average_grade(other.grades):
                return f'{self.name} {self.surname} Круче!'
            elif self._average_grade(self.grades) == other._average_grade(other.grades):
                return "Оба хороши!"
            else:
                return f'{other.name} {other.surname} Круче!'
        else:
            return 'Вы сравниваете несравнимое'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        if isinstance(self, Lecturer):
            Lecturer.lecturers.append(self)
            self.grade = {}
        if isinstance(self, Reviewer):
            Reviewer.reviewers.append(self)


class Lecturer(Mentor):
    lecturers = []

    def _average_grade(self, grade):
        sumgrade = 0
        count = 0
        for values in self.grade.values():
            sumgrade += sum(values)
            count += len(values)
        if count != 0:
            return round(sumgrade / count, 2)
        else:
            return "Ошибка"

    def __str__(self):
        result = f'Имя: {self.name} \n' \
                 f'Фамилия: {self.surname}  \n' \
                 f'Средняя оценка за лекции: {self._average_grade(self.grade)}'
        return result

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self._average_grade(self.grade) > other._average_grade(other.grade):
                return f'{self.name} {self.surname} Круче!'
            elif self._average_grade(self.grade) == other._average_grade(other.grade):
                return "Оба хороши"
            else:
                return f'{other.name} {other.surname} Круче!'
        else:
            return 'Вы сравниваете несравнимое'


class Reviewer(Mentor):
    reviewers = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name} \n' \
                 f'Фамилия: {self.surname}'
        return result


vasya_pupok = Student('Вася', 'Пупок', 'male')
sveta_rodinka = Student('Света', 'Родинка', 'female')

gazimur_sergeevich = Lecturer('Газимур', 'Сергеевич')
larisa_pavlovna = Lecturer("Лариса", "Павловна")

seraya = Reviewer('Серая', ' Мышь')
staryi = Reviewer('Старый', 'Крот')

vasya_pupok.courses_in_progress = ['Philosophy', 'Criminology', 'Maths', 'Biathlon']
sveta_rodinka.courses_in_progress = ['Criminology', 'Biathlon', 'Dancing', 'Calligraphy']

vasya_pupok.finished_courses = ['Drawing', 'horseback_riding']
sveta_rodinka.finished_courses = ['Fencing', 'Meditation']

gazimur_sergeevich.courses_attached = ['Philosophy', 'Dancing', 'Criminology']
larisa_pavlovna.courses_attached = ['Biathlon', 'Maths', 'Calligraphy']

seraya.courses_attached = ['Dancing', 'Biathlon', 'Philosophy']
staryi.courses_attached = ['Criminology', 'Maths', 'Calligraphy']

vasya_pupok.rate_lecturer(gazimur_sergeevich, 'Philosophy', 5)
vasya_pupok.rate_lecturer(gazimur_sergeevich, 'Philosophy', 7)
vasya_pupok.rate_lecturer(gazimur_sergeevich, 'Criminology', 10)
vasya_pupok.rate_lecturer(gazimur_sergeevich, 'Criminology', 8)
vasya_pupok.rate_lecturer(larisa_pavlovna, 'Maths', 9)
vasya_pupok.rate_lecturer(larisa_pavlovna, 'Maths', 6)
vasya_pupok.rate_lecturer(larisa_pavlovna, 'Biathlon', 10)
vasya_pupok.rate_lecturer(larisa_pavlovna, 'Biathlon', 7)

sveta_rodinka.rate_lecturer(gazimur_sergeevich, 'Criminology', 6)
sveta_rodinka.rate_lecturer(gazimur_sergeevich, 'Criminology', 4)
sveta_rodinka.rate_lecturer(larisa_pavlovna, 'Biathlon', 4)
sveta_rodinka.rate_lecturer(larisa_pavlovna, 'Biathlon', 6)
sveta_rodinka.rate_lecturer(gazimur_sergeevich, 'Dancing', 10)
sveta_rodinka.rate_lecturer(gazimur_sergeevich, 'Dancing', 8)
sveta_rodinka.rate_lecturer(larisa_pavlovna, 'Calligraphy', 9)
sveta_rodinka.rate_lecturer(larisa_pavlovna, 'Calligraphy', 7)

seraya.rate_hw(sveta_rodinka, 'Dancing', 8)
seraya.rate_hw(sveta_rodinka, 'Dancing', 6)
seraya.rate_hw(vasya_pupok, 'Biathlon', 10)
seraya.rate_hw(vasya_pupok, 'Biathlon', 9)
seraya.rate_hw(sveta_rodinka, 'Biathlon', 6)
seraya.rate_hw(sveta_rodinka, 'Biathlon', 7)
seraya.rate_hw(vasya_pupok, 'Philosophy', 5)
seraya.rate_hw(vasya_pupok, 'Philosophy', 6)

staryi.rate_hw(vasya_pupok, 'Criminology', 8)
staryi.rate_hw(vasya_pupok, 'Criminology', 9)
staryi.rate_hw(sveta_rodinka, 'Criminology', 7)
staryi.rate_hw(sveta_rodinka, 'Criminology', 7)
staryi.rate_hw(vasya_pupok, 'Maths', 7)
staryi.rate_hw(vasya_pupok, 'Maths', 8)
staryi.rate_hw(sveta_rodinka, 'Calligraphy', 10)
staryi.rate_hw(sveta_rodinka, 'Calligraphy', 10)

for name in Student.students:
    print(name, end='\n -------------------------------------\n')
print()
print(vasya_pupok > sveta_rodinka)
print()
for name in Lecturer.lecturers:
    print(name, end='\n -------------------------------------\n')
print()
print(gazimur_sergeevich > larisa_pavlovna)


def average_student_grade(students, course):
    acc = count = 0
    for name in students:
        if course in name.grades:
            acc += sum(name.grades[course])
            count += len(name.grades[course])
    return round(acc / count, 2)


def average_lecturers_grade(lecturers, course):
    acc = count = 0
    for name in lecturers:
        if course in name.grade:
            acc += sum(name.grade[course])
            count += len(name.grade[course])
    return round(acc / count, 2)
