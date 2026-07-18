# -*- coding: utf-8 -*-
"""Probleme 3 - Regression lineaire."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib_cache"))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


FIGURES_DIR = BASE_DIR / "figures"


def donnees_population():
    """Retourne les donnees observees."""
    x = np.array(
        [
            1950,
            1955,
            1960,
            1965,
            1970,
            1975,
            1980,
            1985,
            1990,
            1995,
            2000,
            2005,
            2010,
            2015,
            2020,
        ],
        dtype=float,
    )
    y = np.array(
        [2.54, 2.77, 3.03, 3.34, 3.70, 4.08, 4.46, 4.87, 5.33, 5.74, 6.14, 6.54, 6.96, 7.38, 7.80],
        dtype=float,
    )
    return x, y


def calculer_regression():
    """Calcule la correlation, la droite de regression et la prediction."""
    x, y = donnees_population()

    x_bar = np.mean(x)
    y_bar = np.mean(y)
    correlation = np.corrcoef(x, y)[0, 1]

    # np.polyfit renvoie la pente a et l'ordonnee a l'origine b.
    a, b = np.polyfit(x, y, 1)
    prediction_2050 = a * 2050 + b

    return {
        "x": x,
        "y": y,
        "x_bar": x_bar,
        "y_bar": y_bar,
        "correlation": correlation,
        "a": a,
        "b": b,
        "prediction_2050": prediction_2050,
    }


def tracer_regression(resultats):
    """Trace les observations, la droite de regression et le point predit."""
    FIGURES_DIR.mkdir(exist_ok=True)
    chemin = FIGURES_DIR / "probleme3_regression_lineaire.png"

    x = resultats["x"]
    y = resultats["y"]
    a = resultats["a"]
    b = resultats["b"]
    prediction_2050 = resultats["prediction_2050"]

    x_ligne = np.linspace(x.min(), 2050, 200)
    y_ligne = a * x_ligne + b

    plt.figure(figsize=(9, 5.5))
    plt.scatter(x, y, color="#1d3557", s=55, label="Observations")
    plt.plot(x_ligne, y_ligne, color="#e76f51", linewidth=2, label="Droite de regression")
    plt.scatter(
        resultats["x_bar"],
        resultats["y_bar"],
        marker="x",
        s=120,
        color="#2a9d8f",
        linewidths=3,
        label="Point moyen",
    )
    plt.scatter(
        2050,
        prediction_2050,
        color="#d62828",
        s=80,
        label=f"Prediction 2050 : {prediction_2050:.3f} milliards",
    )
    plt.title("Regression lineaire de la population mondiale")
    plt.xlabel("Annee")
    plt.ylabel("Population mondiale (milliards)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(chemin, dpi=150)
    plt.close()
    return chemin


def executer():
    """Affiche les resultats du probleme 3 et genere la figure."""
    resultats = calculer_regression()
    chemin = tracer_regression(resultats)

    print("Donnees : population mondiale de 1950 a 2020.")
    print(f"x_bar                         = {resultats['x_bar']:.4f}")
    print(f"y_bar                         = {resultats['y_bar']:.4f}")
    print(f"Coefficient de correlation r  = {resultats['correlation']:.8f}")
    print(f"Pente a                       = {resultats['a']:.12f}")
    print(f"Ordonnee a l'origine b        = {resultats['b']:.12f}")
    print(f"Equation                      = y_hat = {resultats['a']:.6f} x + ({resultats['b']:.6f})")
    print(f"Prediction pour 2050          = {resultats['prediction_2050']:.6f} milliards")
    print(f"Figure sauvegardee            = {chemin}")

    print("\nInterpretation :")
    print("- La correlation est tres forte et positive.")
    print("- La pente represente l'augmentation moyenne annuelle en milliards d'habitants.")
    print("- La prediction de 2050 est une extrapolation, donc elle doit etre interpretee avec prudence.")
    print("- En apprentissage automatique, a et b peuvent etre obtenus en minimisant l'erreur quadratique moyenne.")

    return resultats


if __name__ == "__main__":
    print("=" * 30)
    print("PROBLEME 3")
    print("=" * 30)
    executer()
