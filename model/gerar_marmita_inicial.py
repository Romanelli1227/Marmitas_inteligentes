import random

def gerar_marmita_inicial(numero_porcoes_MAX: int, lista_porcoes_binaria):
    lista_porcoes = lista_porcoes_binaria.copy()
    for i in range(numero_porcoes_MAX):
        numero_randomico = random.randint(0, len(lista_porcoes_binaria) - 1)
        lista_porcoes_binaria[numero_randomico] = 1
    return lista_porcoes