# Lists

# Lists können mehrere Werte aufnehmen,
# nicht nur einen einzigen wie Variablen
# Lists werden durch eckige Klammern [] definiert
# Lists können auch unterschiedliche Datentypen aufnehmen

# Index       0  ,   1   ,    2
strings = ["hund", "igel", 'kuckuck']
zahlen = [1, 3, 5, 9, 3]
my_list = [1, True, "irgendwas", 837.234234234]

# element = strings[3]
# print(element)

# Deklaration der List all_ints
all_ints = []

# Lists sind dynamisch/veränderlich

# Hinzufügen von Elementen zur List
all_ints.append("hund")
all_ints.append("katze")
# all_ints.append("igel")

# Ausgabe der Elemente
print(all_ints[0])
print(all_ints[1])
# print(all_ints[2])

# while-loop zur Ausgabe aller Elemente der List
print("Ausgabe while-Loop:")

zaehler = 0
anzahl_elemente_in_liste = len(all_ints)
while zaehler < anzahl_elemente_in_liste:
    print("Zaehler: " + str(zaehler))   # Debugging Info
    print(all_ints[zaehler])
    # zahler = zaehler + 1
    zaehler += 1


all_ints.remove("katze")




