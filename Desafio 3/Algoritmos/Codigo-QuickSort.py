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



# Função de partição
def particao(vetor, esq, dir):
    global comparacoes, substituicoes
    # Define o pivô como o primeiro elemento
    pivo = vetor[esq]
    i = esq         # Inicialmente i aponta para o início do vetor
    j = dir + 1     # j começa depois do final do vetor

    while True:
        # aumenta i: busca o primeiro elemento à direita do pivô que não seja menor que ele
        i += 1
        while i <= dir and vetor[i] < pivo:
            comparacoes += 1
            i += 1

        # diminui j: busca o primeiro elemento à esquerda do fim que não seja maior que o pivô
        j -= 1
        while j >= esq and vetor[j] > pivo:
            comparacoes += 1
            j -= 1

        # Se os ponteiros se cruzarem, encerra a partição
        if i >= j:
            break

        # Troca  os elementos em vetor[i] e vetor[j]
        vetor[i], vetor[j] = vetor[j], vetor[i]
        substituicoes += 1

     # Coloca o pivô na posição correta (troca com vetor[j])
    vetor[esq], vetor[j] = vetor[j], vetor[esq]
    substituicoes += 1
    return j  # Retorna a posição do pivô


# recursão do QuickSort
def qs(vetor, esq, dir):
    global iteracoes

    # Caso base: segmento vazio ou com 1 elemento já está ordenado
    if esq >= dir:
        return  
    
    p = particao(vetor, esq, dir)  # Particiona o vetor e obtém a posição do pivô
    iteracoes += 1
    print(f"Iteração {iteracoes}: {vetor}")
    qs(vetor, esq, p - 1)         # faz recursivamente na sublista à esquerda do pivô
    qs(vetor, p + 1, dir)         # faz recursivamente na sublista à direita do pivô


def quicksort(vetor):
    qs(vetor, 0, len(vetor) - 1)

quicksort(codigo)

print(f"\nCódigo Ordenado QuickSort: {codigo}")
print(f"Total de comparações: {comparacoes}")
print(f"Total de substituições: {substituicoes}")
print(f"Total de iterações: {iteracoes}")

print(f"\nORDENANDO CODIGO SÓ DE PARES")

comparacoes = 0
substituicoes = 0
iteracoes = 0 

print(f"Código com 'letras Pares' {codigoPares}")
quicksort   (codigoPares)
print(f"\nCódigo Par Ordenado QuickSort: {codigoPares}")