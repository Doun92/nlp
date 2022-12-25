import os

class Preparation_text:
    
    # Lis le texte
    def read_texte(self, texte):
        with open(texte, 'r', encoding='utf8') as f:
            content = f.read()
            print(content)
            f.close()

    def create_file(self, path_to_modif, txt_str, titre, modification):
        # Checks if the path already exist, if not, creates it
        if os.path.exists(path_to_modif) == False:
            os.makedirs(f"{path_to_modif}")

        # Write the file
        one_line_file = open(
            f"{path_to_modif}/{titre}_{modification}.txt", "w", encoding='utf8')
        one_line_file.write(txt_str)
        one_line_file.close()

    def words_in_texte(self, texte, path_to_modif, to_txt: bool = False):
        # Title of the raw file
        title = texte.split("/")[-1][:-4]
        # print(title)

        # Reads the file and create a big one line text
        with open(texte, 'r', encoding='utf8') as f:
            content = f.read()
            one_line = content.replace('\n', ' ')
            one_line = one_line.replace('\xa0', ' ')
            # print(one_line)
            f.close()
        
        # If to_txt=True, create a txt file
        modification = "one_line"
        if to_txt:
            self.create_file(path_to_modif, one_line, title, modification)

        return one_line

    def retirer_apostrophe(self, liste):
        # Comprendre ce qui se passe
        apostrophe = "’"
        # print(liste)
        nouvelle_liste = []
        for el in liste:
            # print(el)
            if apostrophe in el:
                # print(el)
                sans_apostrophe = el.split(apostrophe)
                # On ajoute un e pour enlever l'élision
                if sans_apostrophe[0] in ["d", "qu", "j"]:
                    sans_apostrophe[0] = sans_apostrophe[0]+"e"
                    # print(sans_apostrophe)
                    el = ' '.join(sans_apostrophe)

            #     # TODO
            #     # On devrait aller dans le dictionnaire et voir si sans_apostrophe[0] est féminin ou masculin, 1er cas +a, deuxième cas +e
            #     correction = ' '.join(sans_apostrophe)
            #     # print(el)
            #     return correction

                # print(correction)

        # On fait un dernier test s'il y a un espace du à l'ancienne présence d'une apostrophe
            if " " in el:
                el_ss_apostrophe = el.split(" ")
                for e in el_ss_apostrophe:
                    nouvelle_liste.append(e)
            else:
                nouvelle_liste.append(el)
        return nouvelle_liste

    def remove_punctuation(self, texte, path_to_modif, to_txt: bool = False, title=None):
        modification = 'ss_ponctuation'

        ponctuation = ['.', '?', '!', ',',
                       ';' ':', '"', '[', ']', '«', '»', '/']
        ponctuation_avec_espace = ['(', ')', '-']
        
        if texte[-4:] == '.txt':
            title_from_pathtitle = texte.split("/")[-1][:-4]
            with open(texte, 'r', encoding='utf8') as f:
                content = f.read()
                # Retirer la ponctuation inutile
                one_line = content.replace('\n', ' ')
                one_line = one_line.replace('\xa0', ' ')
                for character in one_line:
                    if character in ponctuation:
                        one_line = one_line.replace(character, '')
                    elif character in ponctuation_avec_espace:
                        one_line = one_line.replace(character, ' ')
                # Pour l'apostrophe, le traitement est un peu spécial puisqu'il faut savoir si le nom est masculin féminin
                # Il ne faut donc pas séparer par caractère, mais pas "mot"
                liste_de_mots = one_line.split(" ")
                liste_de_mots = list(filter(None, liste_de_mots))
                text_ss_apostrophe = self.retirer_apostrophe(liste_de_mots)
                # print(text_ss_apostrophe)
                text_ss_apostrophe = ' '.join(text_ss_apostrophe)
                # On créé un fichier texte sans la ponctuation
                # If to_txt=True, create a txt file
                if to_txt:
                    self.create_file(path_to_modif, text_ss_apostrophe, title_from_pathtitle, modification)
        else:
            one_line = texte.replace('\n', ' ')
            one_line = one_line.replace('\xa0', ' ')
            for character in one_line:
                if character in ponctuation:
                    one_line = one_line.replace(character, '')
                elif character in ponctuation_avec_espace:
                    one_line = one_line.replace(character, ' ')
            # Pour l'apostrophe, le traitement est un peu spécial puisqu'il faut savoir si le nom est masculin féminin
            # Il ne faut donc pas séparer par caractère, mais pas "mot"
            liste_de_mots = one_line.split(" ")
            liste_de_mots = list(filter(None, liste_de_mots))
            text_ss_apostrophe = self.retirer_apostrophe(liste_de_mots)
            text_ss_apostrophe = ' '.join(text_ss_apostrophe)
            self.create_file(path_to_modif, text_ss_apostrophe,title, modification)
        return text_ss_apostrophe
