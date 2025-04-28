# -*- coding: utf-8 -*-

def busca_profundidade(grafo, vertice, visitado, antecessor, ordem_visita):
    visitado[vertice] = True  
    ordem_visita.append(vertice)
    
    for vizinho in grafo[vertice]:
        if not visitado[vizinho]:
            antecessor[vizinho] = vertice
            busca_profundidade(grafo, vizinho, visitado, antecessor, ordem_visita)

if __name__ == '__main__':

    num_vertices = int(input())

    grafo = []
    for _ in range(num_vertices):
        grafo.append([])

    # pegando as conexões
    while True:
        entrada = input().split()
        origem = int(entrada[0])
        destino = int(entrada[1])
        continuar = int(entrada[2])  # terceiro número indica se continua ou não
        
        grafo[origem].insert(0, destino)
        grafo[destino].insert(0, origem)
        
        if continuar == 0:
            break

    for i in range(num_vertices):
        if grafo[i]:
            print(str(i) + ":", end=" ")  
            for j in range(len(grafo[i])):
                if j == len(grafo[i]) - 1:
                    print(grafo[i][j])
                else:
                    print(grafo[i][j], end=" ")
        else:
            print(str(i) + ": Lista vazia")  

    visitado = []
    for _ in range(num_vertices):
        visitado.append(False)

    antecessor = []
    for _ in range(num_vertices):
        antecessor.append(-1)

    ordem_visita = []

    # busca em profundidade a partir do vértice 0
    busca_profundidade(grafo, 0, visitado, antecessor, ordem_visita)

    print(" ".join(str(v) for v in ordem_visita))
