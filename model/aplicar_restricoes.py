from typing import List, Optional
import random
from repositories import CatalogoAlimentos
from model.validar_solucao import validar_solucao

def aplicar_restricoes(solucao: List[str], catalogo: CatalogoAlimentos,
                        capacidade_max: float, proteina_max: float,
                        carboidrato_max: float,
                        exigir_vegetal: Optional[bool] = None,
                        max_tentativas: int = 100) -> List[str]:
    
    solucao = list(solucao)

    for _ in range(max_tentativas):
        valida, viol = validar_solucao(solucao, catalogo, capacidade_max, proteina_max, carboidrato_max, exigir_vegetal)
        if valida:
            break

        if viol["falta_vegetal"]:
            nao_vegetais = [n for n in solucao if not catalogo[n][3]]
            candidatos = [n for n in catalogo if catalogo[n][3] and n not in solucao]
            if nao_vegetais and candidatos:
                sai = random.choice(nao_vegetais)
                solucao[solucao.index(sai)] = random.choice(candidatos)
            continue

        if viol["excesso_vegetal"]:
            vegetais = [n for n in solucao if catalogo[n][3]]
            candidatos = [n for n in catalogo if not catalogo[n][3] and n not in solucao]
            if vegetais and candidatos:
                sai = random.choice(vegetais)
                solucao[solucao.index(sai)] = random.choice(candidatos)
            continue


        dimensao = max(("excesso_peso", 0), ("excesso_proteina", 1),
                        ("excesso_carboidrato", 2), key=lambda par: viol[par[0]])[1]
        pior_item = max(solucao, key=lambda n: catalogo[n][dimensao])
        candidatos = [n for n in catalogo if n not in solucao]
        if candidatos:
            solucao[solucao.index(pior_item)] = random.choice(candidatos)
        else:
            solucao.remove(pior_item)  # sem alternativa -> só remove

    return solucao
