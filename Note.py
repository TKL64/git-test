# note.py
class Note:
    """Représente une note selon le diagramme UML."""

    def __init__(self, id_note: int, valeur: float):
        self.id_note = id_note
        self.valeur = valeur

    def avoirValeur(self) -> float:
        """Retourne la valeur de la note."""
        return self.valeur

    def mettreValeur(self, nouvelle_valeur: float):
        """Modifie la valeur de la note."""
        self.valeur = nouvelle_valeur
