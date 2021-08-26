# from os import X_OK
import pandas as pd
import numpy as np

# Bibliotecas específicas para o aprendizado de máquina
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPRegressor

class AutomacaoCalculo():
  def __init__(self, peso, cilindros, aceleracao, anomodelo):
        self.peso = peso
        self.cilindros = cilindros
        self.aceleracao = aceleracao
        self.anomodelo = anomodelo

  def calcular(self):
    dataset = pd.read_csv("auto-mpg.csv")

    # peso, cilindradas, aceleração
    # X = dataset[["weight", "cylinders", "acceleration", "horsepower"]]
    X = dataset[["weight", "cylinders", "acceleration", "model year"]]
    Y = dataset [["mpg"]]

    print(X);

    # se o carro for mais antigo que 2000, cancatena 19 no retorno do dataset
    if self.anomodelo < '1999':
      X["model year"] = 19+X["model year"]
    else:
      X["model year"] = 20+X["model year"]
    # converter libras pra kg
    X["weight"] = X["weight"] * 0.453592
    # converter milhar pra km
    X["acceleration"] = X["acceleration"] * 1.60934
    Y["mpg"] = Y["mpg"] * 0.425144

    X.describe()

    # Normalização
    escala = StandardScaler()
    escala.fit(X)
    X_norm = escala.transform(X)

    # Dividir o conjunto entre dados de treinamento e teste
    X_norm_train, X_norm_test, Y_train, Y_test = train_test_split(X_norm, Y, test_size=0.3)

    # numero de camadas ocultas (1° 10 neuronios, 2° 5 neur)
    # max de iteração (epocas)
    # tolerancia
    # taxa de aprendizado
    # estrategia (descida do gradiente estocastico)
    # funcao de ativação
    # taxa constante
    rna = MLPRegressor( hidden_layer_sizes=(10, 5),
                        max_iter=4000,
                        tol=0.0000001,
                        learning_rate_init=0.1,
                        solver="sgd",
                        activation="logistic",
                        learning_rate="constant",
                        verbose=2,
                      )

    rna.fit(X_norm_train, Y_train)
    X_futuro = np.array([[self.peso], [self.cilindros], [self.aceleracao], [self.anomodelo]])
    X_futuro_norm = escala.transform(X_futuro.T)
    y_rna_prev_futuro = rna.predict(X_futuro_norm)

    Y_rna_previsao = rna.predict(X_norm_test)
    r2_rna = r2_score(Y_test, Y_rna_previsao)

    return y_rna_prev_futuro, r2_rna
