import random

# 1. Créer et initialiser une liste liste1 d'entiers d'une taille paramétrable supérieure à 20.
def create_list1(size):
    if size <= 20:
        print("La taille de la liste doit être supérieure à 20.")
        return []
    else:
        return [random.randint(1, 100) for _ in range(size)]

# 2. Créer et initialiser une liste liste2 d'entiers copiant les entiers impairs de liste1.
def create_list2(liste1):
    return [x for x in liste1 if x % 2 != 0]

# 3. Afficher les deux listes triées dans un ordre décroissant.
def display_sorted_lists(liste1, liste2):
    print("Liste1 triée décroissante:", sorted(liste1, reverse=True))
    print("Liste2 triée décroissante:", sorted(liste2, reverse=True))

# 4. Ajouter un ou plusieurs entiers à liste1 en fin de liste ou dans un emplacement spécifique.
def add_to_list(liste1, value, index=None):
    if index is None:
        liste1.append(value)
    else:
        liste1.insert(index, value)
    return liste1

# 5. Supprimer toutes les occurrences d'un entier entré par l'utilisateur dans liste1.
def remove_occurrences(liste1, value):
    return [x for x in liste1 if x != value]

# 6. Créer une liste liste3 avec des éléments aléatoires de liste1 et liste2.
def create_list3(liste1, liste2):
    size = random.randint(1, min(len(liste1), len(liste2)))
    return random.sample(liste1, size) + random.sample(liste2, size)

# 7. Inverser toute liste.
def reverse_list(lst):
    return lst[::-1]

# 8. Prendre les indices pairs de liste2 et les indices impairs de liste1.
def separate_pairs_and_impairs(liste1, liste2):
    l_pairs = [liste2[i] for i in range(0, len(liste2), 2)]
    l_impairs = [liste1[i] for i in range(1, len(liste1), 2)]
    return l_pairs, l_impairs

# Script principal
def main():
    #Etape 1
    size = int(input("Entrez la taille de la liste1 (supérieure à 20): "))
    liste1 = create_list1(size)

    #Étape 2
    liste2 = create_list2(liste1)

    #Étape 3
    display_sorted_lists(liste1, liste2)

    #Étape 4
    value = int(input("Entrez un entier à ajouter à liste1: "))
    index = input("Voulez-vous l'ajouter à un emplacement spécifique ? (O/N): ").strip().lower()
    if index == 'o':
        idx = int(input("Entrez l'index où vous voulez insérer la valeur: "))
        liste1 = add_to_list(liste1, value, idx)
    else:
        liste1 = add_to_list(liste1, value)
    print("Liste1 après ajout:", liste1)

    #Étape 5
    value_to_remove = int(input("Entrez un entier à supprimer de liste1: "))
    liste1 = remove_occurrences(liste1, value_to_remove)
    print("Liste1 après suppression:", liste1)

    #Étape 6
    liste3 = create_list3(liste1, liste2)
    print("Liste3 (éléments aléatoires de liste1 et liste2):", liste3)

    #Étape 7
    liste3_reversed = reverse_list(liste3)
    print("Liste3 inversée:", liste3_reversed)

    #Étape 8
    l_pairs, l_impairs = separate_pairs_and_impairs(liste1, liste2)
    print("Indices pairs de liste2:", l_pairs)
    print("Indices impairs de liste1:", l_impairs)

if __name__ == "__main__":
    main()
