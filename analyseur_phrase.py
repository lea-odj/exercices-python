texte = input("choisir le texte : ")
compteur_carac = 0
compteur_digit = 0
compteur_autre = 0
for carac in texte: 
    if carac.isalpha():
        compteur_carac += 1 
    elif carac.isdigit():
        compteur_digit += 1 
    else: 
        compteur_autre += 1

print(f'Il y a {compteur_carac} lettres, {compteur_digit} chiffres et {compteur_autre} autres types de caractères')