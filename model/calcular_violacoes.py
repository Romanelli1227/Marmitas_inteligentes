from typing import Dict, List, Optional
from repositories import CatalogoAlimentos
from model.calcular_metricas import calcular_metricas

def calcular_violacoes(solucao: List[str], catalogo: CatalogoAlimentos,
                        capacidade_max: float, proteina_max: float,
                        carboidrato_max: float,
                        exigir_vegetal: Optional[bool] = None) -> Dict[str, float]:
    
    m = calcular_metricas(solucao, catalogo)
    return {
        "excesso_peso": max(0.0, m["peso_total"] - capacidade_max),
        "excesso_proteina": max(0.0, m["proteina_total"] - proteina_max),
        "excesso_carboidrato": max(0.0, m["carboidrato_total"] - carboidrato_max),
        "falta_vegetal": 1.0 if (exigir_vegetal is True and not m["tem_vegetal"]) else 0.0,
        "excesso_vegetal": 1.0 if (exigir_vegetal is False and m["tem_vegetal"]) else 0.0,
    }