from . import functions

numbers = list("0123456789")
words = "abcdefghinopqrstuvyxwz"
symbols = numbers + list(words) + list(words.upper())

def password(length=15):
   	password = ""
   	for i in range(length):
   		symbol = functions.random_element(symbols)
   		password += symbol

   	return password

       
