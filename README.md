# Comparação de Métodos Numéricos para Cálculo de Massa de Paraquedista

Este projeto implementa três métodos numéricos clássicos para encontrar raízes de equações: o **Método da Falsa Posição**, o **Método da Bisseção** e o **Método de Newton-Raphson**. Esses métodos foram aplicados para resolver um problema do mundo real, relacionado ao cálculo da massa de um paraquedista em queda livre, dado um valor alvo de velocidade e outros parâmetros físicos.

## Métodos Numéricos Utilizados

### Método da Falsa Posição

O **Método da Falsa Posição** (também conhecido como Método da Regula Falsi) é uma técnica iterativa usada para encontrar a raiz de uma função contínua. Ele se baseia no mesmo princípio do método da bisseção, mas em vez de tomar o ponto médio do intervalo, o método calcula uma interpolação linear entre os extremos do intervalo. 

Esse método é eficiente em situações onde a função muda de sinal em um intervalo, e tende a ser mais rápido do que o método da bisseção em certos casos, mas pode não convergir tão rápido quanto o Método de Newton-Raphson.

### Método da Bisseção

O **Método da Bisseção** é um dos métodos numéricos mais simples para encontrar raízes. Ele funciona dividindo repetidamente o intervalo onde a função muda de sinal e selecionando a subparte do intervalo onde ocorre a mudança de sinal. Isso garante que a raiz sempre esteja dentro do intervalo e o método seja extremamente estável, mas ele pode ser mais lento em termos de número de iterações.

### Método de Newton-Raphson

O **Método de Newton-Raphson** é um método iterativo que utiliza a derivada da função para estimar a raiz. Ele converge muito mais rapidamente do que os métodos anteriores quando se tem uma boa estimativa inicial e uma função bem comportada, mas pode falhar se a derivada da função for zero em algum ponto ou se o palpite inicial for muito distante da raiz verdadeira.

## Aplicação no Mundo Real: Cálculo da Massa de um Paraquedista

Neste projeto, utilizamos os três métodos para resolver o problema do cálculo da massa de um paraquedista em queda livre, dado o tempo de queda e a velocidade terminal desejada. O problema é modelado pela seguinte equação física:

\[
v(t) = \frac{mg}{c} \left(1 - e^{-\frac{c}{m}t}\right)
\]

Onde:
- \( v(t) \) é a velocidade em um dado tempo \( t \),
- \( m \) é a massa do paraquedista (variável desconhecida que estamos buscando),
- \( g = 9.81 \, \text{m/s}^2 \) é a aceleração gravitacional,
- \( c \) é o coeficiente de arrasto (supondo um valor constante),
- \( t \) é o tempo de queda.

A equação foi rearranjada para que a função \( f(m) \) tenha a forma:

\[
f(m) = \frac{mg}{c} \left(1 - e^{-\frac{c}{m}t}\right) - v(t) = 0
\]

O objetivo é encontrar a raiz de \( f(m) \), que corresponde à massa \( m \) que satisfaz a equação.

### Método de Arredondamento

Para garantir a consistência nos resultados, utilizamos um método de arredondamento que primeiro arredonda o valor obtido para o inteiro mais próximo e, em seguida, arredonda para duas casas decimais. Esse método é aplicado a todos os resultados finais dos métodos numéricos, a fim de garantir que os valores sejam comparáveis e apropriados para a aplicação prática.

Função de arredondamento:

```python
def round_to_two_decimals(value):
    return round(round(value), 2)
```

## Driver Code e Método Comparativo

### Código Driver

O código driver executa os três métodos numéricos para calcular a massa do paraquedista e exibe o número de iterações que cada método levou para encontrar a solução. Ele define os parâmetros físicos como a aceleração gravitacional \( g \), o coeficiente de arrasto \( c \), o tempo de queda \( t \), e a velocidade alvo \( v(t) \), além dos intervalos ou estimativas iniciais necessárias para cada método.

### Método Comparativo

Além de executar cada método individualmente, o driver inclui uma função de comparação que avalia a eficiência dos métodos com base no número de iterações necessárias para convergir para a solução. O método mais eficiente é aquele que requer o menor número de iterações, embora todos os métodos sejam projetados para retornar a mesma solução final (com pequenas variações numéricas).

Exemplo de saída do código comparativo:

```text
Método da Falsa Posição: Raiz = 82.37, Iterações = 23
Método da Bisseção: Raiz = 82.37, Iterações = 27
Método de Newton-Raphson: Raiz = 82.37, Iterações = 5

O método mais eficiente é Newton-Raphson com 5 iterações.
```