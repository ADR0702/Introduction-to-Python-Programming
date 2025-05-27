numere=[32,41,51,51,12,3,1,312,8,423]

# introduceti numar de la tastatura
# spuneti daca este in lista numere

numar_tastatura=int(input("introduceti un numar\n"))

for i in numere:
    if i == numar_tastatura:
        print(numar_tastatura,"este in lista")

# rezolvarea profesorului


numere=[32,41,51,51,12,3,1,312,8,423]

# introduceti numar de la tastatura
# spuneti daca este in lista numere

introdus=int(input("introduceti un numar\n"))
# versiunea 1
for i in numere:
    if i == introdus:
        print(introdus,"este in lista")
        break
else:
    print("Nu se afla in lista")


# versiunea 2
se_afla=False
for i in numere:
    if i == introdus:
        se_afla=True
if se_afla:
    print("se afla in lista")
else:
    print("nu se afla in lista")

# versiunea 3

if introdus in numere:
    print('se afla')
else:
    print("nu se afla")

    