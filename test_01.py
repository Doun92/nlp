# Imports
import Preparer_text
from pathlib import Path

# Data
data_folder = Path("textes_donnes/")
raw_data = f"{data_folder}/raw/"

author = "Daniel Escoval"
book = "Dans un abîme de béton"
poème = "Incipit"

path_to_text = f"{raw_data}{author}/{book}/{poème}.txt"

texte_traité = Preparer_text.Preparation_text()

# texte_traité.read_texte(path_to_text)

one_line = texte_traité.words_in_texte(path_to_text)
# print(one_line)

testwith_texte = texte_traité.remove_punctuation(path_to_text)
# test_str = texte_traité.remove_punctuation(one_line)
