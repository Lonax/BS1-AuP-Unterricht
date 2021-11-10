Volt = float(input("Spannung in Volt"))
Ampere = float(input("Stromstärke in Ampere"))
# Ohm = float(input("Widerstand in Ohm"))
# Watt = float(input("Leistung in Watt"))

Ohm = Volt / Ampere
Watt = Volt * Ampere

print("Der Strom hat", Ohm, "Widerstand &", Watt, "Watt Stärke")
