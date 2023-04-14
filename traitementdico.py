# -*- coding: utf-8 -*-
import json

lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open('alpha1.0.json','r') as fichier_json:
    contenu = fichier_json.read()

mots = []

mots_filtres = []

for mot in mots:
    est_valide = True
    for lettre in mot:
        if lettre.upper() not in lettres:
            est_valide = False
            break
    if est_valide:
        mots_filtres.append(mot)

# Écriture des mots filtrés dans le fichier JSON
with open('alpha1.1.json', 'w') as f:
    json.dump(mots_filtres, f)

print("Les mots filtrés ont été écrits dans le fichier trimoinscaracteres.json")
