def soma(a,b):
    return a + b


def sub(a,b):
    return a - b


def calculdora():
 while True:       
        n1  =  float(input('= '))
        op =  input('+ ou -')
        if op == '+':
            n2  =  float(input('= '))
            print(soma(n1, n2))
        elif op == '-':
            n2  =  float(input('= '))
            print(sub(n1, n2))
        else:
            print('Digite algo válido')                
            
calculdora()