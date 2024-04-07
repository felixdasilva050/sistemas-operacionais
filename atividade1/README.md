# Simulador simplificado de memória virtual baseado em paginação. 
O objetivo é simular operações de uma leitura e escrita na memória principal, quando se faz uso do recurso de memória virtual, a partir de um conjunto de page misses e page faults, permitindo comparar os algoritmos de substituição LRU, FIFO e Random.

A estrutura que deve ser utilizada para usar esse script é a seguinte (não utilizar os [ ]): 
```
virtual [algoritmo], [arquivo], [tamanho_pagina], [tamanho_memoria]
```
onde: 

- *algoritmo*: algorítimo de substituição a ser utilizado, valores possíveis (LRU, FIFO e RANDOM).
- *arquivo*: contendo as instruções de leitura e escrita (seguir modelo de arquivo.log).
- *tamanho_pagina*: tamanho de cada página. valores aceitáveis 2 até 64.
- *tamanho_memoria*: tamanho total da memória disponível. Valores aceitáveis: 128 a 16384

Para executar esse script é recomendado que você esteja utilizando python 3.0 ou superior. Coloque na pasta "logs" o log de instruções que deseja testar.

## A chamada do script é muito simples (app.py)


1. Entre na pasta pelo terminal (ou CMD)"**simulador-memoriaVirtual**"
2. Digite:
```
python app.py
```
3. Siga as intruções que o script falará; Use "quit()" para sair e respeite o padrão citado anteriormente (dentro do script haverá mais detalhes também)

## Em caso de não ter um log de instruções para utilizar/testar?
Você pode criar um utilizando o script **preload_logs.py**. Nesse caso, você deve executar primeiro esse script **preload_logs.py** e em seguida utilizar o *app.py* para testar. Você deverá informar nesse script: 
- nome do arquivo que deseja criar
- número de **operações** desejadas (1000+)
- número de **páginas** desejadas (50+)
- uma proporção de operações de leitura (podendo ser de 0 **a** 1). Esse arquivo será automaticamente criado na pasta "*logs*".

Destacamos que os valores recomendados para o número de *operações* e *páginas* são apenas sugestões, e podem ser ajustados conforme necessário. Recomenda-se aumentar esses valores para proporcionar uma representação mais precisa do programa. Caso contrário, os resultados podem acabar sendo muito semelhantes ou até idênticos, limitando a eficácia da análise.

### Para executar
1. Entre na pasta pelo terminal (ou CMD) "**simulador-memoriaVirtual**"
2. Digite:
```
python preload_logs.py
```
3. Informe o que o programa pedir.