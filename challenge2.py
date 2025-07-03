notes_eleves = {
    "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2,
    "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,
    "Saad": 11.3, "Hannae": 9.8
}

etudiantAdmis = {}
etudiantNonAdmis = {}

for nom, note in notes_eleves.items():
    if note >= 10:
        etudiantAdmis[nom] = note
    else:
        etudiantNonAdmis[nom] = note

print("Étudiants admis :", etudiantAdmis)
print("Étudiants non admis :", etudiantNonAdmis)
