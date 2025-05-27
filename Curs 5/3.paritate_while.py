
while True:
    numar=input("introduceti un numar\n")
    if numar.isnumeric():
        numar=int(numar)
    
        if numar % 2 ==0:
            print("numarul este par")   
        else:
            print("numarul este impar")
    else:
        print("nu ati introdus un numar")

