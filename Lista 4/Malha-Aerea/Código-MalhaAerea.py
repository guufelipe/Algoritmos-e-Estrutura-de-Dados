# -*- coding: utf-8 -*-


def merge(conexoes, aux, esq, meio, dir):
    #copia os elementos para o vetor auxiliar
    for k in range(esq, dir + 1):
        aux[k] = conexoes[k]

    i = esq
    j = meio + 1
    
    # merge nos elementos dos subvetores de volta no vetor original
    for k in range(esq, dir + 1):
        if i > meio:  # Se o primeiro subvetor acabaram
            conexoes[k] = aux[j]
            j += 1
        elif j > dir:  # Se o segundo subvetor acabaram
            conexoes[k] = aux[i]
            i += 1
        elif aux[i][2] > aux[j][2]:  #Comparando os pesos
            conexoes[k] = aux[j]
            j += 1
        else:
            conexoes[k] = aux[i]
            i += 1

def TDmergesort(conexoes, aux, esq, dir):
    # caso base -> vetor com um elemento já está ordenado.
    if esq >= dir:
        return  
    
    meio = (esq + dir) // 2
    TDmergesort(conexoes, aux, esq, meio)  # ordena a primeira metade
    TDmergesort(conexoes, aux, meio + 1, dir)  # oedena a segunda metade
    merge(conexoes, aux, esq, meio, dir)  # Intercala as metades ordenadas

def mergesort(conexoes):
    aux = [None] * len(conexoes)  # inicializa o vetor auxiliar
    TDmergesort(conexoes, aux, 0, len(conexoes) - 1)

def kruskal(num_aeroportos, num_conexoes, conexoes):
    custo_total = 0

    grupo = [] 
    i = 0
    while i < num_aeroportos:
        grupo.append(i)
        i += 1
    

    mergesort(conexoes) #Chamando a função Mergesort pra ordenar as conexões
    
    # Percorre todas as conexões ordenadas
    for i in range(num_conexoes):
        u = conexoes[i][0]  # vértice (aeroporto) de origem
        v = conexoes[i][1]  # vértice (aeroporto) de destino
        peso = conexoes[i][2]  # Custo da conexão
        
        # Se os vértices/aeroportos pertencem a grupos diferentes:
        if grupo[u] != grupo[v]:
            custo_total += peso
            
            # Atualiza todos os vértices do grupo antigo para o novo grupo
            grupo_antigo = grupo[v]
            grupo_novo = grupo[u]
            
            for x in range(num_aeroportos):
                if grupo[x] == grupo_antigo:
                    grupo[x] = grupo_novo
    
    # No final printa o custo total mínimo da Árvore Geradora Mínima
    print(custo_total)

def main():
    entrada = input().split()
    num_aeroportos = int(entrada[0])
    num_conexoes = int(entrada[1])


    conexoes = []
    i = 0
    while i < num_conexoes:
        valores = input().split()
        aeroporto1 = int(valores[0])
        aeroporto2 = int(valores[1])
        custo = int(valores[2])
        conexoes.append([aeroporto1, aeroporto2, custo])  # Armazena manualmente como lista
        i += 1

    
    kruskal(num_aeroportos, num_conexoes, conexoes)

#Pra rodar no iudex 
if __name__ == "__main__":
    main()