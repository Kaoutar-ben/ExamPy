#Partie 2

class Projet:
    def __init__(self, nom, gestion_taches):
        self.nom = nom
        self.taches = []
        self.gestion_taches = gestion_taches

    def ajouter_tache(self, titre, description):
        """Ajoute une nouvelle tâche au projet."""
        self.gestion_taches.ajouter_tache(titre, description)
        self.taches.append({'titre': titre, 'description': description, 'completee': False})

    def completer_tache(self, titre):
        """Marque une tâche du projet comme complétée."""
        for tache in self.taches:
            if tache['titre'] == titre:
                tache['completee'] = True
                self.gestion_taches.completer_tache(titre)
                break
    
    def supprimer_tache(self, titre):
        """Supprime une tâche du projet."""
        for tache in self.taches:
            if tache['titre'] == titre:
                self.taches.remove(tache)
                break
        else:
            raise ValueError(f"Tâche '{titre}' non trouvée dans le projet.")

    def verifier_tache_dans_projet(self, titre):
        """Vérifie si une tâche est présente dans le projet."""
        for tache in self.taches:
            if tache['titre'] == titre:
                return True
        return False
