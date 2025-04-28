class No:
    proximo = None
    valor = 0

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    

    def empilhar(self, elemento):
        if self.topo == None: #Pilha vazia
            self.topo = elemento
            self.tamanho += 1
            return 
        else:
            elemento.proximo = self.topo #Aponta pro antigo topo
            self.topo = elemento #Atualiza o topo
            self.tamanho += 1 
            return
    
    def desempilhar(self): #pop // Sempre tira o elemento de cima
        if self.topo == None:
            return None #Pilha Vazia

        elemento = self.topo
        self.topo = self.topo.proximo #Move o topo para o próximo nó

        self.tamanho -= 1
        return elemento
    
    def exibir(self):
        elementos = []
        atual = self.topo
        
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        
        if elementos:
            return " -> ".join(elementos)
        
        else:
            return "Pilha vazia"

pilha = Pilha()
pilha.empilhar(No(4))
pilha.empilhar(No(1))
pilha.empilhar(No(3))
pilha.desempilhar()
pilha.empilhar(No(8))
pilha.desempilhar()

print(pilha.exibir())