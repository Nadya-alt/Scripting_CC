# 1. Créer et initialiser la chaîne "MaChaine"
def creer_chaine(n):
    ##Crée et initialise la chaîne avec les lettres de l'alphabet multipliées n fois.
    if n < 5:
        raise ValueError("N doit être supérieur ou égal à 5.")
    return "abcdefghijklmnopqrstuvwxyz" * n

# 2. Afficher la chaîne
def afficher_chaine(chaine):
    ##Affiche la chaîne donnée.
    print(f"MaChaine : {chaine}")

# 3. Copier les 17 derniers caractères
def copier_17_derniers(chaine):
    ##Recopie les 17 derniers caractères de la chaîne.
    return chaine[-17:]

# 4. Alterner les minuscules et majuscules
def alterner_min_maj(chaine):
    ##Alterne les minuscules et majuscules dans la chaîne.
    resultat = ""
    for i in range(len(chaine)):
        if i % 2 == 0:
            resultat += chaine[i].lower()
        else:
            resultat += chaine[i].upper()
    return resultat

# 5. Inverser la chaîne
def inverser_chaine(chaine):
    ##Inverse la chaîne.
    return chaine[::-1]

# 6. Construire une pyramide
def construire_pyramide(chaine):
    ##Crée une pyramide avec les caractères de la chaîne.
    pyramide = ""
    for i in range(1, len(chaine) + 1):
        pyramide += chaine[:i] + "\n"
    return pyramide

# 7. Rechercher une sous-chaîne
def rechercher_sous_chaine(chaine, taille):
    ##Recherche une sous-chaîne d'une taille spécifique dans la chaîne.
    if taille > len(chaine):
        raise ValueError("La taille est trop grande.")
    return chaine[:taille]

# 8. Transformer la chaîne en liste triée
def transformer_en_liste_triee(chaine):
    ##Transforme la chaîne en une liste triée.
    return sorted(chaine)

# script principal #
def main():
    try:
        ##Demander à l'user la taille de la chaîne
        n = int(input(" entrer un nombre N (N >= 5) : "))
        ma_chaine = creer_chaine(n)
        
        ##Afficher la chaîne "MaChaine"
        afficher_chaine(ma_chaine)
        
        ##Copier les 17 derniers caractères
        ta_chaine = copier_17_derniers(ma_chaine)
        print(f"Les 17 derniers caractères : {ta_chaine}")
        
        ##Alterner les minuscules et majuscules
        ma_chaine_alternee = alterner_min_maj(ma_chaine)
        print(f"MaChaine alternée (min/maj) : {ma_chaine_alternee}")
        
        ##Inverser la chaîne
        ma_chaine_inversee = inverser_chaine(ma_chaine)
        print(f"MaChaine inversée : {ma_chaine_inversee}")
        
        ##Construire une pyramide avec TaChaine
        pyramide = construire_pyramide(ta_chaine)
        print("Pyramide avec les 17 derniers caractères :")
        print(pyramide)
        
        ##Rechercher une sous-chaîne de taille spécifiée
        taille_sous_chaine = int(input("Entrez la taille de la sous-chaîne à rechercher : "))
        sous_chaine = rechercher_sous_chaine(ta_chaine, taille_sous_chaine)
        print(f"Sous-chaîne de taille {taille_sous_chaine} : {sous_chaine}")
        
        ##Transformer la chaîne en liste triée
        liste_triee = transformer_en_liste_triee(ta_chaine)
        print(f"Liste triée des caractères de TaChaine : {liste_triee}")
    
    except ValueError as e:
        print(f"Erreur : {e}")

##Exécuter le programme
if __name__ == "__main__":
    main()
