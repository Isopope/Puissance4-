""" ! @brief Ce module permet de gérer le comportement du bot (le joueur non-humain)

    @section import_section Import

    ce module utilise les modules suivants : 

    from jeu import *

    import global_variables
"""

import global_variables
from jeu import *
import copy

def evaluer_position(lPlateau, joueur):
    """
    Évalue la position actuelle du jeu pour le joueur donné.
    Plus la valeur est élevée, meilleure est la position pour le joueur.
    """
    score = 0
    adversaire=global_variables.iJoueur_humain
    if joueur==global_variables.iJoueur_humain:
        adversaire=global_variables.iJoueur_bot
    
    if lPlateau.count(joueur)==global_variables.iNombre_jetons_victoire:
        score+=100
    elif lPlateau.count(joueur)==global_variables.iNombre_jetons_victoire-1 and lPlateau.count(0)==1:
        score+=5
    elif lPlateau.count(joueur)==global_variables.iNombre_jetons_victoire-2 and lPlateau.count(0)==2:
        score+=2
    if lPlateau.count(adversaire)==global_variables.iNombre_jetons_victoire-1 and lPlateau.count(0)==1:
        score-=4


    """for i in range(global_variables.iLignes_plateau):
        for j in range(global_variables.iColonnes_plateau):
            if lPlateau[i][j] == joueur:
                # Évaluation basée sur la proximité des jetons du joueur
                score += evaluer_proximite(lPlateau, i, j, joueur)
"""
    return score

def evaluer_proximite(lPlateau, ligne, colonne, joueur):
    """
    Évalue la proximité des jetons du joueur à une position donnée sur le plateau.
    """
    score = 0
    #score au centre
    center_array=[int(i)for i in list(lPlateau[:,global_variables.iColonnes_plateau//2])]
    center_count=center_array.count(joueur)
    score+=center_count*3

    #score horizontal
    for r in range(global_variables.iLignes_plateau):
        row_array=[int(i) for i in list(lPlateau[r,:])]
        for c in range(global_variables.iColonnes_plateau-global_variables.iNombre_jetons_victoire+1):
            window=row_array[c:c+global_variables.iNombre_jetons_victoire]
            score+=evaluer_position(window,joueur)
    
    #score vertical
    for c in range(global_variables.iColonnes_plateau):
        col_array=[int(i) for i in  list(lPlateau[:,c])]
        for r in range(global_variables.iLignes_plateau-global_variables.iNombre_jetons_victoire+1):
            window=col_array[r:r+global_variables.iNombre_jetons_victoire]
            score+=evaluer_position(window,joueur)

    #score diagonale positive
    for r in range(global_variables.iColonnes_plateau-global_variables.iNombre_jetons_victoire+1):
        for c in range(global_variables.iColonnes_plateau-global_variables.iNombre_jetons_victoire+1):
            window=list(lPlateau[r:r+global_variables.iNombre_jetons_victoire,c:c+global_variables.iNombre_jetons_victoire].diagonal())
            score+=evaluer_position(window,joueur)
    
    #score diagonale negative
    for r in range(global_variables.iNombre_jetons_victoire-1,global_variables.iLignes_plateau):
        for c in range(global_variables.iColonnes_plateau-global_variables.iNombre_jetons_victoire+1):
            window=list(np.fliplr(lPlateau[r-global_variables.iNombre_jetons_victoire+1:r+1,c:c+global_variables.iNombre_jetons_victoire]).diagonal())
            score+=evaluer_position(window,joueur)
    return score

def minmax(lPlateau, profondeur, maximizing_player):
    """
    Algorithme Minimax pour déterminer le meilleur coup pour le bot.
    """
    gagnant=detection_gagnant(lPlateau,global_variables.iLignes_plateau,global_variables.iColonnes_plateau,global_variables.iNombre_jetons_victoire)
    if profondeur==0 or plateau_non_plein(lPlateau,global_variables.iColonnes_plateau) or gagnant:
        if gagnant==global_variables.iJoueur_bot:
            return 100000000
        elif gagnant==global_variables.iJoueur_humain:
            return -100000000
        else:
            return 0
    
    if maximizing_player:
        max_eval=float('-inf')
        for col in range(global_variables.iColonnes_plateau):
            if validite_coup(lPlateau,col):
                copie_plateau=lPlateau.copy()
                placer_jeton(copie_plateau,global_variables.iLignes_plateau,col,global_variables.iJoueur_bot)
                evaluation=minmax(copie_plateau,profondeur-1,False)
                max_eval=max(max_eval,evaluation)
        return max_eval
    else:
        min_eval=float('inf')
        for col in range(global_variables.iColonnes_plateau):
            if validite_coup(lPlateau,col):
                copie_plateau=lPlateau.copy()
                placer_jeton(copie_plateau,global_variables.iLignes_plateau,col,global_variables.iJoueur_humain)
                evaluation=minmax(copie_plateau,profondeur-1,True)
                min_eval=min(min_eval,evaluation)
        return min_eval
    

def meilleur_coup(lPlateau):
    """
    Retourne le meilleur coup à jouer pour le bot en utilisant l'algorithme Minimax.
    """
    meilleur_score = float('-inf')
    meilleur_colonne = -1

    for col in range(global_variables.iColonnes_plateau):
        if validite_coup(lPlateau, col):
            copie_plateau = lPlateau.copy()
            placer_jeton(copie_plateau, global_variables.iLignes_plateau, col, global_variables.iJoueur_bot)
            score = minmax(copie_plateau, global_variables.iDifficulte_bot, False)

            if score > meilleur_score:
                meilleur_score = score
                meilleur_colonne = col

    return meilleur_colonne

if __name__ == "__main__":
    # Exemple d'utilisation
    print("Bot joue le coup :", meilleur_coup(global_variables.lPlateau))
