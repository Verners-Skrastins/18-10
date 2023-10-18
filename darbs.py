def iegut_datus(fails):
    dati = open(fails, 'r')
    skaitli = dati.read()
    return skaitli.split(' ')
dati = iegut_datus('skaitli.txt')

def saskaitit(skaitli):
    rezultats = 0
    for i in skaitli:
        rezultats += int(i)
    return rezultats
def skaitlu_skaits(skaitli):
    rezultats = 0
    for i in skaitli:
        rezultats += 1
    return rezultats
def videjais(skaitli):
    summa = saskaitit(skaitli)
    skaits = skaitlu_skaits(skaitli)
    rezultats = summa // skaits
    return rezultats
print("Summa ir ", saskaitit(dati), '. Kopā ir ', skaitlu_skaits(dati),' skaitļi. To aritmētiskais vidējais ir ', videjais(dati))

