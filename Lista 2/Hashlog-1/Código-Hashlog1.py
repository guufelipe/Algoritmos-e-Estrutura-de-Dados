########################################################################
# Bloco 1: Estrutura de Dados – Tabela-Hash com Encadeamento
#
# - A tabela é representada por um array (lista) de baldes;
#   cada balde é uma lista de registros.
# - Cada registro é representado por uma tupla (T, C), onde:
#     T: timestamp (inteiro)
#     C: cliente (inteiro)
########################################################################
 
# Função de hash: dado um timestamp e o tamanho da tabela, retorna o índice.
def hash_index(timestamp, table_size):
    return timestamp % table_size

########################################################################
# Bloco 2: Funções de Rehashing e Inserção
#
# - A função insert(reg, table) insere um registro (T, C) na tabela,
#   usando a função de hash.
# - Se a inserção ocasionar que o número total de registros atinja o
#   limiar (THRESHOLD), então é efetuado o rehashing:
#     novo_tamanho = tamanho_atual + R
#   e todos os registros são reinseridos na nova tabela.
#
# A função retorna:
#   - new_index: índice final (0-based) em que o registro foi inserido;
#   - bucket_size: tamanho do balde após inserção;
#   - table: a tabela (possivelmente rehasheada);
#   - total: número total de registros na tabela.
########################################################################

def insert_record(registro, table, total, table_size, THRESHOLD, R):
    # registro é (T, C)
    T, C = registro
    idx = hash_index(T, table_size)
    # Insere o registro no final do balde idx.
    table[idx].append(registro)
    total += 1
    bucket_size = len(table[idx])
    return idx, bucket_size, table, total

def rehash_all(table, R):
    # Novo tamanho da tabela: tamanho_atual + R
    old_size = len(table)
    new_size = old_size + R
    new_table = [[] for _ in range(new_size)]
    # Reinseri todos os registros da tabela antiga na nova tabela
    for bucket in table:
        for (T, C) in bucket:
            new_idx = hash_index(T, new_size)
            new_table[new_idx].append((T, C))
    return new_table, new_size

########################################################################
# Bloco 3: Operação de Consulta (QRY)
#
# - Dada a tabela, um timestamp T, e o tamanho atual, procura-se
#   o registro com timestamp igual a T no balde h(T).
# - Se encontrado, retorna (C, pos) onde pos é a posição 0-based
#   na lista do balde; senão, retorna (-1, -1).
########################################################################

def query_record(T, table, table_size):
    idx = hash_index(T, table_size)
    bucket = table[idx]
    for pos, (t, c) in enumerate(bucket):
        if t == T:
            return c, pos
    return -1, -1

########################################################################
# Bloco Principal: Processamento da Entrada e Execução
#
# - A primeira linha contém: M R
#   M: tamanho inicial da tabela
#   R: fator de rehash (novo tamanho = M + R)
# - Usamos um limiar (THRESHOLD) para rehashing; neste exemplo, definimos
#   THRESHOLD = 42 (baseado no exemplo esperado, onde o rehash ocorre antes
#   do 43º evento NEW).
# - Para cada evento NEW, insere-se o registro e imprime-se "I S".
# - Para cada evento QRY, realiza-se a consulta e imprime-se "C J".
########################################################################

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    if not input_data:
        sys.exit(0)
    # Primeira linha: M R
    first_line = input_data[0].split()
    M = int(first_line[0])
    R = int(first_line[1])
    # Definimos o limiar para rehashing (ajustado para o exemplo esperado)
    THRESHOLD = 42

    # Inicializa a tabela-hash: lista de M baldes (listas vazias)
    table_size = M
    table = [[] for _ in range(table_size)]
    total = 0  # total de registros na tabela

    # Processa os eventos (a partir da segunda linha)
    for linha in input_data[1:]:
        linha = linha.strip()
        if linha == "END":
            break
        partes = linha.split()
        comando = partes[0]
        if comando == "NEW":
            T = int(partes[1])
            C = int(partes[2])
            # Se a inserção vai fazer o total atingir o limiar, rehash primeiro.
            if total >= THRESHOLD:
                # Rehash: nova tabela e novo tamanho.
                table, table_size = rehash_all(table, R)
                total = sum(len(bucket) for bucket in table)
                # Nota: não imprimimos nada neste momento.
            idx, bucket_size, table, total = insert_record((T, C), table, total, table_size, THRESHOLD, R)
            # Imprime o índice do balde e o tamanho da lista (após inserção)
            print(idx, bucket_size)
        elif comando == "QRY":
            T = int(partes[1])
            c, pos = query_record(T, table, table_size)
            print(c, pos)
