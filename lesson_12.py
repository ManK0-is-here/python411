"""
Урок 12
14.12.2024

Python функции. Аргументы и модули. Библиотеки plyer и requests. Урок: 12


1. Повторение функций:
    - DRY и SRP принципы
    - Объявление функций (def)
    - Вызов функций
    - Возврат значений (return)
    - Базовые проверки типов (isinstance)

2. Типы аргументов функций:
    - Позиционные аргументы
    - Именованные аргументы  
    - Аргументы по умолчанию
    - Обязательные и необязательные аргументы

3. Работа с внешними библиотеками:
    - Установка через pip
    - Импорт модулей
    - Библиотека plyer для уведомлений
    - Библиотека requests для HTTP запросов

4. Создание модулей:
    - Разделение кода на модули
    - Импорт собственных модулей
    - Относительные и абсолютные импорты
    - __name__ == '__main__'

5. Практика:
    - Создание функций для работы с API
    - Отправка уведомлений через plyer
    - Получение данных через requests
    - Структурирование кода в модули

    """

"""
DRY - Don't repeat yourself
Принцип DRY (Don't Repeat Yourself) - это принцип разработки программного обеспечения, который гласит, что каждая часть программы должна быть написана только один раз и должна быть доступна для использования в других частях программы.

SRP - Single Responsibility Principle
Принцип единственной ответственности (Single Responsibility Principle, SRP) - это принцип разработки программного обеспечения, который гласит, что каждый класс или модуль должен иметь только одну ответственность или задачу.

KISS (Keep It Simple, Stupid) - делай вещи проще. Функция должна быть простой и понятной.

YAGNI (You Ain't Gonna Need It) - не пиши код, который сейчас не нужен. Добавляй функциональность по мере необходимости.
"""

"""
Типы аргументов функций:
1. Позиционные аргументы:
    - Аргументы, передаваемые в функцию в том порядке, в котором они определены в объявлении функции.
    - Количество позиционных аргументов должно соответствовать количеству параметров в объявлении функции.
"""


def say_hello(name: str, age: int) -> None:
    """
    Функция приветствия.
    :param name: Имя пользователя
    :param age: Возраст пользователя
    """
    print(f"Привет, {name.title()}! Тебе {age} лет.")


say_hello("Алексей", 30)  # позиционные аргументы
# say_hello(30, "Алексей")

# message = say_hello("Алексей", 30)


"""
Типы аргументов функций:
2. Именованные аргументы:
    - Аргументы, передаваемые в функцию с указанием имен параметров.
    - Именованные аргументы могут быть переданы в любом порядке.
"""

say_hello(age=20, name="Кристина")


"""
Типы аргументов функций:
3. Аргументы по умолчанию:
    - Аргументы, которые имеют значение по умолчанию, если они не переданы при вызове функции.
    - Если аргумент не передан, используется значение по умолчанию.
"""


def is_adult(age:int, adult_age: int = 18) -> bool:
    """
    Функция проверки возраста.
    :param name: Имя пользователя
    :param age: Возраст пользователя
    :return: True, если пользователь совершеннолетний, False в противном случае
    """
    return age >= adult_age


result = is_adult(20)
result2 = is_adult(17, 16)
result3 = is_adult(age=20, adult_age=16)


# PRACTICE Функция проверки на палиндром
"""
Напишите функцию которая принемает строку и возвращает bool значение является ли строка палиндромом
Используйте аннотацию типов и документацию для функции
Напишите 1 проверку.

Срез
[::-1]
"""
