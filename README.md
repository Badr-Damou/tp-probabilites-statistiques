# Evaluation Probabilites

Ce projet contient une resolution complete de quatre problemes de probabilites et statistiques appliquees au Machine Learning.

## Structure

```text
evaluation_probabilites/
├── README.md
├── requirements.txt
├── main.py
├── probleme1.py
├── probleme2.py
├── probleme3.py
├── probleme4.py
├── figures/
└── rapport.md
```

## Creer un environnement virtuel

Depuis Windows PowerShell, placer le terminal dans le dossier du projet puis executer :

```powershell
python -m venv venv
```

## Activer l'environnement virtuel

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloque temporairement le script d'activation, executer d'abord :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Puis relancer :

```powershell
.\venv\Scripts\Activate.ps1
```

## Installer les dependances

```powershell
python -m pip install -r requirements.txt
```

## Executer le projet

Pour lancer les quatre problemes :

```powershell
python main.py
```

Chaque fichier peut aussi etre execute separement :

```powershell
python probleme1.py
python probleme2.py
python probleme3.py
python probleme4.py
```

## Figures

Les graphiques sont sauvegardes dans le dossier `figures/` :

- `figures/probleme2_histogramme_binomiale.png`
- `figures/probleme2_approximation_normale.png`
- `figures/probleme3_regression_lineaire.png`
- `figures/probleme4_histogramme_abeilles.png`

## Rapport

Le fichier `rapport.md` contient les formules, calculs, resultats numeriques, interpretations et references aux figures.
Il peut etre copie dans Word ou converti en PDF. Un fichier `rapport.pdf` peut aussi etre genere a partir du contenu du rapport.
