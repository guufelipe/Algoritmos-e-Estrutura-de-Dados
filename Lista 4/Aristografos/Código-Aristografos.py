# -*- coding: utf-8 -*-


class MinHeap:
    def __init__(self):
        # Lista com os elementos do heap - começa vazio
        self.dados = []
    
    def inserir(self, elemento):
        # Sempre adiciona um elemento no final da lista e 
        self.dados.append(elemento)
        self._subir(len(self.dados) - 1) # Chama subir() pra manter o heap de minimo
     
    def remover(self):
        # Remove e retorna o menor elemento do heap (a raiz do heap)
        if not self.dados:
            return None
        if len(self.dados) == 1:
            return self.dados.pop()
        
        #Troca a raiz pelo último elemento da lista.
        raiz = self.dados[0]
        self.dados[0] = self.dados.pop()
        self._descer(0) # Chama descer() pra manter o heap de minimo
        return raiz
    
    def _subir(self, indice):
        #Move um elemento para cima se for menor que seu pai p/ manter o heap mínimo
        pai = (indice - 1) // 2
        while indice > 0 and self.dados[indice][0] < self.dados[pai][0]:
            self.dados[indice], self.dados[pai] = self.dados[pai], self.dados[indice]
            indice = pai
            pai = (indice - 1) // 2
    
    def _descer(self, indice):
        #Move um elemento para baixo se for menor que seu pai p/ manter o heap mínimo
        tamanho = len(self.dados)
        while True:
            filho_esq = 2 * indice + 1
            filho_dir = 2 * indice + 2
            menor = indice
            
            if filho_esq < tamanho and self.dados[filho_esq][0] < self.dados[menor][0]:
                menor = filho_esq
            if filho_dir < tamanho and self.dados[filho_dir][0] < self.dados[menor][0]:
                menor = filho_dir
            
            if menor == indice:
                break
            
            self.dados[indice], self.dados[menor] = self.dados[menor], self.dados[indice]
            indice = menor

def dijkstra(grafo, origem, destino, num_quadras):
    infinito = float('inf')
    #Lista de distancia -> Todo mundo começa com infinito menos a distancia que recebe 0
    distancia = []
    for i in range(num_quadras):
        distancia.append(infinito)
    distancia[origem] = 0
    
    #Cria o Min-Heap e coloca a origem na fila
    heap = MinHeap()
    heap.inserir((0, origem))
    

    #Começa a busca
    while heap.dados:
        custo_atual, quadra_atual = heap.remover()  # Remove a quadra com menor custo da fila
        
        if quadra_atual == destino:
            return distancia[destino]  # Se achou o destino, retorna a menor distancia
        
        #Atualizar as distâncias dos vizinhos se encontrarmos um caminho mais curto
        for vizinho, custo_rua in grafo[quadra_atual]:
            novo_custo = custo_atual + custo_rua
            
            if novo_custo < distancia[vizinho]:  # Atualiza a distância se for menor
                distancia[vizinho] = novo_custo
                heap.inserir((novo_custo, vizinho)) #Adiciona os vizinhos ao heap para continuar a busca.

    
    return -1  # Retorna -1 se não tiver caminho

def main():
    entrada = input().split()
    num_quadras = int(entrada[0]) #Q
    num_ruas = int(entrada[1]) #R
    num_eventos = int(entrada[2]) #N 
    
    #Lista de Adjacencias: Cada quadra contem as ruas saindo dela.
    grafo = []
    for _ in range(num_quadras):
        grafo.append([])


        
    #Pego as ruas iniciais da cidade
    i = 0
    while i < num_ruas:
        valores = input().split()
        origem = int(valores[0])
        destino = int(valores[1])
        tempo = int(valores[2])
        grafo[origem].append((destino, tempo))  # adiciona as ruas ao grafo
        i += 1
    

    #Pego os eventos que podem ser: adicionar nova rua ou consultar menor caminho
    i = 0
    while i < num_eventos:
        valores = input().split()
        tipo = int(valores[0])
        
        if tipo == 1: # Adiciona uma nova rua ao grafo
            origem = int(valores[1])
            destino = int(valores[2])
            tempo = int(valores[3])
            grafo[origem].append((destino, tempo))  
        elif tipo == 2: # Processa a consulta de menor caminho
            origem = int(valores[1])
            destino = int(valores[2])
            print(dijkstra(grafo, origem, destino, num_quadras))  
        
        i += 1

if __name__ == "__main__":
    main()
