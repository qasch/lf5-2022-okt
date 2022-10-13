# Ausgabe
print("Ausgabe über den Builtin print()")

# Eingabe
# Der Variablen zahl wird das Ergebnis des Aufrufs
# der Funktion input() zugewiesen
zahl1 = int(input("Bitte gib eine Zahl ein: "))
zahl2 = int(input("Bitte gib eine weitere Zahl ein: "))

ergebnis = zahl1 + zahl2

# Ausgabe des Datentyps der Variable rueckgabe
# Dient hier zum Debugging, bzw. zum Nachvollziehen
# was intern in unserem Code passiert
# rueckgabe = type(ergebnis)
# print(rueckgabe)
# # Exakt gleiches Ergebnis wie oben, nur kürzer
# print(type(ergebnis))

# Casting (implizit/explizit) -> Typumwandlung
# Hier wichtig, damit unser Code weiterhin funktiniert
# und wir keine Fehlermeldung vom Typ TypeError mehr bekommen
ergebnis = str(ergebnis)
# Die folgenden drei Zeilen sind wieder Debugging-Statements
# Sie sind für die Ausführung unseres Scripts nicht notwendig,
# können daher auskommentiert werden
# print(type(ergebnis))
# # Exakt gleiches Ergebnis wie oben, nur kürzer
# print(type(str(ergebnis)))

# Ausgabe des Ergenisses unserer Rechenoperation
print("Ergebnis: " + ergebnis)
