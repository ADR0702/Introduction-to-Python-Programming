

# cuvant="aerisirea"

cuvant="racecar"

# cuvant="elefaccafele"

# inceput=0
sfarsit=-1


for ch in cuvant:
    print(ch)
    if ch != cuvant[sfarsit]:
        print("nu este palindrom")
        break
    sfarsit=sfarsit -1
else:
    print("este palindrom")

