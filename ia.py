import time

class Parqueadero:
    def __init__(self, capacidad, tarifa_por_hora):
        self.capacidad = capacidad
        self.tarifa_por_hora = tarifa_por_hora
        self.espacios = {i: None for i in range(1, capacidad+1)}

    def asignar_espacio(self, placa):
        for espacio, ocupado in self.espacios.items():
            if ocupado is None:
                self.espacios[espacio] = {"placa": placa, "entrada": time.time()}
                print(f"Vehículo {placa} asignado al espacio {espacio}")
                return espacio
        print("No hay espacios disponibles")
        return None

    def liberar_espacio(self, espacio):
        if self.espacios[espacio]:
            datos = self.espacios[espacio]
            tiempo_total = (time.time() - datos["entrada"]) / 3600  # horas
            costo = round(tiempo_total * self.tarifa_por_hora, 2)
            print(f"Vehículo {datos['placa']} salió. Tiempo: {tiempo_total:.2f}h. Costo: ${costo}")
            self.espacios[espacio] = None
            return costo
        else:
            print("Ese espacio ya está libre")
            return 0

    def estado_parqueadero(self):
        for espacio, datos in self.espacios.items():
            if datos:
                print(f"Espacio {espacio}: ocupado por {datos['placa']}")
            else:
                print(f"Espacio {espacio}: libre")

# Ejemplo de uso
parqueadero = Parqueadero(capacidad=5, tarifa_por_hora=2000)

parqueadero.asignar_espacio("ABC123")
time.sleep(2)  # Simula tiempo de parqueo
parqueadero.liberar_espacio(1)
parqueadero.estado_parqueadero()
