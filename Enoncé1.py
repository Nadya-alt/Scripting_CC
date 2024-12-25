def creer_chaine(n):
    """Crée et initialise la chaîne MaChaine."""
    if n < 5:
        raise ValueError("N doit être supérieur ou égal à 5.")
    return "abcdefghijklmnopqrstuvwxyz" * n

def afficher_chaine(chaine):
    """Affiche la chaîne donnée."""
    print(f"MaChaine : {chaine}")

def copier_17_derniers(chaine):
    """Recopie les 17 derniers caractères de la chaîne dans TaChaine."""
    return chaine[-17:]

def alterner_min_maj(chaine):
    """Transforme MaChaine pour alterner minuscule/majuscule."""
    resultat = ""
    for i, char in enumerate(chaine):
        if i % 2 == 0:
            resultat += char.lower()
        else:
            resultat += char.upper()
    return resultat

def inverser_chaine(chaine):
    """Inverse la chaîne."""
    return chaine[::-1]

def construire_pyramide(chaine):
    """Construit une pyramide avec les caractères de la chaîne."""
    pyramide = ""
    for i in range(1, len(chaine) + 1):
        pyramide += chaine[:i] + "\n"
    return pyramide

def rechercher_sous_chaine(chaine, taille):
    """Recherche une sous-chaîne de taille paramétrable dans TaChaine."""
    if taille > len(chaine):
        raise ValueError("La taille est supérieure à la longueur de la chaîne.")
    return chaine[:taille]

def transformer_en_liste_triee(chaine):
    """Transforme TaChaine en une liste triée."""
    return sorted(chaine)

# Programme principal
def main():
    try:
        # Étape 1 : Créer et initialiser MaChaine
        n = int(input("Veuillez entrer une valeur pour N (N >= 5) : "))
        ma_chaine = creer_chaine(n)
        
        # Étape 2 : Afficher MaChaine
        afficher_chaine(ma_chaine)
        
        # Étape 3 : Recopier les 17 derniers caractères dans TaChaine
        ta_chaine = copier_17_derniers(ma_chaine)
        print(f"TaChaine (les 17 derniers caractères) : {ta_chaine}")
        
        # Étape 4 : Transformer MaChaine pour alterner minuscule/majuscule
        ma_chaine_alternee = alterner_min_maj(ma_chaine)
        print(f"MaChaine alternée (min/maj) : {ma_chaine_alternee}")
        
        # Étape 5 : Inverser MaChaine
        ma_chaine_inversee = inverser_chaine(ma_chaine)
        print(f"MaChaine inversée : {ma_chaine_inversee}")
        
        # Étape 6 : Construire une pyramide avec TaChaine
        pyramide = construire_pyramide(ta_chaine)
        print("Pyramide construite avec TaChaine :")
        print(pyramide)
        
        # Étape 7 : Rechercher une sous-chaîne dans TaChaine
        taille_sous_chaine = int(input("Entrez la taille de la sous-chaîne à rechercher : "))
        sous_chaine = rechercher_sous_chaine(ta_chaine, taille_sous_chaine)
        print(f"Sous-chaîne de taille {taille_sous_chaine} : {sous_chaine}")
        
        # Étape 8 : Transformer TaChaine en une liste triée
        liste_triee = transformer_en_liste_triee(ta_chaine)
        print(f"TaChaine transformée en liste triée : {liste_triee}")
    
    except ValueError as e:
        print(f"Erreur : {e}")

# Exécuter le programme principal
if __name__ == "__main__":
    main()
