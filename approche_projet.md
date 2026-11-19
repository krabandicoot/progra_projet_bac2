Nous avons commencé par trier le repository et décomposer les ressources du projet par type de fichiers (sons, images) ainsi que les différentes classes d’objets dans un dossier `classes/`.

La structure du projet est donc la suivante :
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

HEY

# Identification des classes

Nous avons identifié 3 éléments dont les états sont fréquemment modifiés durant la partie et avons créé une classe pour chacun d'eux.

## Classe `Player`

Nous avons regroupé toutes les données du joueur au sein d’un objet `Player` avec les attributs `x`, `y`, `image`, `vitesse` (fixée à `5`) et `x_change` (initialisée à `0`).

### Méthode `move`

Gère les déplacements horizontaux et le blocage aux bords de l'écran. Reprise depuis la boucle `while` du `main.py` original, cette logique permet désormais au joueur de gérer lui-même ses contraintes de déplacement selon la largeur de l'interface.

### Méthode `update`

Chaque entité possède une méthode `update` appelable dans la boucle de jeu, ce qui permet de standardiser la mise à jour par frame en appelant `self.move`.

### Méthode `draw`

Permet d'afficher l'objet dans la fenêtre de jeu (`screen.blit`) tout en garantissant des coordonnées entières grâce à l'arrondi (`round`).

### Méthode `get_rect`

Renvoie le rectangle englobant le joueur (utile pour préparer la gestion des collisions avec le vaisseau et faciliter l'ajout de nouvelles fonctionnalités).

### Méthode `__repr__`

Renvoie l'état de l'objet de manière lisible (permet de déboguer plus facilement le jeu en cas de problème).

## Classes `Enemy`, `BasicEnemy` et `BossEnemy`

Nous avons créé une classe mère `Enemy` qui définit les attributs communs (`x`, `y`, `vitesse`, `direction`, `distance_descente`, `pointvie`, `max_pointvie`, `score_value`, `image`) ainsi que les méthodes génériques auparavant dispersées dans `main.py`, évitant ainsi de tout initialiser un par un.

### Propriété `pointvie`

Nous avons ajouté une protection avec un getter (`@property`) et un setter (`@pointvie.setter`) pour garantir une encapsulation stricte et empêcher qu'une valeur négative lui soit assignée.

### Méthodes `move` et `update`

Gèrent le déplacement individuel des ennemis sans plus dépendre de l'index `i` des listes de la boucle `while`.

### Méthodes `take_damage` et `is_alive` *(nouvelles fonctionnalités)*

Vérifient si l'ennemi est toujours en vie et gèrent la réduction des points de vie (`3` pour le boss et `1` pour l'ennemi classique).

### Méthode `reset`

Reprise de la boucle principale du `main.py` d'origine, elle réinitialise la position et les points de vie de l'ennemi afin d'éviter d'avoir à recréer un nouvel objet.

### Méthodes `draw` et `get_rect`

Remplacent l'appel à `enemy(x, y, i)` de la boucle principale et effectuent le calcul du `Rect` directement sur l'objet lui-même plutôt que via un index de liste.

### Méthode `collides_with`

Remplace `isCollision` et substitue le calcul de distance fixe (`< 27` px) par une détection pixel par pixel (`self.mask.overlap(projectile.mask, ...)`) pour une précision accrue.

### `BasicEnemy` et `BossEnemy` *(nouvelle fonctionnalité)*

Spécialisent la classe générique `Enemy` avec des statistiques qui leur sont propres afin d'introduire différents types d'ennemis (basique et boss), en utilisant `super()` pour gérer l'héritage.

## Classe `Projectile`

À l'origine, une simple fonction gérait les projectiles (`fire_bullet(x, y)`). Afin de rendre le jeu plus modulable, nous avons défini des caractéristiques propres à chaque projectile telles que sa vitesse, ses dégâts et son masque de collision (`mask`).

### Ajout de protection (`vitesse`)

Ajout d'une `@property` sur l'attribut `vitesse` pour empêcher l'attribution de valeurs négatives.

### Méthode `move`

Extraite de la boucle principale, elle gère l'ascension verticale du tir.

### Méthode `draw`

Remplace la fonction `fire_bullet(x, y)` et ne dépend plus d'une variable d'état globale, ce qui rend possibles les tirs multiples simultanés.

### Méthode `get_rect` et `__repr__`

`get_rect` renvoie la zone rectangulaire du projectile pour les collisions, tandis que `__repr__` simplifie le débogage en renvoyant l'objet au format chaîne de caractères (logique implémentée dans chaque classe).

### `ProjectileNormal` et `ProjectileFort` *(nouvelles fonctionnalités)*

Création d'un héritage avec `super()` offrant deux types de munitions aux vitesses et dégâts distincts.

# Simplification de la boucle

Le fichier `main.py` étant surchargé, nous avons implémenté un module `events.py` regroupant les fonctions de contrôle du jeu et de gestion des événements.

## `handle_events()`

Isole tous les événements déclenchés par les touches du clavier dans Pygame (notamment l'ajout des touches dédiées aux deux types de projectiles : `K_SPACE` et `K_x`).

## `update_game()`

Regroupe toutes les mises à jour des instances utilisées durant la partie, le nettoyage des projectiles sortis de l'écran et la résolution des collisions.

# `main.py`

Le fichier `main.py` contient désormais uniquement l'initialisation de Pygame, les instanciations d'objets et la régulation de la vitesse du jeu (`clock.tick(60)`). Il est allégé de toute la logique métier, désormais déportée dans des modules dédiés.

