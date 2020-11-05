from Note import Note


class Bd:
    def __init__(self):
        self.__liste_etudiants = []
        self.__liste_cours = []
        self.__liste_notes = []

    # GETTERS
    def get_liste_etudiants(self):
        return self.__liste_etudiants

    def get_liste_cours(self):
        return self.__liste_cours

    def get_liste_notes(self):
        return self.__liste_notes

    # SETTERS
    def set_liste_etudiants(self, liste_etudiant):
        self.__liste_etudiants = liste_etudiant

    def set_liste_cours(self, liste_cours):
        self.__liste_cours = liste_cours

    def set_list_notes(self, liste_notes):
        self.__liste_notes = liste_notes

    def ajouter_etudiant(self, etudiant):
        if len(self.__liste_etudiants) != 0:
            if etudiant not in self.__liste_etudiants:
                self.__liste_etudiants.append(etudiant)
            else:
                print("etudiant dejas existe dans la liste")
        else:
            self.__liste_etudiants.append(etudiant)

    def supprimer_etudiant(self, etudiant):
        if len(self.__liste_etudiants) == 0:
            print("etudiant n'existe pas")
        else:
            if etudiant in self.__liste_etudiants:
                self.__liste_etudiants.remove(etudiant)
            else:
                print("etudiant n'existe pas dans la base de donnee")

    def modifier_etudiant(self, numero_etudiant, nouveau_prenom=None, nouveau_nom=None, nouveau_niveau=None):
        exist = False
        for etudiant in self.__liste_etudiants:
            if etudiant.get_numero_etudiant() == numero_etudiant:
                exist = True
                if nouveau_niveau is not None:
                    etudiant.set_niveau_etudiant(nouveau_niveau)
                if nouveau_nom is not None:
                    etudiant.set_nom_etudiant(nouveau_nom)
                if nouveau_prenom is not None:
                    etudiant.set_prenom_etudiant(nouveau_prenom)
        if exist is False:
            print("l'etudiant n'existe pas dans la base de donne")

    def ajouter_cours(self, cours):
        if len(self.__liste_cours) != 0:
            if cours not in self.__liste_cours:
                self.__liste_cours.append(cours)
            else:
                print("cours dejas existe dans la liste")
        else:
            self.__liste_cours.append(cours)

    def supprimer_cours(self, cours):
        if len(self.__liste_cours) == 0:
            print("cours n'existe pas")
        else:
            if cours in self.__liste_cours:
                self.__liste_cours.remove(cours)
            else:
                print("etudiant n'existe pas dans la base de donnee")

    def modifier_cours(self, code_cours, nouveau_intitule=None, nouveau_niveau=None):
        exist = False
        for cours in self.__liste_cours:
            if cours.get_code_cours() == code_cours:
                exist = True
                if nouveau_intitule is not None:
                    cours.set_intitule_cours(nouveau_intitule)
                if nouveau_niveau is not None:
                    cours.set_niveau_cours(nouveau_niveau)
        if exist is False:
            print("le cours n'existe pas dans la base de donne")

    def ajouter_note(self, numero_etudiant, code_cours, note):
        for etudiant in self.__liste_etudiants:
            if etudiant.get_numero_etudiant() == numero_etudiant:
                for cours in self.__liste_cours:
                    if cours.get_code_cours() == code_cours:
                        note = Note(numero_etudiant, code_cours, note)
                        self.__liste_notes.append(note)

    def supprimer_note(self, numero_etudiant, code_cours):
        for note in self.__liste_notes:
            if note.get_code_cours() == code_cours and note.get_numero_etudiant() == numero_etudiant:
                self.__liste_notes.remove(note)

    def modifier_note(self, numero_etudiant, code_cours, nouvelle_note):
        for note in self.__liste_notes:
            if note.get_numero_etudiant() == numero_etudiant and note.get_code_cours() == code_cours:
                note.set_note(nouvelle_note)

    def moyenne_classe(self, code_cours):
        nbr_etudiant = len(self.__liste_etudiants)
        note = 0
        for note in self.__liste_notes:
            if note.get_code_cours() == code_cours:
                note += note.get_note()
        moyenne_classe = note/nbr_etudiant
        return moyenne_classe

    def moyenne_etudiant(self, numero_etudiant):
        nbr_cours = 0
        somme_note = 0
        for note in self.__liste_notes:
            if note.get_numero_etudiant() == numero_etudiant:
                somme_note += note.get_note()
                nbr_cours += 1
        moyenne_etudiant = somme_note/nbr_cours
        return moyenne_etudiant

    def consulter_notes_classe(self, code_cours):
        notes_classe = []
        for note in self.__liste_notes:
            if note.get_code_cours() == code_cours:
                notes_classe.append(note)
        return notes_classe

    def consulter_notes_etudiant(self, numero_etudiant):
        notes_etudiant = []
        for note in self.__liste_notes:
            if note.get_numero_etudiant == numero_etudiant:
                notes_etudiant.append(note)
        return notes_etudiant

    def liste_etudiant(self):
        if len(self.__liste_etudiants) == 0:
            print("la liste des etudiants est vide")
        for i in self.__liste_etudiants:
            print(i)

    def liste_notes(self):
        if len(self.__liste_etudiants) == 0:
            print("la liste des etudiants est vide")
        for i in self.__liste_notes:
            print(i)