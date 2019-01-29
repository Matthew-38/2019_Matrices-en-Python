# Matrix Learning (with Python)
Numpy contains some useful tools for manipulating matrices, but without looking at them*, I made my own "Matrix" class with several methods to manipulate it, with the aim of mastering Python functions like Map, and the usage of Lambda.

[Version Française en bas]

# Background
1. Recently I was chatting with my brother and I explained to him that by using mathematics in programming, I have come to understand them much better, and remember. So I had the idea to concretise my knowledge of matrices by making a Python module to manipulate them (even if it is "reinventing the wheel", as one already exists; this case is not for serious use, just to learn in both fields).
2. Lambda functions used to be rather difficult for me to get my head around. I used avoid using them and I would have difficulty understanding their use in others' code. Recently while studying Javascript, I learnt about Arrow Functions, and I realised that it is similar to Lambda in Python. So this little project allows me to get a better grasp of Lambda use, practicing the equivalent of what I learnt in Javascript.
3. To practice using Map, Reduce and Filter in Python. For the moment I have made good use of Map, but not yet the others.
4. To train myself Python good coding practices, using Pycharm which has a rather strict syntax convention suggestion system.
5. To practice a little (but not seriously) the Functional Programming paradigm by making my Matrix class immutable (which will have the side effect of making them quicker - although it means more complicated code within the class).

# Usage
This simple script needs Python 3 to run, notable because it uses the type hinting among other things. 

# Explanation
This class construcs an object in the form of a tuple of tuples. E.g.:

| R1C1 R1C2 |                 is represented as ((R1C1, R2C1), (R1C2, R2C2)).

| R2C1 R2C2 |

The current features are: addition and multiplication of matrices by matrices; addition, subtraction, multiplication and devision of matrices by a scalar; display (print); and transposing.

Printing a matrix gives the following layout:

(R1C1, R1C2

 R2C1, R2C2)

Since the matrix data are immutable, each method returns a new matrix, with the exception of Matrix.print() which just displays the matrix in the console.

I have put no license for this project, because it is just a little code which is not for serious usage. But if you want to do something with it, be my guest.

*Looking at Numpy afterwards, I noticed that their implimentation has some similarities with mine (the same idea of multi-dimentional arrays used, and a similar printing presentation).

###############################################################################################
# Version Française

# Apprentisage de Matrices
Numpy contient déjà des outils pour manipuler les matrices, mais sans les regarder, j'ai fait une Classe «Matrix» avec plusieurs methods pour la manipuler, dans le but de maitriser les fonctions Pythons telles Map et l'usage de Lambda

# Contexte
1. Récemment je discutais avec mon frère et je lui ai expliqué qu'en utilisant des conceptes mathématiques dans la programmation, je les ai beaucoup mieux compris et rétenu. Donc j'ai eu l'idée de concretiser mes connaisances de matrices avec un module Python pour les manipuler (même si c'est réinventer le roue, c'est pas pour usage serieux).
2. Les fonctions «Lambda» étaient autrefois compliqués pour moi, j'évitais de l'utiliser et j'avais du mal à les comprendre dans le code des autres. Récemment en approfondisant mes compétences en Javascript, j'ai appris les Arrow Functions, et je me suis rendu compte que c'est similaire au Lambda de Python. Donc ce petit projet me permet de concretiser l'usage de Lambda.
3. Pour pratiquer l'usage de Map, Reduce and Filter. Pour l'instant je me suis bien servi de Map, mais pas les autres.
4. Pour m'entrainer de bonnes pratiques de programmation Python
5. Pratiquer un peu (mais pas strictement) le paradigme de programmation fonctionnelle en faisant les matrices immutables (ce qui a pour conséquence de rendre plus vites leurs méthodes.

# Usage
Ce script a besoin de Python 3 parce que j'y ai mis du "Type Hinting"

# Explication
Cette classe construit un objet dans la forme d'un tuple de tuples, exemple : 

| R1C1 R1C2 |                est representé comme ((R1C1, R2C1), (R1C2, R2C2)).

| R2C1 R2C2 |

Les fonctionnalités actuelles sont : addition et multiplication des matrices par matrices ; addition, subtraction, multiplication et dévision des matrices par un scalar ; affichage (print) ; et transposer.
L'affichage «print» de la matrice ci-dessus donnerait :
(R1C1, R1C2

 R2C1, R2C2)

Comme les données des matrices sont immutables, chaque méthode retour une matrice nouvelle (Matrix), avec l'exception de Matrix.print() qui sert d'affichage dans le console.

Je ne mets pas une licence dans ce projet, car c'est juste un peu de code qui n'est pas pour usage serieux. Mais si vous voulez faire quoi qu'il soit avec, soyez libre. 

Bien que mes explications sur Github sont en français, mon code est en anglais (commentaires, noms de variables).
