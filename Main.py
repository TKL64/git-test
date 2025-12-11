# main.py
from ihm_console import IHM
from dao import DAO
from groupe import Groupe
from eleve import Eleve
from note import Note

# --- Préparation des données (comme si elles venaient d'une BD) --- #
g = Groupe(1, "Groupe A")
e1 = Eleve(1, "Ali", "Samir")
e2 = Eleve(2, "Kim", "Jenny")

e1.ajouter_note(Note(1, 80))
e1.ajouter_note(Note(2, 90))

e2.ajouter_note(Note(3, 70))

g.ajouterEleve(e1)
g.ajouterEleve(e2)

DAO.ajouter_groupe(g)

# --- Lancement IHM --- #
ihm = IHM()
ihm.afficher_menu()

print("\nListe élèves :", ihm.prof.afficherListeEleves(1))
print("Moyenne groupe :", ihm.prof.afficherMoyenGroup(1))
