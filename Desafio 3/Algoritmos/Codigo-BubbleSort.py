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

def buublesort(vetor):
    global comparacoes, substituicoes, iteracoes

    n = len(vetor)
    #BubbleSort: 
    for i in range(n - 1):
        iteracoes += 1
        for j in range(n - 1 - i):
            comparacoes += 1

            #Valor da letra atual é o indice em que a letra vetor[j] está em letras +1         
            valorAtual = letras.index(vetor[j]) + 1
            #Valor da proxima letra é o indice em que a letra vetor[j+1] está em letras +1
            valorProximo = letras.index(vetor[(j + 1)]) + 1

            #Se a letra atual for maior que a seguinte letra, então troca elas.
            if valorAtual > valorProximo:
                vetor[j], vetor[j + 1] = vetor[j +1], vetor[j]
                substituicoes += 1
        
        print(f"Iteração {iteracoes}: {vetor}")

buublesort(codigo)

print("\nCódigo ordenado por BubbleSort:", codigo)
print(f"Total de comparações: {comparacoes}")
print(f"Total de substituições: {substituicoes}")
print(f"Total de iterações: {iteracoes}")

print(f"\nORDENANDO CODIGO SÓ DE PARES")

comparacoes = 0
substituicoes = 0
iteracoes = 0 

print(f"Código com 'letras Pares' {codigoPares}")
buublesort(codigoPares)
print(f"\nCódigo Par Ordenado BubbleSort: {codigoPares}")
