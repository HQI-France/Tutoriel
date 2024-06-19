# Liste de Publications arXiv

Ce document présente une liste de publications arXiv avec leurs métadonnées, y compris le titre, les auteurs et le résumé.

```{code-cell} python
:tags: [hide-input]

import requests
import xml.etree.ElementTree as ET

def get_arxiv_metadata(arxiv_id):
    url = f"http://export.arxiv.org/api/query?search_query=id:{arxiv_id}"
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        entry = root.find('{http://www.w3.org/2005/Atom}entry')
        if entry:
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            authors = entry.findall('{http://www.w3.org/2005/Atom}author')
            abstract = entry.find('{http://www.w3.org/2005/Atom}summary').text
            
            author_list = [author.find('{http://www.w3.org/2005/Atom}name').text for author in authors]
            
            return {
                "title": title.strip(),
                "authors": author_list,
                "abstract": abstract.strip()
            }
    return None

# Liste de DOIs arXiv à interroger
arxiv_dois = [
    "2307.10729",
    "2307.10730",
    "2307.10731"  # Remplace ces ID par des ID arXiv réels
]

# Répertoire des métadonnées
metadata_list = []

for doi in arxiv_dois:
    metadata = get_arxiv_metadata(doi)
    if metadata:
        metadata_list.append(metadata)
    else:
        print(f"Erreur lors de la récupération des données pour {doi}")

# Afficher les résultats sous forme de tableau
for idx, metadata in enumerate(metadata_list, 1):
    print(f"Publication {idx}")
    print(f"Titre: {metadata['title']}")
    print("Auteurs:")
    for author in metadata['authors']:
        print(f"- {author}")
    print(f"Abstract: {metadata['abstract']}")
    print("\n" + "-"*50 + "\n")
