""" ! @brief Ce module permet l'initialisation de tous les widgets utilisés dans \ref affichage.py

    @section import_section Import

    ce module utilise les modules suivants : 

    from jeu import *

    import tkinter as tk

    import global_variables

    import numpy as np

    from affichage import *
"""

from jeu import *
import tkinter as tk
import global_variables
import numpy as np
from affichage import *
from PIL import ImageTk, Image

def init_widgets_menu_principal(window: tk.Tk, d_widgets: dict[tk.Widget]) -> dict[tk.Widget]:
    """ ! Permet d'initialiser tous les widgets du menu principal.
        @param window est la fenêtre à laquelle les widgets seront rattachés
        @param d_widget est le dictionnaire des widgets auquel vont être ajoutés les nouveaux widgets initialisés par cette fonction
        @return le dictionnaire des widgets qui seront utilisés par le menu principal
    """
    #Initalisation du dictionnaire des widgets du menu principal
    d_widgets_menu_principal = {}

    #On initialise le Label affichant le titre du menu principal
    d_widgets_menu_principal["titre_menu_principal"] = tk.Label(window, text="Puissance 4 (ou plus)")

    #On initialise le bouton jouer
    #command=labmda: fonction(arg1, arg2) permet de passer une fonction avec des paramètres en tant que event pour le bouton
    d_widgets_menu_principal["bouton_jouer"] = tk.Button(window, text="JOUER", command=lambda: afficher_option_jeu(window, d_widgets))

    #On initialise le bouton de partie rapide
    d_widgets_menu_principal["partie_rapide"] = tk.Button(window, text="PARTIE RAPIDE", command=lambda: afficher_jeu(window, d_widgets))

    return d_widgets_menu_principal


def init_widgets_options_jeu(window: tk.Tk, d_widgets: dict[tk.Widget]) -> dict[tk.Widget]:
    """ ! Permet d'initialiser tous les widgets de la page des options de jeu.
        @param window est la fenêtre à laquelle les widgets seront rattachés
        @param d_widget est le dictionnaire des widgets auquel vont être ajoutés les nouveaux widgets initialisés par cette fonction
        @return le dictionnaire des widgets qui seront utilisés par la page des options de jeu.
    """

    #Initalisation du dictionnaire des widgets de la page des options de jeu
    d_widgets_options_jeu = {}

    #On initialise le Label affichant le titre du menu principal
    d_widgets_options_jeu["titre_options"] = tk.Label(window, text="Paramètres")

    #On initialise le bouton jouer
    #command=labmda: fonction(arg1, arg2) permet de passer une fonction avec des paramètres en tant que event pour le bouton
    d_widgets_options_jeu["bouton_lancer"] = tk.Button(window, text="LANCER", command=lambda: afficher_jeu(window, d_widgets))

    #On initialise l'image de maison du bouton de retour au menu principal
    image_retour_menu = Image.open("assets/house.png").resize((40, 40))
    d_widgets["images"]["image_retour_menu"] = ImageTk.PhotoImage(image_retour_menu)
    #On créé le bouton de retour vers le menu principal
    d_widgets_options_jeu["bouton_retour_menu"] = tk.Button(window, text="Menu Principal", image=d_widgets["images"]["image_retour_menu"], compound=tk.LEFT, command=lambda: afficher_menu_principal(window, d_widgets))

    #On créé le le frame contenant les options des dimensions du plateau de jeu
    d_widgets_options_jeu["frame_dimensions"] = tk.LabelFrame(window, text="Dimensions du plateau")

    #On y ajoute deux autres frames pour régler le nombre de lignes et de colonnes du plateau
    d_widgets_options_jeu["frame_dimensions_hauteur"] = tk.Frame(d_widgets_options_jeu["frame_dimensions"])
    d_widgets_options_jeu["frame_dimensions_largeur"] = tk.Frame(d_widgets_options_jeu["frame_dimensions"])

    #On ajoute à la frame hauteur le texte et l'entry pour choisir le nombre de lignes du plateau
    d_widgets_options_jeu["frame_dimensions_hauteur_label"] = tk.Label(d_widgets_options_jeu["frame_dimensions_hauteur"], text="Hauteur")
    d_widgets["variables"]["hauteur_entry"] = tk.StringVar( value=str(global_variables.iLignes_plateau) )
    d_widgets["variables"]["hauteur_entry"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["hauteur_entry"]: changer_hauteur(var)) #Permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_dimensions_hauteur_entry"] = tk.Entry( d_widgets_options_jeu["frame_dimensions_hauteur"],
                                                                       textvariable=d_widgets["variables"]["hauteur_entry"] )
    
    #On ajoute à la frame largeur le texte et l'entry pour choisir le nombre de colonnes du plateau
    d_widgets_options_jeu["frame_dimensions_largeur_label"] = tk.Label(d_widgets_options_jeu["frame_dimensions_largeur"], text="Largeur")
    d_widgets["variables"]["largeur_entry"] = tk.StringVar( value=str(global_variables.iColonnes_plateau) )
    d_widgets["variables"]["largeur_entry"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["largeur_entry"]: changer_largeur(var)) #Trace permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_dimensions_largeur_entry"] = tk.Entry( d_widgets_options_jeu["frame_dimensions_largeur"],
                                                                       textvariable=d_widgets["variables"]["largeur_entry"] )
    
    #On créé le frame Le frame du nombre de jeton à aligner et de la difficulté
    d_widgets_options_jeu["frame_aligner_difficulte"] = tk.Frame(window)
    
    #On créé les frames de choix du nombre de jeton à aligner pour gagner et celui du choix de la difficulté
    d_widgets_options_jeu["frame_aligner_difficulte_frame_aligner"] = tk.LabelFrame(d_widgets_options_jeu["frame_aligner_difficulte"], text="Nombre de jetons à aligner")
    d_widgets_options_jeu["frame_aligner_difficulte_frame_difficulte"] = tk.LabelFrame(d_widgets_options_jeu["frame_aligner_difficulte"], text="Difficulté")

    #On créé l'entry du nombre de jeton à aligner
    d_widgets["variables"]["jetons_entry"] = tk.StringVar( value=str(global_variables.iNombre_jetons_victoire) )
    d_widgets["variables"]["jetons_entry"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["jetons_entry"]: changer_jetons(var)) #Permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_aligner_difficulte_frame_aligner_entry_jetons"] = tk.Entry(d_widgets_options_jeu["frame_aligner_difficulte_frame_aligner"],
                                                                                            textvariable=d_widgets["variables"]["jetons_entry"] )
    
    #On créé l'entry de la difficulté
    d_widgets["variables"]["difficulte_entry"] = tk.StringVar( value=str(global_variables.iDifficulte_bot) )
    d_widgets["variables"]["difficulte_entry"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["difficulte_entry"]: changer_jetons(var)) #Permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_aligner_difficulte_frame_difficulte_entry_difficulte"] = tk.Entry(d_widgets_options_jeu["frame_aligner_difficulte_frame_difficulte"],
                                                                                            textvariable=d_widgets["variables"]["difficulte_entry"] )
    

    #On créé le frame contenant les options de couleurs des jetons des joueurs
    d_widgets_options_jeu["frame_couleurs"] = tk.LabelFrame(window, text="Couleur des jetons")

    #On y ajoute deux autres frames pour gérer chaque joueur
    d_widgets_options_jeu["frame_couleurs_joueur1"] = tk.Frame(d_widgets_options_jeu["frame_couleurs"]) #Joueur humain
    d_widgets_options_jeu["frame_couleurs_joueur2"] = tk.Frame(d_widgets_options_jeu["frame_couleurs"]) #Bot

    #On stocke les options de couleurs possibles pour les deux joueurs
    d_widgets["variables"]["option_couleurs"] = ["Rouge", "Orange", "Bleu", "Vert", "Violet", "Marron"]

    #On ajoute au frame de la couleur du joueur1 le texte et l'optionMenu
    d_widgets_options_jeu["frame_couleurs_joueur1_label"] = tk.Label(d_widgets_options_jeu["frame_couleurs_joueur1"], text="Joueur humain")
    d_widgets["variables"]["couleur_joueur1_option"] = tk.StringVar( value=str(global_variables.sCouleur_joueur1) )
    d_widgets["variables"]["couleur_joueur1_option"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["couleur_joueur1_option"]: changer_couleur_joueur1(var)) #Permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_couleurs_joueur1_optionmenu"] = tk.OptionMenu(d_widgets_options_jeu["frame_couleurs_joueur1"],
                                                                               d_widgets["variables"]["couleur_joueur1_option"],
                                                                               *d_widgets["variables"]["option_couleurs"] )

    #On ajoute au frame de la couleur du joueur2 le texte et l'optionMenu
    d_widgets_options_jeu["frame_couleurs_joueur2_label"] = tk.Label(d_widgets_options_jeu["frame_couleurs_joueur2"], text="Bot")
    d_widgets["variables"]["couleur_joueur2_option"] = tk.StringVar( value=str(global_variables.sCouleur_joueur2) )
    d_widgets["variables"]["couleur_joueur2_option"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["couleur_joueur2_option"]: changer_couleur_joueur2(var)) #Trace permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_couleurs_joueur2_optionmenu"] = tk.OptionMenu(d_widgets_options_jeu["frame_couleurs_joueur2"],
                                                                               d_widgets["variables"]["couleur_joueur2_option"],
                                                                               *d_widgets["variables"]["option_couleurs"] )

    #On créé le frame contenant les options de choix du joueur débutant la partie
    d_widgets_options_jeu["frame_joueur_commencant"] = tk.LabelFrame(window, text="Couleur des jetons")
    d_widgets["variables"]["joueur_commencant_radio"] = tk.StringVar( value=str(global_variables.sCouleur_joueur2) )
    d_widgets["variables"]["joueur_commencant_radio"].trace("w", lambda name, index,mode, var=d_widgets["variables"]["joueur_commencant_radio"]: changer_joueur_commencant(var)) #Trace permet d'appeler une fonction lorsque la valeur de la StringVar est modifiée
    d_widgets_options_jeu["frame_joueur_commencant_radio_1"] = tk.Radiobutton(window, text="Joueur humain", value=1, variable=d_widgets["variables"]["joueur_commencant_radio"])
    d_widgets_options_jeu["frame_joueur_commencant_radio_2"] = tk.Radiobutton(window, text="Bot", value=2, variable=d_widgets["variables"]["joueur_commencant_radio"])
    d_widgets_options_jeu["frame_joueur_commencant_radio_3"] = tk.Radiobutton(window, text="Aléatoire", value=-1, variable=d_widgets["variables"]["joueur_commencant_radio"])
    



    # A CONTINUER
    #
    #


    return d_widgets_options_jeu


def init_widgets_jeu(window: tk.Tk, d_widgets: dict[tk.Widget]) -> dict[tk.Widget]:
    """ ! Permet d'initialiser tous les widgets de la page de jeu.
        @param window est la fenêtre à laquelle les widgets seront rattachés
        @param d_widget est le dictionnaire des widgets auquel vont être ajoutés les nouveaux widgets initialisés par cette fonction
        @return le dictionnaire des widgets qui seront utilisés par la page de jeu
    """

    #Initalisation du dictionnaire des widgets de la page de jeu
    d_widgets_jeu = {}

    return d_widgets_jeu


def init_widgets_programme(window: tk.Tk) -> dict[dict[tk.Widget]]:
    """ ! Permet d'initialiser tous les widgets du programme.
        @param window est la fenêtre à laquelle les widgets seront rattachés
        @return un dictionnaire contenant les dictionnaires des widgets des différentes pages. les clés de ce dictionnaires sont les pages du programme,
    sont des dictionnaires contenant les widgets de la page concernée
    """

    #Initialisation du dictionnaire
    d_widgets_pages = {}

    #On initialise le sous-dictionnaire servant à stocker les images
    d_widgets_pages["images"] = {}

    #On initialise le sous-dictionnaire servant à stocker les valeurs des variables des widgets
    d_widgets_pages["variables"] = {}

    #On insère ensuite dans ce dictionnaire les différents widgets des différentes pages
    #Ce dictionnaire a pour clés les différentes pages du programme, et comme valeurs le dictionnaire contenant leurs widgets associés.
    #Cette structure permet par la suite de parcourir les différents widgets à placer avec une boucle for, dans les fonctions d'affichage des pages (dans le module affichage.py)
    d_widgets_pages["menu_principal"] = init_widgets_menu_principal(window, d_widgets_pages)
    d_widgets_pages["options_jeu"] = init_widgets_options_jeu(window, d_widgets_pages)
    d_widgets_pages["jeu"] = init_widgets_jeu(window, d_widgets_pages)

    return d_widgets_pages