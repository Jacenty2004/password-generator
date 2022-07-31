from datetime import datetime
import random

password = ""

print("Hello User,")
print("This is random passwords generator, created by Jacek Ćwik.")

codeRepetition = True
while codeRepetition == True:

#--- Code lenght inputing ----------------------    
    while True:
        try:
            lenght = int(input("How long password do you want? Write number of signs here: "))
            break
        except ValueError:
            print("What a joke! but be serious, write again.")

    allSigns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Q", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    print("Info: Generator is not using the special signs.")

#--- Strict generator --------------------------
    while lenght > 0:
       password += random.choice(allSigns)
       lenght -= 1

    print(password)
    print("Enjoy your new password.")

#--- Saving in file ----------------------------
    while True: 
        try: 
            saveQestion = str(input("Do you need to save it? "))
            break
        except ValueError: 
                print("Program didn't understand what you wrote. Try again, and remember to answer yes or no.")
        if saveQestion == "yes" or "yeah" or "y" or "1" :
            textInFile = ("\n" + str(datetime.now()) + str(password))
            savingInFile = open("passwords.txt", "a")
            savingInFile.write(str(textInFile))
            savingInFile.close()
            break
        elif saveQestion == "no" or "nah" or "n" or "0" :
            break
        else: 
            print("Program didn't understand what you wrote. Try again, and remember to answer yes or no.")

#--- Exiting ---------------------------------
    while True: 
        try:
            exiting = str(input("Do you need next another password? "))
        except ValueError:
            print("Just print yes or no.")
        if exiting == "yes" or "y" or "yeah" or "1":
            codeRepetition = False
            break
        elif exiting == "no" or "nah" or "n" or "0":
            break
        else:
            print("Program didn't understand. Try again.")