cuvant="abba"
print("lungimea", len(cuvant))

for i in range(len(cuvant)//2):
    print("i=", i, "ch=", cuvant[i])
    if cuvant[i]!=cuvant[-1-i]:
        print("nu este palindrom")
        break
else:
    print("cuvantul este palindrom")




