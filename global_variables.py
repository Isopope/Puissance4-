""" ! @brief Ce module initialise toutes les variables globales pouvant être utilisées dans plusieurs modules 

    @section import_section Import

    ce module utilise les modules suivants : 

    import numpy as np
"""

import numpy as np

#Initialisation des variable globales du plateau/jeu
iLignes_plateau = 6
iColonnes_plateau = 7
iNombre_jetons_victoire = 5
iDifficulte_bot = 6
lPlateau = np.zeros((iLignes_plateau, iColonnes_plateau))
sCouleur_joueur1 = "Orange"
sCouleur_joueur2 = "Rouge"
iJoueur_commencant = 2
iJoueur_humain=1
iJoueur_bot=2