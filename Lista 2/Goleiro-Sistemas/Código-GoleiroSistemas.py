
#   Nó:
# - id: Identificador único do dispositivo
# - wei: Total de bytes (WEI) transmitidos pelo dispositivo
# - altura: Altura do nó na árvore (começa com 1, pois é uma folha)
# - subTotal: Soma de wei de toda a subárvore que tem este nó como raiz (wei do nó + de todos os seus descendentes)
# - esq: Referência para o filho à esquerda.
# - dir: Referência para o filho à direita.

class No:
    def __init__(self, id, wei):
        self.id = id
        self.wei = wei
        self.altura = 1
        self.subTotal = wei
        self.esq = None
        self.dir = None

# AVL:

# - getAltura: Retorna a altura de um nó (0 se None).
# - atualizarNo: Atualiza a altura e o subTotal de um nó com base em seus filhos.
# - obterBalance: Calcula o fator de balanceamento (altura esq - altura dir).
# - rotDireita: Realiza a rotação à direita para balanceamento.
# - rotEsquerda: Realiza a rotação à esquerda para balanceamento.
# - inserirNo: Insere ou atualiza um nó na subárvore e garante o balanceamento.
# - add: Método público para inserir ou atualizar um nó.
# - buscarNo: Busca um nó pelo id, retornando o nó e sua profundidade.
# - consultarWei: Retorna o wei e a profundidade do nó com o id fornecido.
# - consultarRnk: Retorna a soma de wei dos nós com id menor que um valor.
# - _consultarRnk: Função auxiliar recursiva para calcular RNK.
# - totalGlobal: Retorna o total global de wei (subTotal da raiz).


class AVL:
    def __init__(self):
        self.raiz = None

    def getAltura(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizarNo(self, no):
        altEsq = self.getAltura(no.esq)
        altDir = self.getAltura(no.dir)
        if altEsq > altDir:
            maiorAlt = altEsq
        else:
            maiorAlt = altDir
        no.altura = 1 + maiorAlt

        if no.esq is not None:
            subEsq = no.esq.subTotal
        else:
            subEsq = 0

        if no.dir is not None:
            subDir = no.dir.subTotal
        else:
            subDir = 0

        no.subTotal = no.wei + subEsq + subDir

    def obterBalance(self, no):
        if no is None:
            return 0
        return self.getAltura(no.esq) - self.getAltura(no.dir)

    def rotDireita(self, y):
        x = y.esq
        t2 = x.dir
        x.dir = y
        y.esq = t2
        self.atualizarNo(y)
        self.atualizarNo(x)
        return x

    def rotEsquerda(self, x):
        y = x.dir
        t2 = y.esq
        y.esq = x
        x.dir = t2
        self.atualizarNo(x)
        self.atualizarNo(y)
        return y

    def inserirNo(self, no, id, weiNovos):
        if no is None:
            return No(id, weiNovos)
        if id < no.id:
            no.esq = self.inserirNo(no.esq, id, weiNovos)
        elif id > no.id:
            no.dir = self.inserirNo(no.dir, id, weiNovos)
        else:
            no.wei = no.wei + weiNovos
            self.atualizarNo(no)
            return no

        self.atualizarNo(no)
        balance = self.obterBalance(no)
        if balance > 1:
            if no.esq is not None:
                if id < no.esq.id:
                    return self.rotDireita(no)
                else:
                    no.esq = self.rotEsquerda(no.esq)
                    return self.rotDireita(no)
        if balance < -1:
            if no.dir is not None:
                if id > no.dir.id:
                    return self.rotEsquerda(no)
                else:
                    no.dir = self.rotDireita(no.dir)
                    return self.rotEsquerda(no)
        return no

    def add(self, id, weiNovos):
        self.raiz = self.inserirNo(self.raiz, id, weiNovos)

    def buscarNo(self, no, id, prof):
        if no is None:
            return None, -1
        if id == no.id:
            return no, prof
        if id < no.id:
            return self.buscarNo(no.esq, id, prof + 1)
        return self.buscarNo(no.dir, id, prof + 1)

    def consultarWei(self, id):
        no, prof = self.buscarNo(self.raiz, id, 0)
        if no is None:
            return 0, -1
        return no.wei, prof

    def consultarRnk(self, id):
        return self._consultarRnk(self.raiz, id)

    def _consultarRnk(self, no, id):
        if no is None:
            return 0
        if no.id >= id:
            return self._consultarRnk(no.esq, id)
        else:
            if no.esq is not None:
                subEsq = no.esq.subTotal
            else:
                subEsq = 0
            return subEsq + no.wei + self._consultarRnk(no.dir, id)

    def totalGlobal(self):
        if self.raiz is None:
            return 0
        return self.raiz.subTotal

# Comandos:
# - ADD id wei: Adiciona ou atualiza o dispositivo com o id e wei informados, imprimindo o total global de wei na rede.
# - WEI id: Imprime o wei e a profundidade do dispositivo com o id informado; se não existir, imprime "0 -1".
# - RNK id: Imprime a soma de wei dos dispositivos com id menor que o informado.

arvore = AVL()
while True:
    linha = input().strip()
    if linha == "END":
        break
    partes = linha.split()
    comando = partes[0]
    if comando == "ADD":
        idDispositivo = int(partes[1])
        weiNovos = int(partes[2])
        arvore.add(idDispositivo, weiNovos)
        print(arvore.totalGlobal())
    elif comando == "WEI":
        idDispositivo = int(partes[1])
        weiValor, profundidade = arvore.consultarWei(idDispositivo)
        print(weiValor, profundidade)
    elif comando == "RNK":
        idDispositivo = int(partes[1])
        somaWei = arvore.consultarRnk(idDispositivo)
        print(somaWei)