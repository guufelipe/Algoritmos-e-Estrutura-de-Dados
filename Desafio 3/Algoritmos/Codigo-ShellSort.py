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


def shellsort(vetor):
    global comparacoes, substituicoes, iteracoes
    n = len(vetor)

    # vejo o maior valor h da sequência de Knuth que seja menor que n
    h = 1
    while h < n // 3:
        h = 3 * h + 1  # Gera a sequência: 1, 4, 13, 40, 121, ...

    # Enquanto h for maior ou igual a 1, realiza a ordenação com pulo = h.
    while h >= 1:
        # Para cada elemento, a partir do índice h até o final:
        for i in range(h, n):
            j = i

            # Enquanto j >= h e o elemento na posição j tiver um valor menor que o elemento h posições atrás, realiza a troca 
            while j >= h and (letras.index(vetor[j]) + 1) < (letras.index(vetor[j - h]) + 1):
                comparacoes += 1
                aux = vetor[j]
                vetor[j] = vetor[j - h]
                vetor[j - h] = aux
                j -= h
                substituicoes += 1
        
        iteracoes += 1
        print(f"Iteração {iteracoes}: {vetor}")
        
        

        h //= 3

shellsort(codigo)


print(f"\nCódigo Ordenado ShellSort:{codigo}")
print(f"Total de comparações: {comparacoes}")
print(f"Total de substituições: {substituicoes}")
print(f"Total de iterações: {iteracoes}")


print(f"\nORDENANDO CODIGO SÓ DE PARES")

comparacoes = 0
substituicoes = 0
iteracoes = 0 

print(f"Código com 'letras Pares' {codigoPares}")
shellsort(codigoPares)
print(f"\nCódigo Par Ordenado ShellSort: {codigoPares}")

