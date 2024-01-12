""" ! @brief Ce module gère le comportement du jeu de puissance 4

    @section import_section Import

    ce module utilise les modules suivants : 

    import global_variables
    
    import tkinter as tk

    import numpy as np
"""

import numpy as np
import tkinter as tk
import global_variables

## 
# @brief remet à zéro le plateau mis en paramètre, en fonction des ligne et colonnes renseignées en paramètres
#
def initialiser_plateau(lPlateau, iNombre_lignes, iNombre_colonnes) -> None:

    lPlateau = np.zeros((iNombre_lignes, iNombre_colonnes))
    return lPlateau
    


def selectionner_options_jeu() -> None:

    print("Combien de ligne au plateau (8 de base) ?")
    global_variables.iLignes_plateau = int(input(""))

    print("Combien de colonnes au plateau (8 de base) ?")
    global_variables.iColonnes_plateau = int(input(""))

    print("Combien de jeton à aligner pour gagner (8 de base) ?")
    global_variables.iNombre_jetons_victoire = int(input(""))

    global_variables.lPlateau = initialiser_plateau(global_variables.lPlateau, global_variables.iLignes_plateau, global_variables.iColonnes_plateau)

    return None


##
# fonction vérifiant la validité d'un coup, retourne True si c'est possible, False sinon
#
def validite_coup(lPlateau: np.ndarray, iColonne_coup: int) -> bool:

    # Si la position la plus haute de la colonne est libre, alors il possible de jouer au moins un coup dedans, donc la colonne est libre. Le coup est donc valide
    return lPlateau[0][iColonne_coup] == 0 # un valeur de 0 correspond à une case vide


def placer_jeton(lPlateau: np.ndarray, iNombre_lignes: int, iColonne_coup: int, iJoueur: int) -> bool:
    # Initialisation du booléen de retour
    OK = validite_coup(lPlateau, iColonne_coup)

    if OK:
        cpt = 1

        while cpt < iNombre_lignes and lPlateau[cpt][iColonne_coup] == 0:
            cpt += 1
        
        lPlateau[cpt-1][iColonne_coup] = iJoueur
    
    return OK

def plateau_non_plein(lPlateau: np.ndarray, iNombre_colonnes: int) -> bool:

    OK = False

    for i in range(iNombre_colonnes):
        OK = OK or validite_coup(lPlateau, i)

    return OK

def detection_gagnant(lPlateau: np.ndarray, iNombre_lignes: int, iNombre_colonnes: int, iNombre_jetons_victoire: int) -> int:

    OK = False

    #compteur colonne
    i = 0

    while (not(OK) and i < iNombre_colonnes):
        #compteur ligne
        j = 0
        while (not(OK) and j < iNombre_lignes):
            #Si on tombe sur une jeton, on commence à chercher une condition de victoire
            if lPlateau[j][i] != 0:
                jeton_joueur = lPlateau[j][i]
                cpt = 1
                #On parcours les lignes/colonnes/diagonales autour du jeton
				#On ne fait que vers la droite + en haut + diag bas droite et diag haut droite (car les autres directions seront vérifiées lorsque l’on testera les autres jetons)

				#colonne vers le bas
				#On vérifie que la condition gagnant n’a pas été trouvée, puis on teste si on a pas dépassé les limites du tableau, puis on vérifie si le jeton suivant l’alignement est au même joueur
                while (not(OK) and j+cpt < iNombre_lignes and lPlateau[j+cpt][i] == jeton_joueur):
                    #Si cpt = nb_jetons_victoire, c’est que le joueur a gagné
                    cpt += 1
                    OK = (cpt == iNombre_jetons_victoire)
                
                #On réinitialise le compteur pour le nouveau test
                cpt = 1

                #ligne vers la droite
				#On vérifie que la condition gagnant n’a pas été trouvée, puis on teste si on a pas dépassé les limites du tableau, puis on vérifie si le jeton suivant l’alignement est au même joueur
                while (not(OK) and i+cpt < iNombre_colonnes and lPlateau[j][i+cpt] == jeton_joueur):
                    #Si cpt = nb_jetons_victoire, c’est que le joueur a gagné
                    cpt += 1
                    OK = (cpt == iNombre_jetons_victoire)

                #On réinitialise le compteur pour le nouveau test
                cpt = 1
                
                #diagonale vers en bas à droite
				#On vérifie que la condition gagnant n’a pas été trouvée, puis on teste si on a pas dépassé les limites du tableau, puis on vérifie si le jeton suivant l’alignement est au même joueur
                while (not(OK) and j+cpt < iNombre_lignes and i+cpt < iNombre_colonnes and lPlateau[j+cpt][i+cpt] == jeton_joueur):
                    #Si cpt = nb_jetons_victoire, c’est que le joueur a gagné
                    cpt += 1
                    OK = (cpt == iNombre_jetons_victoire)
                
                #On réinitialise le compteur pour le nouveau test
                cpt = 1
                
                #ligne vers la droite
				#On vérifie que la condition gagnant n’a pas été trouvée, puis on teste si on a pas dépassé les limites du tableau, puis on vérifie si le jeton suivant l’alignement est au même joueur
                while (not(OK) and j-cpt > 0 and i+cpt < iNombre_colonnes and lPlateau[j-cpt][i+cpt] == jeton_joueur):
                    #Si cpt = nb_jetons_victoire, c’est que le joueur a gagné
                    cpt += 1
                    OK = (cpt == iNombre_jetons_victoire)
            #On incrémente j
            j += 1
        #On incrémente i
        i += 1

    #Si il y a eu un gagnant, on retourne le joueur ayant gagné, sinon on retourne 0
    if OK:
        return jeton_joueur
    else:
        return 0


def changer_hauteur(svValeur: tk.StringVar) -> None:
    """ ! Permet de mettre à jour la variable globale correspondant au nombre de lignes du plateau de jeu, en fonction de la valeur de l'entry associée dans le module affichage.py
        @param svValeur est la StringVar associée à l'Entry où l'utilisateur rentre le nombre de ligne qu'il souhaite avoir
        \post la valeur globale iLignes_plateau est égale à celle de svValeur. Si la valeur contenue dans svValeur n'est pas un entier, alors la valeur de iLignes_plateau est mise à 0
    """

    #Comme la variable donnée est récupérée sous forme d'une chaine de caractère, on vérifie si c'est un entier
    if svValeur.get().isdigit():
        #On convertit la valeur de la StringVar en entier et on la stocke dans la variable globale correspondant
        global_variables.iLignes_plateau = int(svValeur.get())
    else:
        #Si la valeur contenue dans l'entry n'est pas un entier, on considère que la valeur est 0
        global_variables.iLignes_plateau = 0


def changer_largeur(svValeur: tk.StringVar) -> None:
    """ ! Permet de mettre à jour la variable globale correspondant au nombre de colonnes du plateau de jeu, en fonction de la valeur de l'entry associée dans le module affichage.py
        @param svValeur est la StringVar associée à l'Entry où l'utilisateur rentre le nombre de colonnes qu'il souhaite avoir
        \post la valeur globale iColonnes_plateau est égale à celle de svValeur. Si la valeur contenue dans svValeur n'est pas un entier, alors la valeur de iColonnes_plateau est mise à 0
    """

    #Comme la variable donnée est récupérée sous forme d'une chaine de caractère, on vérifie si c'est un entier
    if svValeur.get().isdigit():
        #On convertit la valeur de la StringVar en entier et on la stocke dans la variable globale correspondant
        global_variables.iColonnes_plateau = int(svValeur.get())
    else:
        #Si la valeur contenue dans l'entry n'est pas un entier, on considère que la valeur est 0
        global_variables.iColonnes_plateau = 0


def changer_jetons(svValeur: tk.StringVar) -> None:
    """ ! Permet de mettre à jour la variable globale correspondant au nombre de jetons à aligner de jeu, en fonction de la valeur de l'entry associée dans le module affichage.py
        @param svValeur est la StringVar associée à l'Entry où l'utilisateur rentre le nombre jetons à aligner qu'il souhaite avoir
        \post la valeur globale iNombre_jetons_victoire est égale à celle de svValeur. Si la valeur contenue dans svValeur n'est pas un entier, alors la valeur de iNombre_jetons_victoire est mise à 0
    """

    #Comme la variable donnée est récupérée sous forme d'une chaine de caractère, on vérifie si c'est un entier
    if svValeur.get().isdigit():
        #On convertit la valeur de la StringVar en entier et on la stocke dans la variable globale correspondant
        global_variables.iNombre_jetons_victoire = int(svValeur.get())
    else:
        #Si la valeur contenue dans l'entry n'est pas un entier, on considère que la valeur est 0
        global_variables.iNombre_jetons_victoire = 0


def changer_couleur_joueur1(svValeur: tk.StringVar) -> None:
    """ ! Permet de mettre à jour la variable globale correspondant à la couleur du joueur1, en fonction de la valeur de l'entry associée dans le module affichage.py
        @param svValeur est la StringVar associée à l'Entry où l'utilisateur rentre la couleur du joueur1
    """

    #On convertit la valeur de la StringVar en chaine de caractères et on la stocke dans la variable globale correspondant
    global_variables.sCouleur_joueur1 = str(svValeur.get())


def changer_couleur_joueur2(svValeur: tk.StringVar) -> None:
    """ ! Permet de mettre à jour la variable globale correspondant à la couleur du joueur1, en fonction de la valeur de l'entry associée dans le module affichage.py
        @param svValeur est la StringVar associée à l'Entry où l'utilisateur rentre la couleur du joueur1
    """

    #On convertit la valeur de la StringVar en chaine de caractères et on la stocke dans la variable globale correspondant
    global_variables.sCouleur_joueur2 = str(svValeur.get())


def changer_joueur_commencant(svValeur: tk.StringVar) -> None:
    """ ! Permet de mettre à jour la variable globale correspondant au joueur commençant la partie, en fonction de la valeur de l'entry associée dans le module affichage.py
        @param svValeur est la StringVar associée à l'Entry où l'utilisateur choisi le joueur commençant la partie
    """

    #On convertit la valeur de la StringVar en chaine de caractères et on la stocke dans la variable globale correspondant
    global_variables.iJoueur_commencant = int(svValeur.get())

    print(global_variables.iJoueur_commencant)




if __name__ == "__main__":

    print(global_variables.lPlateau)
    for i in range(global_variables.iColonnes_plateau):
        for _ in range(global_variables.iLignes_plateau-1):
            placer_jeton(global_variables.lPlateau, global_variables.iLignes_plateau, i, 1)
    
    print(global_variables.lPlateau)

    print(plateau_non_plein(global_variables.lPlateau, global_variables.iColonnes_plateau))