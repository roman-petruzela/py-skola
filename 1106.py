def jmenaIdent():
    import random

    jmena = ["Jana", "Petr", "Eva", "Tomáš", "Lucie"]

    jmenaID = []

    for jmeno in jmena:
        identifikator = random.randint(1000, 9999)
        jmenaID.append([jmeno, identifikator])

    print(jmenaID)

jmenaIdent()
