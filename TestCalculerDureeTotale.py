#Partie 3

import unittest
from utilitaires import calculer_duree_totale 


class TestCalculerDureeTotale(unittest.TestCase):

    def test_liste_vide(self):
        # Teste le cas où la liste de tâches est vide
        taches = []
        resultat = calculer_duree_totale(taches)
        self.assertEqual(resultat, 0, "La durée totale doit être égale à 0 pour une liste vide de tâches.")

    def test_durees_positives(self):
        # Teste le cas où toutes les durées des tâches sont positives
        taches = [
            {'duree': 5},
            {'duree': 8},
            {'duree': 3}
        ]
        resultat = calculer_duree_totale(taches)
        self.assertEqual(resultat, 16, "La durée totale doit être égale à la somme des durées des tâches positives.")

    def test_durees_negatives(self):
        # Teste le cas où certaines durées des tâches sont négatives
        taches = [
            {'duree': 5},
            {'duree': -2},
            {'duree': 8},
            {'duree': -4}
        ]
        with self.assertRaises(ValueError):
            calculer_duree_totale(taches)
            # La fonction doit lever une exception ValueError si une durée de tâche est négative

if __name__ == '__main__':
    unittest.main()
