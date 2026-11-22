import json
import os 

if os.path.exists("eleves.json"): 
    with open("eleves.json", "r") as file:
        eleves = json.load(file)
else: 
    eleves = {}

choix = int(input("que voulez vous faire ? \n 1. Consulter les notes d'un élève \n 2. Consulter les appréciations \n 3. Ajouter un élève \n 4. Enlever un élève \n 5. Quitter \n Choix :  "))

while choix != 5 : 
    #notes d'un élève
    if choix == 1: 
        name = input("Lequel ? ")
        if (eleves.get(name, "erreur")) != "erreur":
            print("la moyenne de", name, "est :", eleves[name]["note"])
        else: 
            print('Ce nom n\'est pas dans la liste !')

    #appréciations
    if choix == 2: 
        for prenom, dico in eleves.items():
            print(prenom, ': ', dico["appréciation"])

    #ajouter un élève
    if choix == 3:
        name = input("Quel est son nom ? : ")
        moyenne = int(input("Quelle est sa moyenne ? : ")) 
        remarque = input("Et son appréciation ? ")

        eleves[name] = {
            'note' : moyenne,
            'appréciation' : remarque, 
        }   
        with open("eleves.json", "w") as file : 
            json.dump(eleves, file, indent = 4)

    #supprimer un élève
    if choix == 4: 
        name = input("Lequel ? : ")
        if (eleves.get(name, "erreur")) != "erreur" :
            del eleves[name]
            print("l'élève est retiré.")

            with open("eleves.json", "w") as file : 
                json.dump(eleves, file, indent = 4)
        else: 
            print("L'élève n'est pas dans la liste")

    choix2 = input('voulez vous faire autre chose ? (oui / non)  ')
    if choix2.lower().strip() == "oui": 
        choix = int(input("que voulez vous faire ? \n 1. Consulter les notes d'un élève \n 2. Consulter les appréciations \n 3. Ajouter un élève \n 4. Enlever un élève \n 5. Quitter \n Choix :  "))
    else: 
        break 

print("terminé")