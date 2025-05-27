# suma_intreaga=int(input("introduceti o suma\n"))

# tens=suma_intreaga//10
# fives=suma_intreaga%tens//5
# twos=suma_intreaga%tens%fives//2
# ones=suma_intreaga%tens%fives//1

# print("tens=", tens)
# print("fives=", fives)
# print("twos", twos)
# print("ones=", ones)


# rezolvare proferor

suma=128
bancnote10=suma//10
print(bancnote10)
restul10=suma%10
print("rest=", restul10)

bancnote5=restul10//5
print("bancnote5=", bancnote5)
restul5= restul10%5
print("rest=", restul5)

bancnote2=restul5//2
print("bancnote 2=", bancnote2)

restul2= restul5%2
print('rest=', restul2)

bancnote1=restul2//1
print("bancnote 1=", bancnote1)