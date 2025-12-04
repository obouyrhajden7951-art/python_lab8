"""utils.py – Fonctions utilitaires pour la gestion des notes et du calcul de prix."""
TAUX_TVA = 0.2  # 20 %
def moyenne(notes):
    """Renvoie la moyenne d'une liste de notes (0 si liste vide)."""
    if not notes:
        return 0
    return sum(notes) / len(notes)

def est_admis(note, seuil=10):
    """Retourne True si la note est ≥ au seuil (par défaut 10)."""
    return note >= seuil

def prix_ttc(prix_ht, taux=TAUX_TVA):
    """Applique un taux de TVA (20 % par défaut) pour obtenir un prix TTC."""
    return prix_ht * (1 + taux)

def formater_rapport(notes):
    """Construit une petite chaîne de rapport à partir d'une liste de notes."""
    moyenne_classe = moyenne(notes)
    notes_valides = [note for note in notes if est_admis(note)]
    lignes = [
        "=== Rapport des notes ===",
        f"Notes : {notes}",
        f"Moyenne : {moyenne_classe:.2f}",
        f"Nombre d'étudiants admis : {len(notes_valides)}",
    ]
    return "\n".join(lignes)
