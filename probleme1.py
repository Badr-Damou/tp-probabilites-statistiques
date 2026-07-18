# -*- coding: utf-8 -*-
"""Probleme 1 - Detection de courriels frauduleux."""


def calculer_probabilites():
    """Calcule les probabilites demandees avec les formules du cours."""
    # Donnees du probleme
    p_f = 0.25
    p_non_f = 1 - p_f
    p_d_sachant_f = 0.92
    p_d_sachant_non_f = 0.06

    # Probabilites complementaires
    p_non_d_sachant_f = 1 - p_d_sachant_f
    p_non_d_sachant_non_f = 1 - p_d_sachant_non_f

    # Formule des probabilites totales :
    # P(D) = P(D|F)P(F) + P(D|non F)P(non F)
    p_d = p_d_sachant_f * p_f + p_d_sachant_non_f * p_non_f
    p_non_d = 1 - p_d

    # Theoreme de Bayes :
    # P(F|D) = P(D|F)P(F) / P(D)
    p_f_sachant_d = (p_d_sachant_f * p_f) / p_d

    # Bayes avec l'evenement complementaire :
    # P(F|non D) = P(non D|F)P(F) / P(non D)
    p_f_sachant_non_d = (p_non_d_sachant_f * p_f) / p_non_d

    return {
        "P(F)": p_f,
        "P(non F)": p_non_f,
        "P(D|F)": p_d_sachant_f,
        "P(D|non F)": p_d_sachant_non_f,
        "P(non D|F)": p_non_d_sachant_f,
        "P(non D|non F)": p_non_d_sachant_non_f,
        "P(D)": p_d,
        "P(non D)": p_non_d,
        "P(F|D)": p_f_sachant_d,
        "P(F|non D)": p_f_sachant_non_d,
    }


def afficher_probabilite(nom, valeur):
    """Affiche une probabilite sous forme decimale et en pourcentage."""
    print(f"{nom:<18} = {valeur:.6f}  ({100 * valeur:.2f} %)")


def executer():
    """Affiche les resultats du probleme 1."""
    resultats = calculer_probabilites()

    print("Traduction des donnees en notation probabiliste :")
    for cle in [
        "P(F)",
        "P(non F)",
        "P(D|F)",
        "P(D|non F)",
        "P(non D|F)",
        "P(non D|non F)",
    ]:
        afficher_probabilite(cle, resultats[cle])

    print("\nCalculs principaux :")
    afficher_probabilite("P(D)", resultats["P(D)"])
    afficher_probabilite("P(non D)", resultats["P(non D)"])
    afficher_probabilite("P(F|D)", resultats["P(F|D)"])
    afficher_probabilite("P(F|non D)", resultats["P(F|non D)"])

    print("\nInterpretation :")
    print("- Le systeme detecte 92 % des courriels frauduleux.")
    print("- Une alerte frauduleuse est fausse dans une partie des cas, car P(D|non F)=6 %.")
    print("- Lorsqu'une alerte est declenchee, la precision vaut P(F|D).")
    print("- Si aucune alerte n'est declenchee, le risque residuel de fraude vaut P(F|non D).")

    return resultats


if __name__ == "__main__":
    print("=" * 30)
    print("PROBLEME 1")
    print("=" * 30)
    executer()
