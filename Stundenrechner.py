print("Stundenrechner")
print("==============")

stunde = input ("Bitte gib an, wiviele Stunden du umrechnen willst: ")
if stunde.isdigit():

    minuten = int(stunde)*60
    sekunde = int(stunde)*60*60

    min = str(minuten)
    sek = str(sekunde)
    print("Das sind", min, "Minuten und " , sek, "Sekunden!\nWow!")
else:
    print("Bitte gib eine Nummer ein!")
    