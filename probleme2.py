# -*- coding: utf-8 -*-
"""Probleme 2 - Authentification biometrique."""

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
SEED = 2026


def etude_binomiale():
    """Calcule les resultats theoriques pour X ~ B(20, 0.95)."""
    n = 20
    p = 0.95

    proba_x_18 = stats.binom.pmf(18, n, p)
    proba_x_sup_egal_19 = stats.binom.sf(18, n, p)
    esperance = n * p
    variance = n * p * (1 - p)
    ecart_type = np.sqrt(variance)

    return {
        "n": n,
        "p": p,
        "P(X=18)": proba_x_18,
        "P(X>=19)": proba_x_sup_egal_19,
        "E(X)": esperance,
        "Var(X)": variance,
        "sigma": ecart_type,
    }


def simulation_binomiale(n=20, p=0.95, nombre_experiences=1000):
    """Simule 1000 experiences independantes avec une graine fixe."""
    rng = np.random.default_rng(SEED)
    x_simulations = rng.binomial(n=n, p=p, size=nombre_experiences)

    moyenne_empirique = np.mean(x_simulations)
    variance_empirique = np.var(x_simulations, ddof=0)
    ecart_type_empirique = np.std(x_simulations, ddof=0)
    proba_x_18_empirique = np.mean(x_simulations == 18)
    proba_x_sup_egal_19_empirique = np.mean(x_simulations >= 19)

    return {
        "x_simulations": x_simulations,
        "moyenne empirique": moyenne_empirique,
        "variance empirique": variance_empirique,
        "ecart-type empirique": ecart_type_empirique,
        "P_emp(X=18)": proba_x_18_empirique,
        "P_emp(X>=19)": proba_x_sup_egal_19_empirique,
    }


def tracer_histogramme_simulation(x_simulations, moyenne_theorique, moyenne_empirique):
    """Trace l'histogramme des simulations et sauvegarde la figure."""
    FIGURES_DIR.mkdir(exist_ok=True)
    chemin = FIGURES_DIR / "probleme2_histogramme_binomiale.png"

    plt.figure(figsize=(9, 5))
    bins = np.arange(-0.5, 21.5, 1)
    plt.hist(
        x_simulations,
        bins=bins,
        color="#4f83cc",
        edgecolor="black",
        alpha=0.80,
        label="Simulations",
    )
    plt.axvline(
        moyenne_theorique,
        color="#d62828",
        linestyle="--",
        linewidth=2,
        label=f"Moyenne theorique = {moyenne_theorique:.2f}",
    )
    plt.axvline(
        moyenne_empirique,
        color="#2a9d8f",
        linestyle="-",
        linewidth=2,
        label=f"Moyenne empirique = {moyenne_empirique:.2f}",
    )
    plt.title("Simulation d'une loi binomiale B(20, 0.95)")
    plt.xlabel("Nombre de reconnaissances correctes")
    plt.ylabel("Frequence")
    plt.xticks(range(0, 21))
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(chemin, dpi=150)
    plt.close()
    return chemin


def approximation_normale():
    """Compare la loi binomiale B(200, 0.95) a son approximation normale."""
    n = 200
    p = 0.95
    mu = n * p
    variance = n * p * (1 - p)
    sigma = np.sqrt(variance)

    proba_exacte_sup_185 = stats.binom.sf(184, n, p)
    proba_normale_sup_185 = stats.norm.sf(184.5, loc=mu, scale=sigma)

    proba_exacte_180_195 = stats.binom.cdf(195, n, p) - stats.binom.cdf(179, n, p)
    proba_normale_180_195 = stats.norm.cdf(195.5, loc=mu, scale=sigma) - stats.norm.cdf(
        179.5, loc=mu, scale=sigma
    )

    return {
        "n": n,
        "p": p,
        "mu": mu,
        "variance": variance,
        "sigma": sigma,
        "P_exacte(X>=185)": proba_exacte_sup_185,
        "P_normale(X>=185)": proba_normale_sup_185,
        "P_exacte(180<=X<=195)": proba_exacte_180_195,
        "P_normale(180<=X<=195)": proba_normale_180_195,
    }


def tracer_comparaison_normale(resultats_normale):
    """Trace une comparaison entre la loi binomiale et l'approximation normale."""
    FIGURES_DIR.mkdir(exist_ok=True)
    chemin = FIGURES_DIR / "probleme2_approximation_normale.png"

    n = resultats_normale["n"]
    p = resultats_normale["p"]
    mu = resultats_normale["mu"]
    sigma = resultats_normale["sigma"]

    x = np.arange(175, 201)
    pmf = stats.binom.pmf(x, n, p)
    densite_normale = stats.norm.pdf(x, loc=mu, scale=sigma)

    plt.figure(figsize=(9, 5))
    plt.bar(x, pmf, color="#90be6d", edgecolor="black", alpha=0.75, label="Loi binomiale")
    plt.plot(x, densite_normale, color="#d62828", linewidth=2, label="Approximation normale")
    plt.axvline(mu, color="#264653", linestyle="--", linewidth=2, label=f"mu = {mu:.0f}")
    plt.title("Approximation normale de B(200, 0.95)")
    plt.xlabel("Nombre de reconnaissances correctes")
    plt.ylabel("Probabilite")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(chemin, dpi=150)
    plt.close()
    return chemin


def executer():
    """Affiche les resultats du probleme 2 et genere les figures."""
    theorique = etude_binomiale()
    simulation = simulation_binomiale()
    chemin_hist = tracer_histogramme_simulation(
        simulation["x_simulations"],
        theorique["E(X)"],
        simulation["moyenne empirique"],
    )
    normale = approximation_normale()
    chemin_normale = tracer_comparaison_normale(normale)

    print("Partie A - Loi binomiale :")
    print("X est discrete car elle compte un nombre entier de connexions reconnues correctement.")
    print("Modele : X suit une loi binomiale B(n=20, p=0.95).")
    print(f"P(X = 18)     = {theorique['P(X=18)']:.6f}")
    print(f"P(X >= 19)    = {theorique['P(X>=19)']:.6f}")
    print(f"E(X)          = {theorique['E(X)']:.4f}")
    print(f"Var(X)        = {theorique['Var(X)']:.4f}")
    print(f"Ecart-type    = {theorique['sigma']:.6f}")

    print("\nPartie B - Simulation Python :")
    print(f"Nombre d'experiences simulees = {len(simulation['x_simulations'])}")
    print(f"Moyenne empirique             = {simulation['moyenne empirique']:.4f}")
    print(f"Variance empirique            = {simulation['variance empirique']:.4f}")
    print(f"Ecart-type empirique          = {simulation['ecart-type empirique']:.6f}")
    print(f"P_emp(X = 18)                 = {simulation['P_emp(X=18)']:.6f}")
    print(f"P_emp(X >= 19)                = {simulation['P_emp(X>=19)']:.6f}")
    print(f"Figure sauvegardee            = {chemin_hist}")

    print("\nPartie C - Approximation normale :")
    print("Pour X ~ B(200, 0.95), on approche X par Y ~ N(mu, sigma^2).")
    print(f"mu             = {normale['mu']:.4f}")
    print(f"sigma^2        = {normale['variance']:.4f}")
    print(f"sigma          = {normale['sigma']:.6f}")
    print(f"P_exacte(X >= 185)         = {normale['P_exacte(X>=185)']:.6f}")
    print(f"P_normale(X >= 185)        = {normale['P_normale(X>=185)']:.6f}")
    print(f"P_exacte(180 <= X <= 195)  = {normale['P_exacte(180<=X<=195)']:.6f}")
    print(f"P_normale(180 <= X <= 195) = {normale['P_normale(180<=X<=195)']:.6f}")
    print(f"Figure sauvegardee         = {chemin_normale}")

    return theorique, simulation, normale


if __name__ == "__main__":
    print("=" * 30)
    print("PROBLEME 2")
    print("=" * 30)
    executer()
