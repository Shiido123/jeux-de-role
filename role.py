import random
userpv = 50
ennemipv = 50
nb_potions = 3
hero_name = ""
ennemy_name = ""
univers = ""
print("Bienvenue sur le jeu de rôle de Shiido.\nLe but du jeu est de tuer votre ennemi avant que celui-ci ne se charge de vous.\nVous avez tout les deux 50 points de vie au début.\nVous disposez de 3 potions pour vous remettre des points de vie alors que votre ennemi n'en a pas.\nBonne chance soldat.")
univers = input("Dans quel univers souhaitez vous évoluer? ")
print(
    f"Bienvenue dans l'univers {univers} jeux de rôle.\n--------------------------")
hero_name = input("Quel héro voulez vous incarner ? ")
ennemy_name = input("Qui souhaitez vous affronter ? ")

while userpv > 0 and ennemipv > 0:
    user_choices = input(
        "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    user_choices = int(user_choices)
    if user_choices != 1 and user_choices != 2:
        print("Veuillez entrer un nombre valide. 1 ou 2")
        continue

    if user_choices == 1:
        ennemipv = ennemipv - random.randint(5, 10)
        if ennemipv < 1:
            print(f"{ennemy_name} est mort, vous avez gagné")
            break
        else:
            print(f"{ennemy_name} n'a plus que {ennemipv} pv. ⚔️")

    elif user_choices == 2:
        if userpv == 50:
            print(
                f"{hero_name} Vous ne pouvez pas vous rajouter de la potion, vous avez 50 pv.")
        elif nb_potions == 0:
            print(f"{hero_name} Vous n'avez plus de potion")
            continue
        else:
            nb_potions = nb_potions - 1
            userpv = userpv + random.randint(15, 50)
            if userpv > 50:
                userpv = 50
                print(f"{hero_name} Vous avez maintenant {userpv} points de vie")
    # attaque de l'ennemi
    userpv = userpv - random.randint(5, 15)
    if userpv < 1:
        print(f"{hero_name} Vous avez perdu, {ennemy_name} a triomphé.")
        break
    else:
        print(
            f"{ennemy_name} a attaqué, {hero_name} vous n'avez plus que {userpv} points de vie. ⚔️")
