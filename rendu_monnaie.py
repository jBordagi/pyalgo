"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest of int div
Use input() to get user entry
"""

achat1 = 56
achat2 = 68 
somme = achat1 + achat2

billet100 = somme // 100
rendu100 =  somme % 100
billet50 = rendu100 // 50
rendu50 = rendu100 % 50
billet20 = rendu50 // 20
rendu20 = rendu50 % 20
billet10 = rendu20 // 10
rendu10 = rendu20 % 10
billet5 = rendu10 // 5
rendu5 = rendu10 %5
piece2 = rendu5 // 2

print("Vous avez acheté un produit à", achat1,"€")
print("et un produit à", achat2,"€")
print("le montant dü est de",somme,"€")

if billet100 > 0:
   print("La machine vous rend",billet100, "billets de 100€")


if billet20 > 0:
    print(billet20,"billets de 20€")


if billet10 >10:
    print(billet10, "billets de 10€")

if billet5 > 0:
    print (billet5,"billets de 5€")


if piece2 > 0:
    print(piece2, "pieces de 2€")

    print("la machine vous rend", billet100, "billet(s) de 100,", billet50, "billet(s) de 50,", billet20,"billet(s) de 20,", billet5,"billet(s) de 5," , piece2, "pièces de 2")