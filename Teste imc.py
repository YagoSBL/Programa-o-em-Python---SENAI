def imc(altura,peso):
    return peso/altura**2

print(imc(1.70,65))


def imc2():
    peso = float(input('peso: '))
    altura = float(input('Altura: '))
    print(peso/altura**2)
imc2()


def imc3():
    print(peso/altura**2)
    return peso/altura**2


print(imc3()+ 250)