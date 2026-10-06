def subida_encosta_por_tentativas(num_tentativas, gerar_inicial, gerar_sucessores, calcular_pontuacao, avaliar_solucao):
    melhor_solucao_global = None
    melhor_pontuacao_global = -float('inf')

    for tentativa in range(num_tentativas):
        solucao_atual = gerar_inicial()
        
        while not avaliar_solucao(solucao_atual):
            solucao_atual = gerar_inicial()
            
        pontuacao_atual = calcular_pontuacao(solucao_atual)

        while True:
            sucessores = gerar_sucessores(solucao_atual)
            sucessores_validos = [s for s in sucessores if avaliar_solucao(s)]
            
            if not sucessores_validos:
                break 
            
            melhor_sucessor = None
            melhor_pontuacao_sucessor = -float('inf')
            
            for sucessor in sucessores_validos:
                pontuacao = calcular_pontuacao(sucessor)
                if pontuacao > melhor_pontuacao_sucessor:
                    melhor_sucessor = sucessor
                    melhor_pontuacao_sucessor = pontuacao
                    
            if melhor_pontuacao_sucessor <= pontuacao_atual:
                break
                
            solucao_atual = melhor_sucessor
            pontuacao_atual = melhor_pontuacao_sucessor
            
        if pontuacao_atual > melhor_pontuacao_global:
            melhor_solucao_global = solucao_atual
            melhor_pontuacao_global = pontuacao_atual
            
    return melhor_solucao_global