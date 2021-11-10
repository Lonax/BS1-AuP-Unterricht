import numbers

Byte = float(input("Gebe die Anzahl an Bytes an"))

Megabyte = Byte * 1e-6
Mebibyte = Byte * 9.5367e-7

print(Byte, "Bytes entsprechen", Megabyte, "Megabyte", "oder", Mebibyte, "Mebibyte")