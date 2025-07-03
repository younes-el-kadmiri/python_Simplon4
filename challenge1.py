First_dict = {
    "Appareil": "Laptop",
    "Marque": "IBM",
    "Carte mère": "MSI Z490",
    "Carte Graphique": "GeForce RTX 3070",
    "RAM": "16G",
    "Processeur": "Intel core i7-G11",
    "SSD": "1 To"
}

First_dict["RAM"] = "32G"

print("Cles :", list(First_dict.keys()))
print("Valeurs :", list(First_dict.values()))
print("Paires cle-valeur :", list(First_dict.items()))

First_dict["Processeur"], First_dict["Carte Graphique"] = First_dict["Carte Graphique"], First_dict["Processeur"]

First_dict["Système d'exploitation"] = "Windows 10"

print("\nDictionnaire modifie :", First_dict)
