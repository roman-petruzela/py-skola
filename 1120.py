def seznamDenNahod():
    import random
    dny=["po","ut","st","ct","pa","so","ne"]
    vyber = random.choice(dny)
    while True:
        guess = input("Hadej den: ")
        if guess == "*":
            print("Ok, koncim.")
        elif guess == vyber:
            print("Spravne")
        else:
            print("Spatne")
            continue
        return
#seznamDenNahod()

def generujecisel():
    import random
    kolik = random.randint(0,100)
    cisla= []
    for i in range(kolik):
        cisla.append(random.randint(-1000,1000))
    cisla.sort()
    while True:
        volba=input("Zadej volbu: 1-vypis, 2-maxmin, 3-konec:\n")
        if volba=="1":
            for c in cisla: print(c)
        elif volba=="2": print("max: ", max(cisla)," min: ", min(cisla))
        elif volba=="3":
            cisla.clear()
            for i in range(kolik):
                cisla.append(random.randint(-1000,1000))
            cisla.sort()
        elif volba=="4":
            prumer=sum(cisla)/len(cisla)
            print("prumerna hodnota: ", prumer)
            for e in cisla:
                if e>prumer:print(e)
        elif volba=="5": return
        else: print("chybna hodnota")

def generujecisel2():
    import random
    kolik = random.randint(0,100)
    cisla= []
    for i in range(kolik):
        cisla.append(random.randint(-1000,1000))
    cisla2=cisla.copy()
    while True:
        volba=input("Zadej volbu: 1-vypis, 2-maxmin, 3-konec:\n")
        if volba=="1":
            for c in cisla: print(c)
        elif volba=="2":
            cisla2.sort()
            for c in cisla2: print(c)
        elif volba=="3":
            cisla2.sort(reverse=True)
            for c in cisla2: print(c)
        elif volba=="4": return
        else: print("chybna hodnota")

def nakemena():
    jmena = ["kamil socha","frajer velky", "frajer mensi", "jan novak", "mi bombo"]
    seznam =[]
    for i in jmena:
        r = i.split()
        print(r)
        n=""
        for c in r:
            c= c.capitalize()
            n+=c+" "
        seznam.append(n[:-1])
    print(seznam)

def nakemena2(jmena):
    return [" ".join(slovo.capitalize() for slovo in jmeno.split()) for jmeno in jmena]

jmena = ["kamil socha", "frajer velky", "frajer mensi", "jan novak", "mi bombo"]
print(nakemena2(jmena))
