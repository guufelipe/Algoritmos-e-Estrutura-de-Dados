letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#O valor de A é o indice de A + 1...
#INPUT: <RMQFPWZYKASIOHBJLVU>


#Transformo o input -string- em array
entrada = "RMQFPWZYKASIOHBJLVU"
codigo = []
codigoPares = []

for i in range (len(entrada)):
    codigo.append(entrada[i])
    if (letras.index(entrada[i]) +1 ) % 2 == 00:
        codigoPares.append(entrada[i])
print(f"codigo não ordenado: {codigo}")



comparacoes = 0
substituicoes = 0
iteracoes = 0




def merge(vetor, aux, esq, meio, dir):
    n = len(vetor)
    global comparacoes, substituicoes
    # Copiando os elementos para o vetor auxiliar
    for k in range(esq, dir + 1):
        aux[k] = vetor[k]

    # Ponteiros para os subvetores
    i = esq
    j = meio + 1
    
    # Intercalando os elementos dos subvetor de volta no vetor original
    for k in range(esq, dir + 1):
        if i > meio:  # Se os elementos do primeiro subvetor acabaram
            vetor[k] = aux[j]
            j += 1
        elif j > dir:  # Se os elementos do segundo subetor acabaram
            vetor[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:  # Se o elemento do segundo subarray é menor
            vetor[k] = aux[j]
            j += 1
            comparacoes += 1
        else:  # Caso contrário, pega o elemento do primeiro subarray
            comparacoes += 1
            vetor[k] = aux[i]
            i += 1

        substituicoes += 1

#Recursão do Mergesort [top-down]
def TDmergesort(vetor, aux, esq, dir):
    global iteracoes

    if esq >= dir:
        return  # Caso base: vetor com um único elemento já está ordenado.
    
    meio = (esq + dir) // 2
    TDmergesort(vetor, aux, esq, meio)  # Ordena a primeira metade
    TDmergesort(vetor, aux, meio + 1, dir)  # Ordena a segunda metade
    merge(vetor, aux, esq, meio, dir)  # Intercala as metades ordenadas
    iteracoes += 1
    print(f"Iteração {iteracoes}: {vetor}")

#Função principal que inicia o vetor auxiliar e executa mergesort
def mergesort(vetor):
    aux = [None] * len(vetor)  # Inicializa o vetor auxiliar
    TDmergesort(vetor, aux, 0, len(vetor) - 1)

mergesort(codigo)

print(f"\nCódigo Ordenado MergeSort: {codigo}")
print(f"Total de comparações: {comparacoes}")
print(f"Total de substituições: {substituicoes}")
print(f"Total de iterações: {iteracoes}")

print(f"\nORDENANDO CODIGO SÓ DE PARES")

comparacoes = 0
substituicoes = 0
iteracoes = 0 

print(f"Código com 'letras Pares' {codigoPares}")
mergesort(codigoPares)
print(f"\nCódigo Par Ordenado MergeSort: {codigoPares}")