# 1. Création et initialisation interactive de My_PC
def create_my_pc():
    my_pc = {}
    my_pc['processeur'] = input("Entrez le modèle du processeur : ")
    my_pc['ram'] = int(input("Entrez la quantité de RAM (en Go) : "))
    my_pc['stockage'] = int(input("Entrez la quantité de stockage (en Go) : "))
    my_pc['carte_graphique'] = input("Entrez le modèle de la carte graphique : ")
    my_pc['système_d’exploitation'] = input("Entrez le système d'exploitation : ")
    return my_pc

# 2. Afficher par une fonction paramétrable les clés de My_PC
def afficher_cle(my_pc):
    print("Clés du dictionnaire My_PC :")
    for cle in my_pc.keys():
        print(cle)

# 3. Afficher par une fonction paramétrable les valeurs de My_PC
def afficher_valeur(my_pc):
    print("Valeurs du dictionnaire My_PC :")
    for valeur in my_pc.values():
        print(valeur)

# 4. Fonction permettant l'extraction des clés dans une liste
def extraire_cle(my_pc):
    return list(my_pc.keys())

# 5. Fonction permettant l'extraction des valeurs dans une liste
def extraire_valeur(my_pc):
    return list(my_pc.values())

# 6. Fonction permettant la correction de la quantité de RAM
def corriger_ram(my_pc):
    nouvelle_ram = int(input("Entrez la nouvelle quantité de RAM (en Go) : "))
    my_pc['ram'] = nouvelle_ram
    print(f"La quantité de RAM a été mise à jour : {my_pc['ram']} Go")

# 7. Fonction permettant le tri de My_PC selon la quantité de stockage
def trier_par_stockage(pc_list):
    return sorted(pc_list, key=lambda pc: pc['stockage'], reverse=True)

# 8. Fonction permettant d'inverser deux paramètres du dictionnaire
def inverser_parametres(my_pc, param1, param2):
    if param1 in my_pc and param2 in my_pc:
        my_pc[param1], my_pc[param2] = my_pc[param2], my_pc[param1]
        print(f"Les paramètres {param1} et {param2} ont été échangés.")
    else:
        print("Un ou plusieurs paramètres ne sont pas présents dans le dictionnaire.")

# 9. Fonction permettant la sauvegarde de My_PC dans un autre dictionnaire CP_MyPC
def sauvegarder_pc(my_pc):
    cp_my_pc = my_pc.copy()
    print("My_PC a été sauvegardé dans CP_MyPC.")
    return cp_my_pc

# 10. Fonction affichant le PC le plus performant de My_PC
def afficher_pc_performant(pc_list):
    meilleur_pc = max(pc_list, key=lambda pc: (pc['ram'], pc['stockage']))
    print("Le PC le plus performant :")
    print(meilleur_pc)

# Programme principal
def main():
    # Création et initialisation interactive de My_PC
    my_pc = create_my_pc()

    # Affichage des clés et valeurs
    afficher_cle(my_pc)
    afficher_valeur(my_pc)

    # Extraction des clés et valeurs dans des listes
    clés = extraire_cle(my_pc)
    valeurs = extraire_valeur(my_pc)
    print("Clés extraites dans une liste :", clés)
    print("Valeurs extraites dans une liste :", valeurs)

    # Correction de la quantité de RAM
    corriger_ram(my_pc)

    # Sauvegarde de My_PC dans CP_MyPC
    cp_my_pc = sauvegarder_pc(my_pc)
    print("Dictionnaire sauvegardé :", cp_my_pc)

    # Inverser deux paramètres dans My_PC
    param1 = input("Entrez le premier paramètre à échanger : ")
    param2 = input("Entrez le deuxième paramètre à échanger : ")
    inverser_parametres(my_pc, param1, param2)
    print("Dictionnaire après échange :", my_pc)

    # Afficher le PC le plus performant
    pc_list = [my_pc]  # Exemple avec une seule entrée, mais peut être étendu à une liste de PC
    afficher_pc_performant(pc_list)

    # Trier les PC par stockage
    pc_list_sorted = trier_par_stockage(pc_list)
    print("PC triés par stockage :", pc_list_sorted)

if __name__ == "__main__":
    main()
