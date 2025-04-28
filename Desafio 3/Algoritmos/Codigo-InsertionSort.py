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

def insertionsort(vetor):
    global comparacoes, substituicoes, iteracoes
    n = len(vetor)
    for i in range (1, n):
        iteracoes += 1
        aux = vetor[i]  # Armazena o elemento a ser inserido na posição correta
        j = i - 1  # Define o índice do último elemento da parte ordenada
        
        # Move os elementos maiores que aux para a direita
        while j >= 0 and vetor[j] > aux:
            comparacoes += 1
            vetor[j + 1] = vetor[j]  # Desloca o elemento para a direita
            j -= 1  # Move para a posição anterior
            substituicoes += 1
        
        # Insere o aux na posição correta
        vetor[j + 1] = aux
        substituicoes += 1
        print(f"Iteração {iteracoes}: {vetor}")


insertionsort(codigo)

print(f"\nCódigo Ordenado InsertionSort: {codigo}")
print(f"Total de comparações: {comparacoes}")
print(f"Total de substituições: {substituicoes}")
print(f"Total de iterações: {iteracoes}")

print(f"\nORDENANDO CODIGO SÓ DE PARES")

comparacoes = 0
substituicoes = 0
iteracoes = 0 

print(f"Código com 'letras Pares' {codigoPares}")
insertionsort(codigoPares)
print(f"\nCódigo Par Ordenado InsertionSort: {codigoPares}")
