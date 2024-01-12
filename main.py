from global_variables import *
from jeu import *
from bot import *
from affichage import *


def main():
    bRun=True
    afficher_plateau(global_variables.lPlateau)

    while (bRun):
        if global_variables.iJoueur_commencant==global_variables.iJoueur_humain:
            iChoix_colonne = int(input("choisir un colonne joueur humain: "))
            placer_jeton(global_variables.lPlateau, global_variables.iLignes_plateau, iChoix_colonne, global_variables.iJoueur_humain)
            OK=detection_gagnant(global_variables.lPlateau,global_variables.iLignes_plateau, global_variables.iColonnes_plateau, global_variables.iNombre_jetons_victoire)
            afficher_plateau(global_variables.lPlateau)
            if OK:
                    print("Le joueur humain a gagné !")
                    bRun=False
            global_variables.iJoueur_commencant=3-global_variables.iJoueur_humain
        elif global_variables.iJoueur_commencant==global_variables.iJoueur_bot:
            iChoix_colonne=meilleur_coup(global_variables.lPlateau)
            placer_jeton(global_variables.lPlateau, global_variables.iLignes_plateau, iChoix_colonne, global_variables.iJoueur_bot)
            OK=detection_gagnant(global_variables.lPlateau,global_variables.iLignes_plateau, global_variables.iColonnes_plateau, global_variables.iNombre_jetons_victoire)
            afficher_plateau(global_variables.lPlateau)
            if OK:
                    print("Le joueur bot a gagné !")
                    bRun=False
            global_variables.iJoueur_commencant=3-global_variables.iJoueur_bot



        

if __name__ == "__main__":
    main()
