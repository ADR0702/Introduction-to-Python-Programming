# rezolvare proprie

# x0=3
# y0=3
# width=6
# height=6

# userx=int(input("Coordonate userx=\n"))
# usery=int(input("Coordonate usery=\n"))

# print("esti in zona") if userx <=width else print("nu esti in zona")
# print("esti in zona") if userx <=height else print("nu esti in zona")

# rezolvare profesor
x0=3
y0=3
width=6
height=6

userx=int(input("Coordonate userx=\n"))
usery=int(input("Coordonate usery=\n"))

if userx >x0:
    if userx < x0+width:
        if usery>0:
            if usery<y0+height:
                print("esti in zona")
            else: 
                print("nu esti in zona")
        else:
            print("nu esti in zona")
else:
    print("nu esti in zona")

# Varianta 2 mai scurta
if userx>x0 and userx<x0+width and usery>0 and usery<y0+height:
    print("esti in zona")
else:
    print("nu esti in zona")

# varianta 3 si mai scurta:
if x0<userx<x0+width and y0<usery<y0+height:
    print("esti in zona")
else:
    print("nu esti in zona")