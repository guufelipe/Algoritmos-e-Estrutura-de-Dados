class NoAVL:
    def __init__(self, chave):
        self.chave = chave  # Valor armazenado no nó
        self.altura = 1  # Altura inicial do nó
        self.esquerda = None  # Filho à esquerda
        self.direita = None  # Filho à direita

class ArvoreAVL:
    def __init__(self):
        self.raiz = None  # Inicializa a raiz como None

    def altura(self, no):
        return no.altura if no else 0  # Retorna a altura do nó ou 0 se for None

    def fator_balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita) if no else 0  # Calcula o fator de balanceamento

    def rotacao_direita(self, no):
        nova_raiz = no.esquerda  # Novo nó raiz
        subarvore_transferida = nova_raiz.direita  # Subárvore a ser ajustada
        
        nova_raiz.direita = no
        no.esquerda = subarvore_transferida
        
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        nova_raiz.altura = 1 + max(self.altura(nova_raiz.esquerda), self.altura(nova_raiz.direita))
        
        return nova_raiz

    def rotacao_esquerda(self, no):
        nova_raiz = no.direita  # Novo nó raiz
        subarvore_transferida = nova_raiz.esquerda  # Subárvore a ser ajustada
        
        nova_raiz.esquerda = no
        no.direita = subarvore_transferida
        
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        nova_raiz.altura = 1 + max(self.altura(nova_raiz.esquerda), self.altura(nova_raiz.direita))
        
        return nova_raiz

    def inserir(self, raiz, chave):
        if not raiz:
            return NoAVL(chave)  # Cria um novo nó caso a raiz seja None
        elif chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)  # Insere na subárvore esquerda
        else:
            raiz.direita = self.inserir(raiz.direita, chave)  # Insere na subárvore direita
        
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        fator = self.fator_balanceamento(raiz)
        
        # Caso de rotação simples para a direita (LL)
        if fator > 1 and chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)
        
        # Caso de rotação simples para a esquerda (RR)
        if fator < -1 and chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)
        
        # Caso de rotação dupla para a direita (LR)
        if fator > 1 and chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        
        # Caso de rotação dupla para a esquerda (RL)
        if fator < -1 and chave < raiz.direita.chave:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)
        
        return raiz
    
    def buscar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz  # Retorna o nó caso encontrado
        if chave < raiz.chave:
            return self.buscar(raiz.esquerda, chave)  # Busca na subárvore esquerda
        return self.buscar(raiz.direita, chave)  # Busca na subárvore direita
    
    def pre_ordem(self, raiz):
        if raiz:
            print(raiz.chave, end=" ")
            self.pre_ordem(raiz.esquerda)
            self.pre_ordem(raiz.direita)
    
    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(raiz.chave, end=" ")
            self.em_ordem(raiz.direita)
    
    def pos_ordem(self, raiz):
        if raiz:
            self.pos_ordem(raiz.esquerda)
            self.pos_ordem(raiz.direita)
            print(raiz.chave, end=" ")

arvore = ArvoreAVL()
valores = [1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15]

for chave in valores:
    arvore.raiz = arvore.inserir(arvore.raiz, chave)

print("Pre-ordem:" )
arvore.pre_ordem(arvore.raiz)
print("\nEm-ordem:")
arvore.em_ordem(arvore.raiz)
print("\nPos-ordem:")
arvore.pos_ordem(arvore.raiz)
