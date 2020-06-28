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
        password = ""
        for i in range(length):
            symbol = functions.random_element(symbols)
            password += symbol

        if special_char and functions.list_in_string(password, special_chars):
            break
        elif False == special_char:
            break


    return password