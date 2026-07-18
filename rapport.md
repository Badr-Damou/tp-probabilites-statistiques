# Rapport - Probabilites et Statistiques pour le Machine Learning

## Page de garde

**Universite :** ............................................................

**Module :** Probabilites et Statistiques

**Etudiant :** Badr DAMOU

**Enseignant :** Hasan KARJOUN

**Annee universitaire :** 2025-2026

**Titre :** Evaluation de probabilites, lois usuelles, regression lineaire et estimation

---

## Introduction

Ce rapport presente la resolution de quatre problemes classiques de probabilites et de statistiques appliques au contexte du Machine Learning. Les notions utilisees sont le theoreme de Bayes, la loi binomiale, l'approximation normale, la regression lineaire et l'estimation par intervalle de confiance.

Les calculs sont verifies avec un projet Python utilisant `numpy`, `scipy` et `matplotlib`. Les scripts affichent les resultats dans le terminal et sauvegardent les graphiques dans le dossier `figures/`.

---

## Probleme 1 - Detection de courriels frauduleux

### Donnees

On note :

- \(F\) : le courriel est frauduleux ;
- \(D\) : le systeme detecte une fraude.

Les donnees du probleme sont :

- \(P(F)=0.25\) ;
- \(P(\overline F)=0.75\) ;
- \(P(D|F)=0.92\) ;
- \(P(D|\overline F)=0.06\).

Les probabilites complementaires sont :

\[
P(\overline D|F)=1-P(D|F)=1-0.92=0.08
\]

\[
P(\overline D|\overline F)=1-P(D|\overline F)=1-0.06=0.94
\]

### Modele mathematique

Le probleme correspond a une situation de classification binaire. En Machine Learning, \(F\) represente la vraie classe, tandis que \(D\) represente la decision du modele. Les notions importantes sont le taux de detection, les faux positifs et les faux negatifs.

### Calculs detailles

La probabilite totale qu'une alerte soit declenchee est :

\[
P(D)=P(D|F)P(F)+P(D|\overline F)P(\overline F)
\]

\[
P(D)=0.92 \times 0.25 + 0.06 \times 0.75
\]

\[
P(D)=0.23+0.045=0.275
\]

La probabilite qu'un courriel soit frauduleux sachant qu'une alerte est declenchee est donnee par le theoreme de Bayes :

\[
P(F|D)=\frac{P(D|F)P(F)}{P(D)}
\]

\[
P(F|D)=\frac{0.92 \times 0.25}{0.275}
=\frac{0.23}{0.275}
=0.836364
\]

Pour le cas ou aucune alerte n'est declenchee :

\[
P(\overline D)=1-P(D)=1-0.275=0.725
\]

\[
P(F|\overline D)=\frac{P(\overline D|F)P(F)}{P(\overline D)}
\]

\[
P(F|\overline D)=\frac{0.08 \times 0.25}{0.725}
=0.027586
\]

### Resultats numeriques

| Quantite                           |   Valeur | Pourcentage |
| ---------------------------------- | -------: | ----------: |
| \(P(F)\)                           | 0.250000 |     25.00 % |
| \(P(\overline F)\)                 | 0.750000 |     75.00 % |
| \(P(D\mid F)\)                     | 0.920000 |     92.00 % |
| \(P(D\mid \overline F)\)           | 0.060000 |      6.00 % |
| \(P(\overline D\mid F)\)           | 0.080000 |      8.00 % |
| \(P(\overline D\mid \overline F)\) | 0.940000 |     94.00 % |
| \(P(D)\)                           | 0.275000 |     27.50 % |
| \(P(F\mid D)\)                     | 0.836364 |     83.64 % |
| \(P(F\mid \overline D)\)           | 0.027586 |      2.76 % |

### Resume du code Python

Le fichier `probleme1.py` definit les probabilites de depart, applique la formule des probabilites totales puis le theoreme de Bayes. Les resultats sont affiches sous forme decimale et en pourcentage.

### Interpretation

Le taux de detection des courriels frauduleux est eleve, car \(P(D|F)=92\%\). Cependant, le systeme produit aussi des faux positifs : \(6\%\) des courriels non frauduleux declenchent une alerte.

La precision de l'alerte vaut \(P(F|D)=83.64\%\). Cela signifie que lorsqu'une alerte apparait, il y a environ 83.64 % de chances que le courriel soit reellement frauduleux.

Le risque de faux negatif est mesure par \(P(F|\overline D)=2.76\%\). Meme si aucune alerte n'est declenchee, une petite probabilite de fraude subsiste. Dans un contexte de Machine Learning, ce point est important car un faux negatif peut laisser passer une attaque.

---

## Probleme 2 - Authentification biometrique

### Donnees

Un systeme biometrique reconnait correctement un utilisateur avec la probabilite :

\[
p=0.95
\]

On considere d'abord \(n=20\) connexions independantes. La variable aleatoire \(X\) represente le nombre de connexions correctement reconnues.

### Partie A - Loi binomiale

#### Modele mathematique

La variable \(X\) est discrete car elle compte un nombre entier de succes parmi 20 connexions. Le modele adapte est la loi binomiale :

\[
X \sim \mathcal B(n=20,p=0.95)
\]

La loi binomiale est appropriee car :

- le nombre d'essais est fixe ;
- chaque essai a deux issues : reconnaissance correcte ou incorrecte ;
- la probabilite de succes reste constante ;
- les connexions sont supposees independantes.

#### Calculs detailles

La probabilite d'obtenir exactement 18 reconnaissances correctes est :

\[
P(X=18)=\binom{20}{18}(0.95)^{18}(0.05)^2
\]

La probabilite d'obtenir au moins 19 reconnaissances correctes est :

\[
P(X \ge 19)=P(X=19)+P(X=20)
\]

Pour une loi binomiale :

\[
E(X)=np=20 \times 0.95=19
\]

\[
Var(X)=np(1-p)=20 \times 0.95 \times 0.05=0.95
\]

\[
\sigma=\sqrt{0.95}=0.974679
\]

#### Resultats numeriques

| Quantite        |   Valeur |
| --------------- | -------: |
| \(P(X=18)\)     | 0.188677 |
| \(P(X \ge 19)\) | 0.735840 |
| \(E(X)\)        |  19.0000 |
| \(Var(X)\)      |   0.9500 |
| \(\sigma\)      | 0.974679 |

### Partie B - Simulation Python

#### Methode

Le fichier `probleme2.py` utilise `numpy.random.default_rng` avec la graine fixe `2026`. Il simule 1000 experiences de la variable \(X\), puis calcule la moyenne, la variance, l'ecart-type et les probabilites empiriques.

#### Resultats empiriques

| Quantite        | Valeur theorique | Valeur empirique |
| --------------- | ---------------: | ---------------: |
| Moyenne         |          19.0000 |          18.9290 |
| Variance        |           0.9500 |           0.9860 |
| Ecart-type      |         0.974679 |         0.992955 |
| \(P(X=18)\)     |         0.188677 |         0.209000 |
| \(P(X \ge 19)\) |         0.735840 |         0.709000 |

Les valeurs empiriques sont proches des valeurs theoriques. Les ecarts sont normaux car la simulation utilise un nombre fini d'experiences.

#### Figure

L'histogramme des simulations est sauvegarde dans :

`figures/probleme2_histogramme_binomiale.png`

Cette figure montre que les valeurs observees sont concentrees autour de 19 et 20, ce qui est coherent avec une probabilite de reconnaissance elevee.

### Partie C - Approximation normale

On considere maintenant :

\[
X \sim \mathcal B(n=200,p=0.95)
\]

Pour une grande valeur de \(n\), on peut approximer \(X\) par une loi normale :

\[
Y \sim \mathcal N(\mu,\sigma^2)
\]

avec :

\[
\mu=np=200 \times 0.95=190
\]

\[
\sigma^2=np(1-p)=200 \times 0.95 \times 0.05=9.5
\]

\[
\sigma=\sqrt{9.5}=3.082207
\]

#### Calculs avec correction de continuite

Pour \(P(X \ge 185)\), on utilise :

\[
P(X \ge 185) \approx P(Y \ge 184.5)
\]

Pour \(P(180 \le X \le 195)\), on utilise :

\[
P(180 \le X \le 195) \approx P(179.5 \le Y \le 195.5)
\]

#### Comparaison numerique

| Probabilite              | Exacte binomiale | Approximation normale |
| ------------------------ | ---------------: | --------------------: |
| \(P(X \ge 185)\)         |         0.955644 |              0.962824 |
| \(P(180 \le X \le 195)\) |         0.972393 |              0.962495 |

L'approximation normale est assez proche des probabilites exactes. Les differences restent faibles, ce qui montre que l'approximation est raisonnable pour \(n=200\), meme si \(p=0.95\) est proche de 1.

#### Figure

La comparaison entre la loi binomiale et l'approximation normale est sauvegardee dans :

`figures/probleme2_approximation_normale.png`

### Interpretation Machine Learning

Le systeme semble fiable et stable : avec 200 connexions, le nombre moyen de reconnaissances correctes est de 190. La probabilite d'obtenir au moins 185 reconnaissances correctes est superieure a 95 %. Dans une application de Machine Learning, cela indique une performance globale elevee, mais il faut aussi surveiller les erreurs d'authentification car elles peuvent avoir des consequences importantes pour l'utilisateur.

---

## Probleme 3 - Regression lineaire

### Donnees

Les donnees representent la population mondiale, en milliards, entre 1950 et 2020 :

| Annee | Population |
| ----: | ---------: |
|  1950 |       2.54 |
|  1955 |       2.77 |
|  1960 |       3.03 |
|  1965 |       3.34 |
|  1970 |       3.70 |
|  1975 |       4.08 |
|  1980 |       4.46 |
|  1985 |       4.87 |
|  1990 |       5.33 |
|  1995 |       5.74 |
|  2000 |       6.14 |
|  2005 |       6.54 |
|  2010 |       6.96 |
|  2015 |       7.38 |
|  2020 |       7.80 |

### Modele mathematique

On cherche une droite de regression lineaire :

\[
\hat y = ax+b
\]

ou :

- \(x\) est l'annee ;
- \(y\) est la population mondiale observee ;
- \(a\) est la pente ;
- \(b\) est l'ordonnee a l'origine.

### Calculs detailles

Le point moyen est :

\[
\bar x = \frac{1}{n}\sum\_{i=1}^n x_i = 1985
\]

\[
\bar y = \frac{1}{n}\sum\_{i=1}^n y_i = 4.9787
\]

Le coefficient de correlation lineaire calcule avec `np.corrcoef` est :

\[
r=0.99791698
\]

Cette valeur est tres proche de 1, ce qui indique une tres forte correlation lineaire positive entre l'annee et la population mondiale observee.

La droite obtenue avec `np.polyfit(x, y, 1)` est :

\[
a=0.077457142857
\]

\[
b=-148.773761904762
\]

Donc :

\[
\hat y = 0.077457x - 148.773762
\]

La prediction pour 2050 est :

\[
\hat y(2050)=0.077457 \times 2050 - 148.773762
\]

\[
\hat y(2050)=10.013381
\]

La population predite pour 2050 est donc environ 10.013 milliards d'habitants.

### Resume du code Python

Le fichier `probleme3.py` cree les vecteurs `x` et `y`, calcule le point moyen, le coefficient de correlation, la droite de regression et la prediction pour 2050. Il produit aussi un graphique contenant les observations, la droite de regression, le point moyen et le point predit pour 2050.

### Figure

Le graphique est sauvegarde dans :

`figures/probleme3_regression_lineaire.png`

### Interpretation Machine Learning

La pente \(a\) indique que, selon le modele lineaire, la population augmente en moyenne d'environ 0.077457 milliard par an, soit environ 77.46 millions de personnes par an.

L'ordonnee a l'origine \(b\) a une interpretation directe limitee, car l'annee 0 est tres loin de l'intervalle observe. Elle sert surtout a positionner la droite mathematiquement.

En Machine Learning, les parametres \(a\) et \(b\) sont choisis pour minimiser une fonction de perte, souvent l'erreur quadratique moyenne :

\[
MSE=\frac{1}{n}\sum\_{i=1}^n (y_i-\hat y_i)^2
\]

Cette minimisation peut se faire par la methode analytique des moindres carres ou par descente de gradient. Dans la descente de gradient, les parametres sont mis a jour iterativement afin de reduire l'erreur.

La prediction obtenue pour 2050 doit etre interpretee avec prudence. Elle repose sur une extrapolation lineaire hors de l'intervalle 1950-2020. Or, l'evolution demographique n'est pas parfaitement lineaire : la fecondite, la mortalite, les migrations, les politiques publiques et les crises peuvent modifier la trajectoire.

---

## Probleme 4 - Estimation et intervalle de confiance

### Donnees

Les longueurs d'abeilles sont donnees par classes :

| Classe (mm)    | Centre | Effectif |
| -------------- | -----: | -------: |
| \([3.5,4.5[\)  |      4 |        1 |
| \([4.5,5.5[\)  |      5 |        2 |
| \([5.5,6.5[\)  |      6 |       23 |
| \([6.5,7.5[\)  |      7 |       46 |
| \([7.5,8.5[\)  |      8 |       24 |
| \([8.5,9.5[\)  |      9 |        3 |
| \([9.5,10.5[\) |     10 |        1 |

Le total est :

\[
n=100
\]

### Reconstruction de l'echantillon

Comme les donnees sont groupees, on reconstruit un echantillon approximatif en repetant chaque centre de classe selon son effectif :

- une valeur egale a 4 ;
- deux valeurs egales a 5 ;
- vingt-trois valeurs egales a 6 ;
- quarante-six valeurs egales a 7 ;
- vingt-quatre valeurs egales a 8 ;
- trois valeurs egales a 9 ;
- une valeur egale a 10.

Cette reconstruction est approximative car on remplace toutes les valeurs d'une classe par son centre.

### Calculs detailles

La moyenne empirique est :

\[
m_e=\frac{\sum n_i c_i}{n}
\]

\[
m_e=\frac{1\times4+2\times5+23\times6+46\times7+24\times8+3\times9+1\times10}{100}
\]

\[
m_e=\frac{703}{100}=7.03
\]

La variance empirique avec denominateur \(n\) est :

\[
V_e=\frac{\sum n_i(c_i-m_e)^2}{n}
\]

\[
V_e=0.849100
\]

L'ecart-type empirique est :

\[
\sigma_e=\sqrt{V_e}=0.921466
\]

L'estimateur de la moyenne de la population est la moyenne empirique :

\[
\hat \mu=m_e
\]

Comme la variance de la population est inconnue, l'estimateur de la variance utilise le denominateur \(n-1\) :

\[
s^2=\frac{\sum (x_i-\bar x)^2}{n-1}
\]

\[
s^2=0.857677
\]

\[
s=0.926108
\]

### Intervalle de confiance a 95 %

La variance de la population etant inconnue, on utilise la loi de Student :

\[
\bar x \pm t\_{0.975,n-1}\frac{s}{\sqrt n}
\]

Avec \(n=100\), \(n-1=99\) et :

\[
t\_{0.975,99}=1.984217
\]

La marge d'erreur est :

\[
1.984217 \times \frac{0.926108}{\sqrt{100}}=0.183760
\]

Donc :

\[
IC\_{95\%}=[7.03-0.183760,\;7.03+0.183760]
\]

\[
IC\_{95\%}=[6.846240,\;7.213760]
\]

L'amplitude de l'intervalle est :

\[
7.213760-6.846240=0.367520
\]

### Taille minimale pour une amplitude inferieure a 0.1 mm

On utilise l'approximation normale :

\[
2z\_{0.975}\frac{s}{\sqrt n}<0.1
\]

Donc :

\[
n>\left(\frac{2z\_{0.975}s}{0.1}\right)^2
\]

Avec \(z\_{0.975}=1.959964\) et \(s=0.926108\) :

\[
n>\left(\frac{2\times1.959964\times0.926108}{0.1}\right)^2
\]

\[
n>1317.85
\]

On arrondit au superieur :

\[
n\_{\min}=1318
\]

Ce calcul utilise l'ecart-type corrige de l'echantillon comme estimation de l'ecart-type de la population.

### Resultats numeriques

| Quantite                                |                   Valeur |
| --------------------------------------- | -----------------------: |
| \(n\)                                   |                      100 |
| Moyenne empirique \(m_e\)               |              7.030000 mm |
| Variance empirique \(V_e\)              |                 0.849100 |
| Ecart-type empirique                    |              0.921466 mm |
| Variance corrigee \(s^2\)               |                 0.857677 |
| Ecart-type corrige \(s\)                |              0.926108 mm |
| \(t\_{0.975,99}\)                       |                 1.984217 |
| IC 95 %                                 | [6.846240 ; 7.213760] mm |
| Amplitude                               |              0.367520 mm |
| Taille minimale pour amplitude < 0.1 mm |                     1318 |

### Resume du code Python

Le fichier `probleme4.py` cree les tableaux `centres` et `effectifs`, reconstruit l'echantillon avec `np.repeat`, calcule les estimateurs et construit l'intervalle de confiance avec `scipy.stats.t`. Il calcule aussi la taille minimale necessaire pour obtenir un intervalle plus precis.

### Figure

L'histogramme est sauvegarde dans :

`figures/probleme4_histogramme_abeilles.png`

### Interpretation statistique

La longueur moyenne estimee est de 7.03 mm. La plupart des observations se concentrent autour des classes centrees en 6, 7 et 8 mm, ce qui montre une tendance centrale nette.

La variabilite est moderee : l'ecart-type corrige est environ 0.926 mm. L'intervalle de confiance a 95 % signifie que, selon le modele statistique utilise, une methode identique de construction d'intervalles contiendrait la vraie moyenne de la population dans environ 95 % des echantillons de meme type.

L'amplitude actuelle, environ 0.368 mm, est superieure a 0.1 mm. Pour obtenir une estimation plus precise, il faudrait augmenter fortement la taille de l'echantillon, jusqu'a au moins 1318 abeilles selon l'approximation normale.

---

## Conclusion

Les quatre problemes montrent comment les probabilites et les statistiques servent a analyser des situations typiques du Machine Learning.

Dans le premier probleme, le theoreme de Bayes permet d'evaluer la precision d'un detecteur de fraude et le risque de faux negatif. Dans le deuxieme probleme, la loi binomiale modelise naturellement le nombre de reconnaissances correctes d'un systeme biometrique, tandis que la simulation et l'approximation normale permettent de verifier et d'etendre l'analyse. Dans le troisieme probleme, la regression lineaire illustre la construction d'un modele predictif simple. Enfin, le quatrieme probleme montre comment estimer une moyenne de population et comment la taille d'echantillon influence la precision d'un intervalle de confiance.

Le projet Python associe a ce rapport permet de reproduire tous les resultats numeriques et de regenerer les figures automatiquement.
