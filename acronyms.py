#A program that generates Acronyms of words given a sentence

#Define the Acronym() function
def Acronym():
    name = str(input("Enter a phrase: "))

    text = name.split()
    a = " "

    for i in text:
        a = a + str(i[0]).upper()
    print(a)

Acronym()
