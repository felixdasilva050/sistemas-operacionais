import os
import sys
import random

class Pagina:
    def __init__(self, numero_pagina):
        self.numero_pagina = numero_pagina
        self.tempo_ultimo_acesso = 0

class MemoriaPrincipal:
    def __init__(self, tamanho_memoria, algoritmo):
        self.tamanho_memoria = tamanho_memoria
        self.paginas = []
        self.algoritmo = algoritmo

    def adicionar_pagina(self, pagina):
        if len(self.paginas) < self.tamanho_memoria:
            self.paginas.append(pagina)
        else:
            # Aplicar algoritmo de substituição
            if self.algoritmo == "LRU":
                self.substituir_pagina_LRU(pagina)
            elif self.algoritmo == "FIFO":
                self.substituir_pagina_FIFO(pagina)
            elif self.algoritmo == "RANDOM":
                self.substituir_pagina_RANDOM(pagina)

    def substituir_pagina_LRU(self, nova_pagina):
        pagina_substituir = min(self.paginas, key=lambda pagina: pagina.tempo_ultimo_acesso)
        self.paginas.remove(pagina_substituir)
        self.paginas.append(nova_pagina)

    def substituir_pagina_FIFO(self, nova_pagina):
        pagina_substituir = self.paginas.pop(0)
        self.paginas.append(nova_pagina)

    def substituir_pagina_RANDOM(self, nova_pagina):
        pagina_substituir = random.choice(self.paginas)
        self.paginas.remove(pagina_substituir)
        self.paginas.append(nova_pagina)

    def acessar_pagina(self, numero_pagina):
        for pagina in self.paginas:
            if pagina.numero_pagina == numero_pagina:
                pagina.tempo_ultimo_acesso += 1
                return True
        return False

class SimuladorMemoriaVirtual:
    txt_exibicao_usuario = "[algoritmo (LRU, FIFO, Random)], [arquivo (tem que estar na pasta logs)], [tamanho_pagina] e [tamanho_memoria]: "

    def __init__(self):
        pass

    def executar(self):
        while True:
            print("\nPara sair do programa, utilize 'quit()'")
            entrada = input(f"Digite {SimuladorMemoriaVirtual.txt_exibicao_usuario}")

            if entrada.strip().lower() == 'quit()':
                print("Saindo do programa...")
                break

            try:
                algoritmo, arquivo, tamanho_pagina, tamanho_memoria = map(str.strip, entrada.split(','))
                tamanho_pagina = int(tamanho_pagina)
                tamanho_memoria = int(tamanho_memoria)

                if tamanho_pagina < 2 or tamanho_pagina > 64 or tamanho_memoria < 128 or tamanho_memoria > 16384:
                    raise ValueError

                self.executar_simulacao(algoritmo, arquivo, tamanho_pagina, tamanho_memoria)

            except ValueError:
                print("Erro: Por favor, verifique se os valores foram digitados corretamente.")
                print(f"Formato correto: {SimuladorMemoriaVirtual.txt_exibicao_usuario}")

    def executar_simulacao(self, algoritmo, arquivo, tamanho_pagina, tamanho_memoria):
        # Ler as instruções do arquivo
        with open(os.path.join("logs", arquivo), 'r') as f:
            instrucoes = [linha.strip().split() for linha in f]

        # Criar a memória principal com o algoritmo escolhido
        memoria_principal = MemoriaPrincipal(tamanho_memoria)
        memoria_principal.algoritmo = algoritmo

        # Realizar a simulação
        for operacao, numero_pagina in instrucoes:
            numero_pagina = int(numero_pagina)
            if operacao == 'R':
                if memoria_principal.acessar_pagina(numero_pagina):
                    print(f'Leitura na página {numero_pagina} sem page fault')
                else:
                    print(f'Leitura na página {numero_pagina} com page fault')
                pagina = Pagina(numero_pagina)
                memoria_principal.adicionar_pagina(pagina)
            elif operacao == 'W':
                if memoria_principal.acessar_pagina(numero_pagina):
                    print(f'Escrita na página {numero_pagina} sem page fault')
                else:
                    print(f'Escrita na página {numero_pagina} com page fault')
                pagina = Pagina(numero_pagina)
                memoria_principal.adicionar_pagina(pagina)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Para iniciar o programa, utilize apenas o comando 'python app.py'")
        sys.exit(1)

    simulador = SimuladorMemoriaVirtual()
    simulador.executar()