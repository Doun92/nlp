from Preparation_text import Preparation_text
import nltk
import os

titre = 'Akaatama'

data_directory = 'C:\\Users\\Maintenant Pret\\OneDrive\\Bureau\\Data'
dictionnaires = "\\Dictionnaire"
folder_genre = '\\Poésie'
folder_auteur = '\\Escoval'
folder_oeuvre = '\\Poèmes spirituels'
name_file = f'\\{titre}.txt'

file = open(f'{data_directory}{folder_genre}{folder_auteur}{folder_oeuvre}{name_file}', 'r', encoding='utf-8')

texte = file.read()
# print(texte)
lignes = texte.split("\n")
# print(lignes)

texte_traité = Preparation_text(lignes)
numérotation = texte_traité.numéroter_lignes()
# print(numérotation)

# Création d'un fichier json avec les lignes numérotées
texte_numéroté = texte_traité.création_json(titre, numérotation, len(numérotation))

#Texte sans ponctuation
texte_ss_ponct = texte_traité.normaliser(titre, numérotation)
# print(texte_ss_ponct)

# Nécessite un dict
one_line_texte = texte_traité.one_line_texte(titre, texte_ss_ponct)

nombre_total_mots = len(nltk.word_tokenize(one_line_texte))

frequence_mots = nltk.FreqDist(nltk.word_tokenize(one_line_texte)).most_common()
# print(frequence_mots)

liste_mots_uniques = texte_traité.tuple_to_list(titre, frequence_mots)
# print(liste_mots_uniques)

mots_et_nombre = texte_traité.liste_et_nombre(titre, frequence_mots)
# print(mots_et_nombre)

ss_conjonctions = texte_traité.dictionnaires_check(titre, liste_mots_uniques, folder_auteur, folder_oeuvre)

# Trouver qqch pour vérifier si la classe est pleine ou pas
# texte_traité.change_json_path()
