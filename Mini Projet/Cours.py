class Cours:

    def __init__(self, code_cours, intitule_cours, niveau_cours):
        self.__code_cours = code_cours
        self.__intitule_cours = intitule_cours
        self.__niveau_cours = niveau_cours

    # GETTERS
    def get_code_cours(self):
        return self.__code_cours

    def get_intitule_cours(self):
        return self.__intitule_cours

    def get_niveau_cours(self):
        return self.__niveau_cours

    # SETTERS
    def set_code_cours(self, code_cours):
        self.__code_cours = code_cours

    def set_intitule_cours(self, intitule_cours):
        self.__intitule_cours = intitule_cours

    def set_niveau_cours(self, niveau_cours):
        self.__niveau_cours = niveau_cours

    def __eq__(self, other):
        if not isinstance(other, Cours):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__code_cours == other.__code_cours \
            and self.__intitule_cours == other.__intitule_cours \
            and self.__niveau_cours == other.__niveau_cours

    def __repr__(self):
        return "Code Cours : "+self.__code_cours+"\nIntitule Cours : "+self.__intitule_cours \
                +"Niveau Cours : "+self.__niveau_cours
