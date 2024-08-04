import timeit  # Medir o tempo de execução de trechos de código
import random  # Gerar números aleatórios
import matplotlib.pyplot as plt  # Criar gráficos

# Função para gerar os valores das barras
def generate_sorted_array(n):
    if n <= 0:
        raise ValueError("O tamanho do vetor deve ser maior que 0.")

    # Gera um array com valores aleatórios e ordena
    array = [random.randint(1, 100) for _ in range(n)]
    array.sort()
    return array

# Função para calcular o lucro máximo iterativo
def rod_cutting(prices, n):
    """
    Calcula o lucro máximo que pode ser obtido cortando uma barra de comprimento n de forma iterativa.
    :param prices: Lista de preços das barras.
    :param n: Comprimento da barra.
    :return: Lucro máximo obtido.
    """
    # Array para armazenar os resultados de subproblemas
    array = [0] * (n + 1)

    # Preenche o array com os valores ótimos para cada tamanho de barra
    for i in range(1, n + 1):
        max_value = -float("inf")
        for j in range(1, i + 1):
            max_value = max(max_value, prices[j - 1] + array[i - j])
        array[i] = max_value
    return array[n]

# Função para calcular o lucro máximo recursivamente com memoização
def rod_cutting_recursive(prices, n, memo=None):
    """
    Calcula o lucro máximo que pode ser obtido cortando uma barra de comprimento n de forma recursiva com memoização.
    :prices: Lista de preços das barras.
    :n: Comprimento da barra.
    :memo: Array para armazenar resultados de subproblemas já calculados.
    :return: Lucro máximo obtido.
    """
    if memo is None:
        memo = [-1] * (n + 1)
    if n == 0:
        return 0
    if memo[n] != -1:
        return memo[n]

    max_value = -float("inf")
    for i in range(1, n + 1):
        max_value = max(
            max_value, prices[i - 1] + rod_cutting_recursive(prices, n - i, memo)
        )
    memo[n] = max_value
    return max_value

# Função para medir o tempo de execução de uma função
def measure_time(func, *args, repetitions=10):
    """
    Mede o tempo de execução de uma função.
    :func: A função a ser medida.
    :args: Argumentos da função.
    :repetitions: Número de vezes que a medição será repetida.
    :return: Tempo mínimo de execução entre as repetições.
    """
    timer = timeit.Timer(lambda: func(*args))
    return min(timer.repeat(repeat=repetitions, number=1))

# Função principal para executar os testes e plotar o gráfico
if __name__ == "__main__":
    # Define os tamanhos das barras que serão testados
    bars = [1, 10, 20, 30]

    # Gera os valores para as barras de acordo com o maior tamanho de barra
    prices = generate_sorted_array(bars[-1])
    temp_iterative = []
    temp_recursive = []

    print("Dados")
    for bar in bars:
        # Mede o tempo de execução para o método iterativo
        time_iterative = measure_time(rod_cutting, prices, bar)

        # Mede o tempo de execução para o método recursivo com memoização
        time_recursive = measure_time(rod_cutting_recursive, prices, bar)

        # Adiciona os tempos de execução às listas para plotar posteriormente
        temp_iterative.append(time_iterative)
        temp_recursive.append(time_recursive)
        # Exibe os resultados para o tamanho de barra atual
        print(f"Tamanho da Barra: {bar}")
        print(f"Tempo iterativo: {time_iterative}")
        print(f"Tempo recursivo: {time_recursive}")
        print()
        
    # Plotando os gráficos
    plt.figure(figsize=(10, 6))
    plt.plot(bars, temp_iterative, label="Iterativo", color="red")
    plt.plot(bars, temp_recursive, label="Recursivo", color="green")
    plt.xlabel("Tamanho das Barras")
    plt.ylabel("Tempo em Segundos")
    plt.title("Comparação de Tempos: Cortes de Barras")
    plt.legend()
    plt.grid(True)
    plt.show()
