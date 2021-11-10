import numbers

Listenpreis = float(input("Listenpreis in €"))
L_Rabatt = float(input("Lieferrantenrabatt in %"))

Einkaufspreis_rabatt = Listenpreis / 100 * L_Rabatt
Einkaufspreis_output = Listenpreis - Einkaufspreis_rabatt

print("Der Einkaufspreis ist",Einkaufspreis_output, "€")