import numpy as np
import matplotlib.pyplot as plt

# Número de drones
n_drones = 10

# Posiciones iniciales (todos en el origen)
drones = np.zeros((n_drones, 2))

def formar_circulo(radio=5):
    """Distribuye los drones en un círculo"""
    angulos = np.linspace(0, 2*np.pi, n_drones, endpoint=False)
    return np.column_stack((radio*np.cos(angulos), radio*np.sin(angulos)))

def formar_cuadrado(lado=8):
    """Distribuye los drones en un cuadrado"""
    puntos = []
    # 4 lados del cuadrado
    for i in range(n_drones):
        if i < n_drones/4:
            puntos.append([i*(lado/(n_drones/4)), 0])
        elif i < n_drones/2:
            puntos.append([lado, (i-n_drones/4)*(lado/(n_drones/4))])
        elif i < 3*n_drones/4:
            puntos.append([lado-(i-n_drones/2)*(lado/(n_drones/4)), lado])
        else:
            puntos.append([0, lado-(i-3*n_drones/4)*(lado/(n_drones/4))])
    return np.array(puntos) - lado/2  # centrar

# Formaciones
pos_circulo = formar_circulo()
pos_cuadrado = formar_cuadrado()

# Visualización
fig, axs = plt.subplots(1, 2, figsize=(10,5))

axs[0].scatter(pos_circulo[:,0], pos_circulo[:,1], color="blue")
axs[0].set_title("Formación en círculo")
axs[0].axis("equal")

axs[1].scatter(pos_cuadrado[:,0], pos_cuadrado[:,1], color="red")
axs[1].set_title("Formación en cuadrado")
axs[1].axis("equal")

plt.show()
