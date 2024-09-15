## Arquivo: `numerical_methods.py`

Este arquivo contém a implementação dos três métodos numéricos: **Falsa Posição**, **Bisseção** e **Newton-Raphson**, além de uma função auxiliar para arredondamento.

### Função `round_to_two_decimals`

```python
def round_to_two_decimals(value):
    return round(round(value), 2)
```

- **Linha 1**: Define a função `round_to_two_decimals`, que recebe um valor como argumento.
- **Linha 2**: A função realiza o arredondamento duplo: primeiro, arredonda o valor para o número inteiro mais próximo e, em seguida, para duas casas decimais. Isso garante consistência nos resultados numéricos.

### Classe `FalsePositionMethod`

Esta classe implementa o **Método da Falsa Posição**.

```python
class FalsePositionMethod:
    def __init__(self, f, lower_bound, upper_bound, max_iterations, epsilon=1e-6):
```

- **Linha 1**: Define a classe `FalsePositionMethod`.
- **Linha 2**: Define o método construtor `__init__` da classe, que recebe:
  - `f`: A função que queremos resolver.
  - `lower_bound`: O limite inferior do intervalo.
  - `upper_bound`: O limite superior do intervalo.
  - `max_iterations`: O número máximo de iterações permitidas.
  - `epsilon`: O critério de convergência, que determina quando parar.

```python
self.f = f
self.lower_bound = lower_bound
self.upper_bound = upper_bound
self.max_iterations = max_iterations
self.epsilon = epsilon
```

- **Linhas 3-7**: Inicializa os atributos da classe com os valores passados.

#### Método `solve`

```python
def solve(self):
    if self.f(self.lower_bound) * self.f(self.upper_bound) > 0:
        raise ValueError("False position method failed. Choose another interval.")
```

- **Linha 1**: Define o método `solve`, que executa o **Método da Falsa Posição**.
- **Linha 2**: Verifica se a função \( f \) tem sinais opostos nos limites inferior e superior (um pré-requisito para o método funcionar).
- **Linha 3**: Se a função não mudar de sinal, o método levanta um erro, pois não há garantia de que uma raiz esteja presente no intervalo.

```python
lower_bound, upper_bound = self.lower_bound, self.upper_bound
```

- **Linha 5**: Define variáveis locais para `lower_bound` e `upper_bound`, copiando os valores dos atributos da classe.

```python
for iteration in range(self.max_iterations):
    root_approx = (lower_bound * self.f(upper_bound) - upper_bound * self.f(lower_bound)) / (self.f(upper_bound) - self.f(lower_bound))
```

- **Linha 7**: Inicia um loop que realiza as iterações até o máximo permitido.
- **Linha 8**: Calcula a aproximação da raiz usando interpolação linear entre os limites do intervalo.

```python
f_approx = self.f(root_approx)
```

- **Linha 9**: Calcula o valor da função no ponto `root_approx`.

```python
if self._check_convergence(f_approx):
    return round_to_two_decimals(root_approx), iteration + 1
```

- **Linhas 10-11**: Verifica se o valor da função em `root_approx` está suficientemente próximo de zero (critério de convergência). Se sim, retorna a raiz arredondada e o número de iterações.

```python
if self.f(lower_bound) * f_approx < 0:
    upper_bound = root_approx
elif self.f(upper_bound) * f_approx < 0:
    lower_bound = root_approx
```

- **Linhas 13-17**: Atualiza o intervalo com base no sinal da função em `root_approx`. Se \( f(root\_approx) \) e \( f(lower\_bound) \) tiverem sinais opostos, a raiz está entre `lower_bound` e `root_approx`, então atualizamos o limite superior. Caso contrário, atualizamos o limite inferior.

```python
return round_to_two_decimals(root_approx), self.max_iterations
```

- **Linha 19**: Se o número máximo de iterações for atingido sem convergência, retorna a última aproximação da raiz e o número de iterações.

#### Funções Auxiliares

```python
def _check_convergence(self, f_approx):
    return abs(f_approx) < self.epsilon
```

- **Linha 1**: Define uma função auxiliar para verificar se \( f(root\_approx) \) está suficientemente próximo de zero.
- **Linha 2**: Se o valor absoluto de \( f \) for menor que `epsilon`, a função retorna `True`.

### Classe `BisectionMethod`

A implementação do **Método da Bisseção** é semelhante à da Falsa Posição, com a diferença de que o ponto intermediário é o **ponto médio** do intervalo, em vez de uma interpolação linear.

```python
midpoint = (lower_bound + upper_bound) / 2
```

- **Linha 8**: Aqui, o ponto intermediário é calculado como o ponto médio do intervalo atual.

### Classe `NewtonRaphsonMethod`

Esta classe implementa o **Método de Newton-Raphson**. Como o método depende da derivada, é necessário definir tanto a função \( f(m) \) quanto sua derivada \( f'(m) \).

```python
df_current_approx = self.df(current_approximation)
```

- **Linha 9**: Calcula a derivada de \( f \) no ponto atual, necessária para o cálculo da próxima aproximação.

```python
current_approximation = current_approximation - f_current_approx / df_current_approx
```

- **Linha 13**: Atualiza a estimativa da raiz com base na fórmula de Newton-Raphson \( x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \).

---

## Arquivo: `driver.py`

Este arquivo é o responsável por aplicar os métodos numéricos ao problema do cálculo da massa de um paraquedista e por comparar o desempenho de cada método.

### Função `f(m)`

```python
def f(m):
    return (m * g / c) * (1 - math.exp(-c * t / m)) - v_alvo
```

- **Linha 1**: Define a função \( f(m) \), que representa a equação física do paraquedista em queda livre.
- **Linha 2**: A função calcula a diferença entre a velocidade \( v(t) \) do paraquedista e o valor alvo, dada uma massa \( m \).

### Função `df(m)`

```python
def df(m):
    return g / c * (1 - math.exp(-c * t / m)) + (g * t * math.exp(-c * t / m)) / m
```

- **Linha 1**: Define a derivada da função \( f(m) \), necessária para o Método de Newton-Raphson.

### Função `comparar_metodos`

Esta função executa os três métodos numéricos e compara o número de iterações necessárias para encontrar a solução.

```python
root_fp, iteracoes_fp = metodo_falsa_posicao.solve()
```

- **Linha 8**: Executa o Método da Falsa Posição e armazena a raiz e o número de iterações.

```python
resultados = {
    "Falsa Posição": {"raiz": raiz_fp, "iterações": iteracoes_fp},
    "Bisseção": {"raiz": raiz_bis, "iterações": iteracoes_bis},
    "Newton-Raphson": {"raiz": raiz_newton, "iterações": iteracoes_newton},
}
```

- **Linhas 18-23**: Armazena os resultados de cada método em um dicionário, facilitando a comparação posterior.

```python
min_iteracoes = min(iteracoes_fp, iteracoes_bis, iteracoes_newton)
if min_iteracoes == iteracoes_fp:
    melhor_metodo = "Falsa Posição"
elif min_iteracoes == iteracoes_bis:
    melhor_metodo = "Bisseção"
else:
    melhor_metodo = "Newton-Raphson"
```

- **Linhas 25-30**: Determina qual método foi o mais eficiente com base no menor número de iterações.

---
