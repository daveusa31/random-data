from . import functions

numbers = "0123456789"
words = "abcdefghinopqrstuvyxwz"
special_chars = "!?@$"



def password(length=15, number=True, word=True, special_char=False, upper=True):
    symbols = ""

    symbols += numbers if number else ""
    symbols += words if word else ""
    symbols += special_chars if special_char else ""

    if upper:
        symbols = symbols.upper()

    symbols = list(symbols)

    while True:
        _password = ""
        for i in range(length):
            symbol = functions.random_element(symbols)
            _password += symbol

        if special_char:
            if functions.list_in_string(_password, special_chars):
                break
            else:
                continue 

    return _password


def uuid(parts=4, length=4):
    _uuid = ""

    for _ in range(parts):
        _uuid += password(length=length, upper=False) + "-"

    _uuid = uuid.strip("-")
    return _uuid