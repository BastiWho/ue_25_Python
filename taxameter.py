km = int(input("Wieviele Kilometer bist du gefahren? "))
grundpreis = 4.50
if km > 4:
    kmpreis = 2.90
else:
    kmpreis = 3.30
costs = grundpreis + kmpreis * km
print ("Die Kosten für diese Fahrt waren:", costs, "€")