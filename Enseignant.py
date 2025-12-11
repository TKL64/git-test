# enseignant.py
from groupe import Groupe
from eleve import Eleve
from service import ServiceNotes

class Enseignant:
    """Classe Enseignant — appel les services (diagramme UML)."""

    def __init__(self, id_ens: int, nom: str, prenom: str, email: str):
        self.id = id_ens
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.service = ServiceNotes()

    def afficherListeEleves(self, groupe_id: int):
        return self.service.getListeEleves(groupe_id)

    def afficherMoyenGroup(self, groupe_id: int):
        return self.service.calculerMoyenneGroupe(groupe_id)
