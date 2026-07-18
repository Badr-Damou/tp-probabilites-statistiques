# -*- coding: utf-8 -*-
"""Probleme 4 - Estimation et intervalle de confiance."""

import math
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib_cache"))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


FIGURES_DIR = BASE_DIR / "figures"


def calculer_statistiques():
    """Calcule les estimateurs et l'intervalle de confiance."""
    centres = np.array([4, 5, 6, 7, 8, 9, 10], dtype=float)
    effectifs = np.array([1, 2, 23, 46, 24, 3, 1], dtype=int)
    bords_classes = np.array([3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5], dtype=float)

    # Reconstruction de l'echantillon groupe avec les centres de classes.
    echantillon = np.repeat(centres, effectifs)
    n = len(echantillon)

    moyenne_empirique = np.mean(echantillon)
    variance_empirique = np.var(echantillon, ddof=0)
    variance_corrigee = np.var(echantillon, ddof=1)
    ecart_type_empirique = np.std(echantillon, ddof=0)
    ecart_type_corrige = np.std(echantillon, ddof=1)

    alpha = 0.05
    ddl = n - 1
    t_critique = stats.t.ppf(1 - alpha / 2, ddl)
    marge = t_critique * ecart_type_corrige / np.sqrt(n)
    borne_inferieure = moyenne_empirique - marge
    borne_superieure = moyenne_empirique + marge
    amplitude = borne_superieure - borne_inferieure

    # Taille minimale avec approximation normale et s comme estimation de sigma.
    z_critique = stats.norm.ppf(1 - alpha / 2)
    n_minimum = math.ceil((2 * z_critique * ecart_type_corrige / 0.1) ** 2)

    return {
        "centres": centres,
        "effectifs": effectifs,
        "bords_classes": bords_classes,
        "echantillon": echantillon,
        "n": n,
        "moyenne empirique": moyenne_empirique,
        "variance empirique": variance_empirique,
        "variance corrigee": variance_corrigee,
        "ecart-type empirique": ecart_type_empirique,
        "ecart-type corrige": ecart_type_corrige,
        "t critique": t_critique,
        "IC 95 inferieur": borne_inferieure,
        "IC 95 superieur": borne_superieure,
        "amplitude": amplitude,
        "z critique": z_critique,
        "n minimum": n_minimum,
    }


def tracer_histogramme(resultats):
    """Trace l'histogramme des longueurs d'abeilles."""
    FIGURES_DIR.mkdir(exist_ok=True)
    chemin = FIGURES_DIR / "probleme4_histogramme_abeilles.png"

    plt.figure(figsize=(9, 5))
    plt.hist(
        resultats["echantillon"],
        bins=resultats["bords_classes"],
        color="#f4a261",
        edgecolor="black",
        alpha=0.85,
        label="Effectifs par classe",
    )
    plt.axvline(
        resultats["moyenne empirique"],
        color="#1d3557",
        linestyle="--",
        linewidth=2,
        label=f"Moyenne = {resultats['moyenne empirique']:.2f} mm",
    )
    plt.title("Histogramme des longueurs d'abeilles")
    plt.xlabel("Longueur (mm)")
    plt.ylabel("Effectif")
    plt.xticks(resultats["bords_classes"])
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(chemin, dpi=150)
    plt.close()
    return chemin


def executer():
    """Affiche les resultats du probleme 4 et genere la figure."""
    resultats = calculer_statistiques()
    chemin = tracer_histogramme(resultats)

    print("Donnees groupees : 100 abeilles, classes de largeur 1 mm.")
    print(f"n                                  = {resultats['n']}")
    print(f"Moyenne empirique m_e              = {resultats['moyenne empirique']:.6f} mm")
    print(f"Variance empirique V_e (ddof=0)    = {resultats['variance empirique']:.6f}")
    print(f"Ecart-type empirique               = {resultats['ecart-type empirique']:.6f} mm")
    print(f"Variance corrigee (ddof=1)         = {resultats['variance corrigee']:.6f}")
    print(f"Ecart-type corrige s               = {resultats['ecart-type corrige']:.6f} mm")
    print(f"t_(0.975, 99)                      = {resultats['t critique']:.6f}")
    print(
        "Intervalle de confiance a 95 %     = "
        f"[{resultats['IC 95 inferieur']:.6f}, {resultats['IC 95 superieur']:.6f}] mm"
    )
    print(f"Amplitude de l'intervalle          = {resultats['amplitude']:.6f} mm")
    print(f"z_(0.975)                          = {resultats['z critique']:.6f}")
    print(f"Taille minimale pour amplitude < 0.1 mm = {resultats['n minimum']}")
    print(f"Figure sauvegardee                 = {chemin}")

    print("\nInterpretation :")
    print("- La tendance centrale est proche de 7.03 mm.")
    print("- La dispersion est moderee autour de cette valeur.")
    print("- L'intervalle de confiance donne une plage plausible pour la moyenne de la population.")
    print("- Augmenter la taille d'echantillon reduit l'amplitude de l'intervalle.")

    return resultats


if __name__ == "__main__":
    print("=" * 30)
    print("PROBLEME 4")
    print("=" * 30)
    executer()
