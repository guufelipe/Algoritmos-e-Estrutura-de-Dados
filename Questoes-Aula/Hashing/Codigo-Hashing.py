'''
1. Implemente duas tabelas HASH, uma do tipo endereçamento fechado e outra do tipo endereçamento aberto:
    1. Considere a inserção das chaves 10,22,31,4,15,28,17,88,59 em uma tabela de espelhamento de comprimento m=11.
        Crie sua função de hash e imprima o conteúdo da tabela final em ambas as implementações.
    2. Implemente a função de eliminar uma chave HASH-DELETE em ambos os tipos de endereçamento.
    3. Implemente a função de busca de uma chave HASH-SEARCH em ambos os tipos de endereçamento.
'''

def funcao_hash(chave, tamanho):
    return chave % tamanho

# Endereçamento Aberto:
class TabelaHashAberta:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def inserir(self, chave):
        indice = funcao_hash(chave, self.tamanho)
        while self.tabela[indice] is not None:
            indice = (indice + 1) % self.tamanho
        self.tabela[indice] = chave

    def buscar(self, chave):
        indice = funcao_hash(chave, self.tamanho)
        indice_inicial = indice  # Para evitar loop infinito
        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                return indice  # Retorna o índice onde a chave foi encontrada
            indice = (indice + 1) % self.tamanho
            if indice == indice_inicial:  # Já percorreu todas as posições possíveis.
                break
        return None  # Retorna None se não encontrar a chave

    def deletar(self, chave):
        indice = self.buscar(chave)
        if indice is not None:
            self.tabela[indice] = None
            # Ajeitar a tabela após a remoção (só os itens que colidiram)
            indice_proximo = (indice + 1) % self.tamanho
            while self.tabela[indice_proximo] is not None:
                chave_rehash = self.tabela[indice_proximo]
                self.tabela[indice_proximo] = None
                self.inserir(chave_rehash)  # Reinsere o item
                indice_proximo = (indice_proximo + 1) % self.tamanho

    def mostrar_tabela(self):
        print(self.tabela)


# Endereçamento Fechado:
class TabelaHashFechada:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = []
        for i in range(tamanho):
            self.tabela.append([])

    def inserir(self, chave):
        indice = funcao_hash(chave, self.tamanho)
        self.tabela[indice].append(chave)

    def buscar(self, chave):
        indice = funcao_hash(chave, self.tamanho)
        if chave in self.tabela[indice]:
            return indice  # Retorna o índice da lista onde a chave foi encontrada
        return None  # Retorna None se não encontrar a chave

    def deletar(self, chave):
        indice = self.buscar(chave)
        if indice is not None:
            self.tabela[indice].remove(chave)  # Remove a chave da lista

    def mostrar_tabela(self):
        for i in range(len(self.tabela)):  # Precisamos iterar de 0 até o tamanho da tabela
            lista = self.tabela[i]  # Acessamos a lista diretamente pelo índice
            print(f"Índice {i}: {lista}")






#Criando uma tabelaHash de Endereçamento Fechado:
TabelaFechada = TabelaHashFechada(11)
#inserindo
for key in [10, 22, 31, 4, 15, 28, 17, 88, 59]:
    TabelaFechada.inserir(key)

#Testando a função Deletar
TabelaFechada.deletar(31)
TabelaFechada.mostrar_tabela()

#Testando a função Buscar
print("Procurando a chave 17")
Indice = TabelaFechada.buscar(17)
print(f"Está no indice {Indice}")


#Criando uma TableHash de Endereçamento Aberto:
TabelaAberta = TabelaHashAberta(11)
for key in [10, 22, 31, 4, 15, 28, 17, 88, 59]:
    TabelaAberta.inserir(key)

#Testando a função deletar:
TabelaAberta.deletar(31)
TabelaAberta.mostrar_tabela()

##Testando a função Buscar
print("Procurando a chave 4")
Indice = TabelaAberta.buscar(4)
print(f"Está no indice {Indice}")