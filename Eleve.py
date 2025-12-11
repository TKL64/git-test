# eleve.py
from note import Note

class Eleve:
    """Classe Élève — possède 0..* notes."""

    def __init__(self, id_eleve: int, nom: str, prenom: str):
        self.id_eleve = id_eleve
        self.nom = nom
        self.prenom = prenom
        self.notes: list[Note] = []

    def ajouter_note(self, note: Note):
        self.notes.append(note)

    def moyenne(self):
        """Calcule la moyenne de l'élève."""
        if not self.notes:
            return None
        
        total = sum(n.avoirValeur() for n in self.notes)
        return total / len(self.notes)
