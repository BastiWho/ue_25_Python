Kleiderschrank = ["Hose", "T-Shirt", "Kleid"]
Kommode = ["Schuhe", "Socken", "Muetze"]

print("Im Kleiderschrank befindet sich:\n")
print(Kleiderschrank[0])
print(Kleiderschrank[1])
print(Kleiderschrank[2])

print ("\nHier noch mal alle Inhalte aufgelistet\n")
for Kleidung in Kleiderschrank:
    print(Kleidung)


print("\nDer Pullover wurde hinzugefügt.\n")


Kleiderschrank.append("Pullover")
for Kleidung in Kleiderschrank:
    print(Kleidung)

print("\nDu hast deine Kommode erfolgreich verkauft und deine Kleidung wurde zum Kleiderschrank hinzugefügt\n")

Kleiderschrank += Kommode
for Kleidung in Kleiderschrank:
    print(Kleidung)