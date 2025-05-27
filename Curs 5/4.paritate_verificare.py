

numar=input("introduceti un numar\n")
# if numar.isnumeric():
#     numar=int(numar)
# else:
#     numar=input("introduceti un numar\n")

#     if numar.isnumeric():
#         numar=int(numar)
#     else:
#         numar=input("introduceti un numar\n")

#         if numar.isnumeric():
#             numar=int(numar)
#         else:
#             numar=input("introduceti un numar\n")


# while numar.isnumeric()==False:

while not numar.isnumeric():
    numar=input("introduceti un numar\n")

numar=int(numar)


if numar % 2 ==0:
    print("numarul este par")   
else:
    print("numarul este impar")