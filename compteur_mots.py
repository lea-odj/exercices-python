#Programme qui donne le nombre de mot et le mot le plus long d'une phrase donnée 
 
phrase = input("entrer une phrase : ")

liste = phrase.split(" ")
print(liste)

def plus_long():
    mot_max = ""
    i = 0
    for mot in liste: 
        if len(mot)> i :
            i = len(mot)
            mot_max = mot 
    return f'le mot le plus long est {mot_max}'

def compteur_mot():
    repetitions = {}
    for mot in liste:
        if mot in repetitions:
            repetitions[mot]+= 1
        else: 
            repetitions[mot]=1 

    lignes = []
    for mot, nb in repetitions.items(): 
        lignes.append(f' {mot} : {nb}')

    return '\n'.join(lignes)

print (compteur_mot(), plus_long())