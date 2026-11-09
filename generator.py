import random

# kmeny přídavných jmen, koncovka se doplní podle rodu (ý / á / é)
pridavna = [
    "vypatlan",
    "zabedněn",
    "natvrdl",
    "přiblbl",
    "tupohlav",
    "ujet",
    "slintav",
    "zablešen",
    "rozcuchan",
    "upocen",
    "zaostal",
    "připitom",
]

# podstatná jména v 5. pádě, rozdělená podle rodu
podstatna = {
    "ý": ["hňupe", "tumpachu", "truhlíku", "ťulpasi", "kokosi", "budižkničemu", "ňoumo", "moulo", "šmudlo", "vole","kamile"],
    "á": ["trubko", "bambulo", "nádivko", "trumpeto", "káčo", "bábovko"],
    "é": ["jelito", "pako", "dřevo", "nemehlo", "trdlo", "hovado"],
}


def nahodna_nadavka():
    koncovka = random.choice(list(podstatna))
    pridavne = random.choice(pridavna) + koncovka
    podstatne = random.choice(podstatna[koncovka])
    return f"ty {pridavne} {podstatne}"


if __name__ == "__main__":
    pocet = int(input("Kolik nadávek chceš? "))
    for _ in range(pocet):
        print(nahodna_nadavka())
