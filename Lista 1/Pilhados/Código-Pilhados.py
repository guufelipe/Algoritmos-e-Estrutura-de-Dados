# -*- coding: utf-8 -*-

class Caixa:
    def __init__(self, valor):
        self.valor = valor 
        self.paridade = valor % 2 # (0 para par, 1 para ímpar)
    


class Pilha:
    
    def __init__(self):
        self.pilha = []  

    def tamanho(self):
        return len(pilha)

    def pilha_vazia(self):
        return len(self.pilha) == 0  #  True = vazia, False = não vazia

    def empilhar(self, valor):
        nova_caixa = Caixa(valor)  # Cria um objeto Caixa com o valor recebido
        self.pilha.append(nova_caixa)  # Adiciona a nova caixa ao topo da pilha
        
        while len(self.pilha) > 1:  # Verifica se há pelo menos duas caixas na pilha
            topo = self.pilha[-1]  # Obtém a caixa no topo da pilha
            abaixo_topo = self.pilha[-2]  # Obtém a caixa imediatamente abaixo do topo
            
            if topo.paridade == abaixo_topo.paridade:  # Se ambas as caixas têm a mesma paridade
                nova_caixa = Caixa(abs(topo.valor - abaixo_topo.valor))  # Cria uma nova caixa com a diferença absoluta dos valores
                self.pilha.pop()  # Remove o topo da pilha
                self.pilha.pop()  # Remove a caixa abaixo do topo
                
                if (nova_caixa.valor != 0):
                    self.pilha.append(nova_caixa)  # Adiciona a nova caixa resultante Só se não for 0
            else:
                break  # Interrompe o laço caso as caixas tenham paridades diferentes

    def desempilhar(self):
        if self.pilha_vazia():  # Verifica se a pilha está vazia antes de remover um elemento
            return None  # Retorna None se não houver caixas na pilha
        return self.pilha.pop()  # Remove e retorna a caixa do topo da pilha


#-------------------------------------------------------------------------------------------------------------------#

num_pilhas = int(input().strip()) 
input().strip() 

vetores = []  
pilhas = []  

for _ in range(num_pilhas):
    vetor_atual = []  
    while True:
        num = int(input().strip())
        if num == 0:
            input().strip() 
            break  
        vetor_atual.append(num)  
    vetores.append(vetor_atual) 

# Criando e processando as pilhas
for vetor in vetores:
    pilha = Pilha()
    for num in vetor:
        pilha.empilhar(num)
    pilhas.append(pilha)

# Exibindo as pilhas após processamento
for i in range(len(pilhas)):
    tamanho_pilha = len(pilhas[i].pilha)
    if tamanho_pilha > 0: 
        topo_pilha = pilhas[i].pilha[-1].valor
    else:
        topo_pilha = -1
    print(f"Pilha {i+1}: {tamanho_pilha} {topo_pilha}") 