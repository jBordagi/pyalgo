"""

@name manip_tableau.py
@author Aélion
@version 1.0.0
    Algorithmique spécifique sur les collections
"""
"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal

        """
getGreaterOf function
return the greater value of two params

        """
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else:
        return secondVal

"""
compare function
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of two depends on desc params
"""

    def compare(firstVal, secondVal, desc=True):
        if (desc):
           return getLowerOf(firstVal,secondVal)
        return getGreaterOf (firstVal, secondVal)
"""
min function
@param anArray The aray from which i want to get the min value
@return the min value of anArray
"""

def min(anArray):
    theMin = anArray[0]
    for value in anArray[1:]:
        theMin = compare(theMin,value)

    """
max function
@param anArray The aray from which i want to get the max value
@return the max value of anArray
"""
def max(anArray):
    theMax = anArray[0]
    for value in anArray[1:]:
        theMax = compare(theMax,value, False)
    return theMax

# Declaration du tatableau de démonstration
monTablo = [15, 3, 25, 12, 7, -15]

# More complex loop with condition
for indice in monTablo:
    if indice % 2 == 0:
        print("L'indice", indice, "est pair")

print("Le nombre", sorted(monTablo)[0], "est le plus petit")

#find a min
mayBeImTheMin = monTablo[0] #Initialize the min as the first item in the array
for val in monTablo[1:]: #loop over the array from the second element
    mayBeImTheMin = getLowerOf (mayBeImTheMin, val)
#finally...
print("And the min is:", mayBeImTheMin)

#find a max
mayBeImTheMax = monTablo[0] #Initialize the min as the first item in the array
for val in monTablo[1:]: #loop over the array from the second element
    mayBeImTheMax = getGreaterOf(mayBeImTheMax, val)

#finally...
print("And the max is:", mayBeImTheMax)


#merge both max and min research

mayBeImTheMin = monTablo[0] #Initialize the min as the first item in the array
for val in monTablo[1:]: #loop over the array from the second element
    if val < mayBeImTheMin: #check if the current value in the array is lower than the current
        mayBeImTheMin =val

#average

def average (anArray):
    total = 0
    nbItems = 0
    for val in anArray:
        total = total + val
        nbItems= nbItems + 1
    return total / nbItems

print("la moyenne est de" ,average(monTablo))

#the same
indice=0
for val in monTablo:
    if indice % 2 ==0:
        print(monTablo[indice]*2)
    indice = indice + 1

#factor
def facto(anArray):
    facto = 1
    for indice in range (len(monTablo)):
        facto = facto * monTablo[indice]
    return facto

print ("La factorielle du tableau est:",facto(monTablo))

