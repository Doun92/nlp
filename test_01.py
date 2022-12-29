# Imports
import Preparer_text
from pathlib import Path

# Data
data_folder = Path("textes_donnes/")
raw_data = f"{data_folder}/raw/"
modified_data = f"{data_folder}/modif/"

author = "Daniel Escoval"
book = "Dans un abîme de béton"
titre = "Incipit"

path_to_text = f"{raw_data}{author}/{book}/{titre}.txt"
path_to_modif = f"{modified_data}{author}/{book}/"

texte_traité = Preparer_text.Preparation_text()

# texte_traité.read_texte(path_to_text)

one_line = texte_traité.words_in_texte(path_to_text, path_to_modif,False)

# testwith_texte = texte_traité.remove_punctuation(path_to_text, path_to_modif, True)
text_ss_ponctuation = texte_traité.remove_punctuation(one_line, path_to_modif, False, titre)

compter_les_mots = texte_traité.count_word(text_ss_ponctuation)

# TODO: 
"""
Créer un fichier qui fait une ligne par mot.
Lire le fichier
Faire le csv de base pour le dictionnaire

Pour chaque mot, chercher sa forme dans
1) Dans mes listes
2) Le Wiktionnaire
3) La Conjugaison de l'obs
"""