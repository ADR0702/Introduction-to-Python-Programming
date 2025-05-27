pret=int(input("introduceti pretu\n"))
prag=140_000

pret_cu_tva=(pret*1.05 if pret<prag else pret*1.2)

print('pret cu tva calculat este:', pret_cu_tva)


procent=1.05 if pret<prag else pret*1.2
print('pret cu tva calculat este:', pret*procent)