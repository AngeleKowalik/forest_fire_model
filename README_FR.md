# Modèle de feu de forêt
[Link to English doc](README.md) | [Lien vers l'installation](#installation)

Ce projet est une implémentation personnelle du modèle de feu de forêt proposé par Drossel et Schwabl dans leur article de 1992. C'est l'un des premiers automates cellulaires dédiés à l'étude de la criticité auto-organisée. Pour le reproduire, cette version écrite en Python s'appuie fortement sur la vectorisation avec NumPy, permettant ainsi d'éviter des boucles `for` coûteuses et de s'approcher de la vitesse du langage C.

## Table des matières
- [Références scientifiques](#références-scientifiques)
- [Architecture du modèle](#architecture-du-modèle)
    - [Paramètres de la matrice](#paramètres-de-la-matrice)
    - [Règles de mise à jour](#règles-de-mise-à-jour)
- [Architecture logicielle](#architecture-logicielle)
    - [NumPy vectorisé](#numpy-vectorisé)
    - [Qualité du code](#qualité-du-code)
    - [Structure du dépôt](#structure-du-dépôt)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)
    - [Explication](#explication)
    - [Exécution](#exécution)
- [Feuille de route](#feuille-de-route)
- [Corrections à apporter](#corrections-à-apporter)

## Références scientifiques
Cette implementation s'appuie significativement sur ces articles : 
* **Modèle fondateur :** P. Bak, K. Chen et C. Tang, *« A forest-fire model and some thoughts on turbulence »*, Physics Letters A, vol. 147, n° 5–6, p. 297–300, 1990. DOI : [10.1016/0375-9601(90)90451-S](https://doi.org/10.1016/0375-9601(90)90451-S)
* **Extension sur la criticité auto-organisée (implémentée ici) :** B. Drossel et F. Schwabl, *« Self-organized critical forest-fire model »*, Physical Review Letters, vol. 69, n° 11, p. 1629–1632, 1992. DOI : [10.1103/PhysRevLett.69.1629](https://doi.org/10.1103/PhysRevLett.69.1629)

Le premier modèle reproduit une dissipation d'énergie en fractale dans un système fermé mais le feu finit toujours par s'éteindre et doit être rallumé manuellement.

Le second modèle met en évidence la criticité auto-organisée : le système évolue naturellement vers une distribution en loi de puissance des zones brûlées dès lors que la fréquence de foudre (probabilité qu'un arbre s'embrase) est très inférieure à la vitesse de pousse des arbres ($f \ll p \ll 1$).

## Architecture du modèle
### Paramètres de la matrice
L'automate est constituée d'une grille 2D discrète de dimensions $R \times C$ ($lignes \times colonnes$). Ses bords sont absorbants : le feu s'arrête en bordure de la matrice et ne réapparaît pas du côté opposé.

Chaque cellule peut prendre l'un de trois états discrets, implémentés avec `IntEnum` pour la sûreté du typage et la lisibilité :
- `VOID`  (0)
- `TREE` (1)
- `FIRE` (2)

### Règles de mise à jour
La simulation utilise des règles de mise à jour synchrones : toute la matrice est mise à jour à chaque pas de temps discret ($t \to t+1$) selon quatre règles :
1) **Propagation :** chaque `FIRE` présent sur la grille se propage aux `TREE` de son voisinage de von Neumann (4 cellules orthogonales, sans les diagonales).
2) **Extinction :** les `FIRE` d'origine se consument et sont remplacés par du `VOID`.
3) **Foudre :** les `TREE` restants s'enflamment spontanément en `FIRE` avec la probabilité de foudroiement $f$.
4) **Pousse :** les cellules `VOID` deviennent des `TREE` avec la probabilité $p$.

## Architecture logicielle
### NumPy vectorisé
Parcourir une grille 2D avec des boucles `for` imbriquées entraîne un surcoût de calcul important et est intrinsèquement lent. Ce programme utilise donc NumPy pour effectuer les opérations matriciel. C'est nettement plus rapide, car les méthodes de NumPy sont écrites en C, ce qui permet des opérations vectorisées efficaces grâce au masquage booléen. De plus, NumPy permet une allocation mémoire efficace avec des matrices `np.uint8`.

Pour corriger l'effet non absorbant des bordures matricielles induites par `np.roll()`, qui laisserait le feu sauter d'un bord de la grille au bord opposé, des masques booléens statiques sont précalculés à l'initialisation de la matrice et appliqués à chaque décalage de la grille.

### Qualité du code
Pour garantir une bonne modularité et la qualité du code, ce script suit plusieurs principes :
- **Séparation des responsabilités :** le moteur mathématique (`Matrix`, `SimParam`, `Proba`, `State`) est strictement découplé des entrées/sorties du terminal (`enter_int`, `enter_proba`). Cela permet une collecte de données rapide et sans interface, et facilitera le portage du script vers Project Mesa.
- **Mesures de sécurité :** pour fiabiliser l'exécution, l'ensemble du script est testé avec `pytest`. Il est entièrement typé et les paramètres de configuration sont rendus immuables grâce à `@dataclass(frozen=True)`.
- **Maintenabilité :** le projet fournit des messages de débogage clairs grâce à une journalisation structurée (`logging`). L'architecture modulaire permet une installation développeur standard et la gestion des dépendances via `pyproject.toml`.

### Structure du dépôt
```
forest-fire-model/
├── pyproject.toml
├── README.md
├── README_FR.md
├── src/
│   └── forest_fire/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## Installation
***L'installation nécessite Python 3.10+ et git.***

---

### Linux et macOS
```bash
# 1. Cloner le dépôt et se placer dans le répertoire
git clone https://github.com/AngeleKowalik/forest_fire_model.git
cd forest_fire_model

# 2. Créer et activer un environnement virtuel isolé
python3 -m venv .venv
source .venv/bin/activate

# 3. Mettre à jour pip (recommandé)
pip install --upgrade pip
```
4a. Installation standard (pour simplement lancer la simulation)
```bash
pip install .
```

4b. Installation développeur (mode éditable, avec les dépendances de test et de linting)
```bash
pip install -e ".[dev]"
```

### Windows
```powershell
# 1. Cloner le dépôt et se placer dans le répertoire
git clone https://github.com/AngeleKowalik/forest_fire_model.git
cd forest_fire_model

# 2. Créer et activer un environnement virtuel isolé
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# (Remarque : en cas d'erreur de stratégie d'exécution, lancer :
# Set-ExecutionPolicy Unrestricted -Scope CurrentUser)

# (Remarque : avec l'invite de commandes classique (cmd.exe), lancer :
# .\.venv\Scripts\activate.bat)

# 3. Mettre à jour pip (recommandé)
python -m pip install --upgrade pip
```

4a. Installation standard (pour simplement lancer la simulation)
```powershell
pip install .
```

4b. Installation développeur (mode éditable, avec les dépendances de test et de linting)
```powershell
pip install -e ".[dev]"
```

## Utilisation
**Linux / macOS**
```bash
python3 -m forest_fire.main
```

**Windows**
```powershell
python -m forest_fire.main
```

Suivez ensuite les instructions affichées dans le terminal.

**Exemple :**
```bash
python3 -m forest_fire.main
# How many rows do you want in your matrix ?
4

# How many columns do you want in your matrix ?
5

# How many cycles should the program run for ?
5

# How many cycle should the program run for ?
6

# [0 0 1 0 0]
# [0 1 0 0 0]
# [1 1 0 0 0]
# [1 0 0 1 0]

# [0 0 1 0 0]
# [1 1 0 1 1]
# [1 1 0 0 1]
# [1 0 1 1 0]

# [1 1 1 0 0]
# [1 1 1 1 1]
# [1 1 0 0 1]
# [1 1 1 1 1]

# [1 1 1 0 0]
# [1 1 2 1 1]
# [1 1 0 0 1]
# [1 1 1 1 1]

# [1 1 2 0 0]
# [1 2 0 2 1]
# [1 1 1 0 1]
# [2 1 1 1 1]

# [1 2 0 0 0]
# [2 0 1 1 2]
# [2 2 1 0 1]
# [1 2 1 1 1]
```

## Tests
### Explication
Pour garantir des résultats fiables, chaque fonction mathématique est confrontée à un oracle.

Pour `Matrix.spread()`, ces oracles sont des tests spatiaux déterministes codés en dur sur une matrice $3 \times 3$. Des oracles couvrent tous les points de départ important afin de prouver que le feu se propage orthogonalement et ne saute jamais d'un bord à l'autre de la matrice.

Pour `probabilistic_insert()`, les cas particulier de 0 et 1 sont testés séparément. Pour les autres probabilités, strictement comprises entre 0 et 1, le test s'appuie sur la loi des grands nombres avec $N = 10 000$ itérations afin de vérifier que la moyenne empirique converge à $\pm 0{,}01$ près de la probabilité cible.

### Exécution
```bash
# Lancer tous les tests unitaires
pytest

# Lancer avec une sortie détaillée (affiche le nom et le statut de chaque fonction de test)
pytest -v

# Lancer un seul test précis (ex. uniquement le test du coin supérieur gauche)
pytest -k "test_top_left_corner"
```

## Feuille de route
- [x] Écrire une fonction permettant à l'utilisateur de saisir un flottant entre 0 et 1 (pour les probabilités)
- [x] Créer des tests avec pytest pour chaque fonction
- [x] Terminer le README.md
- [x] Terminer le README_FR.md
- [ ] Mettre en place un système de garde-fous contre les valeurs codées en dur incorrectes (via IntEnum)
- [ ] Ajouter des graphiques avec Matplotlib
- [ ] Ajouter une visualisation avec pygame ou une bibliothèque similaire
- [ ] Enregistrer les résultats de chaque exécution dans un fichier externe
- [ ] Porter le paquet vers Project Mesa

## Corrections à apporter
- [x] Vérifier l'article original pour établir le bon ordre des opérations
- [x] Refactoriser la fonction de propagation pour supprimer le bug du feu qui saute d'un bord à l'autre de la matrice
- [x] Accélérer les boucles Python lentes en utilisant des méthodes NumPy