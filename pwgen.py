


print ("###############################################################################")
print ("#                                                                             #")
print ("#    				create by Hak9                                #")
print ("#    								              #")
print ("#   				   PwGen                                      #")
print ("#                                   V1.0                                      #")
print ("#                                                                             #")
print ("#  https://github.com/xHak9x                                                  #")
print ("#  http://www.youtube.com/c/Hak9xx			                      #")
print ("###############################################################################")
print(" ")
#/!usr/bin/env python
# -*- coding: utf-8 -*-
print(" INSTRUCTIONS")
print(" #Number one [1] is a personalized password where numbers and characters")
print("  can be include. The program randoms your word and if you include numbers")
print("  it mixes characters and numbers. You can also introduce some extra characters\n")
print(" #Number two [2] is an aleatory password generator where you can include numbers")
print("  so it prints random passwords. This could be good for some Wpa/Wpa2 passwords\n")
print(" #Number three [3] is simply a random number generator\n")
print(" #SOME EXTRA INFO: The passwords will be exported at: [1] will be exported as PwGen1.txt")
print("  [2] will be exported as PwGen2.txt. \n  Finally [3] will be exported as PwGen3.txt \n")
print("  Hope you enjoy!\n\n")
print("  Program created by Hak9\n")
print("  Version 1.0 - PwGen\n\n")
#
# Version 1.0
#


from string import ascii_letters, digits , punctuation
from random import choice , randint


print("    MENU\n")

Var1 = str(raw_input(" || Personalized Password Generator [1]\n || Aleatory Mix Password Generator [2]\n || Number Password Generator [3]\n"))


#
# Start of part 1
#
entexto = []
file = open("PwGen1.txt" , "w")
file.write("")
file.close()
file = open("PwGen1.txt" , "a")

if Var1 == "1":

    lista = []

    palabra = []

    blanc = ""

    num = ""

    ch = ""

    word = str(raw_input("Key word: "))

    inum = str(raw_input("Do you want to include numbers (y/n): "))

    if inum == "y":
            num = str(input("Select a number: "))

    if inum != "y" and inum != "n":
        print("valor no valido")
    else:

        times = int(input("Number of passwords: "))

        min = int(input("min chars: "))

        max = int(input("max chars: "))

        suma = word + num


        for i in range (0 , times):
            temp = "".join(choice(suma) for i in range(randint(min , max)))
            distinto = "".join(choice(suma) for i in range(randint(min , max)))
            if distinto == temp:
                print(blanc)
            else:
                entexto.append("{0}\n".format(temp))
                print(temp)
        for i in range (len(entexto)):
            file.write(entexto[i])
file.close()

###End of part 1

###Start of part 2

entexto2 = []
file2 = open("PwGen2.txt" , "w")
file2.write("")
file2.close()
file2 = open("PwGen2.txt" , "a")

if Var1 == "2":

    blanc2 =""

    ltr2 =""

    num2 =""

    aleatory2 =[]

    inum2 = str(raw_input("Do you want to include numbers (y/n): "))


    if inum2 != "y" and inum2 != "n":
        print("invalid value")
    else:
        times2 = int(input("Number of passwords: "))
        min2 = int(input("min chars: "))

        max2 = int(input("max chars: "))


        if inum2 == "y":
            naleatory2 = digits
            aleatory2.append(naleatory2)

            laleatory2= ascii_letters

            for i in range (0 , times2):
                temp2 = "".join(choice(laleatory2 + naleatory2) for i in range(randint(min2 , max2)))
                distinto2 = "".join(choice(laleatory2 + naleatory2) for i in range(randint(min2 , max2)))
                if distinto2 == temp2:
                    print(blanc2)
                else:
                    print(temp2)
        else:
            for i in range (0 , times2):
                temp2 = "".join(choice(ascii_letters) for i in range(randint(min2 , max2)))
                distinto2 = "".join(choice(ascii_letters) for i in range(randint(min2 , max2)))
                if distinto2 == temp2:
                    print(blanc2)
                else:
                    entexto2.append("{0}\n".format(temp2))
                    print(temp2)

            for i in range (len(entexto2)):
                file2.write(entexto2[i])
file2.close()

###End of part 2

###Start of part 3

entexto3 = []
file3 = open("PwGen3.txt" , "w")
file3.write("")
file3.close()
file3 = open("PwGen3.txt" , "a")
if Var1 == "3":

    palabra = ""

    blanc3 =""

    times3 = int(input("Number of passwords: "))

    min3 = int(input("min chars: "))

    max3 = int(input("max chars: "))



    for i in range (0 , times3):
        temp3 = "".join(choice(digits) for i in range(randint(min3 , max3)))
        distinto3 = "".join(choice(digits) for i in range(randint(min3 , max3)))
        if distinto3 == temp3:
            print(blanc3)
        else:
            entexto3.append("{0}\n".format(temp3))
            print(temp3)
#palabra.append(temp3[i])
    for i in range (len(entexto3)):
        file3.write(entexto3[i])

###End of part 3

file3.close()

if Var1 != "1" and Var1 != "2" and Var1 != "3":
    print("invalid value")
