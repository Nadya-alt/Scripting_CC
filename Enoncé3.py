# 1. Création et initialisation de Mon_pc
def create_mon_pc():
    mon_pc = {}
    mon_pc['processeur'] = input("Entrez le modèle du processeur : ")
    mon_pc['ram'] = int(input("Entrez la quantité de RAM (en Go) : "))
    mon_pc['stockage'] = int(input("Entrez la quantité de stockage (en Go) : "))
    mon_pc['carte_graphique'] = input("Entrez le modèle de la carte graphique : ")
    mon_pc['système_d’exploitation'] = input("Entrez le système d'exploitation : ")
    return mon_pc

# 2. Afficher les clés de Mon_PC
def afficher_cle(mon_pc):
    for cle in mon_pc:
        print(cle)

# 3. Afficher les valeurs de Mon_PC
def afficher_valeur(mon_pc):
    for valeur in mon_pc.values():
        print(valeur)

# 4. Extraire les clés dans une liste
def extraire_cle(mon_pc):
    return list(mon_pc.keys())

# 5. Extraire les valeurs dans une liste
def extraire_valeur(mon_pc):
    return list(mon_pc.values())

# 6. Modifier la quantité de RAM
def corriger_ram(mon_pc):
    mon_pc['ram'] = int(input("Entrez la nouvelle quantité de RAM (en Go) : "))
    print(f"La quantité de RAM a été mise à jour : {mon_pc['ram']} Go")

# 7. Trier les PC par stockage
def trier_par_stockage(pc_list):
    pc_list.sort(key=lambda pc: pc['stockage'], reverse=True)
    return pc_list

# 8. Inverser deux paramètres du dictionnaire
def inverser_parametres(mon_pc, param1, param2):
    if param1 in mon_pc and param2 in mon_pc:
        mon_pc[param1], mon_pc[param2] = mon_pc[param2], mon_pc[param1]
    else:
        print("Un ou plusieurs paramètres ne sont pas présents.")

# 9. Sauvegarder Mon_PC dans un autre dictionnaire
def sauvegarder_pc(mon_pc):
    return mon_pc.copy()

# 10. Afficher le PC le plus performant
def afficher_pc_performant(pc_list):
    pc_performant = max(pc_list, key=lambda pc: (pc['ram'], pc['stockage']))
    print("Le PC le plus performant : ", pc_performant)

# Programme principal
def main():
    mon_pc = create_mon_pc()

    afficher_cle(mon_pc)
    afficher_valeur(mon_pc)

    clés = extraire_cle(mon_pc)
    valeurs = extraire_valeur(mon_pc)
    print("Clés extraites :", clés)
    print("Valeurs extraites :", valeurs)

    corriger_ram(mon_pc)

    cp_mon_pc = sauvegarder_pc(mon_pc)
    print("Dictionnaire sauvegardé : ", cp_mon_pc)

    param1 = input("Entrez le premier paramètre à échanger : ")
    param2 = input("Entrez le deuxième paramètre à échanger : ")
    inverser_parametres(mon_pc, param1, param2)
    print("Dictionnaire après échange :", mon_pc)

    pc_list = [mon_pc]
    afficher_pc_performant(pc_list)

    pc_list_sorted = trier_par_stockage(pc_list)
    print("PC triés par stockage :", pc_list_sorted)

if __name__ == "__main__":
    main()
