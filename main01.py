from repositories.catalogo import catalogo
from model.gerar_problema import gerar_problema, gerar_problema_binario
from model.gerar_marmita_inicial import gerar_marmita_inicial
from model.gerar_sucessor import gerar_sucessor
from model.calcular_metricas import calcular_metricas
from model.subida_encosta import subida_encosta_por_tentativas

tamanho_lista_porcoes = 6
numero_porcoes_MAX = 3
problema_mapeado = gerar_problema(tamanho_lista_porcoes)

# --- FUNÇÕES ADAPTADORAS PARA O ALGORITMO ---
def gerar_inicial_adaptado():
    vetor_base = gerar_problema_binario(problema_mapeado)
    gerar_marmita_inicial(numero_porcoes_MAX, vetor_base)
    return vetor_base

def calcular_pontuacao_adaptado(vetor):
    lista_nomes = [
        problema_mapeado[i] for i in range(len(vetor)) if vetor[i] == 1
    ]
    metricas = calcular_metricas(lista_nomes, catalogo)
    return metricas["proteina_total"] + metricas["carboidrato_total"]

def avaliar_solucao_adaptado(vetor):
    lista_nomes = [
        problema_mapeado[i] for i in range(len(vetor)) if vetor[i] == 1
    ]
    metricas = calcular_metricas(lista_nomes, catalogo)
    # Retorna True se tiver vegetal, False caso contrário
    return metricas["tem_vegetal"]

def dados_sucessor(lista_porcoes, catalogo):
    metricas = calcular_metricas(lista_porcoes, catalogo)
    valor = (metricas["proteina_total"] + metricas["carboidrato_total"])
    return{
        "peso_total": metricas["peso_total"],
        "proteina_total": metricas["proteina_total"],
        "carboidrato_total": metricas["carboidrato_total"],
        "tem_vegetal": metricas["tem_vegetal"],
        "valor": valor
    }

# --- EXECUÇÃO ---
if __name__ == "__main__":
    print(f'Problema mapeado: {problema_mapeado}')
    
    melhor_marmita = subida_encosta_por_tentativas(
        num_tentativas=10, 
        gerar_inicial=gerar_inicial_adaptado, 
        gerar_sucessores=gerar_sucessor, 
        calcular_pontuacao=calcular_pontuacao_adaptado,
        avaliar_solucao=avaliar_solucao_adaptado
    )

    print("\n___________________________________________________________________________________")
    print("A melhor combinação de marmita encontrada (vetor binário) foi:", melhor_marmita)

    if melhor_marmita:
        lista_final = [
            problema_mapeado[i] for i in range(len(melhor_marmita)) if melhor_marmita[i] == 1
        ]
        metricas_finais = calcular_metricas(lista_final, catalogo)
        dados_finais = dados_sucessor(lista_final, catalogo)
        
        print(f"|| Alimentos na melhor solução: {lista_final}")
        print(f"|| Métricas da solução: {metricas_finais}")
        print(f"|| Valor da solução: {dados_finais['valor']}")
    print("___________________________________________________________________________________")