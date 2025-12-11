# groupe.py
from eleve import Eleve

class Groupe:
    """Représente un groupe contenant plusieurs élèves."""

    def __init__(self, id_groupe: int, nom_groupe: str):
        self.id_groupe = id_groupe
        self.nom_groupe = nom_groupe
        self.eleves: list[Eleve] = []

    def ajouterEleve(self, eleve: Eleve):
        self.eleves.append(eleve)
