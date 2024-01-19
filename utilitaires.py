#Partie 3

def calculer_duree_totale(taches):
    """
    Calcule la durée totale nécessaire pour toutes les tâches d'un projet.

    Args:
        taches (list): Liste de tâches, chaque tâche est un dictionnaire avec la clé 'duree'.

    Returns:
        int: Durée totale des tâches.
    
    Raises:
        ValueError: Si une durée de tâche est négative.
    """
    duree_totale = 0

    for tache in taches:
        duree = tache.get('duree', 0)

        if duree < 0:
            raise ValueError("La durée d'une tâche ne peut pas être négative.")

        duree_totale += duree

    return duree_totale
