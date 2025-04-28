# -*- coding: utf-8 -*-

class Jogador: #nodo | #Todo jogador começa com nome e pontuação, mas sem ligações
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
        self.sucessor = None
        self.predecessor = None

class Ranking: #lista duplamente ligada | #Tem referência ao primeiro jogador
    def __init__(self):
        self.head = None



    #INSERÇÃO:

    def inserir_jogador(self, nome, pontuacao):
        novo_jogador = Jogador(nome, pontuacao)

        # Se a lista estiver vazia, ele se torna o primeiro jogador
        if self.head is None:
            self.head = novo_jogador
            print(f"{nome} inserido com sucesso!")
            return

        # Ver se já tem um jogador com essa pontuação
        atual = self.head
        while atual is not None:
            if atual.pontuacao == pontuacao:
                print(f"{nome} já está no sistema.")
                return
            atual = atual.sucessor  # Avança para o próximo jogador



        # Inserção ordenada pela pontuação
        atual = self.head
        anterior = None

        while (atual is not None) and (atual.pontuacao < pontuacao):
            anterior = atual
            atual = atual.sucessor

        if anterior is None: # Quando novo jogador tem a menor pontuação, então vira o novo head
            
            novo_jogador.sucessor = self.head
            self.head.predecessor = novo_jogador
            self.head = novo_jogador
        else: #Quando Inserção no meio ou no final da lista
            novo_jogador.sucessor = atual
            novo_jogador.predecessor = anterior
            anterior.sucessor = novo_jogador

            if atual is not None:
                atual.predecessor = novo_jogador

        print(f"{nome} inserido com sucesso!")



    #Encontrando Predecessores e Sucessores:
    def buscar_proximidades(self, pontuacao):
        atual = self.head

        # Percorre a lista até encontrar o jogador com a pontuação desejada
        while atual is not None and atual.pontuacao != pontuacao:
            atual = atual.sucessor

        # Se não encontrou não faz nada
        if atual is None:
            return  

        # Pega os vizinhos
        predecessor = atual.predecessor
        sucessor = atual.sucessor

        # Mensagens de saída
        if (predecessor is None) and (sucessor is None):
            print(f"Apenas {atual.nome} existe no sistema...")
        elif (predecessor is None):
            print(f"{atual.nome} e o menor! e logo apos vem {sucessor.nome}")
        elif (sucessor is None):
            print(f"{atual.nome} e o maior! e logo atras vem {predecessor.nome}")
        else:
            print(f"{atual.nome} vem apos {predecessor.nome} e antes de {sucessor.nome}")



ranking = Ranking()  #ranking vazio

K = int(input())  #numero de comandos

for _ in range(K):
    comando = input().split()
    
    if comando[0] == "ADD":
        nome = comando[1]
        pontuacao = int(comando[2])
        ranking.inserir_jogador(nome, pontuacao)
    
    elif comando[0] == "PROX":
        pontuacao = int(comando[1])
        ranking.buscar_proximidades(pontuacao)

