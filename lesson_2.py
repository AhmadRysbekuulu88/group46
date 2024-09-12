class Figure:
    unit = "cm"  # Атрибут уровня класса

    def __init__(self):
        pass  # Конструктор без атрибутов уровня объекта

    def calculate_area(self):
        raise NotImplementedError("Method calculate_area is not implemented")  # Нереализованный метод

    def info(self):
        raise NotImplementedError("Method info is not implemented")  # Нереализованный метод


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()  # Вызов конструктора родительского класса
        self.__side_length = side_length  # Приватный атрибут

    def calculate_area(self):
        return self.__side_length ** 2  # Площадь квадрата

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}.")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()  # Вызов конструктора родительского класса
        self.__length = length  # Приватный атрибут
        self.__width = width  # Приватный атрибут

    def calculate_area(self):
        return self.__length * self.__width  # Площадь прямоугольника

    def info(self):
        area = self.calculate_area()
        print(
            f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}.")


if __name__ == "__main__":
    # Создание списка объектов
    shapes = [
        Square(5),
        Square(7),
        Rectangle(5, 8),
        Rectangle(3, 6),
        Rectangle(10, 2)
    ]

    # Вызов метода info для каждого объекта
    for shape in shapes:
        shape.info()
