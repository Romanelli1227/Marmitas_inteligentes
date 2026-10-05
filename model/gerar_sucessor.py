import random
from typing import List

from model.calcular_metricas import calcular_metricas
from repositories import catalogo

def gerar_sucessor(solucao_inicial: List[int]) -> List[List[int]]:
    indices_com_um = [i for i, val in enumerate(solucao_inicial) if val == 1]
    
    if not indices_com_um:
        return []

    indice_sorteado = random.choice(indices_com_um)
    
    sucessores = []

    for i in range(len(solucao_inicial)):
        if i != indice_sorteado and solucao_inicial[i] == 0:
            nova_solucao = solucao_inicial.copy()
            
            nova_solucao[indice_sorteado], nova_solucao[i] = nova_solucao[i], nova_solucao[indice_sorteado]
            
            sucessores.append(nova_solucao)
            
    return sucessores
