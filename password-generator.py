from distutils.log import debug
import random

print("Hello User,")
print("This is random passwords generator, created by Jacek Ćwik.")

while True:
    try:
        lenght = int(input("How long password do you want? Write number of signs here: "))
        break
    except ValueError:
        print("What a joke! but be serious, write again.")

allSigns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Q", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Info: Generator is not using the special signs.")

password = ""
while lenght > 0:
    password += random.choice(allSigns)
    lenght -= 1

print(password)
print("Enjoy your new password.")