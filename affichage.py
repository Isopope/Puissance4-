""" ! @brief Ce module permet de gérer l'affichage graphique de l'application, en utilisant tkinter

    @section import_section Import

    ce module utilise les modules suivants : 

    from jeu import *
    
    import tkinter as tk

    import global_variables

    import numpy as np

    from initalisation_widgets import *

"""

from initialisation_widgets import init_widgets_programme
from jeu import *
import tkinter as tk
import global_variables
import numpy as np
from initialisation_widgets import *


def afficher_plateau(lPlateau: np.ndarray) -> None:
    print(lPlateau)


def init_fenetre() -> tk.Tk:
    """ ! Permet la création de la fenêtre graphique du puissance 4
        @return l'objet représentant la fenêtre grapique.
    """

    #Initialisation de la fenetre graphique
    root = tk.Tk()
    root.geometry("1600x900")
    root.title("Puissance4 (ou plus)")

    return root

def placer_widget(widget: tk.Widget):
    """ ! Permet de placer un widget sur la fenêtre graphique
        @param widget est le widget à placer
    """
    #On affiche le widget
    widget.pack()

def enlever_widget(widget: tk.Widget) -> None:
    """ ! Permet d'enlever un widget de l'affichage graphique, jusqu'à ce qu'il soit réaffiché.
        @param widget est le widget à effacer
    """
    #On efface le wideget
    widget.pack_forget()

def effacer_elements_ecran(window: tk.Tk) -> None:
    """ ! Permet d'effacer tous les éléments présents sur la fenêtre graphique. Les widgets effacés pourront par la suite être réaffichés car ils ne sont pas supprimés.
        @param window est la fenêtre cible pour l'effacement complet de ses widget
    """

    for widget in window.winfo_children():
        enlever_widget(widget)

def afficher_menu_principal(window: tk.Tk, d_item_list: dict[dict[tk.Widget]]) -> None:
    """ ! Permet d'afficher le menu_principal sur la fenêtre graphique.
        @param window est la fenêtre sur laquelle on affiche le menu principal
        @param d_item_list est le dictionnaire de tous les objets ayant été initialisé dans le programme.
        \post tous les éléments qui étaient présents sur la page précédente ont été retiré, puis ceux du menu principal ont été affichés
    """

    #On renome la fenêtre pour correspondre à la page actuelle
    window.title("Puissance4 (ou plus) - Menu Principal")

    #On effectue le nettoyage de la fenêtre
    effacer_elements_ecran(window)

    #On affiche tous les éléments de la page du menu principal
    for widget_a_placer in d_item_list["menu_principal"].values():
        placer_widget(widget_a_placer)


def afficher_option_jeu(window: tk.Tk,d_item_list: dict[dict[tk.Widget]]) -> None:
    """ ! Permet d'afficher la page des options de jeu sur la fenêtre graphique.
        @param window est la fenêtre sur laquelle on affiche la page des options de jeu
        @param d_item_list est le dictionnaire de tous les objets ayant été initialisé dans le programme.
        \post tous les éléments qui étaient présents sur la page précédente ont été retiré, puis ceux de la page des options de jeu ont été affichés
    """

    #On renome la fenêtre pour correspondre à la page actuelle
    window.title("Puissance4 (ou plus) - Options de Jeu")

    effacer_elements_ecran(window)

    #On affiche tous les éléments de la page des options de jeu
    for widget_a_placer in d_item_list["options_jeu"].values():
        placer_widget(widget_a_placer)


def afficher_jeu(window: tk.Tk, d_item_list: dict[dict[tk.Widget]]) -> None:
    """ ! Permet d'afficher la page de jeu sur la fenêtre graphique.
        @param window est la fenêtre sur laquelle on affiche la page de jeu
        @param d_item_list est le dictionnaire de tous les objets ayant été initialisé dans le programme.
        \post tous les éléments qui étaient présents sur la page précédente ont été retiré, puis ceux de la page de jeu ont été affichés
    """

    #On renome la fenêtre pour correspondre à la page actuelle
    window.title("Puissance4 (ou plus) - Partie en Cours")

    effacer_elements_ecran(window)

    #On affiche tous les éléments de la page de jeu
    for widget_a_placer in d_item_list["jeu"].values():
        placer_widget(widget_a_placer)


if __name__ == "__main__":

    #On créé la fenêtre
    rootwindow = init_fenetre()
    
    #On récupère tous les widgets du programme
    d_widget_list = init_widgets_programme(rootwindow)

    #On affiche le menu principal
    afficher_menu_principal(rootwindow, d_widget_list)

    rootwindow.mainloop()