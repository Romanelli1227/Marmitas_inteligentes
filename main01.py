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

if __name__ == "__main__":
    # 1. Gera a lista de porções sorteadas passando o tamanho desejado
    problema_mapeado = gerar_problema(tamanho_lista_porcoes)
    print("Porções selecionadas:")
    print(problema_mapeado)

    # 2. Gera a lista binária (zeros) baseada no tamanho do problema gerado
    vetor_binario = gerar_problema_binario(problema_mapeado)
    print("___________________________________________________________________________________")
    print("\nVetor binário inicial:")
    print(vetor_binario)
    print(vetor_binario)

    print("___________________________________________________________________________________")
    print(f"Lista problema tem tamanho = [{len(problema_mapeado)}]")
    print(f"Lista problema tem tamanho = [{len(vetor_binario)}]")
    print("___________________________________________________________________________________")
    vetor_binario_modificado = gerar_marmita_inicial(numero_porcoes_MAX=numero_porcoes_MAX,lista_porcoes_binaria=vetor_binario)
    print(vetor_binario)
    #print(vetor_binario_modificado)
    print("___________________________________________________________________________________")
    for i in range(len(vetor_binario)):
        if vetor_binario[i] == 1:
            print(f"Item da marmita: {problema_mapeado[i]}")
    print("___________________________________________________________________________________")
    print(f"Lista inicial:\n {vetor_binario}")
    print("___________________________________________________________________________________")
    vetores_sucessores = gerar_sucessor(vetor_binario)
    for idx, sucessor in enumerate(vetores_sucessores, 1):
        print(f"Sucessor {idx}: {sucessor}")
        print("Itens desta marmita:")
        
        lista_nomes_porcoes = [problema_mapeado[j] for j in range(len(sucessor)) if sucessor[j] == 1]       
        # Percorre as posições do SUCESSOR ATUAL para saber os alimentos selecionados nele
        for j in range(len(sucessor)):
            if sucessor[j] == 1:
                print(f"  - [{j}] {problema_mapeado[j]}")
        metricas = calcular_metricas(lista_nomes_porcoes, catalogo)
        print(f"Metricas do Sucessor {idx}: {metricas}")
        valor = metricas["proteina_total"] + metricas["carboidrato_total"]
        print(f"Valor do sucessor: {valor}")
        print("___________________________________________________________________________________")
        
print('Outro dia:\n\n')
vetor_binario = gerar_marmita_inicial(
    numero_porcoes_MAX=numero_porcoes_MAX,
    lista_porcoes_binaria=vetor_binario
)

print("Solução inicial:")
print(vetor_binario)
lista_nomes_porcoes = [
    problema_mapeado[i] for i in range(len(vetor_binario))
    if vetor_binario[i] == 1
    ]
metricas = calcular_metricas(lista_nomes_porcoes,catalogo)

valor_atual = (metricas["proteina_total"]+ metricas["carboidrato_total"])
print(f"Metricas da solução inicial: Proteina: {metricas['proteina_total']}, Carboidrato: {metricas['carboidrato_total']}")
print(f"Valor da solução inicial: {valor_atual}")
print("___________________________________________________________________________________")
print("___________________________________________________________________________________")
melhor_sucessor = None
melhor_valor = valor_atual

print('Aki é o loop')
for sucessor in vetores_sucessores:

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

    print("Sucessor:", sucessor)
    print("Alimentos:", lista_nomes_porcoes)
    print("Proteína:", metricas["proteina_total"])
    print("Carboidrato:", metricas["carboidrato_total"])
    print("Valor:", valor)
    print()

while True:

    vetores_sucessores = gerar_sucessor(vetor_binario)

    melhor_sucessor = None
    melhor_valor = valor_atual
    print("___________________________________________________________________________________")
    print(sucessor)
    print("___________________________________________________________________________________")
    for sucessor in vetores_sucessores:

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

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_sucessor = sucessor

    if melhor_sucessor is not None:
        vetor_binario = melhor_sucessor
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