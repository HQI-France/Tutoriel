# [Qimaera](https://github.com/zamdzhiev/Qimaera)

Qimaera est un outil expérimental de programmation pour les algorithmes quantiques. En tant que proof-of-concept, il démontre qu'il est possible de réaliser une programmation hybride classique-quantique sécurisée avec Idris2. Tout cela est rendu possible grâce à l'utilisation des types dépendants et des types linéaires. 

```{admonition} Les types
:class: note
Un <i>type</i> est la nature de valeurs que peut prendre une donnée : booléen, entiers, réels par exemple. Ainsi, un <i>type dépendant</i> est un type qui change selon la valeurs de certains paramètres. Un <i>type linéaire</i> est un type qui admet des propriétés de linéarité comme le principe de non duplication, qui ici, assure le respect des lois de la physique quantique.
```
Ce projet permet alors la correction et la sécurité des programmes hybride, illustrant que l'on peut manipuler les qubits de manière sécurisée et détecter les erreurs potentielles à la compilation.

```{admonition} Voir également
:class: seealso
L'article des auteurs de Qimaera : [QType-safe (Variational) Quantum Programming in
Idris](https://arxiv.org/pdf/2111.10867), ainsi que le répertoire [Github](https://github.com/zamdzhiev/Qimaera)
```

## Idris2

Idris2 est un langage de programmation fonctionnel avancé conçu pour offrir une vérification formelle rigoureuse grâce à aux types dépendants et linéaires. Comme expliqué précedemment, ces types permettent de garantir la correction des programmes en vérifiant des propriétés complexes au moment de la compilation. Idris2 est particulièrement adapté aux applications nécessitant une grande fiabilité et sécurité.

```{admonition} Voir également
:class: seealso
Voir la [documentation](https://github.com/idris-lang/Idris2)
```

## Exemple : Coin toss (Pile ou face)

Dans ce tutoriel, nous allons implémenter un algorithme simple de pile ou face (Coin Toss) en utilisant Qimaera et Idris 2. L'objectif est de créer un programme qui utilise un qubit et y applique une porte d'Hadamard, pour simuler un lancer de pièce équitable (résultat supposé à 50/50 sur les deux états possibles).

```Idris
module CoinToss

import Data.Vect
import QStateT
import QuantumOp
import LinearTypes
```
Après avoir importé les modules, on créé un nouveau qubit dans l'état 
Ensuite, on applique une porte de Hadamart sur celui-ci, permettant l'état $|+\rangle$.
Finalement, on mesure le qubit et on observe le résultat.

```Idris
export
coin : QuantumOp t => IO Bool
```
Nous venons de définir notre coin, comme un booléen.

```Idris
coin = do
  [b] <- run (do
           q <- newQubit {t = t}
           q <- applyH q
           r <- measure [q]
           pure r
         )
  pure b
```
Nous initions le qubit dans l'état $|0\rangle$ et nous appliquons une porte de Hadamard _applyH_. Puis, nous mesurons son état et retournont un booléen.

```Idris
testCoin : IO Bool
testCoin = coin {t = SimulatedOp}
```
Nous pouvons maintenant exécuter la fonction.

```{note}
Vous pouvez retrouver le fichier Cointoss.idr [ici](https://github.com/zamdzhiev/Qimaera/blob/main/CoinToss.idr)
```

Alors pile, ou face ?