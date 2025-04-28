class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self, capacidade):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.capacidade = capacidade

    def enfileirar(self, valor):
        if self.tamanho == self.capacidade:
            print("Fila cheia!")
            return
        
        novo_no = No(valor)
        
        if self.fim is None:  # Fila vazia
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        
        self.tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            print("Fila vazia!")
            return None
        
        elemento = self.inicio
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:  # Se a fila ficou vazia
            self.fim = None
        
        self.tamanho -= 1
        return elemento.valor

    def exibir(self):
        atual = self.inicio
        elementos = []
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        return " <- ".join(elementos) if elementos else "Fila vazia"

# Teste conforme solicitado
fila = Fila(6)
print(fila.exibir())
fila.enfileirar(4)
print(fila.exibir())  # Ilustração após ENQUEUE(Q,4)

fila.enfileirar(1)
print(fila.exibir())  # Ilustração após ENQUEUE(Q,1)

fila.enfileirar(8)
print(fila.exibir())  # Ilustração após ENQUEUE(Q,8)

fila.desenfileirar()
print(fila.exibir())  # Ilustração após DEQUEUE(Q)
