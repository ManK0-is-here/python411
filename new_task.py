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

pro_print(2, 4, 5, 234)
# pro_print(name = "asdf", diagnoz = "DCP")

def user_print(**user):
    print(user)
    print(type(user))

# user_print(2, 4, 5, 234)
user_print(name = "asdf", diagnoz = "DCP")
user_print(loc = "Msk", time = "20")