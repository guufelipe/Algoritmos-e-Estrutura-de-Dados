'''
EQUIPE:

ARTHUR FERREIRA POMPILIO
GUSTAVO FELIPE ALVES DA SILVA
PAULA NÓBREGA DE CAMPOS GUIMARAES
TOMÉ DA COSTA LIMA

'''

def busca_profundidade(grafo, vertice, visitado, antecessor, pilha):
    visitado[vertice] = True
    
    for vizinho in grafo[vertice]:  
        if not visitado[vizinho]:
            antecessor[vizinho] = vertice 
            busca_profundidade(grafo, vizinho, visitado, antecessor, pilha)
    
    pilha.append(vertice)


def ordenacao_topologica(grafo, num_vertices):
    visitado = [False] * num_vertices  
    antecessor = [-1] * num_vertices 
    pilha = []
    
    for v in range(num_vertices):
        if not visitado[v]:
            busca_profundidade(grafo, v, visitado, antecessor, pilha)
    
    return pilha[::-1]  


num_vertices = int(input())
num_arestas = int(input())

#Lista de adjacencia
grafo = [] 
for _ in range(num_vertices):
    grafo.append([])

for _ in range(num_arestas):
    entrada = input().split()  
    origem = int(entrada[0])
    destino = int(entrada[1])
    grafo[origem].append(destino)


resultado = ordenacao_topologica(grafo, num_vertices)



for i in range(len(resultado)):
    if i == len(resultado) - 1:
        print(resultado[i])
    else:
        print(resultado[i], end=",")