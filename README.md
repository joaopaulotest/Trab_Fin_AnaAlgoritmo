# Trab_Fin_AnaAlgoritmo
 Neste projeto vai comparar dois algoritmos para resolver um problema de otimização que pode ser resolvido com programação dinâmica.  O problema tem subestrutura ótima e a solução recursiva direta deve ter sobreposição de subproblemas.  Dessa forma, os dois algoritmos que serão comparados devem estar relacionados com programação dinâmica da seguinte forma: um algoritmo deve ser uma solução recursiva com memoização e o outro deve ser uma solução iterativa.  Na comparação, deve apresentar um gráfico no qual o eixo horizontal representa o tamanho da entrada e o eixo vertical, e representa o tempo de execução médio.  O código para comparar os dois algoritmos deve escolher tamanhos de entrada n adequados para a comparação.  Além disso, o código deve criar, aleatoriamente e adequadamente (consistente com o problema), entradas para o problema.  Para cada tamanho de entrada n, deve criar m entradas de tamanho n e fazer uma média do tempo de execução para entradas de tamanho n, e deve comparar os algoritmos de forma justa, então você deve criar os tamanhos de entrada e as entradas para executar os algoritmos levando isso em consideração ou seja, os dois algoritmos devem ser comparados com exatamente as mesmas entradas. 

Descrição dos Cortes de Barras
Entrada:
prices: Uma lista de preços onde prices[i] é o preço de uma barra de comprimento i+1.
n: O comprimento da barra a ser cortada.

Saída:
O lucro máximo que pode ser obtido cortando a barra de comprimento n.

Algoritmo Iterativo:
Utiliza um array onde array[i] representa o lucro máximo obtido para uma barra de comprimento i.
Preenche o array de forma iterativa, calculando o lucro máximo para cada comprimento de barra até n.
Algoritmo Recursivo com Memoização:
Utiliza uma função recursiva que calcula o lucro máximo para a barra de comprimento n utilizando memoização para armazenar os resultados de subproblemas já calculados.
A memoização evita a recalculação dos mesmos subproblemas, melhorando a eficiência.

Algoritmo Iterativo
Complexidade de Tempo:
O algoritmo iterativo rod_cutting(prices, n) usa dois loops aninhados:

O loop externo percorre de 1 a n.
O loop interno também percorre de 1 a i (onde i é o índice do loop externo).
Portanto, a complexidade de tempo é Θ(n^2).

Complexidade de Espaço:
O algoritmo usa um array de tamanho n+1 para armazenar os resultados dos subproblemas. Portanto, a complexidade de espaço é Θ(n).

Algoritmo Recursivo com Memoização
Complexidade de Tempo:
O algoritmo recursivo rod_cutting_recursive(prices, n, memo) com memoização evita a recalculação de subproblemas. Cada subproblema é resolvido uma vez e armazenado no array memo.

A função recursiva é chamada no máximo n vezes, e cada chamada envolve um loop de 1 a n.
A complexidade de tempo é Θ(n^2).

Complexidade de Espaço:
O algoritmo utiliza um array memo de tamanho n+1 para armazenar os resultados dos subproblemas. Além disso, a profundidade da pilha de chamadas recursivas é Θ(n).

Portanto, a complexidade de espaço é Θ(n) (para o array memo), mas considerando a pilha de chamadas recursivas, a complexidade total de espaço é Θ(n).

Resumo das Complexidades
Algoritmo			       Complexidade de Tempo	Complexidade de Espaço
Iterativo			         Θ(n^2)				      Θ(n)
Recursivo com Memoização     Θ(n^2)				      Θ(n)
