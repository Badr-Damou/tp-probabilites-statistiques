# -*- coding: utf-8 -*-
"""Execution de tous les problemes de l'evaluation."""

import probleme1
import probleme2
import probleme3
import probleme4


def afficher_titre(titre):
    """Affiche un titre uniforme pour chaque probleme."""
    print("\n" + "=" * 30)
    print(titre)
    print("=" * 30)


def main():
    """Execute les quatre problemes dans l'ordre."""
    afficher_titre("PROBLEME 1")
    probleme1.executer()

    afficher_titre("PROBLEME 2")
    probleme2.executer()

    afficher_titre("PROBLEME 3")
    probleme3.executer()

    afficher_titre("PROBLEME 4")
    probleme4.executer()


if __name__ == "__main__":
    main()
