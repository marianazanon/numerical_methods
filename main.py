from numerical_methods import FalsePositionMethod, BisectionMethod, NewtonRaphsonMethod
import math

# Constantes
g = 9.81  # constante gravitacional (m/s^2)
c = 12.5  # coeficiente de arrasto (kg/s)
v_alvo = 45  # velocidade alvo (m/s)
t = 10  # tempo (s)

def f(m):
    return (m * g / c) * (1 - math.exp(-c * t / m)) - v_alvo

def df(m):
    return g / c * (1 - math.exp(-c * t / m)) + (g * t * math.exp(-c * t / m)) / m

# Função comparativa
def comparar_metodos():
    # Definir os limites para a massa
    limite_inferior = 50  # limite inferior para a massa (kg)
    limite_superior = 200  # limite superior para a massa (kg)
    max_iteracoes = 50
    epsilon = 1e-6
    palpite_inicial = 100  # palpite inicial para Newton-Raphson

    # Método da Falsa Posição
    metodo_falsa_posicao = FalsePositionMethod(f, limite_inferior, limite_superior, max_iteracoes, epsilon)
    raiz_fp, iteracoes_fp = metodo_falsa_posicao.solve()
    print(f"Método da Falsa Posição: Raiz = {raiz_fp:.2f}, Iterações = {iteracoes_fp}")

    # Método da Bisseção
    metodo_bissecao = BisectionMethod(f, limite_inferior, limite_superior, max_iteracoes, epsilon)
    raiz_bis, iteracoes_bis = metodo_bissecao.solve()
    print(f"Método da Bisseção: Raiz = {raiz_bis:.2f}, Iterações = {iteracoes_bis}")

    # Método de Newton-Raphson
    metodo_newton = NewtonRaphsonMethod(f, df, palpite_inicial, epsilon, max_iteracoes)
    raiz_newton, iteracoes_newton = metodo_newton.solve()
    print(f"Método de Newton-Raphson: Raiz = {raiz_newton:.2f}, Iterações = {iteracoes_newton}")

    resultados = {
        "Falsa Posição": {"raiz": raiz_fp, "iterações": iteracoes_fp},
        "Bisseção": {"raiz": raiz_bis, "iterações": iteracoes_bis},
        "Newton-Raphson": {"raiz": raiz_newton, "iterações": iteracoes_newton},
    }

    min_iteracoes = min(iteracoes_fp, iteracoes_bis, iteracoes_newton)
    if min_iteracoes == iteracoes_fp:
        melhor_metodo = "Falsa Posição"
    elif min_iteracoes == iteracoes_bis:
        melhor_metodo = "Bisseção"
    else:
        melhor_metodo = "Newton-Raphson"

    print(f"\nO método mais eficiente é {melhor_metodo} com {min_iteracoes} iterações.")

if __name__ == "__main__":
    comparar_metodos()
