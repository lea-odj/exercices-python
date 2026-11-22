def afficher_menu():
    print("Menu\n1 - Afficher le catalogue\n2 - Ajouter un livre\n3 - Quitter")
    return int(input("Aller à (1-3) : \n"))

def afficher_catalogue(livres):
    if not livres:
        print('Le catalogue est vide, il faut le remplir')
    else:
        for index, (nom, prix, stock) in enumerate(livres,1): 
            print(f'{index}.{nom}\nPrix : {prix}\nStock: {stock} \n')

def ajouter_livre(livres):
    print("Ajouter un livre.")
    nom = input("Titre : ")
    prix = float(input("Prix : "))
    stock = int(input("Stock : "))
    doublon = False 

    #vérification de doublon éventuel 
    for index, (ex_nom, ex_prix, ex_stock) in enumerate(livres):
        if nom == ex_nom :
            doublon = True
            break

    if doublon == True :
        print("le livre existe déjà")

    else: 
        while prix <0:
            print("Prix invalide, veuilez recommencer.")
            prix = float(input('Prix : '))

        while stock <0:
            print('Stock invalide, veuillez recommencer.')
            stock=int(input("Stock : "))

        if stock == 0:
            print("Stock épuisé")
        elif 0 < stock < 3:
            print("Stock Limité !")
        else:
            print("En Stock")

        livres.append([nom, prix, stock])
        print("Le livre a été ajouté au catalogue")

#MAIN
if __name__ == "__main__":

    catalogue = []

    while True : 
        choix = afficher_menu()
        if choix == 1:
            afficher_catalogue(catalogue)
        elif choix == 2:
            ajouter_livre(catalogue)
        elif choix == 3:
            print("Vous avez quitté le menu.")
            break
        else:
            print("Hors de saisie. Réesayer")