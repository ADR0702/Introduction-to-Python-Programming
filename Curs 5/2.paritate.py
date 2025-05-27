numar=int(input("introduceti un numar\n"))
# versiunea 1
if numar % 2 ==0:
    print("numarul este par")   
else:
    print("numarul este impar")

# versiunea 2

print("numarul este par") if numar % 2 ==0 else print("numarul este impar")

# versiunea 3

print("numarul este impar") if numar % 2 !=0 else print("numarul este par")   
print("numarul este impar") if numar % 2 ==1 else print("numarul este par") 

# versiunea 4

print("numarul este par", numar%2==0)