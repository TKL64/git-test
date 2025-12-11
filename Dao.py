# dao.py
class DAO:
    """Simule une base de données en mémoire."""

    groupes = {}

    @classmethod
    def ajouter_groupe(cls, groupe):
        cls.groupes[groupe.id_groupe] = groupe

    @classmethod
    def get_groupe(cls, id_groupe):
        return cls.groupes.get(id_groupe)
