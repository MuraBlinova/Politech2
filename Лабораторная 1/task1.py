# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Book:
    def __init__(self, pages, chapters):

        """
        Создание и подготовка к работе объекта "Книга"

        :param pages: Количество страниц
        :param chapters: Массив названий глав
        :raises TypeError: Если количество страниц не является типом int или float
        :raises ValueError: Если количество страниц меньше или равен нулю

        Примеры:
         >>> book_ = Book(30, ['Восход', 'Полдень', 'Закат'])  # инициализация экземпляра класса
         """

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        self.decorations = chapters

    def addChapter(self, chapter: str) -> None:
        """
                Добавляет главу в конец книги. Принимает аргумент chapter типа
                string, представляющий название lj,fdkztvjqглавы.
                Метод не возвращает никакого значения.

                :param chapter: Глава

                Примеры:
                >>> book_ = Book(50, ['Восход', 'Полдень'])
                >>> book_.addChapter('Закат')
        """
        ...

    def removeChapter(self, chapter: str) -> None:
        """
                Удаляет главу из книги. Принимает аргумент chapter типа str, представляющий
                название главы, которую нужно удалить из книги.
                Метод не возвращает никакого значения.

                :param chapter: Украшение

                Примеры:

                >>> book_ = Book(30, ['Восход', 'Полдень', 'Закат'])
                >>> book_.removeChapter('Полдень')
        """
        ...

    def getCountOfChapters(self) -> int:
        """
                Возвращает количество глав в книге.
                Метод не принимает аргументов и возвращает число глав в книге.

                :return: Число украшений

                Примеры:

                >>> book_ = Book(30, ['Восход', 'Полдень', 'Закат'])
                >>> book_.getCountOfChapters()
        """
        ...

class Сloset:
    def __init__(self, height, numberOfShelves):

        """
        Создание и подготовка к работе объекта "Шкаф"

        :param height: Высота шкафа
        :param numberOfShelves: Количество полок
        :raises TypeError: Если высота шкафа не является типом int или float
        :raises ValueError: Если высота шкафа меньше или равен нулю
        :raises TypeError: Если количество полок не является типом int или float
        :raises ValueError: Если количество полок меньше или равен нулю

        Примеры:
         >>> сloset_ = Сloset(5, 2)  # инициализация экземпляра класса
        """

        if not isinstance(height, int):
            raise TypeError("Высота должна быть типа int")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(numberOfShelves, int):
            raise TypeError("Количество полок должно быть типа int")
        if numberOfShelves <= 0:
            raise ValueError("Количество полок должно быть положительным числом")
        self.decorations = numberOfShelves

    def addShelves(self, shelves: int) -> None:
        """
            Добавляет полки в шкаф.
            Принимает аргумент shelves типа int, представляющий количество полок, которые нужно добавить.
            Метод не возвращает никакого значения.

            :param shelves: Полки

            Примеры:
            >>> сloset_ = Сloset(5, 2)
            >>> сloset_.addShelves(5)
            """
        ...

    def removeShelves(self, shelves: int) -> None:
        """
        Удаляет полки из шкафа.
        Принимает аргумент shelves типа int, представляющий количество полок, которые нужно удалить.
        Метод не возвращает никакого значения.

        :param shelves: Полки

        Примеры:

        >>> сloset_ = Сloset(5, 3)
        >>> сloset_.removeShelves(1)
            """
        ...

    def getCountOfShelves(self) -> int:
        """
        Возвращает количество полок.
        Метод не принимает аргументов и возвращает число полок.

        :return: Число полок

        Примеры:

        >>> сloset_ = Сloset(5, 3)
        >>> сloset_.getCountOfShelves()
            """
        ...

class Pass:
    def __init__(self, institutionName, dateOfIssue):
        """
        :param institutionName: Название учреждения
        :param dateOfIssue: Дата выдачи

        Примеры:

        >>> pass_ = Pass('Выдуманное учреждение', "30.02.3000")

        """
        self.institutionName = institutionName
        self.dateOfIssue = dateOfIssue

    def approved(self, days: int) -> str:
        """

            Активирует пропуск и даёт допуск на заданное количество дней.

            :param days: Количество дней, на которое выдается допуск
            :return: Сообщение о выдачи допуска

        """
        ...

    def blocked(self) -> None:
        """
            Блокирует пропуск.

            :return: None

        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
