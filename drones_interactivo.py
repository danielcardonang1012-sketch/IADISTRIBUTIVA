import pygame
import random
import sys

# Configuración inicial
WIDTH, HEIGHT = 800, 600
NUM_DRONES = 10
FPS = 10

class Drone:
    def __init__(self, drone_id):
        self.drone_id = drone_id
        self.x = random.randint(50, WIDTH-50)
        self.y = random.randint(50, HEIGHT-50)
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
        self.radius = 10

    def move(self):
        dx = random.choice([-10, 0, 10])
        dy = random.choice([-10, 0, 10])
        self.x = max(self.radius, min(WIDTH-self.radius, self.x + dx))
        self.y = max(self.radius, min(HEIGHT-self.radius, self.y + dy))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Movimiento sincronizado de drones")
    clock = pygame.time.Clock()

    # Crear drones
    drones = [Drone(i) for i in range(NUM_DRONES)]

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fondo
        screen.fill((30, 30, 30))

        # Mover y dibujar drones
        for drone in drones:
            drone.move()
            drone.draw(screen)

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
