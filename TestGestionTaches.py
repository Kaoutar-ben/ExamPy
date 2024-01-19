#Partie 1 

import unittest
from gestion_taches import gestion_taches

class TestGestionTaches(unittest.TestCase):

    def setUp(self):
        # Initialisation des objets nécessaires pour les tests
        self.gestion_taches = gestion_taches()

    def test_ajouter_tache(self):
        # Teste l'ajout d'une nouvelle tâche
        self.gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        self.assertIn("Tâche 1", self.gestion_taches.taches)

    def test_completer_tache_existante(self):
        # Teste la complétion d'une tâche existante
        self.gestion_taches.ajouter_tache("Tâche 2", "Description de la tâche 2")
        self.gestion_taches.completer_tache("Tâche 2")
        self.assertTrue(self.gestion_taches.verifier_tache("Tâche 2"))

    def test_completer_tache_inexistante(self):
        # Teste la complétion d'une tâche inexistante
        with self.assertRaises(ValueError):
            self.gestion_taches.completer_tache("Tâche inexistante")

    def test_verifier_tache_non_complete(self):
        # Teste la vérification d'une tâche non complétée
        self.gestion_taches.ajouter_tache("Tâche 3", "Description de la tâche 3")
        self.assertFalse(self.gestion_taches.verifier_tache("Tâche 3"))

    def test_verifier_tache_complete(self):
        # Teste la vérification d'une tâche complétée
        self.gestion_taches.ajouter_tache("Tâche 4", "Description de la tâche 4")
        self.gestion_taches.completer_tache("Tâche 4")
        self.assertTrue(self.gestion_taches.verifier_tache("Tâche 4"))

if __name__ == '__main__':
    unittest.main()
