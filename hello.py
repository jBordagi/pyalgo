"""
    Algotithm #0.0.1
    Declare var
    Store some aithmetics into the var
    Display result
    Operands, operators, functions

    @version 0.0.2
    Add two operands and replace compute method
"""
"""
function setting
"""
def addition(operande1, operande2):
    if operande1 < 0:
        operande1 = operande1 * -1
    if operande2 < 0:
        operande2 = operande2 * -1
    return operande1 + operande2

resultat = 0 #Définition de la variable

operande1 = -3 #imagine it's the min of an array
operande2 = 2 #imagine it's the max of an array
resultat = addition(5, 3) #call addition function with 5 and 3 as params
print(addition(operande1, operande2))
print(resultat)

if resultat > 0:
    print ("le résultat est positif")
else:
    print ("le résultat est négatif")
"""
Fin de l'algorithme
"""