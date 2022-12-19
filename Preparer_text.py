class Preparation_text:
    
    # Lis le texte
    def read_texte(self, texte):
        with open(texte, 'r', encoding='utf8') as f:
            content = f.read()
            print(content)
            f.close()

    def words_in_texte(self, texte):
        with open(texte, 'r', encoding='utf8') as f:
            content = f.read()
            one_line = content.replace('\n', ' ')
            one_line = one_line.replace('\xa0', ' ')
            # print(one_line)
            f.close()
        return one_line

    def retirer_apostrophe(self, liste):
        # TODO: Transformer ça en fonction
        # Comprendre ce qui se passe
        apostrophe = "’"
        # print(liste)
        for el in liste:
            # print(el)
            if apostrophe in el:
                # print(el)
                sans_apostrophe = el.split(apostrophe)
                # print(sans_apostrophe)
                if sans_apostrophe[0] in ["d", "qu"]:
                    sans_apostrophe[0] = sans_apostrophe[0]+"e"
                # print(sans_apostrophe)
            #     # TODO
            #     # On devrait aller dans le dictionnaire et voir si sans_apostrophe[0] est féminin ou masculin, 1er cas +a, deuxième cas +e
            #     correction = ' '.join(sans_apostrophe)
            #     # print(el)
            #     return correction

                # print(correction)

    def remove_punctuation(self, texte):
        ponctuation = ['.', '?', '!', ',',
                       ';' ':', '"', '[', ']', '«', '»', '/']
        ponctuation_avec_espace = ['(', ')', '-']
        
        if texte[-4:] == '.txt':
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
                # Pour l'apostrophe, le traitement es tun peu spécial puisqu'il faut savoir si le nom est masculin féminin
                # Il ne faut donc pas séparer par caractère, mais pas "mot"
                liste_de_mots = one_line.split(" ")
                liste_de_mots = list(filter(None, liste_de_mots))
                # print(liste_de_mots)
                test = self.retirer_apostrophe(liste_de_mots)
                # print(test)
        # else:
        #     for character in texte:
        #         if character in ponctuation:
        #             texte_sans_ponctuation = texte.replace(character, '')
        #             print(texte_sans_ponctuation)
