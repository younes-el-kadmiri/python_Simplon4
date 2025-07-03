etudiant_info = ("Yasmine", 22, "Informatique", 17.4)

print(f"Prenom : {etudiant_info[0]}")
print(f"Age : {etudiant_info[1]}")
print(f"Filiere : {etudiant_info[2]}")
print(f"Moyenne : {etudiant_info[3]}")

info_liste = list(etudiant_info)
info_liste[2] = "Mathematiques"
etudiant_info = tuple(info_liste)

print("Prenom et age :", etudiant_info[:2])

info_supp = ("Tres Bien", 2024)
etudiant_complet = etudiant_info + info_supp
print("Tuple final :", etudiant_complet)
