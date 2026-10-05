from typing import Dict, List, Tuple, Optional
from repositories import CatalogoAlimentos
from model.calcular_violacoes import calcular_violacoes

def validar_solucao(solucao: List[str], catalogo: CatalogoAlimentos,
                     capacidade_max: float, proteina_max: float,
                     carboidrato_max: float,
                     exigir_vegetal: Optional[bool] = None) -> Tuple[bool, Dict[str, float]]:
    viol = calcular_violacoes(solucao, catalogo, capacidade_max, proteina_max, carboidrato_max, exigir_vegetal)
    valida = all(v == 0 for v in viol.values())
    return valida, viol


