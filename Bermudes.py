# -*- coding: utf-8 -*-
from random import *


def fonction_matrice_milieu_partie():
    matrice = [['●', ' ', '●', ' ', '●', '●', '●', ' ', '●'],
               ['●', 'O', '●', '●', '●', '●', '●', '●', '●'],
               ['O', 'O', '●', '●', ' ', ' ', ' ', '●', '●'],
               ['O', ' ', ' ', ' ', ' ', '●', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', '●', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
               ['O', 'O', ' ', 'O', 'O', 'O', 'O', 'O', '●'],
               ['O', ' ', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    return matrice


def fonction_matrice_fin_partie():
    matrice = [['●', ' ', ' ', '●', ' ', 'O', 'O', 'O', '●'],
               ['●', ' ', ' ', 'O', ' ', ' ', ' ', 'O', '●'],
               ['O', ' ', '●', ' ', ' ', ' ', ' ', ' ', ' '],
               ['O', '●', ' ', ' ', '●', ' ', 'O', ' ', ' '],
               [' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', 'O'],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
               ['O', 'O', ' ', ' ', 'O', 'O', ' ', ' ', 'O'],
               ['O', ' ', 'O', 'O', 'O', 'O', ' ', 'O', 'O']]
    return matrice


def fonction_matrice_debut_partie():
    matrice = [['●', '●', '●', '●', '●', '●', '●', '●', '●'],
               ['●', '●', '●', '●', '●', '●', '●', '●', '●'],
               ['●', '●', '●', '●', '●', '●', '●', '●', '●'],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    return matrice


Matrice_debut_partie = fonction_matrice_debut_partie()
Matrice_milieu_partie = fonction_matrice_milieu_partie()
Matrice_fin_partie = fonction_matrice_fin_partie()
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def creer_matrice(taille):  # Créé une matrice d'une taille donnée
    matrice = [" "] * taille
    for i in range(taille):
        matrice[i] = [" "] * taille
    return matrice


def nombre_pions(table):  # Compte le nombre de pions noirs/blancs sur la grille
    pions_noir, pion_blanc = 0, 0
    for ligne in table:
        for elements in ligne:
            if elements == "●":
                pion_blanc += 1
            elif elements == "O":
                pions_noir += 1
    return pions_noir, pion_blanc


def afficher_table_colonne_2(lignes, table, tour_du_joueur, nb_pions_noir, nb_pion_blanc):
    # Affiche les informations complémentaires
    if lignes == 0 and len(table) > 2:
        print(" Au tour du joueur: ", tour_du_joueur)
    elif lignes == 1 and len(table) > 2:
        print(" Nombre pions blancs: ", nb_pion_blanc)
    elif lignes == 2 and len(table) > 2:
        print(" Nombre pions Noirs: ", nb_pions_noir)
    else:
        print("")


def afficher_table(table, alphabet, tour_du_joueur="<Non précisé>"):  # Affiche une table sur la console
    nb_pions_noir, nb_pion_blanc = nombre_pions(table)
    taille_table = len(table)
    # ╔═══════════════════════════════════════╗╔════════════════════════╗
    # ║     1   2   3   4   5   6   7   8   9 ║║     Projet Bermude     ║
    # ║   ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╝╚════════════════════════╝
    print("╔═════" + "".join(["══" for _ in range(1, taille_table * 2)]) + "╗╔════════════════════════╗")
    print("║     " + "   ".join([str(indication_coor) for indication_coor in range(1, taille_table + 1)]) +
          " ║║     Projet Bermude     ║")
    print("║   ╔" + "╤".join(["═══" for _ in range(1, taille_table + 1)]) + "╝╚════════════════════════╝")

    for lignes in range(taille_table):
        print("║ " + alphabet[lignes] + " ║ " +
              " │ ".join([str(table[lignes][elements]) for elements in range(taille_table)]) + " │", end='')
        # ║ C ║ ● │ ● │ ● │ ● │ ● │ ● │ ● │ ● │ ● │

        afficher_table_colonne_2(lignes, table, tour_du_joueur, nb_pions_noir, nb_pion_blanc)
        if lignes == taille_table - 1:  # ║   ╟───┼───┼───┼───┼───┼───┼───┼───┼───┤
            print("╚═══╝" + "┴".join(["───" for _ in range(1, taille_table + 1)]) + "┘")
        else:  # ╚═══╝───┴───┴───┴───┴───┴───┴───┴───┴───┘
            print("║   ╟" + "┼".join(["───" for _ in range(1, taille_table + 1)]) + "┤")


def saisir_nombre(nb_minimum, nb_maximum):  # demande a l'utilisateur de saisir un nombre tant qu'il n'est pas valide
    print("Nombre compris entre ", nb_minimum, " et ", nb_maximum, " (", nb_minimum, "<= x <=", nb_maximum, ").")
    nombre_selectionne_a_verifier = input("Saisir le nombre souhaitée: ")
    while not verification_nombre_saisie(nombre_selectionne_a_verifier, nb_minimum, nb_maximum):
        print("Entrée invalide !")
        nombre_selectionne_a_verifier = input("Saisir le nombre souhaitée: ")
    nombre_selectionne = int(nombre_selectionne_a_verifier)
    return nombre_selectionne


def verification_nombre_saisie(nombre_selectionne_a_verifier, nb_minimum, nb_maximum):
    # Vérifie que le nombre entré est valide
    if len(str(nombre_selectionne_a_verifier)) == 1:
        return ord(str(nb_minimum)) <= ord(str(nombre_selectionne_a_verifier)) <= ord(str(nb_maximum))
    return False


def afficher_grille_predefini(numero_selectionne):  # affiche une des grilles prédéfinie
    if numero_selectionne == 1:
        matrice_selectionnee = Matrice_debut_partie
    elif numero_selectionne == 2:
        matrice_selectionnee = Matrice_milieu_partie
    if numero_selectionne == 3:
        matrice_selectionnee = Matrice_fin_partie
    afficher_table(matrice_selectionnee, Alphabet)


def saisir_coordonees(grille, text_additionel=""):
    # demande a l'utilisateur de saisir les coordonnées tant qu'elles ne sont pas valides
    while True:
        coordonees_a_valider = str(input("Saisir les coordonnées " + text_additionel + ": "))
        while not verification_syntaxe_saisir_coordonees(coordonees_a_valider):
            print("Syntaxe incorrecte. Exemple A2")
            coordonees_a_valider = str(input("Saisir les coordonnées " + text_additionel + ": "))
        ligne, colonne = extraire_coordonees(coordonees_a_valider)
        colonne = int(colonne)
        if est_dans_grille(ligne, colonne, grille):
            return conversion_coordonees(ligne, colonne)
        print("Syntaxe correcte mais coordonée invalide (Coordonnée minimale A1 et maximale",
              "".join(Alphabet[len(grille) - 1] + str(len(grille)) + ")."))


def conversion_coordonees(ligne, colonne):
    # Converti les coordonnées entrées en fonction de leur indice dans la matrice (D3 -> (3, 2))
    ligne = ord(ligne) - 65
    colonne = colonne - 1
    return ligne, colonne


def extraire_coordonees(coordonees):  # Extraie les coordonnées de la chaine de caractères entrée
    liste_temp = []
    for elements in coordonees:
        liste_temp.append(elements)
    ligne, colonne = liste_temp[0], liste_temp[1]
    return ligne.upper(), colonne


def verification_syntaxe_saisir_coordonees(coordonees_a_valider):
    # Vérifie que les coordonnées extraites soient valides
    if len(coordonees_a_valider) == 2:
        ligne, colonne = extraire_coordonees(coordonees_a_valider)
        return ligne in Alphabet and colonne.isdigit()
    return False


def est_dans_grille(ligne, colonne, grille):  # Vérifie si les coordonnées se trouvent dans la grille
    return ligne in Alphabet[0:len(grille)] and 1 <= colonne <= len(grille)


def direction_valide(position_depart, destination):  # Verifie si les coordonée sont bien dans une des 8 diractions.
    if destination == position_depart:
        return False
    if destination[1] == position_depart[1] or destination[0] == position_depart[0] or \
            abs(position_depart[0] - destination[0]) == abs(position_depart[1] - destination[1]):  # H or V or D
        return True
    return False


def detection_orientation(position_depart, destination):
    # Détecte la direction prise entre les coordonnées de départ et d'arrivée
    if destination[0] == position_depart[0] and destination[1] > position_depart[1]:
        return "HD"  # Horizontale Droit
    if destination[0] == position_depart[0] and destination[1] < position_depart[1]:
        return "HG"  # Horizontale Gauche
    if destination[1] == position_depart[1] and destination[0] > position_depart[0]:
        return "VB"  # verticale Bas
    if destination[1] == position_depart[1] and destination[0] < position_depart[0]:
        return "VH"  # verticale Haut
    if destination[1] < position_depart[1] and destination[0] < position_depart[0]:
        return "DGH"  # diagonale Gauche Haut
    if destination[1] < position_depart[1] and destination[0] > position_depart[0]:
        return "DGB"  # diagonale Gauche Bas
    if destination[1] > position_depart[1] and destination[0] > position_depart[0]:
        return "DDB"  # diagonale Droit Bas
    if destination[1] > position_depart[1] and destination[0] < position_depart[0]:
        return "DDH"  # diagonale Droit Haut


def emplacement_libre_entre(position_depart, destination, grille):
    # Vérifie s'il n'y a pas de pions entre les deux coordonnées
    orientation = detection_orientation(position_depart, destination)
    if orientation == "VB" or orientation == "VH" or orientation == "HG" or orientation == "HD":
        return emplacement_libre_entre_hori_verti(orientation, position_depart, destination, grille)
    else:
        return emplacement_libre_entre_diagonale(orientation, position_depart, destination, grille)


def emplacement_libre_entre_hori_verti(orientation, position_depart, destination, grille):
    # Sous fonction de emplacement_libre_entre() pour les verticales et les horizontales
    if orientation == "VB" or orientation == "VH":
        for i in range(min(position_depart[0], destination[0]) + 1, max(position_depart[0], destination[0])):
            if grille[i][position_depart[1]] != " ":
                return False
    elif orientation == "HG" or orientation == "HD":
        for i in range(min(position_depart[1], destination[1]) + 1, max(position_depart[1], destination[1])):
            if grille[position_depart[0]][i] != " ":
                return False
    return True


def emplacement_libre_entre_diagonale(orientation, position_depart, destination, grille):
    # sous fonction de emplacement_libre_entre() pour les diagonales
    pos = position_depart
    while pos != destination:
        if orientation == "DGH":
            pos = pos[0] - 1, pos[1] - 1
        elif orientation == "DDB":
            pos = pos[0] + 1, pos[1] + 1
        elif orientation == "DGB":
            pos = pos[0] + 1, pos[1] - 1
        elif orientation == "DDH":
            pos = pos[0] - 1, pos[1] + 1
        if grille[pos[0]][pos[1]] != " " and pos != destination:
            return False
    return True


def emplacement_libre_apres_position_depart(position_depart, destination, grille):
    # Vérifie si l'emplacement après le pion de départ est vide (dans l'axe du pion de destination)
    orientation = detection_orientation(position_depart, destination)
    if (orientation == "VH" and grille[position_depart[0] - 1][position_depart[1]] == " "
            or orientation == "VB" and grille[position_depart[0] + 1][position_depart[1]] == " "
            or orientation == "HG" and grille[position_depart[0]][position_depart[1] - 1] == " "
            or orientation == "HD" and grille[position_depart[0]][position_depart[1] + 1] == " "
            or orientation == "DGH" and grille[position_depart[0] - 1][position_depart[1] - 1] == " "
            or orientation == "DGB" and grille[position_depart[0] + 1][position_depart[1] - 1] == " "
            or orientation == "DDH" and grille[position_depart[0] - 1][position_depart[1] + 1] == " "
            or orientation == "DDB" and grille[position_depart[0] + 1][position_depart[1] + 1] == " "):
        return True
    return False


def coordonees_pion_avant(position_depart, destination):
    # Renvoie les coordonnées du pion avant le pion destinataire (dans l'axe du pion de départ)
    orientation = detection_orientation(position_depart, destination)
    if orientation == "VB":
        return destination[0] - 1, destination[1]
    elif orientation == "VH":
        return destination[0] + 1, destination[1]
    elif orientation == "HD":
        return destination[0], destination[1] - 1
    elif orientation == "HG":
        return destination[0], destination[1] + 1
    elif orientation == "DDB":
        return destination[0] - 1, destination[1] - 1
    elif orientation == "DDH":
        return destination[0] + 1, destination[1] - 1
    elif orientation == "DGB":
        return destination[0] - 1, destination[1] + 1
    elif orientation == "DGH":
        return destination[0] + 1, destination[1] + 1


def coordonees_pion_apres(position_depart, destination):
    # Vérifie si l'emplacement après le pion de départ est vide (dans l'axe du pion de destination)
    orientation = detection_orientation(position_depart, destination)
    if orientation == "VH":
        return destination[0] - 1, destination[1]
    elif orientation == "VB":
        return destination[0] + 1, destination[1]
    elif orientation == "HG":
        return destination[0], destination[1] - 1
    elif orientation == "HD":
        return destination[0], destination[1] + 1
    elif orientation == "DGH":
        return destination[0] - 1, destination[1] - 1
    elif orientation == "DGB":
        return destination[0] + 1, destination[1] - 1
    elif orientation == "DDH":
        return destination[0] - 1, destination[1] + 1
    elif orientation == "DDB":
        return destination[0] + 1, destination[1] + 1


def element_case(variable, grille):
    # Renvoie l'élément ayant pour coordonnée "variable" dans une grille donnée
    return grille[variable[0]][variable[1]]


def set_element_case(variable, nouveau, grille):
    # remplace un élément (aux coordonnées "variable") par un nouveau dans une grille donnée
    grille[variable[0]][variable[1]] = nouveau


def pion_est_ennemi(position_depart, destination, grille):
    # Vérifie que deux pions sont ennemis et qu'il y a bien un pion à la position destination.
    if element_case(position_depart, grille) != element_case(destination, grille) and \
            element_case(destination, grille) != " ":
        return True
    return False


def fin_partie(grille, affichage=True):
    # Vérifie si la partie est finie ou non
    nb_pions_noir, nb_pion_blanc = nombre_pions(grille)
    if nb_pions_noir < 6 or nb_pion_blanc < 6:
        if nb_pions_noir < 6:
            if affichage:
                return True, print("le joueur \"●\" à gagner !")
            return True
        elif nb_pion_blanc < 6:
            if affichage:
                return True, print("le joueur \"O\" à gagner !")
            return True
    return False


def deplacement_elimination(position_depart, destination, grille, pas_de_deplacement=False):
    # Vérifie si les pions sélectionnés sont valides au déplacement. Si c'est le cas le déplacement est effectué
    if direction_valide(position_depart, destination):  # Vérifie que l'axe entre les deux pions est valide
        if pion_est_ennemi(position_depart, destination, grille):  # Vérifie que les deux pions sont ennemi
            if emplacement_libre_entre(position_depart, destination, grille) and \
                    emplacement_libre_apres_position_depart(position_depart, destination, grille):
                # Verifie qu'il y a bien une case vide entre les deux pions et
                # que les cases (s'il y en a plusieur) entre les deux pions sont toutes vides
                if not pas_de_deplacement:  # Ne réalise pas les déplacements dans le cas des asserts
                    set_element_case(destination, element_case(position_depart, grille), grille)
                    set_element_case(position_depart, " ", grille)
                return True  # Renvoie True si le déplacement est valide ou a été effectué.
    return False


def deplacement_retournement(position_depart, destination, grille, pas_de_deplacement=False):
    # Vérifie si les pions sélectionnés sont valides au déplacement. Si c'est le cas le déplacement est effectué
    if direction_valide(position_depart, destination):  # Vérifie que l'axe entre les deux pions est valide
        if element_case(destination, grille) == " ":  # Vérifie que la case de destination est vide
            pion_avant_destination = coordonees_pion_avant(position_depart, destination)
            if pion_est_ennemi(position_depart, pion_avant_destination, grille):
                # Vérifie que les éléments des deux cases sont différents
                if emplacement_libre_entre(position_depart, pion_avant_destination, grille):
                    # Vérifie que les cases entre les deux pions sont toutes vides
                    if not pas_de_deplacement:  # Ne réalise pas les déplacements dans le cas des asserts
                        set_element_case(destination, element_case(position_depart, grille), grille)
                        set_element_case(pion_avant_destination, element_case(position_depart, grille), grille)
                        set_element_case(position_depart, " ", grille)
                    return True  # Renvoie True si le déplacement est valide ou a été effectué.
    return False


def coordonees_pions_joueur(grille):
    coor_pions_noir, coor_pions_blanc = [], []
    for ligne in range(len(grille)):
        for elements in range(len(grille)):
            if grille[ligne][elements] == "●":
                coor_pions_blanc.append((ligne, elements))
            elif grille[ligne][elements] == "O":
                coor_pions_noir.append((ligne, elements))
    return coor_pions_noir, coor_pions_blanc


def demander_pion_depart(pion_joueur, grille):  # sous fonction de tour_joueur(). Saisie pion depart
    coor_pions_noir, coor_pions_blanc = coordonees_pions_joueur(grille)
    pion_depart = saisir_coordonees(grille, "du pion de départ")
    while pion_joueur == "O" and pion_depart not in coor_pions_noir or pion_joueur == "●" and \
            pion_depart not in coor_pions_blanc:  # Vérifie que le pion sélectionné appartient au joueur
        print("Le pion sélectionné n'est pas un de vos pions.")
        pion_depart = saisir_coordonees(grille, "du pion de départ")
    return pion_depart


def tour_joueur_dp_retournement(position_destination, pion_joueur, assistant, grille):
    # sous fonction de tour_joueur(). Enchainement déplacement par retournement
    print("Vous avez fait un déplacement par retournement.")
    afficher_table(grille, Alphabet, pion_joueur)

    pion_depart = position_destination

    liste_dep_retournement = assistant_deplacement_retournement(pion_joueur, grille, pion_depart)
    if assistant:
        liste_deplacement_possible = affichage_assistant_deplacement(liste_dep_retournement, "retournement")

    if len(liste_deplacement_possible) > 0:
        print("Vous pouvez continuer ce type de déplacement. Écrivez des coordonnées non valide pour arrêter.")
        position_destination = saisir_coordonees(grille, "de la case de destination")

        while deplacement_retournement(pion_depart, position_destination, grille) and len(
                liste_deplacement_possible) > 0:
            # Tant que le déplacement réalisé est valide et que d'autres sont réalisables
            afficher_table(grille, Alphabet, pion_joueur)
            pion_depart = position_destination

            liste_dep_retournement = assistant_deplacement_retournement(pion_joueur, grille, pion_depart)
            if assistant:
                liste_deplacement_possible = affichage_assistant_deplacement(liste_dep_retournement, "retournement")

            if len(liste_deplacement_possible) > 0:
                position_destination = saisir_coordonees(grille, "de la case de destination")
            else:
                print("Aucun déplacement possible.")
    else:
        print("Aucun déplacement possible.")


def format_tuple(tuple):
    return str(tuple).replace(",", "").replace("(", "").replace(")", "").replace(" ", "").replace("'", "")


def tour_robot_dp_retournement(liste_deplacement, grille):
    deplacement_choisi = choice(liste_deplacement)
    pion_depart = deplacement_choisi[0]
    destination = deplacement_choisi[1]

    liste_dep_retour = assistant_deplacement_retournement(grille[pion_depart[0]][pion_depart[1]], grille, pion_depart)
    while deplacement_retournement(pion_depart, destination, grille) and len(liste_dep_retour) > 0:
        print(format_tuple(conversion_coordonees_inv(pion_depart[0], pion_depart[1])), " -> ",
              format_tuple(conversion_coordonees_inv(destination[0], destination[1])))
        pion_depart = destination
        liste_dep_retour = assistant_deplacement_retournement(element_case(pion_depart, grille), grille, pion_depart)
        if len(liste_dep_retour) > 0:
            deplacement_choisi = choice(liste_dep_retour)
            destination = deplacement_choisi[1]


def tour_robot_dp_elimination(liste_deplacement, grille):
    deplacement = choice(liste_deplacement)
    pion_depart = deplacement[0]
    position_destination = deplacement[1]
    deplacement_elimination(pion_depart, position_destination, grille)
    print(format_tuple(conversion_coordonees_inv(pion_depart[0], pion_depart[1])), " -> ",
          format_tuple(conversion_coordonees_inv(position_destination[0], position_destination[1])))


def tour_robot_choix_type_deplacement(liste_dep_retour, liste_dep_elim):
    if len(liste_dep_retour) > 0 and len(liste_dep_elim) > 0:
        # l'ordi choisi aléatoirement si les deux types de déplacement sont disponible
        choix_type_deplacement = randrange(0, 2)
    else:
        if not len(liste_dep_retour) > 0:
            choix_type_deplacement = 0
        elif not len(liste_dep_elim) > 0:
            choix_type_deplacement = 1
    return choix_type_deplacement


def tour_lancer(grille, pion_joueur, assistant, robot=False):  # Effectue le tour d'un joueur
    afficher_table(grille, Alphabet, pion_joueur)

    liste_dep_elim = assistant_deplacement_elimination(pion_joueur, grille)
    liste_dep_retour = assistant_deplacement_retournement(pion_joueur, grille)

    if assistant and not robot:  # Affiche les déplacements possibles si assistant est activé
        affichage_assistant_deplacement(liste_dep_elim, "élimination")
        affichage_assistant_deplacement(liste_dep_retour, "retournement")

    tour_valide = False
    while not tour_valide:
        if robot:
            choix_type_deplacement = tour_robot_choix_type_deplacement(liste_dep_retour, liste_dep_elim)
            if choix_type_deplacement == 0:  # deplacement_elimination
                print("L'ordinateur a fait une prise par elimination")
                tour_robot_dp_elimination(liste_dep_elim, grille)
                tour_valide = True
            elif choix_type_deplacement == 1 and len(liste_dep_retour) > 0:  # deplacement_retournement
                print("L'ordinateur a fait une prise par retournement")
                tour_robot_dp_retournement(liste_dep_retour, grille)
                tour_valide = True
        else:
            pion_depart = demander_pion_depart(pion_joueur, grille)
            position_destination = saisir_coordonees(grille, "de la case de destination")
            if deplacement_elimination(pion_depart, position_destination, grille):  # deplacement_elimination
                print("Vous avez fait un déplacement par élimination.")
                tour_valide = True
            elif deplacement_retournement(pion_depart, position_destination, grille):  # deplacement_retournement
                tour_joueur_dp_retournement(position_destination, pion_joueur, assistant, grille)
                tour_valide = True
            else:  # Déplacement demandé invalide
                print("Merci de respécter les règles de déplacement.")
                tour_valide = False

    afficher_table(grille, Alphabet, pion_joueur)


def assistant_deplacement_convertir_joueur(pion_joueur):
    # sous fonction de assistant_deplacement_elimination / retournement
    if pion_joueur == "O":
        joueur, autre_joueur = 0, 1
    elif pion_joueur == "●":
        joueur, autre_joueur = 1, 0
    return joueur, autre_joueur


def assistant_deplacement_elimination(pion_joueur, grille):  # créé une liste de déplacements par élimination
    position_pions = coordonees_pions_joueur(grille)
    liste_deplacement_possible = []
    joueur, autre_joueur = assistant_deplacement_convertir_joueur(pion_joueur)
    for pions in position_pions[joueur]:
        for pion_adverse in position_pions[autre_joueur]:
            if deplacement_elimination(pions, pion_adverse, grille, True):
                liste_deplacement_possible.append((pions, pion_adverse))
    return liste_deplacement_possible


def assistant_deplacement_retournement(pion_joueur, grille, pion_depart_force=()):
    # créé une liste de déplacements par retournement
    position_pions = coordonees_pions_joueur(grille)
    liste_deplacement_possible = []
    joueur, autre_joueur = assistant_deplacement_convertir_joueur(pion_joueur)
    if pion_depart_force == ():
        for pions in position_pions[joueur]:
            liste_deplacement_possible = assistant_determiner_retournement(
                liste_deplacement_possible, position_pions, autre_joueur, pions, grille)
    else:
        liste_deplacement_possible = assistant_determiner_retournement(
            liste_deplacement_possible, position_pions, autre_joueur, pion_depart_force, grille)
    return liste_deplacement_possible


def assistant_determiner_retournement(liste_deplacement_possible, position_pions, autre_joueur, pion_depart, grille):
    # sous fonction pour eviter une répétition de boucle dans assistant_deplacement_retournement()
    for pion_adverse in position_pions[autre_joueur]:
        pion_apres = coordonees_pion_apres(pion_depart, pion_adverse)
        if 0 <= pion_apres[0] <= 8 and 0 <= pion_apres[1] <= 8:
            if deplacement_retournement(pion_depart, pion_apres, grille, True):
                liste_deplacement_possible.append((pion_depart, pion_apres))
    return liste_deplacement_possible


def affichage_assistant_deplacement(liste, type_deplacement):  # affiche les déplacements créés par l'assistant
    print('\nles déplacements par {0} possible sont :'.format(type_deplacement))
    for element in liste:
        pion1 = conversion_coordonees_inv(element[0][0], element[0][1])
        pion2 = conversion_coordonees_inv(element[1][0], element[1][1])
        print(pion1[0] + str(pion1[1]) + " -> " + pion2[0] + str(pion2[1]))
    return liste


def conversion_coordonees_inv(ligne, colonne):
    # Converti les coordonnées entrées ( (3, 2) -> ('D', 3) )
    ligne = chr(ligne + 65)
    colonne = colonne + 1
    return ligne, colonne


def partie_ordi_ordi(grille, assistant):
    cpt_tour = 1
    while not fin_partie(grille):
        print("=============================================================================================")
        print("tour n°", cpt_tour)
        print("=============================================================================================")
        tour_lancer(grille, "O", assistant, robot=True)
        print("-----------------------------------------------------------")
        if not fin_partie(grille, affichage=False):
            tour_lancer(grille, "●", assistant, robot=True)
        cpt_tour += 1


def partie_joueur_ordi(grille, assistant):
    while not fin_partie(grille):
        print("=============================================================================================")
        tour_lancer(grille, "O", assistant)
        print("-----------------------------------------------------------")
        if not fin_partie(grille, affichage=False):
            tour_lancer(grille, "●", assistant, robot=True)
            print("=============================================================================================")


def partie_joueur_joueur(grille, assistant):
    while not fin_partie(grille):
        print("=============================================================================================")
        tour_lancer(grille, "O", assistant)
        print("-----------------------------------------------------------")
        if not fin_partie(grille, affichage=False):
            tour_lancer(grille, "●", assistant)
            print("=============================================================================================")


def test_creer_matrice():  # Teste la fonction "cree_matrice"
    valeur_aleatoire = randint(1, 10)
    matrice_aleatoire = creer_matrice(valeur_aleatoire)
    assert creer_matrice(0) == [], "Matrice de taille 0 (vide) incorrect"
    assert creer_matrice(2) == [[' ', ' '], [' ', ' ']], "Matrice de taille 2 incorrects"
    assert len(matrice_aleatoire) == valeur_aleatoire, "Nombre de lignes invalident dans la matrice"
    assert len(matrice_aleatoire) == len(matrice_aleatoire[0]), "Nombre de lignes different de celle des colonnes"


def test_est_dans_grille():  # Teste la fonction "est_dans_grille"
    grille = creer_matrice(randint(1, 10))
    assert est_dans_grille("A", 1, grille), "Vérifie les coordonnées minimales de la grille"
    assert est_dans_grille(Alphabet[len(grille) - 1], len(grille), grille), \
        "Vérifie les coordonnées maximales de la grille"
    assert not est_dans_grille(Alphabet[len(grille)], 1, grille), \
        "Vérifie que la ligne entrée ne peut pas être supérieur à la taille de la grille"
    assert not est_dans_grille("A", len(grille) + 1, grille), \
        "Vérifie que la colonne entrée ne peut pas être supérieur à la taille de la grille"
    assert not est_dans_grille("A", 0, grille), "Vérifie que la colonne entrée ne peut pas être inférieur à \"1\""


def test_saisir_coordonnees():  # Teste la fonction "verification_syntaxe_saisir_coordonees"
    assert verification_syntaxe_saisir_coordonees("A5"), "Vérifie que les colonnes soient bien un nombre"
    assert not verification_syntaxe_saisir_coordonees("AA"), "Vérifie que les colonnes soient bien un nombre"
    assert verification_syntaxe_saisir_coordonees("D6"), "Vérifie que les lignes sont bien des lettres"
    assert not verification_syntaxe_saisir_coordonees("66"), "Vérifie que les lignes sont bien des lettres"
    assert verification_syntaxe_saisir_coordonees("c8"), \
        "Vérifie que les lignes sont bien des lettres (teste minuscule)"
    assert not verification_syntaxe_saisir_coordonees("A12"), \
        "Vérifie que les coordonnées saisies ne dépassent pas \"9\""


def test_saisir_nombre():  # Teste la fonction "verification_nombre_saisie"
    nb_minimum = randint(0, 5)
    nb_maximum = randint(5, 9)
    assert not verification_nombre_saisie(Alphabet[randint(0, 25)], nb_minimum, nb_maximum), \
        "Seuls les nombres sont autorisés"
    assert verification_nombre_saisie(nb_minimum, nb_minimum, nb_maximum), "Le minimum doit être inclut"
    assert verification_nombre_saisie(nb_minimum, nb_minimum, nb_maximum), "Le maximum doit être inclut"


def test_nombre_pions():  # Teste la fonction "nombre_pions"
    assert (27, 27) == nombre_pions(Matrice_debut_partie), "Nombre de pions incorrects (grille debut partie)"
    assert (20, 21) == nombre_pions(Matrice_milieu_partie), "Nombre de pions incorrects (grille milieu partie)"
    assert (24, 8) == nombre_pions(Matrice_fin_partie), "Nombre de pions incorrects (grille fin partie)"


def test_conversion_coordonees():  # Teste la fonction "conversion_coordonees"
    assert (0, 0) == conversion_coordonees("A", 1), "Conversion case A1"
    assert (8, 8) == conversion_coordonees("I", 9), "Conversion case I9"


def test_direction_valide():  # Teste la fonction "direction_valide"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("D", 5)), "direction valide VH"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("F", 5)), "direction valide VB"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("E", 4)), "direction valide HG"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("E", 6)), "direction valide HD"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("D", 4)), "direction valide DGH"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("D", 6)), "direction valide DDH"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("F", 4)), "direction valide DGB"
    assert direction_valide(conversion_coordonees("E", 5), conversion_coordonees("F", 6)), "direction valide DDB"


def test_detection_orientation():  # Teste la fonction "detection_orientation"
    assert "VH" == detection_orientation((4, 4), (0, 4)), "VH detection orientation"
    assert "VB" == detection_orientation((4, 4), (5, 4)), "VB detection orientation"
    assert "HG" == detection_orientation((4, 4), (4, 0)), "HG detection orientation"
    assert "HD" == detection_orientation((4, 4), (4, 7)), "HD detection orientation"
    assert "DGH" == detection_orientation((4, 4), (0, 0)), "DGH detection orientation"
    assert "DGB" == detection_orientation((4, 4), (6, 2)), "DGB detection orientation"
    assert "DDH" == detection_orientation((4, 4), (3, 5)), "DDH detection orientation"
    assert "DDB" == detection_orientation((4, 4), (6, 6)), "DDB detection orientation"


def test_emplacement_libre_entre():  # Teste la fonction "emplacement_libre_entre"
    assert emplacement_libre_entre(conversion_coordonees("H", 1), conversion_coordonees("D", 1),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation VH"
    assert not emplacement_libre_entre(conversion_coordonees("H", 5), conversion_coordonees("B", 5),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation VH"
    assert emplacement_libre_entre(conversion_coordonees("C", 9), conversion_coordonees("G", 9),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation VB"
    assert not emplacement_libre_entre(conversion_coordonees("B", 6), conversion_coordonees("H", 6),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation VB"
    assert emplacement_libre_entre(conversion_coordonees("D", 6), conversion_coordonees("D", 1),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation HG"
    assert not emplacement_libre_entre(conversion_coordonees("A", 9), conversion_coordonees("A", 6),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation HG"
    assert emplacement_libre_entre(conversion_coordonees("C", 4), conversion_coordonees("C", 8),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation HD"
    assert not emplacement_libre_entre(conversion_coordonees("H", 2), conversion_coordonees("H", 5),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation HD"
    assert emplacement_libre_entre(conversion_coordonees("G", 9), conversion_coordonees("D", 6),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation DGH"
    assert not emplacement_libre_entre(conversion_coordonees("H", 9), conversion_coordonees("B", 3),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation DGH"
    assert emplacement_libre_entre(conversion_coordonees("H", 2), conversion_coordonees("E", 5),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation DDH"
    assert not emplacement_libre_entre(conversion_coordonees("E", 5), conversion_coordonees("B", 8),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation DDH"
    assert emplacement_libre_entre(conversion_coordonees("C", 9), conversion_coordonees("H", 4),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation DGB"
    assert not emplacement_libre_entre(conversion_coordonees("D", 6), conversion_coordonees("H", 2),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation DGB"
    assert emplacement_libre_entre(conversion_coordonees("C", 3), conversion_coordonees("E", 5),
                                   Matrice_milieu_partie), "Emplacement libre entre orientation DDB"
    assert not emplacement_libre_entre(conversion_coordonees("B", 4), conversion_coordonees("G", 9),
                                       Matrice_milieu_partie), "Emplacement libre entre orientation DDB"


def test_pion_est_ennemi():  # Teste la fonction "pion_est_ennemi"
    assert pion_est_ennemi(conversion_coordonees("B", 7), conversion_coordonees("H", 1), Matrice_milieu_partie), \
        "Pion est ennemie"
    assert not pion_est_ennemi(conversion_coordonees("A", 1), conversion_coordonees("B", 1), Matrice_milieu_partie), \
        "Pion n'es pas ennemie"


def test_emplacement_libre_apres_position_depart():  # Teste la fonction "emplacement_libre_apres_position_depart"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("C", 4), conversion_coordonees("B", 4),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation VH"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("D", 6), conversion_coordonees("B", 6),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation VH"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("C", 9), conversion_coordonees("E", 9),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation VB"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("B", 4), conversion_coordonees("D", 4),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation VB"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("C", 8), conversion_coordonees("C", 4),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation HG"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("A", 6), conversion_coordonees("A", 4),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation HG"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("A", 1), conversion_coordonees("A", 3),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation HD"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("H", 4), conversion_coordonees("H", 6),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation HD"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("D", 6), conversion_coordonees("B", 4),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation DGH"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("C", 8), conversion_coordonees("A", 6),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation DGH"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("D", 6), conversion_coordonees("B", 8),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation DDH"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("E", 5), conversion_coordonees("C", 7),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation DDH"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("C", 7), conversion_coordonees("E", 5),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation DGB"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("E", 5), conversion_coordonees("H", 3),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation DGB"
    assert emplacement_libre_apres_position_depart(conversion_coordonees("D", 6), conversion_coordonees("G", 9),
                                                   Matrice_milieu_partie), "Emplacement libre apres orientation DDB"
    assert not emplacement_libre_apres_position_depart(conversion_coordonees("A", 6), conversion_coordonees("C", 8),
                                                       Matrice_milieu_partie), "Emplacement libre apres orientation DDB"


def test_coordonees_pion_avant():  # Teste la fonction "coordonees_pion_avant"
    assert (2, 4) == coordonees_pion_avant(conversion_coordonees("E", 5), conversion_coordonees("B", 5)), \
        "coordonees pion avant orientation VH"
    assert (1, 8) == coordonees_pion_avant(conversion_coordonees("A", 9), conversion_coordonees("C", 9)), \
        "coordonees pion avant orientation VB"
    assert (1, 1) == coordonees_pion_avant(conversion_coordonees("B", 4), conversion_coordonees("B", 1)), \
        "coordonees pion avant orientation HG"
    assert (3, 4) == coordonees_pion_avant(conversion_coordonees("D", 1), conversion_coordonees("D", 6)), \
        "coordonees pion avant orientation HD"
    assert (1, 3) == coordonees_pion_avant(conversion_coordonees("D", 6), conversion_coordonees("A", 3)), \
        "coordonees pion avant orientation DGH"
    assert (2, 6) == coordonees_pion_avant(conversion_coordonees("E", 5), conversion_coordonees("B", 8)), \
        "coordonees pion avant orientation DDH"
    assert (7, 1) == coordonees_pion_avant(conversion_coordonees("E", 5), conversion_coordonees("I", 1)), \
        "coordonees pion avant orientation DGB"
    assert (5, 7) == coordonees_pion_avant(conversion_coordonees("A", 3), conversion_coordonees("G", 9)), \
        "coordonees pion avant orientation DDB"


def test_element_case():  # Teste la fonction "element_case"
    assert element_case(conversion_coordonees("C", 2), Matrice_milieu_partie) == "O", "element case \"O\""
    assert element_case(conversion_coordonees("C", 3), Matrice_milieu_partie) == "●", "element case \"●\""
    assert element_case(conversion_coordonees("C", 5), Matrice_milieu_partie) == " ", "element case \" \""


def test_deplacement_elimination():  # Teste la fonction "deplacement_elimination"
    assert deplacement_elimination(conversion_coordonees("H", 5), conversion_coordonees("E", 5), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation VH"
    assert not deplacement_elimination(conversion_coordonees("H", 2), conversion_coordonees("C", 2),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation VH"
    assert deplacement_elimination(conversion_coordonees("D", 6), conversion_coordonees("H", 6), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation VB"
    assert not deplacement_elimination(conversion_coordonees("D", 1), conversion_coordonees("H", 1),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation VB"
    assert deplacement_elimination(conversion_coordonees("D", 6), conversion_coordonees("D", 1), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation HG"
    assert not deplacement_elimination(conversion_coordonees("C", 8), conversion_coordonees("C", 4),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation HG"
    assert deplacement_elimination(conversion_coordonees("D", 1), conversion_coordonees("D", 6), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation HD"
    assert not deplacement_elimination(conversion_coordonees("A", 3), conversion_coordonees("A", 5),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation HD"
    assert deplacement_elimination(conversion_coordonees("E", 5), conversion_coordonees("H", 2), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation DGH"
    assert not deplacement_elimination(conversion_coordonees("D", 6), conversion_coordonees("H", 2),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation DGH"
    assert deplacement_elimination(conversion_coordonees("G", 9), conversion_coordonees("D", 6), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation DDH"
    assert not deplacement_elimination(conversion_coordonees("E", 5), conversion_coordonees("C", 3),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation DDH"
    assert deplacement_elimination(conversion_coordonees("H", 2), conversion_coordonees("E", 5), Matrice_milieu_partie,
                                   True), "deplacement elimination orientation DGB"
    assert not deplacement_elimination(conversion_coordonees("I", 1), conversion_coordonees("H", 2),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation DGB"
    assert deplacement_elimination(conversion_coordonees("B", 1), conversion_coordonees("E", 4), Matrice_fin_partie,
                                   True), "deplacement elimination orientation DDB"
    assert not deplacement_elimination(conversion_coordonees("C", 2), conversion_coordonees("H", 1),
                                       Matrice_milieu_partie, True), "deplacement elimination orientation DDB"


def test_deplacement_retournement():  # Teste la fonction "deplacement_retournement"
    assert deplacement_retournement(conversion_coordonees("E", 5), conversion_coordonees("C", 5), Matrice_fin_partie,
                                    True), "deplacement elimination orientation VH"
    assert not deplacement_retournement(conversion_coordonees("I", 1), conversion_coordonees("G", 1),
                                        Matrice_fin_partie, True), "deplacement elimination orientation VH"
    assert deplacement_retournement(conversion_coordonees("D", 2), conversion_coordonees("I", 2), Matrice_fin_partie,
                                    True), "deplacement elimination orientation VB"
    assert not deplacement_retournement(conversion_coordonees("B", 4), conversion_coordonees("F", 4),
                                        Matrice_fin_partie, True), "deplacement elimination orientation VB"
    assert deplacement_retournement(conversion_coordonees("D", 7), conversion_coordonees("D", 4), Matrice_fin_partie,
                                    True), "deplacement elimination orientation HG"
    assert not deplacement_retournement(conversion_coordonees("E", 9), conversion_coordonees("E", 3),
                                        Matrice_fin_partie, True), "deplacement elimination orientation HG"
    assert deplacement_retournement(conversion_coordonees("D", 5), conversion_coordonees("D", 8), Matrice_fin_partie,
                                    True), "deplacement elimination orientation HD"
    assert not deplacement_retournement(conversion_coordonees("D", 1), conversion_coordonees("D", 6),
                                        Matrice_fin_partie, True), "deplacement elimination orientation HD"
    assert deplacement_retournement(conversion_coordonees("E", 5), conversion_coordonees("B", 2), Matrice_fin_partie,
                                    True), "deplacement elimination orientation DGH"
    assert not deplacement_retournement(conversion_coordonees("G", 9), conversion_coordonees("A", 3),
                                        Matrice_fin_partie, True), "deplacement elimination orientation DGH"
    assert deplacement_retournement(conversion_coordonees("E", 4), conversion_coordonees("C", 6), Matrice_fin_partie,
                                    True), "deplacement elimination orientation DDH"
    assert not deplacement_retournement(conversion_coordonees("H", 2), conversion_coordonees("D", 6),
                                        Matrice_fin_partie, True), "deplacement elimination orientation DDH"
    assert deplacement_retournement(conversion_coordonees("B", 9), conversion_coordonees("E", 6), Matrice_fin_partie,
                                    True), "deplacement elimination orientation DGB"
    assert not deplacement_retournement(conversion_coordonees("B", 4), conversion_coordonees("E", 2),
                                        Matrice_fin_partie, True), "deplacement elimination orientation DGB"
    assert deplacement_retournement(conversion_coordonees("C", 3), conversion_coordonees("F", 6), Matrice_fin_partie,
                                    True), "deplacement elimination orientation DDB"
    assert not deplacement_retournement(conversion_coordonees("C", 1), conversion_coordonees("I", 7),
                                        Matrice_fin_partie, True), "deplacement elimination orientation DDB"


def test_coordonees_pions_joueur():
    assert coordonees_pions_joueur(Matrice_debut_partie) == (
        [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 0), (7, 1), (7, 2), (7, 3),
         (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7),
         (8, 8)], [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2),
                   (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
                   (2, 6), (2, 7),
                   (2, 8)]), "coordonees pions joueur Matrice debut partie"
    assert coordonees_pions_joueur(Matrice_milieu_partie) == ([(1, 1), (2, 0), (2, 1), (3, 0), (6, 8), (7, 0), (7, 1),
                                                               (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 0), (8, 2),
                                                               (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)],
                                                              [(0, 0), (0, 2), (0, 4), (0, 5), (0, 6), (0, 8), (1, 0),
                                                               (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                                                               (1, 8), (2, 2), (2, 3), (2, 7), (2, 8), (3, 5), (4, 4),
                                                               (7, 8)]), "coordonees pions joueur Matrice milieu partie"
    assert coordonees_pions_joueur(Matrice_fin_partie) == ([(0, 5), (0, 6), (0, 7), (1, 3), (1, 7), (2, 0), (3, 0),
                                                            (3, 6), (4, 3), (4, 4), (4, 8), (6, 8), (7, 0), (7, 1),
                                                            (7, 4), (7, 5), (7, 8), (8, 0), (8, 2), (8, 3), (8, 4),
                                                            (8, 5), (8, 7), (8, 8)],
                                                           [(0, 0), (0, 3), (0, 8), (1, 0), (1, 8), (2, 2), (3, 1),
                                                            (3, 4)]), \
        "coordonees pions joueur Matrice fin partie"


def test_coordonees_pion_apres():  # Teste la fonction "coordonees_pion_avant"
    assert (1, 2) == coordonees_pion_apres(conversion_coordonees("I", 3), conversion_coordonees("C", 3)), \
        "coordonees pion avant orientation VH"
    assert (5, 4) == coordonees_pion_apres(conversion_coordonees("D", 5), conversion_coordonees("E", 5)), \
        "coordonees pion avant orientation VB"
    assert (3, 3) == coordonees_pion_apres(conversion_coordonees("D", 7), conversion_coordonees("D", 5)), \
        "coordonees pion avant orientation HG"
    assert (0, 4) == coordonees_pion_apres(conversion_coordonees("A", 1), conversion_coordonees("A", 4)), \
        "coordonees pion avant orientation HD"
    assert (1, 1) == coordonees_pion_apres(conversion_coordonees("E", 5), conversion_coordonees("C", 3)), \
        "coordonees pion avant orientation DGH"
    assert (0, 8) == coordonees_pion_apres(conversion_coordonees("E", 5), conversion_coordonees("B", 8)), \
        "coordonees pion avant orientation DDH"
    assert (8, 0) == coordonees_pion_apres(conversion_coordonees("E", 5), conversion_coordonees("H", 2)), \
        "coordonees pion avant orientation DGB"
    assert (5, 4) == coordonees_pion_apres(conversion_coordonees("B", 1), conversion_coordonees("E", 4)), \
        "coordonees pion avant orientation DDB"


def lancer_testes_fonctions():  # Exécute l'ensemble des fonctions teste_X
    space = "     "
    test_creer_matrice()
    print(space + "test_creer_matrice                           : OK")
    test_est_dans_grille()
    print(space + "test_est_dans_grille                         : OK")
    test_saisir_coordonnees()
    print(space + "test_saisir_coordonnees                      : OK")
    test_saisir_nombre()
    print(space + "test_saisir_nombre                           : OK")
    test_nombre_pions()
    print(space + "test_nombre_pions                            : OK")
    test_conversion_coordonees()
    print(space + "test_conversion_coordonees                   : OK")
    test_detection_orientation()
    print(space + "test_detection_orientation                   : OK")
    test_emplacement_libre_entre()
    print(space + "test_emplacement_libre_entre                 : OK")
    test_pion_est_ennemi()
    print(space + "test_pion_ennemi                             : OK")
    test_direction_valide()
    print(space + "test_direction_valide                        : OK")
    test_emplacement_libre_apres_position_depart()
    print(space + "test_emplacement_libre_apres_position_depart : OK")
    test_coordonees_pion_avant()
    print(space + "test_coordonees_pion_avant                   : OK")
    test_element_case()
    print(space + "test_element_case                            : OK")
    test_deplacement_elimination()
    print(space + "test_deplacement_elimination                 : OK")
    test_deplacement_retournement()
    print(space + "test_deplacement_retournement                : OK")
    test_coordonees_pions_joueur()
    print(space + "test_coordonees_pions_joueur                 : OK")
    test_coordonees_pion_apres()
    print(space + "test_coordonees_pion_apres                   : OK")


def clear(hauteur):  # Permets de "clear" la console en affichant du vide sur une hauteur donnée
    for i in range(hauteur):
        print()


def afficher_menu():  # affichage du menu sur la console
    print('''
    ┌───────────────────────────────────────────┐
      N°                 Menu
    └───────────────────────────────────────────┘
     [01]   Afficher grille début
     [02]   Afficher grille milieu
     [03]   Afficher grille fin
     [04]   Lancer une partie
     [05]   lancer les testes de fonctions
     [06]   Quitter
     
    ''')


def afficher_sous_menu_partie(assistant):  # affichage du sous menu tour d'un joueur sur la console
    print(f'''
    ┌─────────────────────────────────────────────┐
      N°           Lancer une partie
    └─────────────────────────────────────────────┘
                  assistant : {assistant}
     Permets d'afficher les déplacements possibles. 
     Utile pour vérifier les fonctions déplacement. 
     Paramètre dans sous_menu_tour_joueur().

     [01]   Contre l'ordinateur
     [02]   Contre un autre joueur
     [03]   Deux ordinateurs
     [04]   Retour menu

    ''')


def afficher_sous_menu_choix_matrice(qui_contre):
    print(f'''
    ┌─────────────────────────────────────────────┐
      N°           Lancer une partie
    └─────────────────────────────────────────────┘
        {qui_contre}
     [01]   Grille début partie
     [02]   Grille milieu partie
     [03]   grille fin partie
     [04]   Retour menu

    ''')


def sous_menu_choix_matrice(qui_contre, assistant):
    afficher_sous_menu_choix_matrice(qui_contre)
    selection = saisir_nombre(nb_minimum=1, nb_maximum=4)
    clear(80)
    if selection == 1:
        return fonction_matrice_debut_partie()
    elif selection == 2:
        return fonction_matrice_milieu_partie()
    elif selection == 3:
        return fonction_matrice_fin_partie()
    elif selection == 4:
        sous_menu_partie(assistant)


def sous_menu_partie(assistant):
    afficher_sous_menu_partie(assistant)
    selection = saisir_nombre(nb_minimum=1, nb_maximum=4)
    clear(80)
    if selection == 1:
        matrice = sous_menu_choix_matrice("    Joueur - Ordinateur", assistant)
        partie_joueur_ordi(matrice, assistant)
    elif selection == 2:
        matrice = sous_menu_choix_matrice("    Joueur - Joueur    ", assistant)
        partie_joueur_joueur(matrice, assistant)
    elif selection == 3:
        matrice = sous_menu_choix_matrice("Ordinateur - Ordinateur", assistant)
        partie_ordi_ordi(matrice, assistant)
    elif selection == 4:
        menu()


def menu():  # centralise et exécute les fonctions appropriées selon le numéro sélectionné
    assistant = True
    afficher_menu()
    numero_selectionne = saisir_nombre(nb_minimum=1, nb_maximum=6)
    clear(80)
    if 1 <= numero_selectionne <= 3:
        afficher_grille_predefini(numero_selectionne)
    elif numero_selectionne == 4:
        sous_menu_partie(assistant)
    elif numero_selectionne == 5:
        lancer_testes_fonctions()
    elif numero_selectionne == 6:
        quit()
    menu()


def start():  # Affichage au lancement du jeu
    clear(80)  # nettoie la console lors du lancement du jeu
    print('''
       __   ___  __              __   ___  __  
      |__) |__  |__)  |\/| |  | |  \ |__  /__` 
      |__) |___ |  \  |  | \__/ |__/ |___ .__/ 
    ''')
    menu()  # ouvre le menu du jeu


start()
