import global_variables
from jeu import *

def evaluer_position(lPlateau, joueur):
    """
    Évalue la position actuelle du jeu pour le joueur donné.
    Plus la valeur est élevée, meilleure est la position pour le joueur.
    """
    score = 0

    for i in range(global_variables.iLignes_plateau):
        for j in range(global_variables.iColonnes_plateau):
            if lPlateau[i][j] == joueur:
                # Évaluation basée sur la proximité des jetons du joueur
                score += evaluer_proximite(lPlateau, i, j, joueur)

    return score

def evaluer_proximite(lPlateau, ligne, colonne, joueur):
    """
    Évalue la proximité des jetons du joueur à une position donnée sur le plateau.
    """
    score = 0

    # Définir les directions à vérifier (horizontale, verticale, diagonale)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for direction in directions:
        count = 0  # Compte le nombre de jetons consécutifs dans la direction actuelle
        for step in range(-3, 4):  # Vérifie les 7 positions possibles dans la direction
            new_ligne = ligne + step * direction[0]
            new_colonne = colonne + step * direction[1]

            if 0 <= new_ligne < global_variables.iLignes_plateau and 0 <= new_colonne < global_variables.iColonnes_plateau:
                if lPlateau[new_ligne][new_colonne] == joueur:
                    count += 1
                    score += count  # Ajoute au score en fonction du nombre consécutif de jetons
                else:
                    count = 0  # Réinitialise le compteur si le jeton suivant n'appartient pas au joueur

    return score

def minmax(lPlateau, profondeur, maximizing_player):
    """
    Algorithme Minimax pour déterminer le meilleur coup pour le bot.
    """
    if profondeur == 0 or plateau_non_plein(lPlateau, global_variables.iColonnes_plateau):
        return evaluer_position(lPlateau, global_variables.iJoueur_bot)

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(global_variables.iColonnes_plateau):
            if validite_coup(lPlateau, col):
                copie_plateau = lPlateau.copy()
                placer_jeton(copie_plateau, global_variables.iLignes_plateau, col, global_variables.iJoueur_bot)
                evaluation = minmax(copie_plateau, profondeur - 1, False)
                max_eval = max(max_eval, evaluation)
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(global_variables.iColonnes_plateau):
            if validite_coup(lPlateau, col):
                copie_plateau = lPlateau.copy()
                placer_jeton(copie_plateau, global_variables.iLignes_plateau, col, global_variables.iJoueur_humain)
                evaluation = minmax(copie_plateau, profondeur - 1, True)
                min_eval = min(min_eval, evaluation)
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
            score = minmax(copie_plateau, global_variables.iDifficulte_bot, True)

            if score > meilleur_score:
                meilleur_score = score
                meilleur_colonne = col

    return meilleur_colonne

if __name__ == "__main__":
    # Exemple d'utilisation
    print("Bot joue le coup :", meilleur_coup(global_variables.lPlateau))
