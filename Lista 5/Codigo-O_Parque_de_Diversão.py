# -*- coding: utf-8 -*-

def main():
    quantidadeBrinquedos = int(input())

    diversaoInicial = []        # S[i]: diversão na primeira corrida
    fatorAborrecimento = []     # B[i]: quanto perde de diversão a cada corrida extra
    custoPorCorrida = []        # C[i]: custo em créditos por cada corrida

    for i in range(quantidadeBrinquedos):
        entrada = input().split()
        diversaoInicial.append(int(entrada[0]))
        fatorAborrecimento.append(int(entrada[1]))
        custoPorCorrida.append(int(entrada[2]))

    quantidadeVisitas = int(input())

    # Para cada visita
    for indiceVisita in range(quantidadeVisitas):
        totalCreditos = int(input())

        corridasPossiveis = []  #Guardar todas as possíveis corridas com diversão > 0

        # Simula as corridas de cada brinquedo
        for indiceBrinquedo in range(quantidadeBrinquedos):
            numeroCorrida = 1

            maxCorridas = 100 

            while numeroCorrida <= maxCorridas:
                # Calcula a diversão da corrida atual
                diversaoCorrida = diversaoInicial[indiceBrinquedo] - (numeroCorrida - 1) * (numeroCorrida - 1) * fatorAborrecimento[indiceBrinquedo]

                if diversaoCorrida <= 0:
                    break  # Se não for mais divertido, para

                custo = custoPorCorrida[indiceBrinquedo]

                if custo > totalCreditos:
                    break  # Se o custo já é maior do que temos de crédito, para também

                corridasPossiveis.append((custo, diversaoCorrida))
                numeroCorrida += 1  # Vai pra próxima corrida

        # dp[x] = maior diversão possível com x créditos
        dp = [0] * (totalCreditos + 1)

        # PD estilo da mochila 0-1
        for corrida in corridasPossiveis:
            custoCorrida = corrida[0]
            diversaoCorrida = corrida[1]

            # Atualiza de trás pra frente pra não sobrescrever valores antes de usar
            for creditoAtual in range(totalCreditos, custoCorrida - 1, -1):
                novaDiversao = dp[creditoAtual - custoCorrida] + diversaoCorrida

                if novaDiversao > dp[creditoAtual]:
                    dp[creditoAtual] = novaDiversao  # Atualiza se for melhor

        # Imprime o resultado para esse visitante
        print(str(indiceVisita) + ": " + str(dp[totalCreditos]))


if __name__ == "__main__":
    main()
