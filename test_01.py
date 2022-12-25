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

one_line = texte_traité.words_in_texte(path_to_text, path_to_modif)
print(one_line)

# testwith_texte = texte_traité.remove_punctuation(path_to_text)
text_ss_ponctuation = texte_traité.remove_punctuation(one_line)
print(text_ss_ponctuation)