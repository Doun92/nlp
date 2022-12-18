# Imports
import json
import nltk

# Variables
titre = 'Incipit'

data_directory = 'C:\\Users\\Maintenant Pret\\OneDrive\\Bureau\\Data\\'
folder_genre = 'Poésie\\'
folder_auteur = 'Escoval\\'
folder_oeuvre = 'Dans un abîme de béton\\'
name_file = f'{titre}.txt'

textes_secondaires = f'{data_directory}traitements_secondaires\\'

ponctuation = ",;:.()[]{}`´!?‘-"

# Functions
# Create a dictionnary, key = number of line, value = line
def numéroter_lignes(lignes):
    num_ligne = 1
    poème_id = {}
    for ligne in lignes:
        if ligne != '':
            poème_id[num_ligne] = ligne
            num_ligne += 1
    return poème_id

# Create a json file from the json file
def création_json(titre, dictionnaire, lignes):
    objet_json = json.dumps(dictionnaire, indent=lignes, ensure_ascii=False)
    with open(f"{textes_secondaires}{folder_genre}{folder_auteur}{folder_oeuvre}{titre}.json", "w", encoding='utf8') as outfile:
        outfile.write(objet_json)
    return objet_json

# Create a file without any punctuation
def normaliser(titre, texte_numéroté):
    # print(titre)
    # print(texte_numéroté)
    for vers in texte_numéroté:
        for caractère in texte_numéroté[vers]:
            texte_numéroté[vers] = texte_numéroté[vers].replace(u'\xa0', u' ')
            if caractère in ponctuation:
                texte_numéroté[vers] = texte_numéroté[vers].replace(caractère, "")
            elif caractère in ["'", "’"]:
                texte_numéroté[vers] = texte_numéroté[vers].replace(caractère, " ")
        print(texte_numéroté[vers])
        new_file = open(f'{textes_secondaires}{folder_genre}{folder_auteur}{folder_oeuvre}{titre}_encoded.txt', 'w', encoding='utf-8')
        for each_line in texte_numéroté:
            new_file.write(f'{texte_numéroté[each_line]}\n')
        new_file.close()
    return texte_numéroté

# Create a txt file with the text in 1 unique line
def one_line_texte(titre, texte_dict):
    empty_list = []
    for value in texte_dict:
        empty_list.append(texte_dict[value])
        texte_final = " ".join(empty_list)
    texte_final = texte_final.lower()
    new_file = open(
        f'{textes_secondaires}{folder_genre}{folder_auteur}{folder_oeuvre}{titre}_one_line.txt', 'w', encoding='utf-8')
    new_file.write(texte_final)
    new_file.close()
    return texte_final

# Open the file
file = open(f'{data_directory}{folder_genre}{folder_auteur}{folder_oeuvre}{name_file}',
            'r', 
            encoding='UTF-8'
            )

# Read the file
texte = file.read()
# print(texte)

# Split each line and create a list item by line
lignes = texte.split("\n")
# print(lignes)

# Numerate the texte
numérotation = numéroter_lignes(lignes)
# print(numérotation)

# From numeration to json
texte_numéroté = création_json(titre, numérotation, len(numérotation))
# print(texte_numéroté)

# Remove punctuation from text
texte_normalisé = normaliser(titre, numérotation)
# print(texte_normalisé)

# The text becomes 1 unique line
one_line = one_line_texte(titre, texte_normalisé)
# print(one_line)

# Transformation du poème en liste
liste_mots = list(one_line.split(" "))
# print(liste_mots)

# Fréquence des mots
# for mot in one_line:
#     print(mot)
# frequence_mots = nltk.FreqDist(nltk.word_tokenize(one_line)).most_common()
# print(frequence_mots)