import statistics

def calcular_media(lista):
    return statistics.mean(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_moda(lista):
    try:
        return statistics.mode(lista)
    except statistics.StatisticsError:
        return "Sem moda"

def calcular_variancia(lista):
    return statistics.variance(lista)

def calcular_desvio_padrao(lista):
    return statistics.stdev(lista)

def calcular_amplitude(lista):
    return max(lista) - min(lista)
