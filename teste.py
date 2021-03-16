# import Bermudes
# from Bermudes import *
from random import randrange

coordonnees_des_cases = {
    (0, 0): "A1", (0, 1): "A2", (0, 2): "A3", (0, 3): "A4", (0, 4): "A5", (0, 5): "A6", (0, 6): "A7", (0, 7): "A8",
    (0, 8): "A9", (0, 9): "A10", (1, 0): "B1", (1, 1): "B2", (1, 2): "B3", (1, 3): "B4", (1, 4): "B5", (1, 5): "B6",
    (1, 6): "B7", (1, 7): "B8", (1, 8): "B9", (1, 9): "B10", (2, 0): "C1", (2, 1): "C2", (2, 2): "C3", (2, 3): "C4",
    (2, 4): "C5", (2, 5): "C6", (2, 6): "C7", (2, 7): "C8", (2, 8): "C9", (2, 9): "C10", (3, 0): "D1", (3, 1): "D2",
    (3, 2): "D3", (3, 3): "D4", (3, 4): "D5", (3, 5): "D6", (3, 6): "D7", (3, 7): "D8", (3, 8): "D9", (3, 9): "D10",
    (4, 0): "E1", (4, 1): "E2", (4, 2): "E3", (4, 3): "E4", (4, 4): "E5", (4, 5): "E6", (4, 6): "E7", (4, 7): "E8",
    (4, 8): "E9", (4, 9): "E10", (5, 0): "F1", (5, 1): "F2", (5, 2): "F3", (5, 3): "F4", (5, 4): "F5", (5, 5): "F6",
    (5, 6): "F7", (5, 7): "F8", (5, 8): "F9", (5, 9): "F10", (6, 0): "G1", (6, 1): "G2", (6, 2): "G3", (6, 3): "G4",
    (6, 4): "G5", (6, 5): "G6", (6, 6): "G7", (6, 7): "G8", (6, 8): "G9", (6, 9): "G10", (7, 0): "H1", (7, 1): "H2",
    (7, 2): "H3", (7, 3): "H4", (7, 4): "H5", (7, 5): "H6", (7, 6): "H7", (7, 7): "H8", (7, 8): "H9", (7, 9): "H10",
    (8, 0): "I1", (8, 1): "I2", (8, 2): "I3", (8, 3): "I4", (8, 4): "I5", (8, 5): "I6", (8, 6): "I7", (8, 7): "I8",
    (8, 8): "I9", (8, 9): "I10", (9, 0): "J1", (9, 1): "J2", (9, 2): "J3", (9, 3): "J4", (9, 4): "J5", (9, 5): "J6",
    (9, 6): "J7", (9, 7): "J8", (9, 8): "J9", (9, 9): "J10"}

# print(Bermudes.emplacement_libre_entre(Bermudes.conversion_coordonees("H",1),Bermudes.conversion_coordonees("H",3), Bermudes.Matrice_milieu_partie))

# def Tour_joueur(grille):
#     pion_depart = saisir_coordonees(grille, " du pion de départ")
#     position_destination = saisir_coordonees(grille, " de la case de destination")
#     if direction_valide(pion_depart, position_destination):
#         if grille[position_destination[0]][position_destination[1]] == " ":
#             pion_avant_destination = coordonees_pion_avant(pion_depart, position_destination)
#             if emplacement_libre_entre(pion_depart, pion_avant_destination, grille):
#                 if pion_ennemi(pion_depart, pion_avant_destination, grille):
#                     deplacement_retournement(pion_depart, position_destination, pion_avant_destination, grille)
#                 else:
#                     print("le pion devant etre retourné n'est pas un ennemi")
#             else:
#                 print("Il ne doit avoir aucun pion entre les deux séléctionné.")
#         elif pion_ennemi(pion_depart, position_destination, grille):
#             if emplacement_libre_entre(pion_depart, position_destination, grille):
#                 deplacement_elimination(pion_depart, position_destination, grille)
#             else:
#                 print("Il ne doit avoir aucun pion entre les deux séléctionné.")
#         else:
#             print("le pion attaqué n'est pas un ennemi")
#     else:
#         print("les pions séléctionnées ne sont pas jouables (direction incorrect)")
#     nb_pions_noir, nb_pion_blanc = nombre_pions(grille)
#     afficher_table(grille, Alphabet, tour_du_joueur=grille[pion_depart[0]][pion_depart[1]], nb_pions_noir=nb_pions_noir,
#                    nb_pion_blanc=nb_pion_blanc)
#
#
# def deplacement_elimination(position_depart, destination, grille):
#     grille[destination[0]][destination[1]] = grille[position_depart[0]][position_depart[1]]
#     grille[position_depart[0]][position_depart[1]] = " "
#
#
# def deplacement_retournement(position_depart, destination, pion_avant_destination, grille):
#     grille[destination[0]][destination[1]] = grille[position_depart[0]][position_depart[1]]
#     grille[pion_avant_destination[0]][pion_avant_destination[1]] = grille[position_depart[0]][position_depart[1]]
#     grille[position_depart[0]][position_depart[1]] = " "

# def coor_pion_joueur(grille):
#     coor_pions_noir, coor_pions_blanc = [], []
#     for ligne in range(len(grille)):
#         for elements in range(len(grille)):
#             if grille[ligne][elements] == "●":
#                 coor_pions_blanc.append((ligne, elements))
#             elif grille[ligne][elements] == "O":
#                 coor_pions_noir.append((ligne, elements))
#     return coor_pions_noir, coor_pions_blanc


while True:
    print(randrange(0, 2))
# print("Il est impossible de commencer par une prise par élimination et d’enchaîner avec une prise par retournement")

# elif deplacement_retournement(pion_depart, position_destination, grille):
# nb_pions_noir, nb_pion_blanc = nombre_pions(grille)
# afficher_table(grille, Alphabet, tour_du_joueur=grille[position_destination[0]][position_destination[1]],
#                nb_pions_noir=nb_pions_noir, nb_pion_blanc=nb_pion_blanc)
# print("vous avez fait un deplacement parcretournement. Vous pouvez continuer ce déplacement."
#       "Ecrivez nimporte quelle coor non valide pour arreter")
#
# pion_depart = position_destination
# position_destination = saisir_coordonees(grille, " de la case de destination")
# while deplacement_retournement(pion_depart, position_destination, grille) :
#     nb_pions_noir, nb_pion_blanc = nombre_pions(grille)
#     afficher_table(grille, Alphabet,
#                    tour_du_joueur=grille[position_destination[0]][position_destination[1]],
#                    nb_pions_noir=nb_pions_noir, nb_pion_blanc=nb_pion_blanc)
#     pion_depart = position_destination
#     position_destination = saisir_coordonees(grille, " de la case de destination")

# def tour_joueur_dp(prise_elimination_avant, position_destination, pion_joueur, assistant, grille, deplacement_robot, robot=False):
#     # sous fonction de tour_joueur(). Enchainement déplacement par retournement
#     if not prise_elimination_avant:  # sera utile pour atelier 4, explication dans print() à la fin de la fonction.
#         tour_valide = True
#         print("Vous avez fait un déplacement par retournement.")
#         afficher_table(grille, Alphabet, pion_joueur)
#
#         pion_depart = position_destination
#         liste_deplacement_possible = assistant_deplacement_retournement(pion_joueur, grille, pion_depart)
#         if assistant:
#             affichage_assistant_deplacement(liste_deplacement_possible, "retournement")
#
#         if len(liste_deplacement_possible) > 0:
#             if not robot:
#                 print("Vous pouvez continuer ce type de déplacement. Écrivez des coordonnées non valide pour arrêter.")
#                 position_destination = saisir_coordonees(grille, "de la case de destination")
#             else:
#                 deplacement_choisi = random.choice(liste_deplacement_possible)
#                 position_destination = deplacement_choisi[1]
#             while deplacement_retournement(pion_depart, position_destination, grille) and len(liste_deplacement_possible)>0:
#                 # Tant que le déplacement réalisé est valide et que d'autres sont réalisables
#                 afficher_table(grille, Alphabet, pion_joueur)
#                 pion_depart = position_destination
#
#                 liste_deplacement_possible = assistant_deplacement_retournement(pion_joueur, grille, pion_depart)
#                 if assistant:
#                     affichage_assistant_deplacement(liste_deplacement_possible, "retournement")
#
#                 if len(liste_deplacement_possible) > 0 and not robot:
#                     position_destination = saisir_coordonees(grille, "de la case de destination")
#                 elif len(liste_deplacement_possible) > 0 and robot:
#                     deplacement_choisi = random.choice(liste_deplacement_possible)
#                     position_destination = deplacement_choisi[1]
#                 else:
#                     print("Aucun déplacement possible.")
#         else:
#             print("Aucun déplacement possible.")
#         return tour_valide
#     print("Il est impossible de commencer par une prise par élimination et d’enchaîner avec une prise par retournement")



# def tour_joueur_dp_joueur(position_destination, pion_joueur, assistant, grille):
#     # sous fonction de tour_joueur(). Enchainement déplacement par retournement
#     tour_valide = True
#     print("Vous avez fait un déplacement par retournement.")
#     afficher_table(grille, Alphabet, pion_joueur)
#
#     pion_depart = position_destination
#     liste_dep_retournement = assistant_deplacement_retournement(pion_joueur, grille, pion_depart)
#     if assistant:
#         liste_deplacement_possible = affichage_assistant_deplacement(liste_dep_retournement, "retournement")
#
#     if len(liste_deplacement_possible) > 0:
#         print("Vous pouvez continuer ce type de déplacement. Écrivez des coordonnées non valide pour arrêter.")
#         position_destination = saisir_coordonees(grille, "de la case de destination")
#
#         while deplacement_retournement(pion_depart, position_destination, grille) and len(liste_deplacement_possible)>0:
#             # Tant que le déplacement réalisé est valide et que d'autres sont réalisables
#             afficher_table(grille, Alphabet, pion_joueur)
#             pion_depart = position_destination
#
#             liste_dep_retournement = assistant_deplacement_retournement(pion_joueur, grille, pion_depart)
#             if assistant:
#                 liste_deplacement_possible = affichage_assistant_deplacement(liste_dep_retournement, "retournement")
#
#             if len(liste_deplacement_possible) > 0:
#                 position_destination = saisir_coordonees(grille, "de la case de destination")
#             else:
#                 print("Aucun déplacement possible.")
#     else:
#         print("Aucun déplacement possible.")
#     return tour_valide