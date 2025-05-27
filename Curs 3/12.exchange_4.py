eur=4.97
usd=4.63
pounds=5.00

suma_in_ron =input("introduceti suma pe care doriti sa o schimbati\n")
suma_in_ron=int(suma_in_ron)

print("aveti:", suma_in_ron, "RON")

while True:
    moneda=input("introduceti moneda(euro/usd)\n")

    if moneda=="euro":
        suma_euro=suma_in_ron/eur
        print("Aveti in EURO", round(suma_euro,2))
        break
    elif moneda=="dollar":
        suma_dollar=suma_in_ron/usd
        print("aveti in USD:", round(suma_dollar,2))
        break
    elif moneda=="pounds":
        suma_pounds=suma_in_ron/pounds
        print("aveti in POUNDS:", round(suma_pounds,2))
        break
    else:
        print ("nu stim moneda")