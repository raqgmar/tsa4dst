import numpy as np
# Define el espacio de búsqueda de los hiperparámetros discretos
kernels = ['linear']

# Define el espacio de búsqueda de los hiperparámetros continuos discretizados
C_values = np.logspace(-3, 2, num=8)  # 8 valores entre 1e-3 y 1e2
epsilon_values = np.logspace(-4, 1, num=6)  # 6 valores entre 1e-4 y 1e1

# Función para imprimir el nombre de la variable y su valor
def print_variable_values(variables):
    for name, value in variables.items():
        print(f"{name} = {value}")

# Diccionario de variables
variables = {
    "kernels": kernels,
    "C_values": C_values,
    "epsilon_values": epsilon_values
}

# Imprimir los valores
print_variable_values(variables)
# Define el espacio de búsqueda de los hiperparámetros discretos
kernels = ['rbf']
gamma_values = ['scale', 'auto']  # Para el kernel 'rbf'

# Define el espacio de búsqueda de los hiperparámetros continuos discretizados
C_values = np.logspace(-3, 3, num=6)  # 6 valores entre 1e-3 y 1e3
epsilon_values = np.logspace(-4, 1, num=4)  # 4 valores entre 1e-4 y 1e1

# Función para imprimir el nombre de la variable y su valor
def print_variable_values(variables):
    for name, value in variables.items():
        print(f"{name} = {value}")

# Diccionario de variables
variables = {
    "kernels": kernels,
    "gamma_values": gamma_values,
    "C_values": C_values,
    "epsilon_values": epsilon_values
}

# Imprimir los valores
print_variable_values(variables)


# Define el espacio de búsqueda de los hiperparámetros discretos
kernels = ['poly']
degrees = [3, 4, 5]  # Para el kernel 'poly'
coef0_values = [1e-1, 1]  # Para los kernels 'poly' y 'sigmoid'
gamma_values = ['scale']  # Para el kernel 'rbf']

# Define el espacio de búsqueda de los hiperparámetros continuos discretizados
C_values = np.logspace(-3, 3, num=3)  # 4 valores entre 1e-3 y 1e3
epsilon_values = np.logspace(-2, 1, num=3)  # 4 valores entre 1e-4 y 1e1

# Función para imprimir el nombre de la variable y su valor
def print_variable_values(variables):
    for name, value in variables.items():
        print(f"{name} = {value}")

# Diccionario de variables
variables = {
    "kernels": kernels,
    "degrees": degrees,
    "coef0_values": coef0_values,
    "gamma_values": gamma_values,
    "C_values": C_values,
    "epsilon_values": epsilon_values
}

# Imprimir los valores
print_variable_values(variables)

######
