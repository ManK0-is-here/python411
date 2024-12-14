def is_palindrom(*str_text: str)-> list[bool]:
    """
    Проверка на палиндром
    """
    print(str_text)
    print(type(str_text))
    
    list_bool = []
    for i in str_text:
        i.lower()
        bool_str = i == i[::-1]
        list_bool.append(bool_str)
    return list_bool
print(is_palindrom("HI", "GOG"))
