def say_bro(say: int, bro: str)-> None:
    """
    Коментарий к функции: 
    Функция скажи Бро,
    где первый аргумент это сколько раз ты хочешь сказать Бро,
    а вторая само слово Бро,
    это явная отсылка на сериал кремневая(селиконовая) долина.
    """
    print(f"Ты скажешь {bro}, всего {say} раз")


# messange: None = say_bro(30, "Bro")
say_bro(say=52, bro= "Bro")


def is_Palindrom(pal:str)->bool:
    pal.lower()
    """
    берёи строку приводим к нижнему регистру
    выполняем сравнение строки после ссреза и до среза 
    возвращаем булевое значение
    """
    return pal[::-1] == pal
print(is_Palindrom("х10101Х"))


def is_palindrom(*str_text: str)-> list[bool]:
    """
    Проверка на палиндром
    """
    # print(str_text)
    # print(type(str_text))
    
    list_bool = []
    for i in str_text:
        i.lower()
        bool_str = i == i[::-1]
        list_bool.append(bool_str)
    return list_bool
# print(is_palindrom("HI", "GOG"))


# user :dict[str, Any] = {"name": "Jojo", "age": 16}
# name: Any, age: Any = user.value()

d = {3: 4, 5: 6}
c = {1: 2}
s = {**c, **d} # в один словарь
# g = {d, c}
# print(g)
# print(s)

def pro_print(*user):
    print(type(user))

# pro_print(2, 4, 5, 234)
# pro_print(name = "asdf", diagnoz = "DCP")

def user_print(**user):
    print(user)
    print(type(user))

# user_print(2, 4, 5, 234)
# user_print(name = "asdf", diagnoz = "DCP")
# user_print(loc = "Msk", time = "20")


# def streat_run(**us) -> None:
#     return us
# config_ai = {

# }

def print_us(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


user: dict[str, any] = {"name": "Jojo", "age": 16, "city": "N"}
print_us(**user)

# user1 = {"sep":  " ", "end": "\n"}
# print("asdf",**user1)