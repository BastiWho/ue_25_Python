print("\nKostenrechner")
print("=============")

rotwein = (12.99)
rose = (9.98)
weiss = (11.99)

anzahl_rot = float(input ("Anzahl Rotweinflaschen: "))
anzahl_rose = float(input ("Anzahl Roseweinflaschen: "))
anzahl_weiss = float(input ("Anzahl Weißweinflaschen: "))

rechnung_1 = anzahl_rot*rotwein
rechnung_2 = anzahl_rose*rose
rechnung_3 = anzahl_weiss*weiss

rechnung = rechnung_1+rechnung_2+rechnung_3

print("\nDie Gesamtkosten belaufen sich auf:", rechnung, "Euro.\n")