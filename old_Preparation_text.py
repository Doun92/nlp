"""
Objet pour préparer tout texte
"""
# Imports
import json
import os
from os import listdir
import shutil
import pandas as pd

dict_pat = "C:\\Users\\Maintenant Pret\\OneDrive\\Bureau\\Data\\Dictionnaire\\"

liste_classes= [
            {"conjonction":     os.listdir(f'{dict_pat}\\conjonction')},
            {"particule":       os.listdir(f'{dict_pat}\\particule')},
            {"préposition":     os.listdir(f'{dict_pat}\\préposition')},
            {"interjection":    os.listdir(f'{dict_pat}\\interjection')},
            {"adverbe":         os.listdir(f'{dict_pat}\\adverbe')},
            {"nom_propre":      os.listdir(f'{dict_pat}\\nom_propre')},
            {"pronom":          os.listdir(f'{dict_pat}\\pronom')},
            {"déterminant":     os.listdir(f'{dict_pat}\\déterminant')},
            {"nom":             os.listdir(f'{dict_pat}\\nom')},
            {"adjectif":        os.listdir(f'{dict_pat}\\adjectif')},
            {"verbe":           os.listdir(f'{dict_pat}\\verbe')},
            {"pokemon":         os.listdir(f'{dict_pat}\\nom_propre\\pokemon')},
            {"yokai":           os.listdir(f'{dict_pat}\\nom_propre\\yokai')}
        ]

class Preparation_text:

    def __init__(self, lignes):
        self.lignes = lignes
        self.emplacement = "C:\\Users\\Maintenant Pret\\OneDrive\\Bureau\\Data\\traitements_secondaires\\"
        self.dictionnaires_folder = dict_pat
        self.ponctuation = ",;.:!?()"



    def numéroter_lignes(self):
        num_ligne = 1
        poème_id = {}
        for ligne in self.lignes:
            if ligne != '':
                poème_id[num_ligne] = ligne
                num_ligne += 1
        return poème_id

    def création_json(self, titre, dictionnaire, lignes):
        objet_json = json.dumps(dictionnaire, indent = lignes, ensure_ascii=False)
        with open(f"{self.emplacement}{titre}.json", "w", encoding='utf8') as outfile:
            outfile.write(objet_json)
        return objet_json

    def normaliser(self, titre, texte_numéroté):
        for vers in texte_numéroté:
            for caractère in texte_numéroté[vers]:
                if caractère in self.ponctuation:
                    texte_numéroté[vers] = texte_numéroté[vers].replace(caractère, "")
            for apostrophe in texte_numéroté[vers]:
                if apostrophe in ["'", "’"]:
                    texte_numéroté[vers] = texte_numéroté[vers].replace(apostrophe, "e ")
        new_file = open(f'{self.emplacement}{titre}_encoded.txt', 'w', encoding='utf-8')
        for each_line in texte_numéroté:
            new_file.write(f'{texte_numéroté[each_line]}\n')
        new_file.close()
        return texte_numéroté

    def one_line_texte(self, titre, texte_dict):
        empty_list = []
        for value in texte_dict:
            empty_list.append(texte_dict[value])
            texte_final = " ".join(empty_list)
        texte_final = texte_final.lower()
        new_file = open(f'{self.emplacement}{titre}_one_line.txt', 'w', encoding='utf-8')
        new_file.write(texte_final)
        new_file.close()
        return texte_final

    def liste_et_nombre(self, titre, frequence_mots):
        all_items = open(f"{self.emplacement}{titre}_all_items.txt", "w")
        for item in frequence_mots:
            all_items.write(f"{item},")
        all_items.close()

    def tuple_to_list(self, titre, tpl):
        liste_de_mots = []
        mots_uniques = open(f"{self.emplacement}{titre}_mots_uniques.txt", "w")
        # mots_uniques.write("[")
        for unité in tpl:
            liste_interne = []
            liste_interne.append(unité[0])
            liste_interne.append(unité[1])
            liste_de_mots.append(liste_interne)
            mots_uniques.write(f"{unité[0]} ")
        # mots_uniques.write("]")
        mots_uniques.close()
        return liste_de_mots



    def dictionnaires_check(self, titre, mots_et_fréquence, auteur, oeuvre):
        # print(mots_et_fréquence)
        self.change_json_path()


        columns=["mot", 'occurrence', 'classe', 'genre', 'nombre', 'personne', 'temps']
        df = pd.DataFrame()

        frames = []
        for i in range(len(mots_et_fréquence)):
            mot = mots_et_fréquence[0][0]
            fréquence = mots_et_fréquence[0][1]

            # print(oeuvre[1:])
            if oeuvre[1:] == 'Petits poèmes de poche':
                is_pokemon = self.is_pokemon(mot, fréquence)
                frame = df.append(is_pokemon, ignore_index=True)
                frames.append(frame)
            elif oeuvre[1:] == 'Poèmes spirituels':
                is_yokai = self.is_yokai(mot, fréquence)
                frame = df.append(is_yokai, ignore_index=True)
                frames.append(frame)

            is_mot_complexe = self.is_mot_complexe(mot, fréquence)

            if is_mot_complexe != None:
                frame = df.append(is_mot_complexe, ignore_index=True)
                frames.append(frame)
            else:
                is_conjonction = self.is_conjonction(mot, fréquence)
                if is_conjonction != None:
                    frame = df.append(is_conjonction, ignore_index=True)
                    frames.append(frame)
                else:
                    is_particule = self.is_particule(mot, fréquence)
                    if is_particule != None:
                        frame = df.append(is_particule, ignore_index=True)
                        frames.append(frame)
                    else:
                        is_preposition = self.is_preposition(mot, fréquence)
                        if is_preposition != None:
                            frame = df.append(is_preposition, ignore_index=True)
                            frames.append(frame)
                        else:
                            is_interjection = self.is_interjection(mot, fréquence)
                            if is_interjection != None:
                                frame = df.append(is_interjection, ignore_index=True)
                                frames.append(frame)
                            else:
                                is_adverbe = self.is_adverbe(mot, fréquence)
                                if is_adverbe != None:
                                    frame = df.append(is_adverbe, ignore_index=True)
                                    frames.append(frame)
                                else:
                                    is_nom_propre = self.is_nom_propre(mot, fréquence)
                                    if is_nom_propre != None:
                                        frame = df.append(is_nom_propre, ignore_index=True)
                                        frames.append(frame)
                                    else:
                                        is_pronom = self.is_pronom(mot, fréquence)
                                        if is_pronom != None:
                                            frame = df.append(is_pronom, ignore_index=True)
                                            frames.append(frame)
                                        else:
                                            is_déterminant = self.is_déterminant(mot,fréquence)
                                            if is_déterminant != None:
                                                frame = df.append(is_déterminant, ignore_index=True)
                                                frames.append(frame)
                                            else:
                                                is_nom = self.is_nom(mot, fréquence)
                                                if is_nom != None:
                                                    frame = df.append(is_nom, ignore_index=True)
                                                    frames.append(frame)
                                                else:
                                                    is_adjectif = self.is_adjectif(mot, fréquence)
                                                    if is_adjectif != None:
                                                        frame = df.append(is_adjectif, ignore_index=True)
                                                        frames.append(frame)
                                                    else:
                                                        is_verbe = self.is_verbe(mot, fréquence)
                                                        if is_verbe != None:
                                                            frame = df.append(is_verbe, ignore_index=True)
                                                            frames.append(frame)
                                                        else:
                                                            # print(mot)
                                                            self.create_json(mot)

            mots_et_fréquence.remove(mots_et_fréquence[0])
            # print(mots_et_fréquence)
        result = pd.concat(frames, ignore_index = True)
        print(result)

        result.to_csv(f"{self.emplacement}csv_files{auteur}{oeuvre}\\{titre}_dataframe.csv", mode='w', header=True, index=False, encoding='utf-8')

    def is_conjonction(self, mot, fréquence):
        # print(liste_classes[0]["conjonction"])
        list_termes_dico = liste_classes[0]["conjonction"]
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"conjonction"}
                # print(t)
                return t

    def is_particule(self, mot, fréquence):
        # print(mot)
        # print(liste_classes[0]["conjonction"])
        list_termes_dico = liste_classes[1]["particule"]
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"particule"}
                # print(t)
                return t

    def is_preposition(self, mot, fréquence):
        # print(mot)
        # print(liste_classes[0]["conjonction"])
        list_termes_dico = liste_classes[2]["préposition"]
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"préposition"}
                # print(t)
                return t

    def is_interjection(self, mot, fréquence):
        list_termes_dico = liste_classes[3]["interjection"]
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"interjection"}
                # print(t)
                return t

    def is_adverbe(self, mot, fréquence):
        # print(mot)
        # print(liste_classes[0]["conjonction"])
        list_termes_dico = liste_classes[4]["adverbe"]
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"adverbe"}
                # print(t)
                return t
            elif mot == 'encor':
                t = {'mot':mot+"e", 'occurrence':fréquence, 'classe':"adverbe"}
                return t


    def is_nom_propre(self, mot, fréquence):
        list_termes_dico = liste_classes[5]["nom_propre"]
        # print(list_termes_dico)
        for item in list_termes_dico:
            if item[:-5] == mot:
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"nom propre"}
        #         # print(t)
                return t

    def is_pronom(self, mot, fréquence):
        list_termes_dico = liste_classes[6]["pronom"]
        # print(list_termes_dico)
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                with open(f"{self.dictionnaires_folder}pronom\\{mot}.json", encoding='utf-8') as jsonfile:
                        data = json.load(jsonfile)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"pronom", 'genre':data["genre"], 'nombre':data["nombre"]}
                return t

    def is_déterminant(self, mot, fréquence):
        list_termes_dico = liste_classes[7]["déterminant"]
        # print(list_termes_dico)
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                with open(f"{self.dictionnaires_folder}déterminant\\{mot}.json", encoding='utf-8') as jsonfile:
                        data = json.load(jsonfile)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"déterminant", 'genre':data["genre"], 'nombre':data["nombre"]}
                # print(t)
                return t
            else:
                if mot == 'aux':
                    with open(f"{self.dictionnaires_folder}déterminant\\au-x.json", encoding='utf-8') as jsonfile:
                        data = json.load(jsonfile)
                    t = {'mot':mot, 'occurrence':fréquence, 'classe':"déterminant", 'genre':data["genre"], 'nombre':data["nombre"]}
                    # print(t)
                    return t

    def is_nom(self, mot, fréquence):
        list_termes_dico = liste_classes[8]["nom"]
        # print(list_termes_dico)
        # print(mot)
        for item in list_termes_dico:
            if item[:-5] == mot:
                with open(f"{self.dictionnaires_folder}nom\\{mot}.json", encoding='utf-8') as jsonfile:
                        data = json.load(jsonfile)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"nom", 'genre':data["genre"], 'nombre':"singulier"}
                return t
            elif item[:-5] == mot[:-1]:
                # print(mot)
                with open(f"{self.dictionnaires_folder}nom\\{mot[:-1]}.json", encoding='utf-8') as jsonfile:
                        data = json.load(jsonfile)
                t = {'mot':mot[:-1], 'occurrence':fréquence, 'classe':"nom", 'genre':data["genre"], 'nombre':"pluriel"}
                # print(t)
                return t
            elif mot == 'yeux':
                t = {'mot':"oeil", 'occurrence':fréquence, 'classe':"nom", 'genre':"masculin", 'nombre':"pluriel"}
                # print(t)
                return t


    def is_adjectif(self, mot, fréquence):
        list_termes_dico = liste_classes[9]["adjectif"]
        # print(list_termes_dico)
        for item in list_termes_dico:
            # print(str(mot[-2:]))
            # print(mot[-4])
            if mot == 'nul':
                t = {'mot':'nul', 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                return t
            elif mot == 'tous':
                t = {'mot':'tout', 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                return t
            else:
                if item[:-5] == mot:
                    # print(mot)
                    with open(f"{self.dictionnaires_folder}adjectif\\{mot}.json", encoding='utf-8') as jsonfile:
                            data = json.load(jsonfile)
                    t = {'mot':mot, 'occurrence':fréquence, 'classe':"adjectif", 'genre':'masculin', 'nombre':"singulier"}
                    return t
                elif item[:-5] == mot[:-1]:
                    # print(mot)
                    if mot[-1] == 's':
                        with open(f"{self.dictionnaires_folder}adjectif\\{mot[:-1]}.json", encoding='utf-8') as jsonfile:
                            data = json.load(jsonfile)
                        t = {'mot':mot[:-1], 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"pluriel"}
                        return t
                    elif mot[-1] == 'e':
                        with open(f"{self.dictionnaires_folder}adjectif\\{mot[:-1]}.json", encoding='utf-8') as jsonfile:
                            data = json.load(jsonfile)
                        t = {'mot':mot[:-1], 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"singulier"}
                        return t
                elif item[:-5] == mot[:-2]:
                    # print(mot)
                    t = {'mot':mot[:-2], 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"pluriel"}
                    return t
                elif "elle" in mot:
                    masc = f"{mot[:-3]}au"
                    if masc == item[:-5]:
                        t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                        return t
                    else:
                        if mot[-1] == 's':
                            masc = f"{mot[:-4]}aux"
                            t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                            return t
                elif mot[-2:] == 'es' or mot[-1] == 'e':
                    # print(mot)
                    if mot[-2:] in ['se', 'ce']:
                        # print(mot)
                        masc_1 = f"{mot[:-2]}x"
                        masc_2 = f"{mot[:-2]}r"
                        if item[:-5] == masc_1:
                            t = {'mot':masc_1, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"singulier"}
                            return t
                        elif item[:-5] == masc_2:
                            t = {'mot':masc_2, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"singulier"}
                            return t
                        else:
                            if mot[-4:] == 'rice':
                                masc_1 = f"{mot[:-4]}eur"
                                if item[:-5] == masc_1:
                                    t = {'mot':masc_1, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"singulier"}
                                    return t
                    elif mot[-3:] in ['ses', 'ces']:
                        print(mot)
                        masc_1 = f"{mot[:-3]}x"
                        masc_2 = f"{mot[:-3]}r"
                        if item[:-5] == masc_1:
                            t = {'mot':masc_1, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"pluriel"}
                            return t
                        elif item[:-5] == masc_2:
                            t = {'mot':masc_2, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"pluriel"}
                            return t
                        else:
                            if mot[-4:] == 'rice':
                                masc_1 = f"{mot[:-4]}eur"
                                if item[:-5] == masc_1:
                                    t = {'mot':masc_1, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"pluriel"}
                                    return t
                    elif len(mot) >= 4:
                        # print(mot)
                        if "è" in mot[-4]:
                            # print(mot)
                            if mot[-3] in ['r', 'p', 't', 'c', 'b', 'm', 'n', 'l']:
                                masc = f"{mot[:-5]}e{mot[-3]}"
                                t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                                return t
                        elif 'è' in mot[-3]:
                            # print(mot)
                            if mot[-2] in ['r', 'p', 't', 'c', 'b', 'm', 'n', 'l']:
                                masc = f"{mot[:-4]}e{mot[-2]}"
                                t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                                return t
                    elif len(mot) >= 3:
                        if "è" in mot[-3]:
                            print(mot)
                            if mot[-2] in ['r', 'p', 't', 'c', 'b', 'm', 'n', 'l']:
                                masc = f"{mot[:-4]}e{mot[-2]}"
                                t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                                return t
                elif mot[-3:] == 'aux':
                    masc = f"{mot[:-3]}al"
                    t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"masculin", 'nombre':"singulier"}
                    return t
                elif mot[-4:] == 'elle':
                    masc = mot.replace(mot[-4:], "eau")
                    if item[:-5] == masc:
                        t = {'mot':masc, 'occurrence':fréquence, 'classe':"adjectif", 'genre':"féminin", 'nombre':"singulier"}
                        return t
                # print(mot)

    # columns=["mot", 'occurrence', 'classe', 'genre', 'nombre', 'personne', 'temps', 'mode']
    def is_verbe(self, mot, fréquence):
        list_termes_dico = liste_classes[10]["verbe"]
        for item in list_termes_dico:
            # print(mot[-3:])
            # print(mot.replace(mot[-3:], "er"))
            #verbe être indicatif présent
            if mot in ['suis', 'es', 'est', 'sommes', 'êtes', 'sont']:
                if mot == "suis":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == "es":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == "est":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == "sommes":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == "êtes":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == "sont":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
            #verbe être subjonctif présent
            if mot in ['sois', 'soit', 'soyons', 'soyez', 'soient']:
                if mot == "sois":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == "soit":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == "soyons":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == "soyez":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == "soient":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"subjonctif"}
                    return t
            #verbe vouloir à l'indicatif présent
            elif mot in ['veux', 'veut', 'voulons', 'voulez', 'veulent']:
                if mot == 'veux':
                    t = {'mot':'vouloir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'veut':
                    t = {'mot':'vouloir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'voulons':
                    t = {'mot':'vouloir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'voulez':
                    t = {'mot':'vouloir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'veulent':
                    t = {'mot':'vouloir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
            #verbe devoir à l'indicatif présent
            elif mot in ['dois', 'doit', 'devons', 'devez', 'doivent']:
                if mot == 'dois':
                    t = {'mot':'devoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'doit':
                    t = {'mot':'devoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'devons':
                    t = {'mot':'devoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'devez':
                    t = {'mot':'devoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'doivent':
                    t = {'mot':'devoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
            #verbe faire à l'indicatif présent
            elif mot in ['fais', 'fait', 'faisons', 'faites', 'font']:
                if mot == 'fais':
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'fait':
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'faisons':
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'faites':
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'font':
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
            #verbe pouvoir à l'indicatif présent
            elif mot in ['peux', 'peut', 'pouvons', 'pouvez', 'peuvent']:
                if mot == 'peux':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'peut':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'pouvons':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'pouvez':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'peuvent':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
            #verbe pouvoir subjonctif
            elif mot in ['puisse', 'puisses', 'puissions', 'puissiez', 'puissent']:
                if mot == 'puisse':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == 'puisses':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == 'puissions':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == 'puissiez':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"subjonctif"}
                    return t
                elif mot == 'puissent':
                    t = {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"subjonctif"}
                    return t
            #verbe avoir à l'indicatif présent
            elif mot in ['ai', 'as', 'a', 'avons', 'avez', 'ont']:
                if mot == 'ai':
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'as':
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'a':
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'avons':
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'avez':
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif mot == 'ont':
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
            elif mot == 'faut':
                t = {'mot':'falloir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                return t
            elif item[:-5] == mot:
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"verbe", "temps":"présent", "mode":"infinitif"}
                return t
            #verbe être à l'indicatif imparfait
            elif mot in ['étais', 'était', 'étions', 'étiez', 'étaient']:
                if mot == "étais":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfinie", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif mot == "était":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif mot == "étions":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif mot == "étiez":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif mot == "étaient":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                    return t
            #verbe avoir à l'indicatif futur
            elif mot in ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront']:
                if mot == "aurai":
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "auras":
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "aura":
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "aurons":
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "aurez":
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "auront":
                    t = {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
            #verbe être à l'indicatif futur
            elif mot in ['serai', 'seras', 'sera', 'serons', 'serez', 'seront']:
                if mot == "serai":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "seras":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "sera":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "serons":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "serez":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "seront":
                    t = {'mot':'être', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
            #verbe faire à l'indicatif futur
            elif mot in ['ferai', 'feras', 'fera', 'ferons', 'ferez', 'feront']:
                if mot == "ferai":
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "feras":
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "fera":
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "ferons":
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "ferez":
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif mot == "feront":
                    t = {'mot':'faire', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
            #verbe naître passé simple
            elif mot in ['naquis', 'naquit', 'naquîmes', 'naquîtes', 'naquirent']:
                if mot == "naquis":
                    t = {'mot':'naître', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"passé simple", "mode":"indicatif"}
                    return t
                elif mot == "naquit":
                    t = {'mot':'naître', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"passé simple", "mode":"indicatif"}
                    return t
                elif mot == "naquîmes":
                    t = {'mot':'naître', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"passé simple", "mode":"indicatif"}
                    return t
                elif mot == "naquîtes":
                    t = {'mot':'naître', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"passé simple", "mode":"indicatif"}
                    return t
                elif mot == "naquirent":
                    t = {'mot':'naître', 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"passé simple", "mode":"indicatif"}
                    return t
            #Peut-être mettre les différents temps ensemble dans différentes fonctions
            elif mot[-5:] in ['aient']:
                inf_1 = mot.replace(mot[-5:], "er")
                inf_2 = mot.replace(mot[-5:], "r")
                inf_3 = mot.replace(mot[-5:], "re")
                if item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_3:
                    t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                    return t
            #indicatif futur simple
            elif mot[-4:] in ['rons', 'ront']:
                # print(f"{mot}")
                if mot[-4:] == 'rons':
                    inf_1 = mot.replace(mot[-4:], "er")
                    inf_2 = mot.replace(mot[-4:], "r")
                    inf_3 = mot.replace(mot[-4:], "re")
                    # print(f"{inf_1} ou {inf_2} ou {inf_3}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"futur", "mode":"indicatif"}
                        return t
                elif mot[-4:] == 'ront':
                    inf_1 = mot.replace(mot[-4:], "er")
                    inf_2 = mot.replace(mot[-4:], "r")
                    inf_3 = mot.replace(mot[-4:], "re")
                    # print(f"{inf_1} ou {inf_2} ou {inf_3}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                        return t
            elif mot[-4:] == 'ions':
                racine = None
                # print(mot[:-6])
                if mot[-6:-4] == 'gn':
                    racine = f"{mot[:-6]}n"
                # print(racine)
                if racine != None:
                    inf_1 = f'{racine}dre'
                    inf_2 = f'{racine}er'
                    inf_3 = f'{racine}r'
                    inf_4 = f'{racine}re'

                else:
                    inf_1 = f'{mot[:-4]}dre'
                    inf_2 = f'{mot[:-4]}er'
                    inf_3 = f'{mot[:-4]}r'
                    inf_4 = f'{mot[:-4]}re'
                # print(f"{inf_1} ou {inf_2} ou {inf_3} ou {inf_4}")
                if item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_3:
                    t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"imparfait", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_4:
                    t = {'mot':inf_4, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"première", "temps":"imparfait", "mode":"indicatif"}
                    return t
            elif mot[-3:] in ['rai', 'ras', 'rez']:
                if mot[-3:] == 'rai':
                    inf_1 = f"{mot[:-3]}er"
                    inf_2 = f"{mot[:-3]}r"
                    inf_3 = f"{mot[:-2]}e"
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"futur", "mode":"indicatif"}
                        return t
                elif mot[-3:] == 'ras':
                    inf_1 = f"{mot[:-3]}er"
                    inf_2 = f"{mot[:-2]}"
                    # print(f"{inf_1} ou {inf_2}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                        return t
                    else:
                        if 'viend' in mot:
                            inf_venir = mot.replace('viendras', "venir")
                            t = {'mot':inf_venir, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                            return t
                elif mot[-3:] == 'rez':
                    # inf = f"{racine[:-1]}ir"
                    inf_1 = f"{mot[:-3]}er"
                    inf_2 = f"{mot[:-3]}rer"
                    # print(inf)
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"futur", "mode":"indicatif"}
                        return t
            # Participe présent
            elif mot[-3:] == 'ant':
                inf_1 = f"{mot[:-3]}er"
                inf_2 = f"{mot[:-3]}ir"
                if item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "temps":"présent", "mode":"participe"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "temps":"présent", "mode":"participe"}
                    return t
            #Imparfait
            elif mot[-3:] in ['ais', 'ait']:
                if mot[-3:] == 'ais':
                        inf = f"{mot[:-3]}er"
                        if item[:-5] == inf:
                            t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"imparfait", "mode":"indicatif"}
                            return t
                elif mot[-3:] == 'ait':
                    # print(mot)
                    inf_1 = f"{mot[:-3]}er"
                    inf_2 = f"{mot[:-3]}r"
                    inf_3 = f"{mot[:-3]}ir"
                    inf_4 = f"{mot[:-3]}re"
                    inf_5 = f"{mot[:-1]}re"
                    # print(f"{inf_1} ou {inf_2} ou {inf_3} ou {inf_4} ou {inf_5}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_4:
                        t = {'mot':inf_4, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_5:
                        t = {'mot':inf_5, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"imparfait", "mode":"indicatif"}
                        return t
            elif mot[-2:] == 'ra':
                if 'vien' in mot:
                    mot = mot.replace('viend', 'veni')
                inf_1 = f"{mot[:-2]}er"
                inf_2 = mot[:-1]
                inf_3 = f"{mot[:-2]}re"
                inf_4 = f"{mot[:-2]}r"
                if item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_3:
                    t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_4:
                    t = {'mot':inf_4, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                    return t
                else:
                    if 'oi' in inf_1:
                        inf_1 = inf_1.replace('oi', "oy")
                        if item[:-5] == inf_1:
                            t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                            return t
                        elif 'oi' in inf_2:
                            inf_2 = inf_2.replace('oi', "oy")
                            if item[:-5] == inf_2:
                                t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                                return t
                    elif 'è' in inf_1:
                        inf_1 = inf_1.replace('è', "é")
                        if item[:-5] == inf_1:
                            t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                            return t
                        elif 'è' in inf_2:
                            inf_2 = inf_2.replace('è', "é")
                            if item[:-5] == inf_2:
                                t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"futur", "mode":"indicatif"}
                                return t
            #indicatif présent, troisième personne
            elif mot[-3:] == 'ent':
                # print(mot)
                if 'vien' in mot:
                    # print(mot)
                    racine = mot.replace("vien", 'ven')
                    inf = f"{racine[:-1]}ir"
                    # print(inf)
                    if inf == item[:-5]:
                        t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                elif 'vienn' in mot:
                    racine = mot.replace("vienn", "ven")
                    inf = f"{racine[:-3]}ir"
                    t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif "régissent" in mot:
                    inf = mot.replace("régissent", "régir")
                    t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif 'aissent' in mot:
                    inf = mot.replace("aissent", "aître")
                    t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif 'çoivent' in mot:
                    inf = mot.replace("çoivent", "cevoir")
                    t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                else:
                    # print(mot[-3:])
                    inf_1 = f"{mot[:-3]}er"
                    inf_2 = f"{mot[:-3]}re"
                    inf_3 = f"{mot[:-3]}ir"
                    inf_4 = f"{mot[:-3]}oir"
                    # print(f"{inf_1} ou {inf_2} ou {inf_3} ou {inf_4}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_3    , 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_4:
                        t = {'mot':inf_4    , 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                    if mot[-4] == 's':
                        inf_1 = f"{mot[:-4]}er"
                        inf_2 = f"{mot[:-4]}re"
                        inf_3 = f"{mot[:-4]}ir"
                        inf_4 = f"{mot[:-4]}oir"
                        # print(f"{inf_1} ou {inf_2} ou {inf_3} ou {inf_4}")
                        if item[:-5] == inf_1:
                            t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif item[:-5] == inf_2:
                            t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif item[:-5] == inf_3:
                            t = {'mot':inf_3    , 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif item[:-5] == inf_4:
                            t = {'mot':inf_4    , 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                            return t
            elif mot[-2:] == 'ez':
                inf_1 = f"{mot[:-2]}er"
                inf_2 = f"{mot[:-2]}r"
                inf_3 = f"{mot[:-2]}ir"
                if item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_3:
                    t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"pluriel", "personne":"deuxième", "temps":"présent", "mode":"indicatif"}
                    return t
            elif mot[-1:] == 'e':
                inf = mot
                inf_1 = mot + "r"
                inf_2 = mot[:-1] + "ir"
                inf_3 = mot[:-1] + "r"
                if "è" in mot[-3:]:
                    racine_è = mot.replace('è','é')
                    inf = racine_è + "r"
                # print(inf)
                if item[:-5] == inf:
                    t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_3:
                    t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                    return t
                else:
                    if inf[:-2]+'ir'== 'recueillir':
                        # print(inf[:-2]+'ir')
                        t = {'mot':inf[:-2]+'ir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
            #indicatif présent, troisième groupe
            elif mot[-1] in ['s', 't', 'd', 'x', 'z']:
                if mot[-1] == 's':
                    racine = None
                    if 'vien' in mot:
                        racine = mot.replace('vien', 'veni')
                    # print(mot)
                    if racine == None:
                        if mot[-2] == 'd':
                            inf_1 = f"{mot[:-1]}er"
                            inf_2 = f"{mot[:-1]}r"
                            inf_3 = f"{mot[:-1]}ir"
                            inf_4 = f"{mot[:-1]}re"
                            inf_5 = f"{mot[:-2]}ire"
                        else:
                            inf_1 = f"{mot[:-2]}er"
                            inf_2 = f"{mot[:-2]}r"
                            inf_3 = f"{mot[:-2]}ir"
                            inf_4 = f"{mot[:-2]}re"
                            inf_5 = f"{mot[:-2]}ire"
                    else:
                        inf_1 = f"{racine[:-2]}er"
                        inf_2 = f"{racine[:-2]}r"
                        inf_3 = f"{racine[:-2]}ir"
                        inf_4 = f"{racine[:-2]}re"
                        inf_5 = f"{racine[:-2]}ire"
                        print(f"{inf_1} ou {inf_2} ou {inf_3} ou {inf_4} ou {inf_5}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_3:
                        t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_4:
                        t = {'mot':inf_4, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_5:
                        t = {'mot':inf_5, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    else:
                        if 'eu' in inf_1:
                            inf_eu = mot.replace('eu', "ou")
                            t = {'mot':inf_eu, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif 'eu' in inf_2:
                            inf_eu = mot.replace('eu', "ou")
                            t = {'mot':inf_eu, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif 'eu' in inf_3:
                            inf_eu = mot.replace('eu', "ou")
                            t = {'mot':inf_eu, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif 'eu' in inf_4:
                            inf_eu = mot.replace('eu', "ou")
                            t = {'mot':inf_eu, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                elif mot[-1] == 't':
                    # print(mot)
                    if 'vien' in mot:
                        racine = mot.replace('vien', 'ven')
                        inf = f"{racine}ir"
                        if item[:-5] == inf:
                            t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                    elif mot == 'met':
                        t = {'mot':'mettre', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif mot == 'sert':
                        t = {'mot':'servir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif 'sui' in mot:
                        racine = mot.replace('sui', 'suiv')
                        inf_1 = racine + 're'
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    else:
                        # print(mot[:-2])
                        racine = None
                        if mot[-2] == "î":
                            racine = f"{mot}"
                        if racine == None:
                            inf_1 = f"{mot[:-1]}ir"
                            inf_2 = f"{mot[:-1]}r"
                            inf_3 = f"{mot[:-1]}re"
                        else:
                            inf_1 = f"{racine}ir"
                            inf_2 = f"{racine}r"
                            inf_3 = f"{racine}re"
                        # print(f"{inf_1} ou {inf_2} ou {inf_3}")
                        if item[:-5] == inf_1:
                            t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif item[:-5] == inf_2:
                            t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                        elif item[:-5] == inf_3:
                            t = {'mot':inf_3, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                            return t
                elif mot[-1] == 'd':
                    inf_1 = mot.replace(mot[-1], "ir")
                    inf_2 = mot.replace(mot[-1], 'dre')
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                elif mot[-1] == 'x':
                    inf = mot.replace(mot[-1], "ir")
                    if item[:-5] == inf:
                        t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
                elif mot[-1] == 'z':
                    inf = mot.replace(mot[-1], "r")
                    if item[:-5] == inf:
                        t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"}
                        return t
            #passé simple, troisième personne
            elif mot[-1] in ['a', 'u']:
                #meilleure méthode: à standardiser !!!!!!!!!!!!!!!!!!!!!!
                inf_1 = f"{mot[:-1]}er"
                inf_2 = f"{mot[:-1]}oir"
                # print(f"{inf_1} ou {inf_2}")
                if item[:-5] == inf_1:
                    t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"passé simple", "mode":"indicatif"}
                    return t
                elif item[:-5] == inf_2:
                    t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"passé simple", "mode":"indicatif"}
                    return t
                else:

                    if mot[-2] in ['s', 'ç']:
                        # print(mot)
                        inf_s_1 = f"{mot[:-2]}cer"
                        inf_s_2 = f"{mot[:-2]}ser"
                        # print(inf_s)
                        if item[:-5] == inf_s_1:
                            t = {'mot':inf_s_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"passé simple", "mode":"indicatif"}
                            return t
                        if item[:-5] == inf_s_2:
                            t = {'mot':inf_s_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"passé simple", "mode":"indicatif"}
                            return t
            #participe passé
            elif mot[-1] in ['i', 'é']:
                if mot[-1] == 'é':
                    inf = mot.replace(mot[-1], "er")
                    if item[:-5] == inf:
                        t = {'mot':inf, 'occurrence':fréquence, 'classe':"verbe", "temps":"passé", "mode":"participe"}
                        return t
                elif mot[-1] == 'i':
                    inf_1 = f"{mot[:-1]}ir"
                    inf_2 = f"{mot[:-1]}r"
                    # print(f"{inf_1} ou {inf_2}")
                    if item[:-5] == inf_1:
                        t = {'mot':inf_1, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t
                    elif item[:-5] == inf_2:
                        t = {'mot':inf_2, 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"indéfini", "temps":"présent", "mode":"indicatif"}
                        return t

    def is_mot_complexe(self, mot, fréquence):
        if '-' in mot:
            liste = mot.split('-')
            is_verbe = self.is_verbe(liste[0], 1)
            if is_verbe != None:
                t = is_verbe
                return t

            if liste[-1] == 'ce':
                pass
            else:
                is_pronom = self.is_pronom(liste[-1], 1)
                if is_pronom != None:
                    return is_pronom


        if mot == 'a-t-il':
            liste = [
                {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"troisième", "temps":"présent", "mode":"indicatif"},
                {'mot':'il', 'occurrence':fréquence, 'classe':"pronom", 'genre':'épicène', 'nombre':'singulier'}
            ]
            for item in liste:
                return item
        elif mot == 'puis-je':
            liste = [
                {'mot':'pouvoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"présent", "mode":"indicatif"},
                {'mot':'je', 'occurrence':fréquence, 'classe':"pronom", 'genre':'épicène', 'nombre':'singulier'}
            ]
            for item in liste:
                return item
        elif mot == 'ai-je':
            liste = [
                {'mot':'avoir', 'occurrence':fréquence, 'classe':"verbe", "nombre":"singulier", "personne":"première", "temps":"présent", "mode":"indicatif"},
                {'mot':'je', 'occurrence':fréquence, 'classe':"pronom", 'genre':'épicène', 'nombre':'singulier'}
            ]
            for item in liste:
                return item

    def is_pokemon(self, mot, fréquence):
        list_termes_dico = liste_classes[11]["pokemon"]
        # print(mot)
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"Pokemon", "nombre":"singulier"}
                return t
            elif item[:-5] == mot[:-1]:
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"Pokemon", "nombre":"pluriel"}
                return t

    def is_yokai(self, mot, fréquence):
        list_termes_dico = liste_classes[12]["yokai"]
        # print(mot)
        for item in list_termes_dico:
            if item[:-5] == mot:
                # print(mot)
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"Yokai", "nombre":"singulier"}
                return t
            elif item[:-5] == mot[:-1]:
                t = {'mot':mot, 'occurrence':fréquence, 'classe':"Yokai", "nombre":"pluriel"}
                return t

    def create_json(self, mot):
        json_data = {"entrée": mot, "classe":""}
        jsonString = json.dumps(json_data, ensure_ascii=False)
        jsonFile = open(f"{self.dictionnaires_folder}{mot}.json", "w", encoding='utf-8')
        jsonFile.write(jsonString)
        jsonFile.close()

    def change_json_path(self):
        size_dict_folder = len([item for item in os.listdir(self.dictionnaires_folder)])
        # print (size_dict_folder)
        if size_dict_folder > 10:
            print('Des fichier json vont être rangés.')
            for fichier in os.listdir(self.dictionnaires_folder):
                # print(fichier)
                if fichier[-5:] == '.json':
                    # print(fichier)
                    with open(f"{self.dictionnaires_folder}{fichier}", encoding='utf-8') as jsonfile:
                        data = json.load(jsonfile)

                    if data['classe'] == 'pokemon':
                        shutil.move(f"{self.dictionnaires_folder}{data['entrée']}.json", f"{self.dictionnaires_folder}nom_propre\\pokemon\\{data['entrée']}.json")
                    elif data['classe'] == 'yokai':
                        shutil.move(f"{self.dictionnaires_folder}{data['entrée']}.json", f"{self.dictionnaires_folder}nom_propre\\yokai\\{data['entrée']}.json")
                    else:
                        shutil.move(f"{self.dictionnaires_folder}{data['entrée']}.json", f"{self.dictionnaires_folder}{data['classe']}\\{data['entrée']}.json")
                    # print(f"{data['entrée']}.json transféré vers {data['classe']}")
