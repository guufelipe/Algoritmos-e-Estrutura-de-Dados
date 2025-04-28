# EQUIPE:
# 
# ARTHUR FERREIRA POMPILIO
# GUSTAVO FELIPE ALVES DA SILVA
# PAULA NÓBREGA DE CAMPOS GUIMARAES
# TOMÉ DA COSTA LIMA

class No:
    def __init__(self):
        self.valor = 0
        self.proximo = None

class Fila:
    def __init__(self):
        self.frente = None
        self.tras = None
        self.tamanho = 0

def cria_fila():
    fila = Fila()
    cabeca = No()
    cabeca.valor = -1
    fila.frente = cabeca
    fila.tras = cabeca
    fila.tamanho = 0
    return fila

def libera_fila(fila):
    while fila.frente:
        temporario = fila.frente
        fila.frente = fila.frente.proximo
        del temporario
    del fila

def enfileira(fila, numero):
    elemento = No()
    elemento.valor = numero
    elemento.proximo = None
    fila.tras.proximo = elemento
    fila.tras = fila.tras.proximo
    fila.tamanho += 1

def desenfileira(fila):
    if fila.tamanho != 0:
        elemento = fila.frente.proximo
        fila.frente.proximo = fila.frente.proximo.proximo
        if fila.frente.proximo is None:
            fila.tras = fila.frente
        fila.tamanho -= 1
        return elemento.valor
    else:
        return -1

def menor_caminho(antecessor, inicio, final):
    caminho_invertido = []
    x = final

    while True:
        if x == -1:
            print("---")
            break

        if x == inicio:
            caminho_invertido.append(x)
            for k in range(len(caminho_invertido) - 1, -1, -1):
                if k == 0:
                    print(caminho_invertido[k])
                else:
                    print(f"{caminho_invertido[k]}", end=",")
            break

        caminho_invertido.append(x)
        x = antecessor[x]
    
    return

def busca_em_largura(grafo, inicio, final, n):
    visitado = [False] * n
    antecessor = [-1] * n

    fila = cria_fila()
    enfileira(fila, inicio)
    visitado[inicio] = True

    while fila.tamanho > 0:
        v = desenfileira(fila)

        for g in range(len(grafo[v])):
            h = grafo[v][g]

            if not visitado[h]:
                visitado[h] = True
                antecessor[h] = v
                enfileira(fila, h)

    menor_caminho(antecessor, inicio, final)
    
    return

def main():
    n = int(input())
    q = int(input())

    grafo = [[] for _ in range(n)]

    for _ in range(q):
        vi = int(input())
        vj = int(input())
        grafo[vi].append(vj)

    while True:
        try:
            vx = int(input())
            vd = int(input())
            print(f"A={vx}, B={vd}:")
            busca_em_largura(grafo, vx, vd, n)
            print(" ")
        except:
            break

if __name__ == "__main__":
    main()
