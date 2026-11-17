# Space Invaders

Un petit jeu de style Space Invaders créé avec Python et Pygame.
## Démarrage rapide

### Prérequis

* Python 3.10 ou plus récent
* Pygame (listé dans `requirements.txt`)

Depuis la racine du projet, créez et activez un environnement virtuel, puis installez la dépendance :

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

```

Lancez le jeu depuis la racine du projet pour qu'il puisse trouver les fichiers d'images et de sons :

```bash
python main.py

```

Fermez la fenêtre du jeu pour quitter. Sur certains systèmes, utilisez `python` au lieu de `python3` pour la commande d'installation.

## Comment jouer

| Touche | Action |
| --- | --- |
| ← / → | Déplacer le vaisseau vers la gauche / droite |
| Espace | Tirer un coup normal (1 point de dégât) |
| X | Tirer un coup puissant (2 points de dégâts) |

Votre vaisseau est limité aux bords de l'écran. Les ennemis se déplacent horizontalement et descendent lorsqu'ils atteignent un bord.

Tirez-leur dessus avant qu'un ennemi ne descende trop bas : le jeu se termine lorsque la position d'un ennemi dépasse le seuil inférieur de l'écran.

Le score s'affiche dans le coin supérieur gauche. Les ennemis basiques valent 1 point ; le boss vaut 5 points et nécessite trois points de dégâts pour être vaincu. Les ennemis détruits réapparaissent près du haut de l'écran, le jeu continue donc jusqu'à ce que vous perdiez.

## Aperçu du projet

Le jeu est divisé en une boucle principale, des fonctions d'événements/mises à jour, et des classes pour les objets du jeu :

* [`main.py`](https://github.com/krabandicoot/progra_projet_bac2/blob/main/main.py) initialise Pygame, charge les images et les sons, crée le joueur et les ennemis, et exécute la boucle de jeu à 60 FPS. Chaque frame gère les entrées, met à jour l'état du jeu, dessine les objets et le score, puis affiche la frame.
* [`events.py`](https://github.com/krabandicoot/progra_projet_bac2/blob/main/events.py) gère les événements du clavier/fenêtre et met à jour les mouvements, les positions des projectiles, les collisions, le score, la réapparition des ennemis et l'état de fin de jeu (game over).
* [`classes/player.py`](https://github.com/krabandicoot/progra_projet_bac2/blob/main/classes/player.py) définit la position du joueur, la vitesse de déplacement, les limites de l'écran et le comportement d'affichage.
* [`classes/enemy.py`](https://github.com/krabandicoot/progra_projet_bac2/blob/main/classes/enemy.py) définit le comportement partagé des ennemis en matière de mouvement, de santé, de dégâts, de collisions et de réapparition. `BasicEnemy` et `BossEnemy` définissent leur propre vitesse, santé, distance de descente et valeur de score.
* [`classes/projectile.py`](https://github.com/krabandicoot/progra_projet_bac2/blob/main/classes/projectile.py) définit les projectiles se déplaçant vers le haut. `ProjectileNormal` et `ProjectileFort` spécifient les tirs normaux et puissants.
* [`pictures/`](https://github.com/krabandicoot/progra_projet_bac2/tree/main/pictures) contient les illustrations du joueur, de l'ennemi, du boss, des projectiles, de l'icône OVNI et du fond d'écran. `sounds/` contient la musique de fond, le laser et les effets d'explosion.

### Que se passe-t-il dans une frame ?

1. `main.py` interroge les événements. `events.py` modifie le mouvement horizontal du joueur ou crée un projectile lorsque vous tirez.
2. `update_game()` déplace le joueur, les ennemis et les projectiles. Il vérifie les collisions projectile/ennemi à l'aide des masques Pygame (formes de collision au niveau du pixel), applique les dégâts et attribue des points lorsqu'un ennemi est vaincu.
3. `main.py` dessine l'arrière-plan, le joueur, les ennemis et projectiles restants, le score et — si nécessaire — le message **GAME OVER**.

## Fichiers

```text
.
├── main.py
├── events.py
├── classes/
│   ├── enemy.py
│   ├── player.py
│   └── projectile.py
├── pictures/
├── sounds/
└── requirements.txt

```