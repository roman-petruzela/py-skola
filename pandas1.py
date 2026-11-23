import pandas
def pr0():
    mesta = pandas.read_csv("mesta.csv",encoding="utf-8")
    print(mesta)

def pr1():
    mesta = pandas.read_csv("mesta.csv",encoding="utf-8")
    print(mesta.info(),"\n\n")
    linky=mesta["linky"]
    print(linky,"\n\n")
    print(
        linky.sum(),
        linky.mean(),#prumer
        linky.median(),
        linky.max(),
        linky.min()
    )

def pr2():
    mesta = pandas.read_csv("mesta.csv",encoding="utf-8")
    mesta['vymera']=mesta['vymera'].round(0)
    print(mesta)

def pr3():
    mesta = pandas.read_csv("mesta.csv",encoding="utf-8")
    print(  mesta.iloc[0,0],
        mesta.shape
    )
    mesta.to_csv("mestaOprava.csv")

def pr4(cesta):
    tabul = pandas.read_csv(cesta,encoding="utf-8")
    radky = tabul.shape
    for i in range(radky[0]):
        hodnota= tabul.iloc[i,0]
        hodnota= hodnota.capitalize()
        tabul.iloc[i,0] =hodnota
    tabul.to_csv("oprava"+cesta,index=False,encoding="utf-8")
#pr4("mesta.csv")

def pr5(cesta):
    tabul = pandas.read_csv(cesta,encoding="utf-8")
    radky = tabul.shape
    for i in range(radky[0]):
        hodnota= tabul.iloc[i,2]
        hodnota=hodnota.replace(" ","")
        tabul.iloc[i,2] =hodnota
    tabul.to_csv("oprava"+cesta,index=False,encoding="utf-8")
    tabul.to_html("oprava"+cesta+".html",index=False,encoding="utf-8")
#pr5("mesta.csv")

def pr6():
    tabul = pandas.read_csv("mesta2.csv",encoding="utf-8")
    prumer = tabul["obyvatel"].mean()
    print("Prumerny pocet obyvatel: ",prumer)
    radky = tabul.shape
    for i in range(radky[0]):
        hodnota= tabul.iloc[i,2]
        if hodnota>prumer:
            print(tabul.iloc[i,0],tabul.iloc[i,1], tabul.iloc[i,2])

def pr7():
    mesta = pandas.read_csv("mesta2.csv",encoding="utf-8")
    mesta2=mesta[["kraj","mesto"]].copy()
    jmeno=input("Zadej jmeno: ")
    mesta2.to_csv(jmeno if jmeno.endswith(".csv") else jmeno + ".csv", index=False, encoding="utf-8")
pr7()
