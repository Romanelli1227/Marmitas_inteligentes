from typing import Dict, List
from repositories import CatalogoAlimentos

def calcular_metricas(solucao: List[str], catalogo: CatalogoAlimentos) -> Dict[str, float]:
    peso_total = sum(catalogo[nome][0] for nome in solucao)
    proteina_total = sum(catalogo[nome][1] for nome in solucao)
    carboidrato_total = sum(catalogo[nome][2] for nome in solucao)
    tem_vegetal = any(catalogo[nome][3] for nome in solucao)
    return {
        "peso_total": peso_total,
        "proteina_total": proteina_total,
        "carboidrato_total": carboidrato_total,
        "tem_vegetal": tem_vegetal,
    }