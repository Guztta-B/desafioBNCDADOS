from estatisticas import *

produtos = {
    f'produto{i+1}': round(10 + i * 1.5 + (i % 3) * 0.7, 2) for i in range(30)
}

valores = list(produtos.values())


print("Valores dos produtos:", valores)

print("Média:", calcular_media(valores))
print("Mediana:", calcular_mediana(valores))
print("Moda:", calcular_moda(valores))
print("Variância:", calcular_variancia(valores))
print("Desvio padrão:", calcular_desvio_padrao(valores))
print("Amplitude:", calcular_amplitude(valores))
