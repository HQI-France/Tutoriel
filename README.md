# Github repository of the HQI Program ![image](/docs/image/logo.jpg)

Please access the page [here](https://hqi-france.github.io/Tutoriel/)

## The pages are generated using jupyter-book and Github pages

To update the page, first install [Jupyter-Book](https://pypi.org/project/jupyter-book/) and [GitHub Pages Import](https://pypi.org/project/ghp-import/).

Then clone the repository localy, you can modify files.
Once you finished, build the HTMLs files with

```batch
jb build ./docs
```
or 

```batch
jb build --all ./docs
```
for deep modification (yaml file, new pages...)

Look at the result by opening one of the pages and navigate in ./docs/_build/html

To publish online, use ghp-import

```batch
ghp-import -n -p -f _build/html
```

# How to contribute

If you are a part of the program, you can freely modify pages, add tutorial, create your own page or the page of your project.

