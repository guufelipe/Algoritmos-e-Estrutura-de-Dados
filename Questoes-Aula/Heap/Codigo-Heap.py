'''
1. Implemente um HEAP com as operações de Heapfy, constrói heap, insere em um heap, remove elemento de um heap
2. Implemente o algoritmo de heapsort a partir das funções criadas anteriormente.
3. Ilustre as operações de HEAP-EXTRACT-MAX sobre o heap A = <15,13,9,5,12,8,7,4,0,6>
4. Ilustre as operações de MAX-HEAP-INSERT(A,10) sobre o heap A= <5,13,9,5,12,8,7,4,0,6,2,1>
5. Como seria a operação HEAP-DELETE(A,i) que exclui a chave da posição i em um heap de A?
'''

class HeapMaximo:
    def __init__(self):
        self.heap = [None]  # Índice 0 não é usado para facilitar os cálculos
        self.tamanho = 0

    def pai(self, i):
        return i // 2

    def filho_esquerda(self, i):
        return 2 * i

    def filho_direita(self, i):
        return 2 * i + 1

    # Função para manter a propriedade de Heap Máximo
    def ajustar_heap(self, i):
        esquerda = self.filho_esquerda(i)
        direita = self.filho_direita(i)
        maior = i

        # Verifica se o filho esquerdo é maior que o pai
        if esquerda <= self.tamanho and self.heap[esquerda] > self.heap[i]:
            maior = esquerda
        # Verifica se o filho direito é maior que o maior encontrado até agora
        if direita <= self.tamanho and self.heap[direita] > self.heap[maior]:
            maior = direita

        # Se o maior não é o pai, troca e continua ajustando a estrutura
        if maior != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[maior]
            self.heap[maior] = temp
            self.ajustar_heap(maior)

    # Função para construir um Heap a partir de uma lista de elementos
    def construir_heap(self, lista):
        self.heap = [None] + lista  # Adiciona um índice vazio no início
        self.tamanho = len(lista)

        # Ajusta a estrutura do heap de baixo para cima
        for i in range(self.tamanho // 2, 0, -1):
            self.ajustar_heap(i)

    # Função para extrair o maior elemento do heap
    def extrair_maximo(self):
        if self.tamanho < 1:
            raise Exception("Heap vazio! Não é possível extrair o máximo.")

        maximo = self.heap[1]  # O maior elemento está na raiz
        self.heap[1] = self.heap[self.tamanho]  # Substituímos pelo último elemento
        self.tamanho -= 1
        self.heap.pop()  # Remove o último elemento
        self.ajustar_heap(1)  # Reajusta o heap
        return maximo

    # Função para inserir um novo elemento no heap
    def inserir(self, chave):
        self.tamanho += 1
        self.heap.append(float('-inf'))  # Adiciona um valor mínimo no final
        self.aumentar_chave(self.tamanho, chave)

    # Função para aumentar o valor de uma chave já existente
    def aumentar_chave(self, i, chave):
        if chave < self.heap[i]:
            raise Exception("Nova chave é menor que a chave atual!")

        self.heap[i] = chave
        # Sobe a chave para a posição correta
        while i > 1 and self.heap[self.pai(i)] < self.heap[i]:
            temp = self.heap[i]
            self.heap[i] = self.heap[self.pai(i)]
            self.heap[self.pai(i)] = temp
            i = self.pai(i)

    # Função de ordenação HeapSort
    def ordenar(self):
        copia_heap = self.heap[:]
        copia_tamanho = self.tamanho
        lista_ordenada = []

        while self.tamanho > 0:
            lista_ordenada.insert(0, self.extrair_maximo())

        self.heap = copia_heap  # Restaura a estrutura original
        self.tamanho = copia_tamanho
        return lista_ordenada

    # Função para remover um elemento do heap em qualquer posição
    def remover(self, i):
        if i > self.tamanho or i < 1:
            raise Exception("Índice inválido!")

        self.heap[i] = self.heap[self.tamanho]  # Substituímos pelo último elemento
        self.tamanho -= 1
        self.heap.pop()
        self.ajustar_heap(i)  # Ajusta a estrutura do heap

    # Função para exibir o heap
    def exibir(self):
        print(self.heap[1:])  # Ignora o índice 0


# ----------------------------------------------------
# TESTES E RESOLUÇÃO DAS QUESTÕES
# ----------------------------------------------------

# 1. Criando um heap e realizando operações básicas
heap = HeapMaximo()
heap.construir_heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6])

print("\nHeap Construído:")
heap.exibir()

# 2. Teste da inserção de um novo elemento
print("\nInserindo o elemento 16:")
heap.inserir(16)
heap.exibir()

# 3. Teste da extração do maior elemento
print("\nExtraindo o maior elemento:")
print("Máximo extraído:", heap.extrair_maximo())
heap.exibir()

# 4. Teste do HeapSort
print("\nOrdenação usando HeapSort:")
lista_desordenada = [4, 10, 3, 5, 1]
heap.construir_heap(lista_desordenada)
print("Lista ordenada:", heap.ordenar())

# 5. Ilustração da operação HEAP-EXTRACT-MAX em [15,13,9,5,12,8,7,4,0,6]
print("\nIlustração de HEAP-EXTRACT-MAX em [15,13,9,5,12,8,7,4,0,6]:")
heap.construir_heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6])
heap.exibir()
print("Extraindo o máximo...")
print("Máximo extraído:", heap.extrair_maximo())
heap.exibir()

# 6. Ilustração de MAX-HEAP-INSERT(A,10) em [5,13,9,5,12,8,7,4,0,6,2,1]
print("\nIlustração de MAX-HEAP-INSERT(A,10) em [5,13,9,5,12,8,7,4,0,6,2,1]:")
heap.construir_heap([5, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
heap.exibir()
print("Inserindo 10...")
heap.inserir(10)
heap.exibir()

# 7. Teste da remoção de um elemento específico
print("\nRemovendo elemento na posição 3 do Heap:")
heap.remover(3)
heap.exibir()
