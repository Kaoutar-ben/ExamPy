#Partie 4

import unittest
from unittest.mock import patch
from app_console import afficher_liste_taches, main

class TestAppConsole(unittest.TestCase):

    @patch('builtins.print')
    def test_afficher_liste_taches(self, mock_print):
        taches = [{'nom': 'Tâche 1', 'duree': 5}, {'nom': 'Tâche 2', 'duree': 8}]
        afficher_liste_taches(taches)
        mock_print.assert_called_with("Tâche 1 - Durée : 5")
        mock_print.assert_called_with("Tâche 2 - Durée : 8")

if __name__ == '__main__':
    unittest.main()
