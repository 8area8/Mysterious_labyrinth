<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>README</title>
<link rel="stylesheet" href="https://stackedit.io/res-min/themes/base.css" />
<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
</head>
<body><div class="container"><h1 id="mysterious-labyrinth">Mysterious labyrinth</h1>



<h2 id="table-des-matières">Table des matières</h2>

<p><div class="toc">
<ul>
<li><a href="#mysterious-labyrinth">Mysterious labyrinth</a><ul>
<li><a href="#table-des-matières">Table des matières</a></li>
<li><a href="#bonjour-chers-utilisateurs">Bonjour chers utilisateurs!</a></li>
<li><a href="#respect-des-consignes">Respect des consignes</a><ul>
<li><ul>
<li><a href="#control-du-robot">Control du robot</a></li>
<li><a href="#affichage-du-labyrinthe">Affichage du labyrinthe</a></li>
<li><a href="#fonctionnalités-du-jeu">Fonctionnalités du jeu</a></li>
<li><a href="#au-lancement-du-programme">Au lancement du programme</a></li>
<li><a href="#les-conditions-de-notation">Les conditions de notation</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#explications-sur-pygame">Explications sur Pygame</a><ul>
<li><ul>
<li><a href="#les-surfaces">Les surfaces</a></li>
<li><a href="#les-sprites">Les Sprites</a></li>
<li><a href="#les-événements">Les événements</a></li>
<li><a href="#les-musiques-et-le-temps">Les musiques et le temps</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#agencement-du-jeu">Agencement du jeu</a><ul>
<li><ul>
<li><a href="#le-module-data">Le module data</a></li>
<li><a href="#le-module-cartography">Le module cartography</a></li>
<li><a href="#le-module-camera">Le module camera</a></li>
<li><a href="#le-module-pathfinder">le module pathfinder</a></li>
<li><a href="#le-reste">le reste</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#contenu-du-jeu">Contenu du jeu</a></li>
<li><a href="#linstant-qui-fâche">L’instant qui fâche</a><ul>
<li><ul>
<li><a href="#cool-story-bro-mais-si-je-veux-pas-linstaller">Cool Story bro’, mais si je veux pas l’installer?</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#le-mot-de-la-fin">Le mot de la fin</a></li>
</ul>
</li>
</ul>
</div>
</p>

<hr>

<p><img src="https://lh3.googleusercontent.com/-z-iJlgOTHn0/WYHThNX3EpI/AAAAAAAAEJI/iIaPPwD2FjcZWoqWPDPq4aG5M0WWLrlSACLcBGAs/s0/ingame.jpg" alt="enter image description here" title="ingame.jpg"></p>

<hr>



<h2 id="bonjour-chers-utilisateurs">Bonjour chers utilisateurs!</h2>

<p>L’exercice donné dans le cours était déjà compliqué… Mais allez savoir pourquoi, je me suis mis des barrages en plus, en voulant en faire une application fenêtré.  </p>

<p>L’idée de base était de rendre le programme facilement <em>diffusable</em>; je me suis penché sur <strong>tkinter</strong>, module de base de python. <br>
Et… ce module m’a fait tirer les cheveux plus d’une fois, la gestion de l’espace étant pauvre à l’extrême!</p>

<p>J’ai donc finis par me pencher sur <strong>pygame</strong>, et après plus d’un mois de codage, j’arrive enfin à un résultat exploitable..!</p>

<blockquote>
  <p><strong>Note:</strong> Je reconnais que j’ai fait beaucoup plus que ce qui était demandé, et que le projet peut être incompréhensible, car il utilise des outils qui n’ont pas été abordés par le tuto. Mais j’ai voulu me faire plaisir dans cette exercice, et vous faire partager une version qui sort de l’ordinaire (et qui peut être vous donnera envie de vous plonger dans pygame).</p>
</blockquote>

<hr>



<h2 id="respect-des-consignes">Respect des consignes</h2>

<p>Je vais rapidement vous passer les spécificités du jeu, en rapport avec les consignes données par l’exercice. L’application étant fenêtré, certaines choses ont dus être faites sous un angle différent.</p>



<h4 id="control-du-robot">Control du robot</h4>

<p>Les contrôles de base étaient simples; avancer à gauche, à droite, haut et bas une ou plusieurs fois. J’ai pour le coup un peu dévié de la demande, en intégrant un système de pathfinding plus recherché.  </p>

<p>Si vous connaissez Dofus et Wakfu, le système est le même. Le personnage possède des points de mouvements, qui détermine son déplacement maximal. <br>
Il peut ensuite se déplacer dans un rayon de cases tout autour de lui, en empruntant un chemin déterminé:  </p>

<ul>
<li>par la souris (en faisant glisser la souris de la case du héros jusqu’à la case voulue)  </li>
<li>par un système de recherche automatique, qui va déterminer les cases possibles, et le chemin à afficher si la souris pointe sur une case possible.</li>
</ul>

<blockquote>
  <p><strong>Note:</strong> L’alliance des deux est d’ailleurs possible; après avoir déterminé un chemin avec la recherche automatique, on peut modifier ce chemin en glissant de case en case avec la souris.</p>
</blockquote>

<p><img src="https://lh3.googleusercontent.com/-KHra8Oy0Z9w/WYHVWk7JbFI/AAAAAAAAEJY/pBN-4yvXp_4Jpe5-ayZ8G2OiGPpjUztYwCLcBGAs/s0/Sans+titre-1.jpg" alt="enter image description here" title="movement.jpg"></p>

<ul>
<li><em>Le jeu trouve un chemin depuis le curseur de la souris, et par glissement de souris, on enlève ou ajoute une case…</em></li>
</ul>



<h4 id="affichage-du-labyrinthe">Affichage du labyrinthe</h4>

<p>J’ai repris les cartes fournies dans l’énoncé; et j’ai crée un affichage vue de dessus en associant chaque symbole à des images. Tout est respecté, c’est assez classique.</p>

<blockquote>
  <p><strong>Note</strong> Un menu est aussi présent, pour effectuer certaines actions (la plupart des boutons présents dans le menus ne sont pas encore implémentés).</p>
</blockquote>



<h4 id="fonctionnalités-du-jeu">Fonctionnalités du jeu</h4>

<p>Le jeu enregistre automatiquement la partie et ce en permanence (oui je sais, c’est pas très opti!). <br>
J’ai d’ailleurs fait quelques modification pour améliorer les performances, il n’enregistre plus que… 30 fois par secondes (c’est énorme je sais)… Contre un nombre bien plus important avant. Point à modérer malgré tout: les données à enregistrer sont minimes (le personnage, et le nom de la map).</p>

<p>Les cartes sont au nombre de deux, ce sont celles fournies par l’exercice. Je ne les ais pas modifiés, et vous pouvez en rajouter autant que vous voulez. <br>
Attention par contre, deux points à prendre en compte:</p>

<ul>
<li>J’ai pas fini d’implémenter le menu de <strong>sélection de niveaux</strong>. Ce menu montre les cinq premières cartes, et doit ensuite permettre via des flèches un défilement vers la droite ou la gauche, comme si on lisait un livre. Et bah, ces flèches n’existent pas encore. :) Vous n’aurez donc que les 5 premières cartes de dispo.</li>
<li>Si vous créer une carte, il existe un calcul que je n’ai pas revu encore, lors de la génération de la carte. Il spécifie la largeur de la map selon la première ligne de symboles. Donc faites en sorte que votre première ligne soit aussi large ou plus large que les autres (sinon votre map sera coupé).</li>
<li>Ah quand même, dernier point: je vous conseille dans tout les cas, de faire une map au moins aussi large et longue que la carte ‘facile’ donné par l’exercice, et de ne pas trop tenter de différer la largeur entre chaque ligne: je ne sais pas si mon module <em>caméra</em> appréciera (encore du code à revoir)! :D</li>
</ul>



<h4 id="au-lancement-du-programme">Au lancement du programme</h4>

<p>On nous propose de commencer une partie, d’en charger une ou de quitter le jeu. <br>
Le bouton <strong>charger une partie</strong> se grise s’il n’y a aucune partie à charger (obvious). <br>
C’est ma façon de proposer de rejouer une partie, sans l’utilisation de texte, juste par l’aspect visuel.</p>

<p><img src="https://lh3.googleusercontent.com/-2U5hkf41AZg/WYHZJRwHVjI/AAAAAAAAEJw/cGxmN0equckcFM1x-WvvhYqUSgp3Q1gXACLcBGAs/s0/chargerpartie.jpg" alt="enter image description here" title="chargerpartie.jpg"></p>



<h4 id="les-conditions-de-notation">Les conditions de notation</h4>

<ul>
<li>Le programme fonctionne en le lançant. Il y a cependant le <strong>principale problème</strong> de ma version, que j’explique à la fin de ce document dans la partie <strong>l’instant qui fâche</strong>.</li>
<li>le code est lisible; j’ai dus réécrire tout le système une seconde fois en délimitant bien chaque partie dans différents fichiers. Les conventions de nommages python sont respectés. Cependant vous remarquerez que je nomme mes classes/variables en <strong>anglais</strong>. Ecrire en anglais est une bonne habitude à prendre en programmation, même pour moi qui n’aime pas cette langue.</li>
<li>Le projet est découpé en plein de fichiers différents. Certains ne contiennent presque rien, mais permettent une évolutivité importante. Seul petit point: j’aurai peut être dus départager la partie qui met à jour les éléments, de la partie qui dessine les éléments. Et dans la même veine, certains événements ne sont en fait que des mises à jours (genre de chose qu’on se rend compte avec le temps).</li>
<li>Le projet est souvent documenté (et cette fois ci, en <strong>français</strong>); j’essai d’être le plus concis possible (tout en étant claire): trop de documentation nuit à la lisibilité du code.</li>
<li>pour ce qui est de l’ouverture à l’amélioration: j’ai découpé mon projet en pleins de parties différentes, que j’ai essayé au maximum de rendre indépendantes. Cela m’a permit d’enlever et rajouter facilement des éléments, et pour la suite ça me permettra de modifier le projet à mon aise.</li>
<li>Petit point de fin; j’ai voulu faire quelque chose des portes, elle ‘s’allument’ et font un son quand le personnage passe dessus.</li>
</ul>

<hr>



<h2 id="explications-sur-pygame">Explications sur Pygame</h2>

<p>Alors, pygame est un gros module qui crée des applications fenêtrés, avec gestion des images, du son, de l’animation, des événements…Il est parfait pour faire des petits jeux. Ma connaissance en la matière n’est <strong>clairement pas exhaustive</strong>, j’ai appris sur le tas et je continus d’apprendre, je peux cependant vous donner une vision d’ensemble, et mieux vous faire comprendre mon petit jeu.</p>

<p>Comme la plupart des modules d’applications fenêtré, pygame repose sur <strong>une boucle qui tourne en permanence lorsque le programme est ouvert</strong>. <br>
Dans cette boucle, on aura dans l’ordre:</p>

<ul>
<li>L’appel des différents événements (appuie sur une touche, clic de souris…) et des méthodes qui les utilisent.</li>
<li>La mise à jours des différents éléments du jeu (on change leur positions sur les images).</li>
<li>Le dessin des différents éléments  du jeu(on ‘colle’ les images à l’écran).</li>
<li>Puis un rafraîchissement global du jeu (méthode <em>pygame.display.flip()</em>).</li>
</ul>

<p>A cela s’ajoute une variable de temps, qui va contrôler le nombre d’images par seconde (FPS).</p>



<h4 id="les-surfaces">Les surfaces</h4>

<p>pygame utilise des ‘surfaces’, qui sont des sortes de conteneurs d’images, sur lesquels on colle un peu tout ce qu’on veut. Chaque surface sera collé en définitive à l’écran principal, celui qui affiche tout (qui est définit par <em>pygame.display.set_mode(size)</em>).</p>



<div class="flow-chart"><svg height="229.171875" version="1.1" width="119.515625" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="overflow: hidden; position: relative; left: -0.1px; top: -0.75px;"><desc style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Created with Raphaël 2.1.2</desc><defs style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><marker id="raphael-marker-endblock33-obj230" markerHeight="3" markerWidth="3" orient="auto" refX="1.5" refY="1.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 1.5 1.5) scale(0.6,0.6)" stroke-width="1.6667" fill="black" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker><marker id="raphael-marker-endblock33-obj231" markerHeight="3" markerWidth="3" orient="auto" refX="1.5" refY="1.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 1.5 1.5) scale(0.6,0.6)" stroke-width="1.6667" fill="black" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker></defs><rect x="0" y="0" width="104.921875" height="38.390625" rx="0" ry="0" fill="#ffffff" stroke="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" stroke-width="2" class="flowchart" id="op" transform="matrix(1,0,0,1,8.2969,4)"></rect><text x="10" y="19.1953125" text-anchor="start" font-family="sans-serif" font-size="14px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: sans-serif; font-size: 14px; font-weight: normal;" id="opt" class="flowchartt" font-weight="normal" transform="matrix(1,0,0,1,8.2969,4)"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">petite surface</tspan></text><rect x="0" y="0" width="112.1875" height="38.390625" rx="0" ry="0" fill="#ffffff" stroke="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" stroke-width="2" class="flowchart" id="op2" transform="matrix(1,0,0,1,4.6641,96.3906)"></rect><text x="10" y="19.1953125" text-anchor="start" font-family="sans-serif" font-size="14px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: sans-serif; font-size: 14px; font-weight: normal;" id="op2t" class="flowchartt" font-weight="normal" transform="matrix(1,0,0,1,4.6641,96.3906)"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">grande surface</tspan></text><rect x="0" y="0" width="113.515625" height="38.390625" rx="0" ry="0" fill="#ffffff" stroke="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" stroke-width="2" class="flowchart" id="op3" transform="matrix(1,0,0,1,4,188.7813)"></rect><text x="10" y="19.1953125" text-anchor="start" font-family="sans-serif" font-size="14px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: start; font-family: sans-serif; font-size: 14px; font-weight: normal;" id="op3t" class="flowchartt" font-weight="normal" transform="matrix(1,0,0,1,4,188.7813)"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">écran principal</tspan><tspan dy="18" x="10" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></tspan></text><path fill="none" stroke="#000000" d="M60.7578125,42.390625C60.7578125,42.390625,60.7578125,82.04472494125366,60.7578125,93.39106408460066" stroke-width="2" marker-end="url(#raphael-marker-endblock33-obj230)" font-family="sans-serif" font-weight="normal" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); font-family: sans-serif; font-weight: normal;"></path><path fill="none" stroke="#000000" d="M60.7578125,134.78125C60.7578125,134.78125,60.7578125,174.43534994125366,60.7578125,185.78168908460066" stroke-width="2" marker-end="url(#raphael-marker-endblock33-obj231)" font-family="sans-serif" font-weight="normal" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); font-family: sans-serif; font-weight: normal;"></path></svg></div>

<p>Dans mon projet, j’ai un module ‘surface’ qui comprend pratiquement toutes les images de mon jeu, pour les différents moments du jeu (menu et ingame). <br>
Je pioche ensuite ces images (qui sont de petites surfaces) à l’appel des classes correspondantes, pour les coller à des surfaces plus grandes.</p>



<h4 id="les-sprites">Les Sprites</h4>

<p>Chacune des images  crée utilise d’autres modules crées par mes soins, qui sont <em>pygame_extend</em>, et <em>pygame_xtd_entity</em>, pour le personnage principale.</p>

<p>Les classes de ce module héritent de la classe <strong>Sprite</strong> de pygame, une classe qui gère les différentes images et qui permet de les regrouper facilement dans des ‘groupes’ conçus pour, de les mettre à jour, et les dessiner à l’écran.</p>

<blockquote>
  <p><strong>note</strong>: on utilise donc une variable de type <em>pygame.sprite.Group()</em>. Cette variable <br>
  met à jour tout les sprites contenus avec la méthode <strong>update()</strong>, et les dessine avec la méthode <strong>draw()</strong>.</p>
</blockquote>

<p><em>pygame_extend</em> et <em>pygame_xtd_entity</em> sont un aspect technique du programme et assez bas niveau (on doit définir beaucoup de choses pour un résultat simple), c’est donc certainement chiant à lire. :) <br>
Ils me permettent la création d’images simples, de boutons, d’images animés…</p>



<h4 id="les-événements">Les événements</h4>

<p>Ils sont appelés lors de la boucle principale du jeu. J’utilise ensuite une méthode <em>events()</em> dans mes classes de menus et du jeu, qui va prendre l’événements courant et le tester en fonction des méthodes implémentés.</p>

<p>Un module <em>events.py</em> a aussi été crée; il est instancié dans mes classes de menus et de jeu (qu’elles appelleront ensuite via leur méthode <em>event</em>). Il permet une meilleure répartition du code.</p>



<h4 id="les-musiques-et-le-temps">Les musiques et le temps</h4>

<p>C’est très peu documenté car j’en fais une application très simple (encore plus pour le temps), et qu’ils restent assez évidents à lire. <br>
J’ai crée un module <em>musics.py</em> par soucis d’organisation, instancié aussi lors de l’appel des classes principales.</p>

<hr>



<h2 id="agencement-du-jeu">Agencement du jeu</h2>

<p>Bon, là on rentre dans le gros du travail.</p>

<p>Concrètement, je démarre par le fichier <em>roboc.py</em> (comme demandé), qui instancie pygame et la boucle du jeu, dans le fichier <em>loop.py</em></p>

<p>La classe Loop va instancier une variable, <em>self.active_screen</em>, qui contiendra les différentes classes de menus et du jeu. Lors de l’instanciation, la variable appel directement le menus d’écran titre.</p>



<div class="sequence-diagram"><svg height="280.34375" version="1.1" width="478.1953125" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="overflow: hidden; position: relative; left: -0.6px; top: -0.3625px;"><desc style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Created with Raphaël 2.1.2</desc><defs style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><marker id="raphael-marker-endblock55-obj157" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker><marker id="raphael-marker-endblock55-obj160" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker><marker id="raphael-marker-endblock55-obj163" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker></defs><rect x="10" y="10" width="209.6875" height="28.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="15.046875" y="15" width="199.6875" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="114.84375" y="24.1953125" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">active_screen: valeurs possibles</tspan></text><rect x="10" y="48.390625" width="106.15625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="19.984375" y="58.390625" width="86.15625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="63.078125" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">active_screen</tspan></text><rect x="10" y="221.953125" width="106.15625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="19.984375" y="231.953125" width="86.15625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="63.078125" y="241.1484375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">active_screen</tspan></text><path fill="none" stroke="#000000" d="M63.078125,86.78125L63.078125,221.953125" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="150.1796875" y="48.390625" width="91.859375" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="160.171875" y="58.390625" width="71.859375" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="196.109375" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">TitleMenu()</tspan></text><rect x="150.1796875" y="221.953125" width="91.859375" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="160.171875" y="231.953125" width="71.859375" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="196.109375" y="241.1484375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">TitleMenu()</tspan></text><path fill="none" stroke="#000000" d="M196.109375,86.78125L196.109375,221.953125" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="262.0390625" y="48.390625" width="100.390625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="272.03125" y="58.390625" width="80.390625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="312.234375" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">SelectLevel()</tspan></text><rect x="262.0390625" y="221.953125" width="100.390625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="272.03125" y="231.953125" width="80.390625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="312.234375" y="241.1484375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">SelectLevel()</tspan></text><path fill="none" stroke="#000000" d="M312.234375,86.78125L312.234375,221.953125" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="382.4296875" y="48.390625" width="65.765625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="392.421875" y="58.390625" width="45.765625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="415.3125" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Game()</tspan></text><rect x="382.4296875" y="221.953125" width="65.765625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="392.421875" y="231.953125" width="45.765625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="415.3125" y="241.1484375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Game()</tspan></text><path fill="none" stroke="#000000" d="M415.3125,86.78125L415.3125,221.953125" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="73.15625" y="102.578125" width="113.03125" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="129.59375" y="111.78125" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.1953125">module menus.py</tspan></text><path fill="none" stroke="#000000" d="M63.078125,125.171875C63.078125,125.171875,166.92918701656163,125.171875,191.11715409756744,125.171875" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj157)" stroke-dasharray="6,2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="131.21875" y="140.96875" width="113.03125" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="187.65625" y="150.171875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.1953125">module menus.py</tspan></text><path fill="none" stroke="#000000" d="M63.078125,163.5625C63.078125,163.5625,272.02987758256495,163.5625,307.22926949710836,163.5625" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj160)" stroke-dasharray="6,2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="186.65625" y="179.359375" width="105.265625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="239.1953125" y="188.5625" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.1953125">module game.py</tspan></text><path fill="none" stroke="#000000" d="M63.078125,201.953125C63.078125,201.953125,367.4409911369439,201.953125,410.3163265278171,201.953125" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj163)" stroke-dasharray="6,2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path></svg></div>

<p>Ensuite vient la boucle. Cette boucle teste les événements de la variable <em>self.active_screen</em>,  et met à jour <em>self.active_screen</em> en permanence.</p>

<p>Voici ce qu’il se passe lorsque la variable self.active_screen prend la classe <strong>Game</strong> en valeur:</p>



<div class="sequence-diagram"><svg height="263.5625" version="1.1" width="640.84375" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="overflow: hidden; position: relative; left: -0.6px; top: -0.9625px;"><desc style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Created with Raphaël 2.1.2</desc><defs style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><marker id="raphael-marker-endblock55-obj214" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker><marker id="raphael-marker-endblock55-obj217" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker><marker id="raphael-marker-endblock55-obj220" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker><marker id="raphael-marker-endblock55-obj223" markerHeight="5" markerWidth="5" orient="auto" refX="2.5" refY="2.5" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#raphael-marker-block" transform="rotate(180 2.5 2.5) scale(1,1)" stroke-width="1.0000" fill="#000" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></use></marker></defs><rect x="10" y="10" width="129.625" height="28.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="14.640625" y="15" width="119.625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="74.8125" y="24.1953125" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Appel des modules</tspan></text><rect x="10" y="48.390625" width="106.15625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="19.984375" y="58.390625" width="86.15625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="63.078125" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">active_screen</tspan></text><rect x="10" y="205.171875" width="106.15625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="19.984375" y="215.171875" width="86.15625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="63.078125" y="224.3671875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">active_screen</tspan></text><path fill="none" stroke="#000000" d="M63.078125,86.78125L63.078125,205.171875" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="148.65625" y="48.390625" width="56.6875" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="158.640625" y="58.390625" width="36.6875" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="177" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Game</tspan></text><rect x="148.65625" y="205.171875" width="56.6875" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="158.640625" y="215.171875" width="36.6875" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="177" y="224.3671875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Game</tspan></text><path fill="none" stroke="#000000" d="M177,86.78125L177,205.171875" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="225.34375" y="48.390625" width="111.671875" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="235.328125" y="58.390625" width="91.671875" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="281.1796875" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Musics.Game()</tspan></text><rect x="225.34375" y="205.171875" width="111.671875" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="235.328125" y="215.171875" width="91.671875" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="281.1796875" y="224.3671875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Musics.Game()</tspan></text><path fill="none" stroke="#000000" d="M281.1796875,86.78125L281.1796875,205.171875" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="357.015625" y="48.390625" width="122.765625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="367" y="58.390625" width="102.765625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="418.3984375" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Surfaces.Game()</tspan></text><rect x="357.015625" y="205.171875" width="122.765625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="367" y="215.171875" width="102.765625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="418.3984375" y="224.3671875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Surfaces.Game()</tspan></text><path fill="none" stroke="#000000" d="M418.3984375,86.78125L418.3984375,205.171875" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="499.78125" y="48.390625" width="111.0625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="509.765625" y="58.390625" width="91.0625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="555.3125" y="67.5859375" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Events.Game()</tspan></text><rect x="499.78125" y="205.171875" width="111.0625" height="38.390625" rx="0" ry="0" fill="none" stroke="#000000" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><rect x="509.765625" y="215.171875" width="91.0625" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="555.3125" y="224.3671875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.203125">Events.Game()</tspan></text><path fill="none" stroke="#000000" d="M555.3125,86.78125L555.3125,205.171875" stroke-width="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="73.0625" y="102.578125" width="93.921875" height="18.390625" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="120.0390625" y="111.78125" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.1953125">appel de Game</tspan></text><path fill="none" stroke="#000000" d="M63.078125,125.171875C63.078125,125.171875,150.00776894018054,125.171875,171.99485661645667,125.171875" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj214)" stroke-dasharray="0" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="0" y="0" width="0" height="0" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="229.08984375" y="150.171875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="150.171875"></tspan></text><path fill="none" stroke="#000000" d="M177,145.171875C177,145.171875,255.38871936080977,145.171875,276.1724471991495,145.171875" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj217)" stroke-dasharray="6,2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="0" y="0" width="0" height="0" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="297.69921875" y="170.171875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="170.171875"></tspan></text><path fill="none" stroke="#000000" d="M177,165.171875C177,165.171875,378.85251345613506,165.171875,413.39807301002924,165.171875" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj220)" stroke-dasharray="6,2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path><rect x="0" y="0" width="0" height="0" rx="0" ry="0" fill="#ffffff" stroke="none" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect><text x="366.15625" y="190.171875" text-anchor="middle" font-family="Andale Mono, monospace" font-size="16px" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-family: &quot;Andale Mono&quot;, monospace; font-size: 16px;"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="190.171875"></tspan></text><path fill="none" stroke="#000000" d="M177,185.171875C177,185.171875,505.70222468674183,185.171875,550.3209837018367,185.171875" stroke-width="2" marker-end="url(#raphael-marker-endblock55-obj223)" stroke-dasharray="6,2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path></svg></div>

<p>Comme j’ai compartimenté la plupart des éléments dans des fichiers séparés, Game va aller chercher ces fichiers un à un.</p>

<p>Mais Game, contrairement aux autres classes principales qui gèrent les menus, va instancier en plus d’autres modules, complexes (<em>cartography.py</em>, <em>camera.py</em> et pathfinder.py), et moins complexes (<em>entity.py</em>, <em>case_entity.py</em>).</p>

<p>Nous allons d’ailleurs voir les modules particuliers au jeu.</p>



<h4 id="le-module-data">Le module data</h4>

<p>Ce premier module est relativement simple; il permet d’importer les noms de fichiers de cartes pour le menu de sélection de niveau, et de gérer les sauvegardes de données lors du lancement du jeu.</p>

<p>Il crée aussi un liste des symboles contenus dans la carte choisie. Cette liste sera utilisé par la module <em>cartography.py</em></p>



<h4 id="le-module-cartography">Le module cartography</h4>

<p>Appelé dans la classe Game, la classe Map de ce module se charge de créer la carte du jeu (et le héro par la même occasion).</p>

<p>Elle a besoin pour cela, du nom de la carte choisie. Avec ce nom, elle appel la méthode du module <em>data.py</em>, qui renvoi une liste contenant tout les symboles de la carte choisie. <br>
Après, la classe va créer un dictionnaire avec comme clés, les coordonnées, et comme valeurs, les objets correspondant aux symboles associés.</p>

<p>exemple:</p>

<ul>
<li>coordonnées[0, 0] = mur</li>
<li>coordonnées[1, 1] = chemin</li>
</ul>

<p>Ces objets sont définis dans le module <em>case_entity.py</em>, et contiennent simplement une variable d’image (leur apparence dans le jeu), leur coordonnée, et un booléen solid, qui permet de tester si le personnage peut passer dessus ou non.</p>

<blockquote>
  <p><strong>note</strong>: le héro est crée dans cette classe, de la même manière que les autres objets (avec le module <em>entity.py</em>).</p>
</blockquote>



<h4 id="le-module-camera">Le module camera</h4>

<p>Ce module, appelé dans la classe Game après le module cartography, définit une surface qui va englober la carte du jeu, et la déplacer selon diverses méthodes.</p>

<p>Le principe, simple, consiste à afficher la carte à différentes positions de l’écran (qui est représenté par la surface caméra).</p>

<p>La caméra permet de bouger la carte via un clic droit de la souris enfoncé (méthode définit dans <em>events.Game</em>), et de suivre le personnage, quand ce dernier bouge.</p>

<blockquote>
  <p><strong>note</strong>: La caméra évite aussi de pouvoir <em>sortir</em> de la carte</p>
</blockquote>



<h4 id="le-module-pathfinder">le module pathfinder</h4>

<p>Celui qui m’a prit le plus la tête.</p>

<p>Basiquement, et comme expliqué plus tôt, la classe PathController est appelé dans les événements de Game, et fait un calcul en fonction de la position de la souris.</p>

<p>Ce calcul détermine si un chemin est possible depuis le héro jusqu’à la souris.</p>

<p>La classe DisplayPath se contente d’afficher le chemin, s’il y en a un.</p>

<p>Enfin, Game possède un événements qui se charge de faire bouger le héro si on clique sur un chemin.</p>

<blockquote>
  <p><strong>note</strong>: changer la valeur de la variable <em>moves_point</em> de la classe Hero (présente dans <em>entity.py</em>) changera les possibilités de déplacement (plus de case ou moins de cases possibles)</p>
</blockquote>



<h4 id="le-reste">le reste</h4>

<p>J’ai développé chacun des fichiers présents dans le dossier du jeu, et vous devriez avoir une vision global du code maintenant.</p>

<p>Je ne détail pas la classe du personnage, car je la trouve simple; seul le mouvement serait intéressant à expliquer, mais il faut juste retenir que dans un jeu, chaque mouvement se fait en parallèle d’un autre; et pour y parvenir, on doit faire bouger chaque chose une à une petit à petit, frame par frame, image par image.</p>

<hr>



<h2 id="contenu-du-jeu">Contenu du jeu</h2>

<p>Je ne vais pas m’attarder plus, mais une fois dans le jeu:</p>

<ul>
<li>Vous pouvez déplacer la caméra avec un clic gauche enfoncé de la souris.</li>
<li>vous avez une croix en haut à droite de l’écran, qui affichera un petit écran qui vous proposera de revenir au menu principal.</li>
<li>vous pouvez cliquer sur une case ‘verte’ (un chemin), pour faire bouger le héro jusqu’à cette case.</li>
<li>enfin, si vous atteignez la carte, vous aurez une animation de victoire. Cliquez n’importe où pour revenir à l’écran titre.</li>
</ul>

<p>par contre:</p>

<ul>
<li>le menu du bas est purement décoratif à l’heure actuelle. Vous avez cependant les coordonnées de la souris qui s’affichent en bas à gauche en continue.</li>
</ul>



<h2 id="linstant-qui-fâche">L’instant qui fâche</h2>

<p>Et voici venu l’instant qui fâche! ‘<em>cris et sifflements</em>’</p>

<p>Utilisant une bibliothèque qui n’est pas native à python, j’ai dus la télécharger sur le site officiel. Je pensais me dépatouiller avec cx_freeze, qui transforme l’application en un executable. Seulement deux choses:</p>

<ol>
<li>j’arrive pas à l’installer (‘ouh le nul!’).</li>
<li>et ça m’a pas plus donné envie de résoudre le premier problème, quand j’ai su qu’il ne compilais pas directement le programme sur toutes les plateformes, mais seulement sur la plateforme actuelle (donc amis MAC et LINUX, pas de chance pour vous…!)</li>
</ol>

<p>Alors je me suis simplement dis que vous l’installerez, puisqu’en tant qu’apprentis programmeurs comme moi, vous devriez y arriver dans trop de problèmes.</p>

<p>Voici le lien qui vous permettra d’installer pygame: <br>
<a href="http://www.pygame.org/wiki/GettingStarted#Pygame">http://www.pygame.org/wiki/GettingStarted#Pygame</a></p>

<p>J’ai programmé le jeu en python 3 (version 3.2 pour être exact, mais ça ne devrait pas du tout importer). Faites juste attention, si vous avez plusieurs versions de python (l’enfer pythonien), d’appeler celle qui contient la librairie pygame (peut être aurez vous aucun problèmes, contrairement à moi). :)</p>



<h4 id="cool-story-bro-mais-si-je-veux-pas-linstaller">Cool Story bro’, mais si je veux pas l’installer?</h4>

<p>Ah, là j’oblige personne. Je vous ai donné du travail supplémentaire pour un exercice normalement simple à corriger, et je m’en excuse… <br>
Si vous ne voulez pas vous embêter à télécharger pygame, corrigez sans tester et mettez la note que vous voulez.</p>

<hr>



<h2 id="le-mot-de-la-fin">Le mot de la fin</h2>

<p>Si vous êtes arrivés jusqu’ici sans sauter de parties, je vous félicite! Un pavé pareil pour une simple correction, c’était pas donné d’avance.</p>

<p>Merci d’avance si vous prenez le temps de télécharger pygame, et merci dans tout les cas pour la correction. :)</p>

<p>-Mikael B.</p>

<blockquote>
  <p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote></div></body>
</html>