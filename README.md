## Règles du jeu Bermudes - UE S2 Projet

# 1 Objectif

```
Le but du jeu est de réduire le nombre de pions de l’adversaire à moins de 6.
```
# 2 Matériel

```
— Plateau de 9 × 9
— 54 pions réversibles
— Configuration de départ :
```

```
fig
```

# 3 Déplacements possibles

```
Les déplacements sont possibles dans les 8 directions.
```
## 3.1 Prise par élimination

```
C’est un déplacement pour prendre la place d’un pion adverse en l’éliminant du jeu (comme aux
échecs).
Un pion peut se déplacer et éliminer un pion adverse si :
— l’emplacement de destination est occupé par un pion de l’adversaire
— toutes les cases entre le départ et l’arrivée sont vides
— il y a au moins une case vide entre les deux pions (départ/arrivée)
Dans ce cas, le pion de l’adversaire est éliminé.
Ce schéma montre des déplacements d’élimination possibles (en vert), impossibles en rouge. Le
pion noir en G4 peut éliminer le pion blanc en I4, I6 ou encore le pion blanc en C8. Il ne peut pas
éliminer les pions G3, H3 ou G5 car ils sont voisins.
```

```
Figure1 – Déplacement avec élimination
```

## 3.2 Prise par retournement (saut)

```
C’est un déplacement pour faire "changer de camp" un pion de l’adversaire.
Un pion peut se déplacer et retourner un pion de l’adversaire si :
— l’emplacement est vide immédiatement derrière le pion adverse, on dit que le pion "saute"
l’adversaire.
— toutes les cases entre le départ et le pion adversaire sont vides (il peut n’y avoir aucune case).
Dans ce cas, le pion adverse est retourné (il prend la couleur du joueur courant).
Lorsque cela est possible, le joueur peut effectuer un enchaînement de plusieurs sauts (uniquement
des sauts) et ainsi retourner plusieurs pions.
Voici un exemple d’enchaînement et sa conséquence sur le plateau.
```

```
fig

F2 va en F4, H4 puis E7 Les pions sautés changent de camp F3, G4 et F
```

```
Il est impossible de commencer par une prise par élimination et d’enchaîner avec une prise par
retournement (saut).
```

# 4 Fin du jeu

```
Pour gagner il faut que votre adversaire ait moins de 6 pions.
Au moment ou vous réduisez le nombre des pions de votre adversaire à moins de 6 (par élimi-
nation ou retournement), votre adversaire est éliminé.
```

