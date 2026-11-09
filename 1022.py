def obvodCtverce(a):
    return 4*a
def obvodObdelniku():
    a = float(input("strana a: "))
    b = float(input("strana b: "))
    print("Obvod obdelniku: ",2*a+2*b)
def obsahCtverce(a):
    return a**2
#obvodObdelniku()

def zeptase():
    while True:
        vek = int(input("Zadejte vek"))
        if vek>0 & vek<130:
            break
    if vek>18:
        print("osoba je plnoleta")
    else:
        print("osoba neni plnoleta")

def nacte():
    text = input("Zadejte text: ")
    text.strip()
    text = text[0].upper() + text[1:]
    text.replace(" ","_")
    print(text)
nacte()
