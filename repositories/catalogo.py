
from typing import Dict, List, Tuple, Optional

CatalogoAlimentos = Dict[str, List]
catalogo: CatalogoAlimentos = {
    "Frango grelhado (50g)": [50, 15.5, 0, False],
    "Frango grelhado (100g)": [100, 31, 0, False],
    "Frango grelhado (150g)": [150, 46.5, 0, False],
    "Frango grelhado (150g)": [200, 250, 0, False],
    "Patinho moído (100g)": [100, 35, 0, False],
    "Patinho moído (150g)": [150, 52.5, 0, False],
    "Peito de peru (50g)": [50, 11, 0, False],
    "Peito de peru (100g)": [100, 22, 0, False],
    "Tilápia grelhada (100g)": [100, 26, 0, False],
    "Tilápia grelhada (150g)": [150, 39, 0, False],
    "Lombo suíno assado (100g)": [100, 27, 0, False],
    "Atum em conserva (80g)": [80, 21, 0, False],
    "Ovo cozido (unidade ~50g)": [50, 6, 0.6, False],
    "Ovo cozido (2 unidades ~100g)": [100, 12, 1.2, False],

    # --- Carboidratos e Grãos ---
    "Arroz integral (80g)": [80, 2.0, 18.4, False],
    "Arroz integral (100g)": [100, 2.5, 23, False],
    "Arroz integral (150g)": [150, 3.75, 34.5, False],
    "Arroz branco (100g)": [100, 2.5, 28, False],
    "Quinoa cozida (80g)": [80, 3.5, 16.8, False],
    "Quinoa cozida (100g)": [100, 4.4, 21, False],
    "Batata doce (80g)": [80, 1.3, 16, True],
    "Batata doce (100g)": [100, 1.6, 20, True],
    "Batata doce (150g)": [150, 2.4, 30, True],
    "Batata inglesa cozida (100g)": [100, 1.8, 12, True],
    "Mandioca cozida (100g)": [100, 1.2, 30, True],
    "Macarrão integral (100g)": [100, 5.3, 26.5, True],

    # --- Leguminosas ---
    "Feijão (50g)": [50, 3.1, 8.7, False],
    "Feijão (80g)": [80, 5, 14, False],
    "Feijão (120g)": [120, 7.5, 21, False],
    "Lentilha (50g)": [50, 3.75, 10, False],
    "Lentilha (80g)": [80, 6, 16, False],
    "Grão-de-bico (80g)": [80, 7, 22, False],
    "Grão-de-bico (120g)": [120, 10.5, 33, False],

    # --- Vegetais e Legumes ---
    "Brócolis (50g)": [50, 1.5, 3.5, True],
    "Brócolis (100g)": [100, 3, 7, True],
    "Cenoura (50g)": [50, 0.45, 5, True],
    "Cenoura (100g)": [100, 0.9, 10, True],
    "Abobrinha (50g)": [50, 0.6, 1.5, True],
    "Abobrinha (100g)": [100, 1.2, 3, True],
    "Couve-flor (100g)": [100, 1.9, 4, True],
    "Vagem (100g)": [100, 1.8, 7, True],
    "Couve refogada (50g)": [50, 1.2, 3, True],

    # --- Proteínas Vegetais ---
    "Tofu grelhado (100g)": [100, 8, 2, True],
    "Proteína de Soja/PTS (80g)": [80, 13.6, 7.2, True],
    }