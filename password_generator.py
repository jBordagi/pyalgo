"""
password generator
8-12 charactere
au moins une minuscule, un chiffre, une ponctuation
reelement aleatoire
"""
#definition variables ce dont j'ai besoin
listAlphabetMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listAlphabetMaj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listPonctuation = [",", ".",";", ":", "!","-","(",")"]
minPassworLength = 8
maxPasswordLength = 12

import random
#on définit une variable comme un chiffre compris entre 8 et 12
passwordLength = random.randint(8,12)
print (passwordLength)

#on définit une variable comme un chiffre compris entre 0 et 25
randomMaj = random.randint (0,25)

#on choisit un des indices compris entre 0 et 25 de la liste donc une lettre
maj = listAlphabetMaj[randomMaj]
print (maj)
#on définit une vaiable comme un chiffre compris entre 0 et 9
randomNum= random.randint (0,9)
#on choisit un indice dans la listnumber donc un chiffre
num = listNumber[randomNum]

#on définit un chiffre compris entre 0 et 7 pour la ponctuation
randomPonc= random.randint(0,7)

#on choisit un des indcices compris entre 0 et 9 de la liste donc un chiffre
ponc= listPonctuation[randomPonc]
print (ponc)

password = [maj, num, ponc]
print (password)

while len (password) < passwordLength:
    quelBoite =random.randint(0,3)
    if quelBoite == 0:  
            bigBox == listNumber
    if quelBoite== 1:
            bigBox = listPonctuation
    if quelBoite == 2:
            bigbBox = listAlphabetMaj
    if quelBoite == 3:
            bigBox = listAlphabetMin

    randomNum = random.randint(0, len(bigBox)-1)
    password.append (bigBox[randomNum])
print (password)

random.shuffle (password)
print (password)