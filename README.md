#  Projet Gestion des Notes – UML + Python

Ce projet implémente un système de gestion scolaire en Python basé sur :

- un **diagramme UML de classes**
- plusieurs **diagrammes de séquence**
- une architecture organisée en modules (Python multi-fichiers)
- un service métier qui applique la logique des cas d’utilisation

Le but du projet est d’illustrer l’application concrète de l’UML dans un code Python structuré.

---

##  Fonctionnalités principales

- Gestion des **élèves** et de leurs notes
- Attribution de notes via un **examen**
- Calcul de la **moyenne d’un élève**
- Calcul de la **moyenne d’un groupe** (diagramme de séquence respecté)
- Affichage de la **liste des élèves d’un groupe**
- Gestion simulée d’une BD via un **DAO en mémoire**
- Interface console (IHM)

---

##  Structure du Projet

projet_notes/
│── main.py
│── enseignant.py
│── eleve.py
│── note.py
│── examen.py
│── groupe.py
│── service.py
│── dao.py
│── ihm_console.py
└── README.md


Chaque fichier correspond à une classe du diagramme UML.

---

##  Architecture UML

### ✔ Classes implémentées
- **Enseignant** : utilise les services pour afficher les listes d’élèves et les moyennes.
- **Groupe** : contient une liste d’élèves.
- **Élève** : possède 0..* notes et une méthode `moyenne()`.
- **Note** : contient une valeur et des accesseurs.
- **Examen** : relie les élèves à leurs notes.
- **ServiceNotes** : logique métier (calcul moyennes, récupération des listes).
- **DAO** : simule une base de données en mémoire.

###  Respect des diagrammes de séquence
- *Afficher la liste des élèves*  
- *Calculer la moyenne d’un groupe*

Les messages entre IHM → Service → DAO sont respectés.

---

##  Exécution du programme

###  Cloner le projet
```bash
git clone https://github.com/<ton_nom>/<nom_du_repo>.git
cd <nom_du_repo>

python main.py

1. Afficher liste élèves
2. Afficher moyenne groupe
3. Quitter

Liste élèves : [<eleve.Eleve object at ...>, <eleve.Eleve object at ...>]
Moyenne groupe : 80.0

Jeu de données initial (dans main.py)

Deux élèves sont créés :

Ali Samir → notes : 80 et 90

Jenny Kim → note : 70

La moyenne affichée pour le groupe = 80.0

👨‍💻 Auteur
Liam Levesque
Sam Hendriks
Osman Dirieh
Mohamed Djibril Omar