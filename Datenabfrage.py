print("   DATENABFRAGE")
print("---------------------\n")
print("Bitte geben Sie folgene Daten ein:\n")

name = input("Nachname: ")
vorname = input("Vorname: ")
alter = input("Alter: ")
plz = input("Postleitzahl: ")
ort = input("Wohnort: ")

print(vorname.capitalize(), name.capitalize(), "ist", alter, "Jahre alt und wohnt in", plz, ort.capitalize())