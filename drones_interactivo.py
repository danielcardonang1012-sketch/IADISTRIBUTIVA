import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

# Número de drones
n_drones = 10
drones = np.zeros((n_drones, 2))

def formar_circulo(radio=5):
    angulos = np.linspace(0, 2*np.pi, n_drones, endpoint=False)
    return np.column_stack((radio*np.cos(angulos), radio*np.sin(angulos)))

def formar_cuadrado(lado=8):
    puntos = []
    for i in range(n_drones):
        if i < n_drones/4:
            puntos.append([i*(lado/(n_drones/4)), 0])
        elif i < n_drones/2:
            puntos.append([lado, (i-n_drones/4)*(lado/(n_drones/4))])
        elif i < 3*n_drones/4:
            puntos.append([lado-(i-n_drones/2)*(lado/(n_drones/4)), lado])
        else:
            puntos.append([0, lado-(i-3*n_drones/4)*(lado/(n_drones/4))])
    return np.array(puntos) - lado/2

def formar_triangulo(lado=8):
    puntos = []
    for i in range(n_drones):
        if i < n_drones/3:
            puntos.append([i*(lado/(n_drones/3)), 0])
        elif i < 2*n_drones/3:
            puntos.append([lado - (i-n_drones/3)*(lado/(n_drones/3)), lado])
        else:
            puntos.append([0 + (i-2*n_drones/3)*(lado/(n_drones/3)), (lado/2)])
    return np.array(puntos) - lado/2

# Diccionario de órdenes
ordenes = {
    "circulo": formar_circulo(),
    "cuadrado": formar_cuadrado(),
    "triangulo": formar_triangulo()
}

orden_actual = "circulo"
objetivo = ordenes[orden_actual]

# Configuración de la figura
fig, ax = plt.subplots()
scat = ax.scatter(drones[:,0], drones[:,1], color="blue")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Formación de drones")
ax.axis("equal")

def update(frame):
    global drones, objetivo
    drones += 0.1 * (objetivo - drones)  # movimiento suave
    scat.set_offsets(drones)
    return scat,

def escuchar_ordenes():
    global objetivo, orden_actual
    while True:
        comando = input("Escribe la formación (circulo, cuadrado, triangulo): ").strip().lower()
        if comando in ordenes:
            orden_actual = comando
            objetivo = ordenes[orden_actual]
            print(f"➡️ Cambiando formación a: {orden_actual}")
        else:
            print("❌ Orden no reconocida. Usa: circulo, cuadrado, triangulo.")

# Hilo para escuchar órdenes mientras corre la animación
threading.Thread(target=escuchar_ordenes, daemon=True).start()

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
