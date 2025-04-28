# -*- coding: utf-8 -*-

P = int(input())

for K in range(P):
    colunas = []  # Lista onde cada elemento representa uma pilha (coluna de pedras)

    while True:
        linha = input()

        # ver se chegou ao fim da partida
        if linha == "END":
            break
        
        # Separa = s(posição) e c(cor da pedra)
        s, c = linha.split()
        s = int(s)
        c = int(c)

        # Adiciona a pedra
        if s == 0:  # Cria uma nova coluna na esquerda
            nova_coluna = [c]
            colunas.insert(0, nova_coluna)
        elif s == len(colunas) + 1:  # Cria uma nova coluna na direita
            nova_coluna = [c]
            colunas.append(nova_coluna)
        else:  # Adiciona pedra em uma coluna que ja existe
            coluna_atual = colunas[s - 1]
            coluna_atual.append(c)

            # Se a nova pedra no topo for da mesma cor da anterior remover todas as do topo
            if len(coluna_atual) > 1 and coluna_atual[-1] == coluna_atual[-2]:
                cor_removida = coluna_atual[-1]

                # Remove todas as pedras dessa cor no topo
                while coluna_atual and coluna_atual[-1] == cor_removida:
                    coluna_atual.pop()

        # Se a coluna ta vazia remove e desloca as restantes
        colunas_nao_vazias = []
        for coluna in colunas:
            if len(coluna) > 0:  
                colunas_nao_vazias.append(coluna)

        colunas = colunas_nao_vazias  # Atualiza a lista de colunas

    if K < P - 1:
        input()

    # Gerando a saída no formato correto
    if len(colunas) > 0:
        topo_pedras = []
        for coluna in colunas:
            pedra_no_topo = coluna[-1]
            topo_pedras.append(str(pedra_no_topo))  

        resultado = " ".join(topo_pedras)  # Junta os valores com espaços
        print(f"caso {K}: {resultado}")  
    else:
        print(f"caso {K}:")  
