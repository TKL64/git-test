# service.py

from dao import DAO

class ServiceNotes:
    """Service qui applique les use cases selon les diagrammes de séquence."""

    def getListeEleves(self, groupe_id: int):
        groupe = DAO.get_groupe(groupe_id)

        if groupe is None:
            raise Exception("Groupe introuvable")

        return groupe.eleves

    def calculerMoyenneGroupe(self, groupe_id: int):
        groupe = DAO.get_groupe(groupe_id)

        if groupe is None:
            raise Exception("Groupe introuvable")

        if not groupe.eleves:
            return None

        # Diagramme : chargerNotesParGroupe -> calcul moyenne
        toutes_notes = []
        for e in groupe.eleves:
            if e.moyenne() is not None:
                toutes_notes.append(e.moyenne())

        if not toutes_notes:
            return None

        return sum(toutes_notes) / len(toutes_notes)
