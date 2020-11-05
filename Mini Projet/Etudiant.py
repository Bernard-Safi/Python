class Etudiant:

    def __init__(self, numero_etudiant, prenom_etudiant, nom_etudiant, niveau_etudiant, ):
        self.__numero_etudiant = numero_etudiant
        self.__prenom_etudiant = prenom_etudiant
        self.__nom_etudiant = nom_etudiant
        self.__niveau_etudiant = niveau_etudiant

    # GETTERS
    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_prenom_etudiant(self):
        return self.__prenom_etudiant

    def get_nom_etudiant(self):
        return self.__nom_etudiant

    def get_niveau_etudiant(self):
        return self.__niveau_etudiant

    # SETTERS
    def set_numero_etudiant(self, numero_ertudiant):
        self.__numero_etudiant = numero_ertudiant

    def set_prenom_etudiant(self, prenom_etudiant):
        self.__prenom_etudiant = prenom_etudiant

    def set_nom_etudiant(self, nom_etudiant):
        self.__nom_etudiant = nom_etudiant

    def set_niveau_etudiant(self, niveau_etudiant):
        self.__niveau_etudiant = niveau_etudiant

    def __eq__(self, other):
        if not isinstance(other, Etudiant):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__numero_etudiant == other.__numero_etudiant \
            and self.__prenom_etudiant == other.__prenom_etudiant \
            and self.__nom_etudiant == other.__nom_etudiant \
            and self.__niveau_etudiant == other.__niveau_etudiant

    def __repr__(self):
        return "numero etudiant : "+str(self.__numero_etudiant)+"\nnom etudiant : "+self.__nom_etudiant + \
            "\nprenom etudiant : "+self.__prenom_etudiant+"\nniveau etudiant : "+self.__niveau_etudiant + "\n"

    def modifier_etudiant(self,):
        print("Inserer un nouveau prenom etudiant :")
        nouveau_prenom = input()
        self.__prenom_etudiant = nouveau_prenom

        print("Inserer un nouveau nom etudiant :")
        nouveau_nom = input()
        self.__nom_etudiant = nouveau_nom

        print("Inserer un nouveau niveau etudiant :")
        nouveau_niveau = input()
        self.__niveau_etudiant = nouveau_niveau
