#le programme choisit un nombre entre 1 et 20

import random

num = random.randint(1,20)

guess = 0
while guess != num:
    guess = int(input('nombre : '))
    if guess > num:
        print("c'est plus bas!")
    elif guess < num:
        print("c'est plus haut!")

print("Gagné !")