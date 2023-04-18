import json
import unicodedata


def dicoCreate(nomfichier):
    # Ouvre le fichier contenant les caractères
    with open(nomfichier, 'r', encoding='utf-8') as f:
        characters = f.readlines()

    # Enlève les espaces et les retours à la ligne
    characters = [c.strip() for c in characters]

    # Met les mots en majuscule et enlève les accents
    characters = [unicodedata.normalize('NFKD', c).encode('ASCII', 'ignore').decode('utf-8').upper() for c in characters]

    # Écrit la liste de caractères dans le fichier JSON
    with open('alpha1.2.json', 'w') as f:
        json.dump(characters, f, ensure_ascii=False, indent=4)

def fusionner_dictionnaires(nom_fichier1, nom_fichier2, nom_fichier_resultat):
    
    with open(nom_fichier1, 'r') as fichier1:
        dict1 = set(fichier1.read().splitlines())
    
    with open(nom_fichier2, 'r') as fichier2:
        dict2 = set(fichier2.read().splitlines())
    fusion = dict1.union(dict2)
    
    with open(nom_fichier_resultat, 'w') as fichier_resultat:
        for mot in fusion:
            fichier_resultat.write(mot+'\n')


if __name__ == '__main__':
    fusionner_dictionnaires('alpha1.1.json', 'alpha1.2.json', 'alpha1.3.json')