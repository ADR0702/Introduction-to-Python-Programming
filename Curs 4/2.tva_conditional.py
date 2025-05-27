
# rezolvare proprie
apartament=int(input("introduceti un pret\n"))
tva5=apartament*1.05
tva19=apartament*1.19

if apartament < 140000:
    print(tva5)
else:
    print(tva19)

#  rezolvare profesor

pret=int(input("introduceti pretu\n"))
prag=140_000
if pret < prag:
    print("pret mai mic")
    pret_cu_tva=pret*1.05
elif pret == prag:
    print ("pret este egal")
    pret_cu_tva=pret*1.2
else:
    print("pret mai mare")
    pret_cu_tva=pret*1.2

print("pret cu tva calculat este:", pret_cu_tva)
