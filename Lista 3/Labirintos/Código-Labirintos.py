# -*- coding: utf-8 -*-

def busca_largura(matriz, inicio, destino, linhas, colunas):
    vertices = []
    vertices.append(inicio)  # Fila para armazenar posições a serem visitadas

    # movimentos possiveis: direita, esquerda, para baixo, para cima
    movimentos = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    marcado = []  
    antecessor = []  
    distancias = []  

    for i in range(linhas):
        marcado.append([False] * colunas)
        antecessor.append([(-1, -1)] * colunas)
        distancias.append([-1] * colunas)

    marcado[inicio[0]][inicio[1]] = True  # Posição inicial = visitada
    distancias[inicio[0]][inicio[1]] = 0 

    # Faz a busca em profundidade enquanto tiver posições pra visitar
    while len(vertices) > 0:
        posicao_atual = vertices.pop(0)
        linha_atual, coluna_atual = posicao_atual

        # explorando os vizinhos validos
        for movimento in movimentos:
            nova_linha = linha_atual + movimento[0]
            nova_coluna = coluna_atual + movimento[1]
            # vendo se a nova posição está no limite do labirinto
            if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                if matriz[nova_linha][nova_coluna] != 1 and not marcado[nova_linha][nova_coluna]:
                    marcado[nova_linha][nova_coluna] = True
                    antecessor[nova_linha][nova_coluna] = (linha_atual, coluna_atual)
                    distancias[nova_linha][nova_coluna] = distancias[linha_atual][coluna_atual] + 1
                    if (nova_linha, nova_coluna) == destino:
                        return distancias[nova_linha][nova_coluna]  # Caminho encontrado
                    vertices.append((nova_linha, nova_coluna))  # adiciona novas posições alcançáveis à fila para serem exploradas depois
    
    # Se não encontrar caminho
    return "Labirinto Impossivel"  


if __name__ == '__main__':
    linhas, colunas = input().split()
    linhas = int(linhas)
    colunas = int(colunas)

    matriz = []
    inicio = (-1, -1)
    destino = (-1, -1)  

    for i in range(linhas):
        linha = input().split()
        linha_convertida = []
        for elemento in linha:
            linha_convertida.append(int(elemento))
        matriz.append(linha_convertida)

        for j in range(colunas):
            if linha_convertida[j] == 2:
                inicio = (i, j)
            elif linha_convertida[j] == 3:
                destino = (i, j)

    # ver se as posições de início e destino foram encontradas antes de executar a busca
    if inicio != (-1, -1) and destino != (-1, -1):
        resultado = busca_largura(matriz, inicio, destino, linhas, colunas)
        print(resultado)
    else:
        print("Labirinto Impossivel")
