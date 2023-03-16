Kleiderschrank = ["Hose", "T-Shirt", "Kleid"]
Kommode = ["Schuhe", "Socken", "Muetze"]

print("Im Kleiderschrank befindet sich:")
print(Kleiderschrank[0])
print(Kleiderschrank[1])
print(Kleiderschrank[2])

print ("Hier noch mal alle Inhalte aufgelistet")
print("")
for Kleidung in Kleiderschrank:
    print(Kleidung)

print("")
print("Der Pullover wurde hinzugefügt.")
print("")

Kleiderschrank.append("Pullover")
for Kleidung in Kleiderschrank:
    print(Kleidung)

print("")
print("Du hast deine Kommode erfolgreich verkauft und deine Kleidung wurde zum Kleiderschrank hinzugefügt")
print("")

Kleiderschrank += Kommode
for Kleidung in Kleiderschrank:
    print(Kleidung)