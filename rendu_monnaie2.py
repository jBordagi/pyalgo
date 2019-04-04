somme = 460
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
rendu2 = rendu5 % 2
piece1= rendu2


listeBillet = [billet100,billet50,billet20,billet10,billet5,piece2,piece1]
listeChaine = ["","","","","","",""]
listeMonnaie = [100,50,20,10,5,2,1]
for i in range(7) :
    if listeBillet[i] == 1:
        listeChaine[i] = str(listeBillet[i]) + "billet de" + str(listeMonnaie[i])
    elif listeBillet[i] ==0:
        listeChaine[i]= ""
    else :
            listeChaine[i]= str(listeBillet[i]) + "billets de" + str(listeMonnaie[i])
            
    print ("je vous rend:")
    for i in range(7):
        if listeChaine[i] !="":
            print(listeChaine[i])


    print("Merci")