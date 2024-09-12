class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "замужем" if self.is_married else "не замужем"
        print(f"Меня зовут {self.fullname}, мне {self.age} лет, я {marital_status}.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks=None):
        super().__init__(fullname, age, is_married)
        self.marks = marks if marks is not None else {}

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def introduce_myself(self):
        super().introduce_myself()
        print("Мои оценки:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Средняя оценка: {self.average_mark():.2f}")


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = 2000  # базовая зарплата

    def calculate_salary(self):
        bonus = 0.05 * max(0, self.experience - 3)  # Бонус за опыт больше 3 лет
        return self.base_salary * (1 + bonus)

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт работы: {self.experience} лет")
        print(f"Зарплата: {self.calculate_salary():.2f} $")


def create_students():
    students = []

    student1 = Student("Иван Иванов", 16, False, {'Математика': 5, 'Физика': 4, 'История': 3})
    student2 = Student("Мария Петрова", 17, False, {'Математика': 3, 'Физика': 5, 'История': 4})
    student3 = Student("Сергей Сидоров", 16, False, {'Математика': 4, 'Физика': 4, 'История': 5})

    students.append(student1)
    students.append(student2)
    students.append(student3)

    return students


# Создаём объект учителя
teacher = Teacher("Алексей Смирнов", 40, True, 5)

# Распечатываем информацию о teacher
teacher.introduce_myself()

# Создаём учеников
students = create_students()

# Распечатываем информацию о каждом ученике
for student in students:
    student.introduce_myself()
    print()  # Для разделения учеников
