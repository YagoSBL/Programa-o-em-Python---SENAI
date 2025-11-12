import statistics

def estatistica (lista_notas):
    
                            
    media = statistics.mean(lista_notas)
    print("Média: ", media)

def estatistica1 (notas_alunos):
                        
    moda = statistics.mode(notas_alunos)
    print("Moda: ", moda)

def estatistica2 (lista3):
                             
    desvio_padrao = statistics.mean(lista3)
    print("Desvio padrão: ", desvio_padrao)    

