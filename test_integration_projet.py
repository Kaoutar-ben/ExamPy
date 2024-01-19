#Partie 2

import unittest
from gestion_taches import gestion_taches 
from Projet import Projet

class TestIntegrationProjet(unittest.TestCase):

    def setUp(self):
        # Initialisation des objets nécessaires pour les tests
        self.gestion_taches = gestion_taches()  # Correction du nom de classe
        self.projet = Projet("Projet Test", self.gestion_taches)
    

    def test_ajout_tache_dans_projet(self):
        # Teste l'ajout d'une tâche dans le projet
        self.projet.ajouter_tache("Tâche Projet", "Description de la tâche dans le projet")
        self.assertTrue(self.projet.taches)  # Vérifie que le projet a des tâches
        self.assertTrue(self.gestion_taches.verifier_tache("Tâche Projet"))  
        # Vérifie que la tâche a été ajoutée à la gestion des tâches

    def test_completer_tache_dans_projet(self):
        # Teste la complétion d'une tâche dans le projet
        self.projet.ajouter_tache("Tâche Projet", "Description de la tâche dans le projet")
        self.projet.completer_tache("Tâche Projet")
        self.assertTrue(self.projet.taches[0]['completee'])  
        # Vérifie que la tâche dans le projet est complétée
        self.assertTrue(self.gestion_taches.verifier_tache("Tâche Projet"))  
        # Vérifie que la tâche dans la gestion des tâches est également complétée

    def test_supprimer_tache_dans_projet(self):
        # Teste la suppression d'une tâche dans le projet
        self.projet.ajouter_tache("Tâche Projet", "Description de la tâche dans le projet")
        self.projet.supprimer_tache("Tâche Projet")
        self.assertFalse(self.projet.taches)  # Vérifie que le projet n'a plus de tâches
        with self.assertRaises(ValueError):
            self.gestion_taches.verifier_tache("Tâche Projet")  
            # Vérifie que la tâche a été supprimée de la gestion des tâches

if __name__ == '__main__':
    unittest.main()
