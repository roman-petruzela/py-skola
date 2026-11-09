def vypisklesajici(n):
    print(n)
    if n ==1:
        return 1
    else:
        return n-vypisklesajici(n-1)

#vypisklesajici(800)

def vypisrostouci(n):
    if n ==1:
        return 1
    vypisrostouci(n-1)
    print(n)

#vypisrostouci(800)

def mocnina(zaklad, exponent):
    if exponent ==0:
        return 1
    return zaklad * mocnina(zaklad, exponent-1)

print(mocnina(5,4))
