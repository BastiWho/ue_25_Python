import random

while True:

    witze = [
"Hast du ein Bad genommen?“ – Warum, fehlt eins?",
"Egal, wie gut du schläfst: Albert schläft wie Einstein",
"Wissenschaftler haben herausgefunden – und sind wieder reingegangen.",
"Sitzt einer im Stehcafé.",
"Wie heißt der Schutzpatron der Vergesslichen? – Dings",
"Hast du was zu trinken? – Wasser. – Nee, was Härteres! – Ok, Eis.",
"Was ist rot und steht im Wald? – Ein Kirsch",
"Was ist weiß und rollt den Berg rauf? – Eine Lawine mit Heimweh",
"Wie nennt man einen Bumerang, der nicht zurückkommt? – Stock",
"Was ist das Gegenteil von Reformhaus? – Reh hinterm Haus",
"Wie nennt man ein Delfin in Unterhose? – Slipper",
"Egal wie voll du bist, Rudi war Völler.",
]

    print(random.choice(witze))

    again = input("War gut? Wie wäre es mit noch einer Runde (j/n)? ").lower()
    if again != "j":
            break

print("\nHoffe du hattest Spaß. Bis später!\n")
input("Dücke eine beliebige Taste zum Beenden")
