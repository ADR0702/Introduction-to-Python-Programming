import random
while True:
    utilizator=int(input("introduceti un numar de la 1 la 10\n"))
    calculator= random.randint(1, 10)

    print(calculator)

    if utilizator == calculator:
        print ("felicitari, ati ghicit numarul")
        break
        
    else:
        print('Mai incearca')

