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

# SelectSort -> Escolhe o menor, coloca o menor na primeira posição e repete sem considerar a primeira posição
def selectsort(vetor):
    global comparacoes, substituicoes, iteracoes
    n = len(vetor)
    
    for i in range(n):
        # Assume que o menor elemento está inicialmente na posição i
        indiceMenor = i
        
        # Percorre a sublista que está depois do menor elemento para encontrar outro menor
        for j in range(i + 1, n):
            comparacoes += 1
            # Se a letra na posição j for menor que a do índiceMenor, atualiza indiceMenor
            if letras.index(vetor[j]) < letras.index(vetor[indiceMenor]):
                indiceMenor = j
        
        # Se encontrou um valor menor, faz a troca dos elementos
        if indiceMenor != i:
            vetor[i], vetor[indiceMenor] = vetor[indiceMenor], vetor[i]
            substituicoes += 1  
        
        iteracoes += 1
        print(f"Iteração {iteracoes}: {vetor}")


selectsort(codigo)

print(f"\nCódigo Ordenado SelectSort: {codigo}")
print(f"Total de comparações: {comparacoes}")
print(f"Total de substituições: {substituicoes}")
print(f"Total de iterações: {iteracoes}")

print(f"\nORDENANDO CODIGO SÓ DE PARES")

comparacoes = 0
substituicoes = 0
iteracoes = 0 

print(f"Código com 'letras Pares' {codigoPares}")
selectsort   (codigoPares)
print(f"\nCódigo Par Ordenado SelectSort: {codigoPares}")