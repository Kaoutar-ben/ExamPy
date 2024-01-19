#Partie 1

class gestion_taches:
    def __init__(self):
        self.taches = {}

    def ajouter_tache(self, titre, description):
        """Ajoute une nouvelle tâche au projet."""
        self.taches[titre] = {'description': description, 'completee': False}

    def completer_tache(self, titre):
        """Marque une tâche comme complétée."""
        if titre not in self.taches:
            raise ValueError(f"Tâche '{titre}' non trouvée.")
        self.taches[titre]['completee'] = True

    def verifier_tache(self, titre):
        """Vérifie si une tâche est complétée."""
        if titre not in self.taches:
            raise ValueError(f"Tâche '{titre}' non trouvée.")
        return self.taches[titre]['completee']
    
