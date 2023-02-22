matriz1 = [[3,1,3],[6,5,5]]
matriz2 = [[100,50],[50,100],[50,50]]

if len(matriz1[0]) != len(matriz2):
    print("Impossível multiplicar as matrizes.")
else:
    #  Definindo o tamanho da matriz resultado, colocando todos os espaços com 0
     resultado = [[0 for j in range(len(matriz2[0]))] for i in range(len(matriz1))]

    # a variável i serve para definir a quantidade de linhas que tem a matriz1 e em qual
    # vai multiplicar primeiro.

    # a variável j serve para definir a quantidade de colunas que tem a matriz 2 e em qual dos itens ele vai
    # selecionar para realizar a multiplicação.


    # já a variável k, vai servir para ficar alternando entre as colunas da matriz1 com as
    # linhas da matriz2, multiplicando e armazenando em valorResultado na posição em que
    # o calculo está sendo realizado.

    # resumindo, ele está trabalhando com posições para definir quais termos serão multiplicado
    # por outros, se adaptar as matrizes para outros tamanhos e outros resultados, se o calculo
    # for possível de realizar, ele irá permitir, depende se a quantidade de colunas da primeira
    # matriz for igual a quantidade de linhas da segunda (ele valida pelo tamanho)

    # ao usar o módulo len, quando usa colocando somente o nome da variável, ele vai retornar
    # a quantidade de linhas, já quando usa colocando o nome da variável e o índice 0
    # por exemplo: matriz1[0], ele vai retornar a quantidade de colunas.

     for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            valorResultado = 0
            for k in range(len(matriz2)):
                valorResultado += matriz1[i][k] * matriz2[k][j]
            resultado[i][j] = valorResultado

     for row in resultado:
        print(row)