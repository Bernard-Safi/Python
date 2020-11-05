from Cours import Cours
from Etudiant import Etudiant
from Bd import Bd
# from Print import print_name
from Note import Note

bd = Bd()
etudiant = Etudiant(10, "Bernard", "Safi", "A")
et = Etudiant(2, "toni", "hanna", "C")
bd.liste_etudiant()
bd.ajouter_etudiant(et)
bd.liste_etudiant()
bd.ajouter_etudiant(etudiant)
bd.supprimer_etudiant(etudiant)
bd.supprimer_etudiant(etudiant)
bd.ajouter_etudiant(etudiant)
bd.ajouter_etudiant(etudiant)
bd.modifier_etudiant(10, "fadi")
cours = Cours("A", "bernard", "c")
bd.ajouter_cours(cours)
bd.ajouter_note(10, "A", 15)
bd.liste_etudiant()
bd.liste_notes()

#pour chercher les notes d'une classe
list(filter(lambda x: x.get_code_cours() == "A", bd.get_liste_notes()))

#pour chercher les notes d'un etudiant
list(filter(lambda x: x.get_numero_etudiant() == 10, bd.get_liste_notes()))
