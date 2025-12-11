# examen.py
from note import Note

class Examen:
    """Classe Examen — évalue 1..* élèves avec une note."""

    def __init__(self, id_examen: int, titre: str, date_examen: str):
        self.id_examen = id_examen
        self.titre = titre
        self.date_examen = date_examen
        self.notes_eleves: dict[int, Note] = {}  # id_eleve -> Note

    def avoirNoteEleve(self, id_eleve: int):
        return self.notes_eleves.get(id_eleve)
