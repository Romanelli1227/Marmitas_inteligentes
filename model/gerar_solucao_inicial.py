import random
from typing import List
from repositories.catalogo import CatalogoAlimentos

def gerar_solucao_inicial(catalogo: CatalogoAlimentos, num_porcoes) -> List[str]:
    # 1. Pega todas as chaves (nomes dos alimentos) do dicionário
    nomes_alimentos = list(catalogo.keys())
    
    # 2. Garante que não tente sortear mais itens do que existem no catálogo
    k = min(num_porcoes, len(nomes_alimentos))
    
    # 3. Sorteia 'k' alimentos aleatórios da lista sem repetição
    marmita_sorteada = random.sample(nomes_alimentos, k)
    
    return marmita_sorteada