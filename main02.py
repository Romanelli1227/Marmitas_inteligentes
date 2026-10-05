from repositories.catalogo import catalogo
from model.gerar_solucao_inicial import gerar_solucao_inicial
from model.gerar_problema import gerar_problema, gerar_problema_binario
from model.gerar_marmita_inicial import gerar_marmita_inicial
from model.gerar_sucessor import gerar_sucessor
from model.calcular_metricas import calcular_metricas


def dados_sucessor(lista_porcoes, catalogo):

    metricas = calcular_metricas(lista_porcoes, catalogo)
    valor = (metricas["proteina_total"]+ metricas["carboidrato_total"])

    return{
        "peso_total": metricas["peso_total"],
        "proteina_total": metricas["proteina_total"],
        "carboidrato_total": metricas["carboidrato_total"],
        "tem_vegetal": metricas["tem_vegetal"],
        "valor": valor
    }

tamanho_lista_porcoes = 6
numero_porcoes_MAX = 3
problema_mapeado = gerar_problema(tamanho_lista_porcoes)
#vetor_binario = gerar_marmita_inicial(numero_porcoes_MAX, vetor_binario)
print(f'Problema mapeado: {problema_mapeado}')
vetor_binario = gerar_problema_binario(problema_mapeado)
print(f'Vetor_binario: {vetor_binario}')

vetor_binario_zeros = gerar_marmita_inicial(numero_porcoes_MAX,vetor_binario)
print(f'Vetor_binario_zeros: {vetor_binario_zeros}')
print(f'Vetor_binario: {vetor_binario}')
vetores_sucessores = gerar_sucessor(vetor_binario)
print(f'Vetores sucessores: {vetores_sucessores}')

#Problema mapeada = Lista inical de porções selecionadas
#Vetor binario = lista de zeros e uns que representa a seleção das porções do problema mapeado
lista_sucessores = []
for sucessor in vetores_sucessores:
    melhor_sucessor = None
    melhor_valor = 0

    lista_nomes_porcoes = [
        problema_mapeado[i]
        for i in range(len(sucessor))
        if sucessor[i] == 1
    ]
    metricas = calcular_metricas(
        lista_nomes_porcoes,
        catalogo
    )

    valor = (
        metricas["proteina_total"]
        + metricas["carboidrato_total"]
    )

    item ={
        "vetor_binario": sucessor,
        "lista_nomes_porcoes": lista_nomes_porcoes,
        "valor":valor
    }
    lista_sucessores.append(item)
    
    
'''
while True:


    vetores_sucessores = lista_sucessores

    for i in vetores_sucessores:
        print(f"Sucessor: {i['vetor_binario']}\nAlimentos: {i['lista_nomes_porcoes']}\nValor: {i['valor']}\n")

    melhor_sucessor = None
    melhor_valor = 0
    print("___________________________________________________________________________________")
    print(sucessor)
    print("___________________________________________________________________________________")
    for sucessor in vetores_sucessores:
        
        lista_nomes_porcoes = [
            lista_sucessores[i]["lista_nomes_porcoes"][0]
            for i in range(len(sucessor))
            if lista_sucessores[i]["lista_nomes_porcoes"][0] == 1
        ]

        

        valor = (
            metricas["proteina_total"]
            + metricas["carboidrato_total"]
        )

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_sucessor = sucessor

    if melhor_sucessor is not None:
        vetor_binario = melhor_sucessor["vetor_binario"]
        valor_atual = melhor_valor

    else:
        print('Melhor solução encontrada:')
        print(vetor_binario)
        #aqui o vetor binário é usado para criar o vetor de keys para vascular o dicionário
        lista_nomes_porcoes = [
            problema_mapeado[i] for i in range(len(vetor_binario))
            if vetor_binario[i] == 1
        ]
        metricas = calcular_metricas(lista_nomes_porcoes, catalogo)
        dados_sucessor = dados_sucessor(lista_nomes_porcoes, catalogo)
        print(f"|| Alimentos na melhor solução: { lista_nomes_porcoes}\n|| Métricas da solução: {metricas}\n|| Valor da solução: {dados_sucessor['valor']} ",)
        #print(f"Valor da solução: {dados_sucessor['valor']}")
        break
'''
lista_nomes_porcoes_atual = [
    problema_mapeado[i]
    for i in range(len(vetor_binario))
    if vetor_binario[i] == 1
]
metricas_atual = calcular_metricas(lista_nomes_porcoes_atual, catalogo)
valor_atual = metricas_atual["proteina_total"] + metricas_atual["carboidrato_total"]

while True:

    print("SUCESSORES ATUAIS")
    print("___________________________________________________________________________________")

    for sucessor in lista_sucessores:
        print(
            f"Sucessor: {sucessor['vetor_binario']}\n"
            f"Alimentos: {sucessor['lista_nomes_porcoes']}\n"
            f"Valor: {sucessor['valor']}\n"
        )

    melhor_sucessor = None
    melhor_valor = valor_atual

    for sucessor in lista_sucessores:
        if sucessor["valor"] > melhor_valor:
            melhor_valor = sucessor["valor"]
            melhor_sucessor = sucessor

    if melhor_sucessor is not None:

        vetor_binario = melhor_sucessor["vetor_binario"]
        valor_atual = melhor_sucessor["valor"]
        print("___________________________________________________________________________________")
        print("MELHOR SUCESSOR:")
        print(vetor_binario)
        print("Valor:", valor_atual)
        print("___________________________________________________________________________________")

        novos_vetores = gerar_sucessor(vetor_binario)
        lista_sucessores = []

        for sucessor in novos_vetores:
            lista_nomes_porcoes = [
                problema_mapeado[i]
                for i in range(len(sucessor))
                if sucessor[i] == 1
            ]

            metricas = calcular_metricas(lista_nomes_porcoes, catalogo)
            valor = metricas["proteina_total"] + metricas["carboidrato_total"]

            lista_sucessores.append({
                "vetor_binario": sucessor,
                "lista_nomes_porcoes": lista_nomes_porcoes,
                "valor": valor
            })

    else:
        print("Melhor solução encontrada:")
        print(vetor_binario)

        lista_nomes_porcoes = [
            problema_mapeado[i]
            for i in range(len(vetor_binario))
            if vetor_binario[i] == 1
        ]

        metricas = calcular_metricas(lista_nomes_porcoes, catalogo)
        dados = dados_sucessor(lista_nomes_porcoes, catalogo)

        print(
            f"|| Alimentos na melhor solução: {lista_nomes_porcoes}\n"
            f"|| Métricas da solução: {metricas}\n"
            f"|| Valor da solução: {dados['valor']}"
        )

        break