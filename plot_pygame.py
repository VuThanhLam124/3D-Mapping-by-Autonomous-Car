import pygame
import numpy as np
import lidar_process as lp
# Initialize lidar data
lidar_data = lp.data

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw lidar data as points on the screen
    for angle, distance in enumerate(lidar_data):
        x = int(distance * np.cos(np.deg2rad(angle))) + 400
        y = int(distance * np.sin(np.deg2rad(angle))) + 300
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()