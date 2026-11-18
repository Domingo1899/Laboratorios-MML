import numpy as np

A = np.array([[1 + 10**-14, 0],
              [0, 1]])

VAP = np.linalg.eigvals(A)
print(VAP)
# Polinomio característico de A: coeficientes de det(A - lambda*I)
coef = np.poly(A)
print("Coeficientes del polinomio característico:", coef)

raices = np.roots(coef)
print("Raíces (autovalores calculados así):", raices)