##USADO PARA CRIAR UM ARQUIVO LOG DE MAIOR COMPLEXIDADE
##AFIM DE TESTAR O APP DE SIMULACAO DE MEMORIA VIRTUAL
import os
import random

def criar_log(nome_arquivo, num_operacoes, num_paginas, proporcao_leitura=0.7):
    caminho_arquivo = os.path.join("logs", nome_arquivo)
    with open(caminho_arquivo, 'w') as f:
        for _ in range(num_operacoes):
            operacao = 'R' if random.random() < proporcao_leitura else 'W'
            pagina = random.randint(1, num_paginas)
            f.write(f"{operacao} {pagina}\n")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de log a ser criado: ")
    num_operacoes = int(input("Digite o número de operações desejado: "))
    num_paginas = int(input("Digite o número de páginas desejado: "))
    proporcao_leitura = float(input("Digite a proporção de operações de leitura (0 a 1): "))

    criar_log(nome_arquivo, num_operacoes, num_paginas, proporcao_leitura)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso com {num_operacoes} operações na pasta 'logs'.")
