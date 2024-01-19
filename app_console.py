#Partie 4

from utilitaires import calculer_duree_totale

def afficher_liste_taches(taches):
    print("Liste des Tâches :")
    for tache in taches:
        print(f"{tache['nom']} - Durée : {tache['duree']}")

def main():
    # Exemple de liste de tâches
    taches = [
        {'nom': 'Tâche 1', 'duree': 5},
        {'nom': 'Tâche 2', 'duree': 8},
        {'nom': 'Tâche 3', 'duree': 3}
    ]

    # Calculer la durée totale
    duree_totale = calculer_duree_totale(taches)

    # Afficher la liste des tâches
    afficher_liste_taches(taches)

    # Afficher la durée totale
    print(f"\nDurée totale : {duree_totale}")

if __name__ == '__main__':
    main()
