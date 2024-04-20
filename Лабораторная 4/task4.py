class Fruit:
    #Базовый класс, описывающий фрукт.
    def __init__(self, color: str, country: str, weight: float):
        """
        Инициализирует экземпляр класса Person.

        Args:
            color (str): Цвет фрукта.
            country (str): Страна происхождения.
            weight (float): Вес фрукта.

        :raises TypeError: Если вес фрукта не является типом int или float
        :raises ValueError: Если вес фрукта меньше или равен нулю
        """
        self.color = color
        self.country = country
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес должнен быть положительным числом")
        self.weight = weight

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса Fruit.

        Returns:
            str: Строковое представление экземпляра класса Fruit.
        """
        return f"Фрукт из {self.country} имеет цвет {self.color} и вес {self.weight} грамм."

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладочных целей.

        Returns:
            str: Строковое представление объекта для отладочных целей.
        """
        return f"Fruit(цвет={self.color}, страна={self.country}, вес={self.weight})"

    def get_color(self) -> str:
        """
        Возвращает цвет фрукта.

        Returns:
            str: Цвет фрукта.
        """
        return self.color

    def get_country(self) -> str:
        """
        Возвращает страну происхлждения фрукта.

        Returns:
            str: Страна фрукта.
        """
        return self.country

    def get_weight(self) -> float:
        """
        Возвращает вес фрукта.

        Returns:
            str: Вес фрукта.
        """
        return self.weight

    def is_heavy(self):
        """
        Проверяет, весит ли фрукт не меньше 50 грамм.

        Returns:
            bool: True, если фрукт весит не меньше 50 грамм иначе False.
        """
        return self.weight >= 50

class Apple(Fruit):
    """
        Дочерний класс, описывающий яблоко.
        """

    def __init__(self, color: str, country: str, weight: float, grade: str):
        """
        Инициализирует экземпляр класса Student.

        Args:
            color (str): Цвет яблока.
            country (str): Страна, где собрано яблоко.
            weight (float): Вес яблока.
            grade (str): Сорт яблока.
        """
        super().__init__(color, country, weight)


        self.grade = grade  # Непубличный атрибут

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса Apple.

        Returns:
            str: Строковое представление экземпляра класса Apple.
        """
        return f"Яблоко сорта {self.grade} из {self.country} имеет цвет {self.color} и вес {self.weight} грамм."

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладочных целей.

        Returns:
            str: Строковое представление объекта для отладочных целей.
        """
        return f"Apple(цвет={self.color}, страна={self.country}, вес={self.weight}, сорт={self.grade})"

    # Переопределенный метод
    def is_heavy(self):
        """
        Переопределенный метод, проверяющий, весит ли яблоко не меньше 25 грамм.

        Returns:
            bool: True, если яблоко весит не меньше 25 грамм иначе False.
        """
        return self.weight >= 25

    def get_grade(self):
        """
        Возвращает сорт яблока.

        Returns:
            str: Сорт яблока.
        """
        return self.grade

if __name__ == "__main__":
    apple_ = Apple("зеленый","Россия", 15.04, "Антоновка")
    print(apple_) #Яблоко сорта Антоновка из Россия имеет цвет зеленый и вес 15.04 грамм.

    print(repr(apple_)) #Apple(цвет=зеленый, страна=Россия, вес=15.04, сорт=Антоновка)

    # Проверка переопределенного метода is_heavy()
    print(apple_.is_heavy())  # False
    print(Apple("зеленый","Россия", 30, "Антоновка").is_heavy()) # True

    print(apple_.get_color()) #зеленый
    print(apple_.get_country()) #Россия
    print(apple_.get_weight()) #15.04
    print(apple_.get_grade()) #Антоновка

    pass
