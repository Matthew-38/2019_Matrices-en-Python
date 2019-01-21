# Apprentisage de Matrices
Numpy contient déjà des utiles pour manipuler les matrices, mais sans les regarder, j'ai fait une Classe «Matrix» avec plusieurs methods pour la manipuler, dans le but de maitriser les fonctions Pythons telles Map et l'usage de Lambda

# Contexte
1. Récemment je discutais avec mon frère et je lui ai expliqué qu'en utilisant des conceptes mathématiques dans la programmation, je les ai beaucoup mieux compris et rétenu. Donc j'ai eu l'idée de concretiser mes connaisances de matrices avec un module Python pour les manipuler (même si c'est réinventer le roue, c'est pas pour usage serieux).
2. Les fonctions «Lambda» étaient autrefois compliqués pour moi, j'évitais de l'utiliser et j'avais du mal à les comprendre dans le code des autres. Récemment en approfondisant mes compétences en Javascript, j'ai appris les Arrow Functions, et je me suis rendu compte que c'est similaire au Lambda de Python. Donc ce petit projet me permet de concretiser l'usage de Lambda.
3. Pour pratiquer l'usage de Map, Reduce and Filter. Pour l'instant je me suis bien servi de Map, mais pas les autres.
4. Pour m'entrainer de bonnes pratiques de programmation Python
5. Pratiquer un peu (mais pas strictement) le paradigme de programmation fonctionnelle en faisant les matrices immutables (ce qui a pour conséquence de rendre plus vites leurs méthodes.

# Explication
Cette classe construit un objet dans la forme d'un tuple de tuples, exemple : 
| R1C1 R1C2 |  est representé comme ((R1C1, R2C1), (R1C2, R2C2)).
| R2C1 R2C2 |
Les fonctionnalités actuelles sont : addition et multiplication des matrices par matrices ; addition, subtraction, multiplication et dévision des matrices par un scalar ; affichage (print) ; et inverser (invert)
L'affichage «print» de la matrice ci-dessus donnerait :
(R1C1, R1C2
 R2C1, R2C2)

Comme les données des matrices sont immutables, chaque méthode retour une matrice nouvelle (Matrix), avec l'exception de Matrix.print() qui sert d'affichage dans le console.

Je ne mets pas une licence dans ce projet, car c'est juste un peu de code qui n'est pas pour usage serieux. Mais si vous voulez faire quoi qu'il soit avec, soyez libre. 

Bien que mes explications sur Github sont en français, mon code est en anglais (commentaires, noms de variables).
