
bancnote=[100,50,20,10,5]

# bancnote=[10, 5, 2, 1,]


# print(type(bancnote))
suma_initiala=int(input("introduceti suma\n"))
suma=suma_initiala

for valoare in bancnote:
    # print(valoare)
    nr_bancnote=suma//valoare
    print (f"Valoarea {valoare} ai {nr_bancnote} bancnote")

    suma=suma%valoare
print(suma)
print(suma_initiala)