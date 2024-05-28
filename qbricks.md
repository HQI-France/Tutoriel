---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Qbricks


<img src="https://user-images.githubusercontent.com/83573296/120336791-fdbf9f00-c2f2-11eb-986b-5116dbe7bb71.png" align="right" alt="drawing" width="350"  >

[Qbricks](https://github.com/Qbricks/qbricks.github.io) est un environnement open-source pour la vérification formelle automatisée des programmes quantiques. Il permet d'écrire des programmes de construction de circuits quantiques, spécifiés avec leurs fonctions d'E/S et/ou leurs besoins en ressources. Son langage hôte, l'environnement de vérification déductive Why3, fournit une interface avec les résolveurs SMT, permettant un haut niveau d'automatisation dans la vérification des spécifications Qbricks.

```{seealso}
 Voir également l'article des auteurs de Qbricks [An Automated Deductive Verification Framework for Circuit-building Quantum Programs](https://github.com/Qbricks/qbricks.github.io/files/6414263/final--ESOP-2021.pdf)
```

## Méthode formelle

Dans de nombreux domaines critiques (nucléaire, ferroviaire...) il est nécessaire de garantir l'absence de bug dans les logiciels. Pour cela, les méthodes formelles apparaîssent comme étant des techniques efficaces permettant de raisonner logiquement sur un programme informatique, afin de démontrer la validité de ce dernier par rapport à une spécification.

## Exemple : Quantum Order-finding