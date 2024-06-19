# [Qimaera](https://github.com/zamdzhiev/Qimaera)

Qimaera est un outil de programmation expérimental pour les algorithmes quantiques, conçu pour garantir la correction et la sécurité des programmes grâce aux types dépendants et linéaires d'Idris 2. Il permet de développer des algorithmes quantiques comme QAOA et VQE en s'assurant que les qubits sont manipulés correctement et en détectant les erreurs potentielles à la compilation. Ses principales fonctionnalités incluent la préparation sécurisée des qubits, l'application d'opérations unitaires et la mesure, tout en offrant une intégration fluide entre les calculs classiques et quantiques.

```{admonition} Voir également
:class: seealso
L'article des auteurs de Qimaera : [QType-safe (Variational) Quantum Programming in
Idris](https://arxiv.org/pdf/2111.10867).
```

## Idris2

Idris2 est un langage de programmation fonctionnel avancé conçu pour offrir une vérification formelle rigoureuse grâce à aux types dépendants et linéaires. Ces types permettent de garantir la correction des programmes en vérifiant des propriétés complexes au moment de la compilation. Ce langage est particulièrement adapté aux applications nécessitant une grande fiabilité et sécurité.

```{admonition} Voir également
:class: seealso
Voir la [documentation](https://github.com/idris-lang/Idris2)
```

## Exemple : Coin toss (Pile ou face)

Dans ce tutoriel, nous allons implémenter un algorithme simple de pile ou face (Coin Toss) en utilisant Qimaera et Idris 2. L'objectif est de créer un programme qui utilise un qubit pour simuler un lancer de pièce équitable.

```Idris
module CoinToss

import Data.Vect
import QStateT
import QuantumOp
import LinearTypes
```
Après avoir importé les modules, on créé un nouveau qubit dans l'état $|0\rangle$.
Ensuite, on applique une porte de Hadamart sur celui-ci, permettant l'état $|+\rangle$.
Finalement, on mesure le qubit et on observe le résultat.

```Idris
export
coin : QuantumOp t => IO Bool
coin = do
  [b] <- run (do
           q <- newQubit {t = t}
           q <- applyH q
           r <- measure [q]
           pure r
         )
  pure b

testCoin : IO Bool
testCoin = coin {t = SimulatedOp}
```

```{note}
Vous pouvez retrouver le fichier Cointoss.idr [ici](https://github.com/zamdzhiev/Qimaera/blob/main/CoinToss.idr)
```

Alors pile, ou face ?