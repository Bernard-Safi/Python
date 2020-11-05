class Note:
    def __init__(self, numero_etudiant, code_cours, note):
        self.__numero_etudiant = numero_etudiant
        self.__code_cours = code_cours
        self.__note = note

    # GETTERS
    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_code_cours(self):
        return self.__code_cours

    def get_note(self):
        return self.__note

    # SETTERS
    def set_numero_etudiant(self, numero_etudiant):
        self.__numero_etudiant = numero_etudiant

    def set_code_cours(self, code_cours):
        self.__code_cours = code_cours

    def set_note(self, note):
        self.__note = note

    def __eq__(self, other):
        if not isinstance(other, Note):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__code_cours == other.__code_cours \
            and self.__note == other.__note \
            and self.__numero_etudiant == other.__numero_etudiant

    def __repr__(self):
        return "Code Cours : " + self.__code_cours + "\nNumero Etudiant : " + str(self.__numero_etudiant) \
               + "\nNote : " + str(self.__note)
