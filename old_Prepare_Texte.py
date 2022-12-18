import nltk
import csv
import pandas as pd
import os
import json

data_directory = 'C:\\Users\\Maintenant Pret\\OneDrive\\Bureau\\Data'
folder_genre = '\\Poésie'
folder_auteur = '\\Mallarmé'
folder_oeuvre = '\\Poésies'
name_file = '\\Sonnet en X.txt'

file = open(f'{data_directory}{folder_genre}{folder_auteur}{folder_oeuvre}{name_file}', 'r', encoding='utf-8')
# print(file.read())

ponctuation = ",;.:!?()"

texte = file.read()
# print(texte)

lignes = texte.split("\n")
# print(lignes)

num_ligne = 1
poème_id = {}

for ligne in lignes:
    if ligne != '':
        poème_id[num_ligne] = ligne
        num_ligne += 1

for vers in poème_id:
    # print(poème_id[vers])
    for caractère in poème_id[vers]:
        # print(caractère)
        if caractère in ponctuation:
            poème_id[vers] = poème_id[vers].replace(caractère, "")
    for apostrophe in poème_id[vers]:
        if apostrophe == "'":
            poème_id[vers] = poème_id[vers].replace(apostrophe, "e ")
# print(poème_id)

# new_file = open(f'{data_directory}{folder_genre}{folder_auteur}{folder_oeuvre}textes_traités{name_file}'[:-4]+'_encoded.txt', 'a', encoding='utf-8')
# for each_line in poème_id:
    # new_file.write(f'{poème_id[each_line]}\n')
# new_file.close()

empty_list = []
for value in poème_id:
    # print(poème_id[value])
    empty_list.append(poème_id[value])
    texte_final = " ".join(empty_list)

# new_file = open(f'{data_directory}{folder_genre}{folder_auteur}{folder_oeuvre}textes_traités{name_file}'[:-4]+'_one_line.txt', 'a', encoding='utf-8')
# new_file.write(texte_final.lower())
# new_file.close()
# print(texte_final.lower())

mots = nltk.word_tokenize(texte_final.lower())
# print(len(mots))

frequence_mots = nltk.FreqDist(mots)
# print(frequence_mots.most_common())

# all_items = open(f"{data_directory}\\listes_mots\\all_items.txt", "w")
# for item in frequence_mots:
#     all_items.write(f"{item},")
# all_items.close()

"""
Reprendre ici
"""

dict_path = f'{data_directory}\\Dictionnaire'
adjectifs = os.listdir(f'{dict_path}\\adjectif')
adverbes = os.listdir(f'{dict_path}\\adverbe')
conjonctions = os.listdir(f'{dict_path}\\conjonction')
déterminants = os.listdir(f'{dict_path}\\déterminant')
noms = os.listdir(f'{dict_path}\\nom')
noms_propres = os.listdir(f'{dict_path}\\nom_propre')
particules = os.listdir(f'{dict_path}\\particule')
prépositions = os.listdir(f'{dict_path}\\préposition')
pronoms = os.listdir(f'{dict_path}\\pronom')
verbes = os.listdir(f'{dict_path}\\verbe')

all_words_list = open(f"{data_directory}\\listes_mots\\all_items.txt", "r")
# print(all_words_list.read())
list_from_file = all_words_list.read().split(',')
print(list_from_file)

# Premier rasage: conjonctions
list_of_files = []
for file in conjonctions:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\conjonction\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)

# Deuxième rasage: déterminants
list_of_files = []
for file in déterminants:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\déterminant\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)

# Troisième rasage: prépositions
list_of_files = []
for file in prépositions:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\préposition\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)

# Quatrième rasage: pronoms
list_of_files = []
for file in pronoms:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\pronom\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)

# Cinquième rasage: particules
list_of_files = []
for file in particules:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\particule\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)

# Sixième rasage: nom propres
list_of_files = []
for file in noms_propres:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\nom_propre\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)

# Septième rasage: adverbes
list_of_files = []
for file in adverbes:
        list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\adverbe\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)
    if word == 'encor':
        # print(word)
        with open(f'{dict_path}\\adverbe\\encore.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                list_from_file.remove('encor')

# Huitième rasage: noms
list_of_files = []
for file in noms:
    list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\nom\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)
    # print(word[:-1])
    if word[:-1] in list_of_files:
        sng = word[:-1]
        with open(f'{dict_path}\\nom\\{sng}.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
            # print(data['syntagme'])
            list_from_file.remove(word)

# Neuvième rasage: adjectifs
list_of_files = []
for file in adjectifs:
    list_of_files.append(file[:-5])
for word in list_from_file:
    for item in list_of_files:  
        if item in list_from_file:
            with open(f'{dict_path}\\adjectif\\{item}.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(item)
    if word == 'nul':
        with open(f'{dict_path}\\adjectif\\-nul.json', encoding='utf-8') as json_file:
                data = json.loads(json_file.read())
                # print(data['syntagme'])
                list_from_file.remove(word)
    elif word[:-1] in list_of_files:
        sng = word[:-1]
        with open(f'{dict_path}\\adjectif\\{sng}.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
            # print(data['syntagme'])
            list_from_file.remove(word)
    elif word[:-2] in list_of_files:
        sng = word[:-2]
        with open(f'{dict_path}\\adjectif\\{sng}.json', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
            # print(data['syntagme'])
            list_from_file.remove(word)

# Dixième rasage: verbes
# list_of_files = []
# for file in adverbes:
#         list_of_files.append(file[:-5])
# for word in list_from_file:
#     for item in list_of_files:  
#         if item in list_from_file:
#             with open(f'{dict_path}\\adverbe\\{item}.json', encoding='utf-8') as json_file:
#                 data = json.loads(json_file.read())
#                 # print(data['syntagme'])
#                 list_from_file.remove(item)

print(len(list_from_file))
print(list_from_file)