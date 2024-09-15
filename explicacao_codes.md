# Explicação em Profundidade do Projeto: Métodos Numéricos

Este arquivo `.md` fornece uma explicação detalhada dos dois principais componentes deste projeto:

1. **numerical_methods.py**: Onde estão implementados os três métodos numéricos (Falsa Posição, Bisseção, Newton-Raphson).
2. **driver.py**: O código que usa esses métodos para resolver um problema real relacionado ao cálculo da massa de um paraquedista, além de um método comparativo para determinar qual técnica é mais eficiente.

## Arquivo: `numerical_methods.py`

Este arquivo contém a implementação dos três métodos numéricos usados para encontrar a raiz de uma equação: **Método da Falsa Posição**, **Método da Bisseção** e **Método de Newton-Raphson**. Além disso, foi implementada uma função auxiliar para arredondamento dos resultados.

### Função `round_to_two_decimals`

```python
def round_to_two_decimals(value):
    return round(round(value), 2)
```

Esta função realiza o arredondamento duplo: primeiro arredonda o valor para o número inteiro mais próximo e, em seguida, o arredonda para duas casas decimais. É utilizada para garantir consistência nos resultados e facilitar a interpretação prática dos mesmos.

### Classe: `FalsePositionMethod`

Esta classe implementa o **Método da Falsa Posição**. 

#### Atributos:
- `f`: Função que queremos resolver (no caso, relacionada ao cálculo da massa do paraquedista).
- `lower_bound` e `upper_bound`: Limites inferior e superior do intervalo em que a solução (raiz) será procurada.
- `max_iterations`: Número máximo de iterações permitidas para encontrar a raiz.
- `epsilon`: Critério de convergência, ou seja, quão próximo de zero \( f(m) \) deve ser para aceitarmos a solução.

#### Método `solve()`

Este método realiza o cálculo da raiz usando o Método da Falsa Posição. A cada iteração, ele calcula um ponto intermediário usando interpolação linear e verifica se o valor da função nesse ponto é suficientemente próximo de zero (critério de convergência). Se a solução não for encontrada após o número máximo de iterações, ele retorna o melhor valor encontrado até o momento.

```python
root_approx = (lower_bound * self.f(upper_bound) - upper_bound * self.f(lower_bound)) / (self.f(upper_bound) - self.f(lower_bound))
```

Este cálculo representa o ponto intermediário gerado pela interpolação linear entre os extremos do intervalo.

#### Funções Auxiliares:

- `_check_convergence(f_approx)`: Verifica se o valor \( f(m) \) está suficientemente próximo de zero.
- `_print_iteration(...)`: Imprime os detalhes de cada iteração (usado para depuração e análise de resultados).

### Classe: `BisectionMethod`

Esta classe implementa o **Método da Bisseção**, que é um método robusto e garantido de encontrar uma solução se a função mudar de sinal no intervalo fornecido.

#### Método `solve()`

Este método itera dividindo o intervalo ao meio, a cada passo, e verificando se a raiz está no subintervalo esquerdo ou direito. A convergência ocorre quando o valor da função no ponto médio do intervalo for suficientemente pequeno.

```python
midpoint = (lower_bound + upper_bound) / 2
```

Aqui, simplesmente calculamos o ponto médio do intervalo atual. O método repete essa operação até que a solução seja encontrada ou até atingir o número máximo de iterações.

### Classe: `NewtonRaphsonMethod`

A classe **NewtonRaphsonMethod** implementa o Método de Newton-Raphson, que é conhecido por sua rápida convergência, especialmente quando temos uma boa estimativa inicial.

#### Atributos:
- `f`: Função que queremos resolver.
- `df`: Derivada da função \( f \), necessária para o cálculo da próxima aproximação.
- `initial_guess`: Estimativa inicial da raiz.
- `epsilon` e `max_iterations`: Critério de convergência e número máximo de iterações.

#### Método `solve()`

Este método utiliza a seguinte fórmula iterativa:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

Onde \( x_n \) é a aproximação atual e \( f'(x_n) \) é o valor da derivada da função no ponto \( x_n \). O método é altamente eficiente, mas pode falhar se \( f'(x_n) = 0 \), ou se a estimativa inicial for muito longe da raiz real.

## Arquivo: `driver.py`

O arquivo `driver.py` é responsável por aplicar os três métodos numéricos ao problema real de cálculo da massa de um paraquedista, além de fornecer uma comparação quantitativa da eficiência de cada método com base no número de iterações.

### Função `f(m)`

```python
def f(m):
    return (m * g / c) * (1 - math.exp(-c * t / m)) - v_alvo
```

Esta função representa a equação que modela o comportamento da queda livre do paraquedista, conforme explicada na seção do problema físico. Queremos encontrar o valor de \( m \) (massa) que satisfaz a equação, dado o valor alvo da velocidade \( v(t) \).

### Função `df(m)`

```python
def df(m):
    return g / c * (1 - math.exp(-c * t / m)) + (g * t * math.exp(-c * t / m)) / m
```

Esta é a derivada de \( f(m) \), necessária para o Método de Newton-Raphson.

### Função `comparar_metodos()`

Esta função compara os três métodos numéricos, executando cada um com os mesmos parâmetros e imprimindo tanto a raiz (massa encontrada) quanto o número de iterações necessárias para que cada método convergisse. Ela também determina qual método foi o mais eficiente, ou seja, aquele que utilizou o menor número de iterações.

#### Exemplo de Uso:

1. **Método da Falsa Posição**:
   - Raiz = 82.37 kg
   - Iterações = 23

2. **Método da Bisseção**:
   - Raiz = 82.37 kg
   - Iterações = 27

3. **Método de Newton-Raphson**:
   - Raiz = 82.37 kg
   - Iterações = 5

#### Lógica de Comparação:

```python
min_iteracoes = min(iteracoes_fp, iteracoes_bis, iteracoes_newton)
if min_iteracoes == iteracoes_fp:
    melhor_metodo = "Falsa Posição"
elif min_iteracoes == iteracoes_bis:
    melhor_metodo = "Bisseção"
else:
    melhor_metodo = "Newton-Raphson"
```

Este trecho de código determina qual método foi o mais eficiente com base no menor número de iterações. No exemplo acima, o Método de Newton-Raphson foi o mais rápido, com apenas 5 iterações.
