# Modèle de feu de forêt
[Link to English doc](README.md) | [Lien vers l'installation](#installation)

Ce projet est une implémentation personnelle du modèle de feu de forêt proposé par Drossel et Schwabl dans leur article de 1992. C'est l'un des premiers automates cellulaires dédiés à l'étude de la criticité auto-organisée. Pour le reproduire, cette version écrite en Python s'appuie fortement sur la vectorisation avec NumPy, permettant ainsi d'éviter des boucles `for` coûteuses et de s'approcher de la vitesse du langage C.

## Table des matières
- **[Références scientifiques](#références-scientifiques)**


## Références scientifiques
Cette implementation s'appuie significativement sur ces articles : 
* **Modèle fondateur :** P. Bak, K. Chen et C. Tang, *« A forest-fire model and some thoughts on turbulence »*, Physics Letters A, vol. 147, n° 5–6, p. 297–300, 1990. DOI : [10.1016/0375-9601(90)90451-S](https://doi.org/10.1016/0375-9601(90)90451-S)
* **Extension sur la criticité auto-organisée (implémentée ici) :** B. Drossel et F. Schwabl, *« Self-organized critical forest-fire model »*, Physical Review Letters, vol. 69, n° 11, p. 1629–1632, 1992. DOI : [10.1103/PhysRevLett.69.1629](https://doi.org/10.1103/PhysRevLett.69.1629)

