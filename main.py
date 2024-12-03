import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum with Custom Colors")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)  # Color for the rope
BLUE = (0, 0, 255)       # Color for the pendulum bob

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Pendulum properties
origin = (WIDTH // 2, 100)  # Origin point of the pendulum
length = 400               # Increased length for slower swings
angle = math.pi / 4        # Initial angle (45 degrees)
angle_velocity = 0         # Initial angular velocity
angle_acceleration = 0     # Initial angular acceleration
gravity = 0.3              # Reduced gravity for longer swings
damping = 0.999            # Reduced damping for slower energy loss

# Trail settings
trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
trail_surface.fill((0, 0, 0, 0))  # Transparent background

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Physics calculations
    angle_acceleration = -gravity / length * math.sin(angle)  # Angular acceleration
    angle_velocity += angle_acceleration                     # Update angular velocity
    angle_velocity *= damping                                # Apply damping
    angle += angle_velocity                                  # Update angle

    # Calculate pendulum position
    pendulum_x = origin[0] + length * math.sin(angle)
    pendulum_y = origin[1] + length * math.cos(angle)
    pendulum_pos = (int(pendulum_x), int(pendulum_y))

    # Fade the trail over time
    trail_surface.fill((0, 0, 0, 5), special_flags=pygame.BLEND_RGBA_SUB)  # Slow fading

    # Draw the pendulum bob onto the trail surface
    pygame.draw.circle(trail_surface, BLUE, pendulum_pos, 15)

    # Drawing
    screen.fill(BLACK)                                       # Clear the screen
    screen.blit(trail_surface, (0, 0))                      # Draw the trail
    pygame.draw.line(screen, WHITE, origin, pendulum_pos, 2) # White pendulum rod
    pygame.draw.circle(screen, BLUE, pendulum_pos, 15)       # Blue pendulum bob

    pygame.display.flip()                                    # Update the display
    clock.tick(60)                                           # Limit frame rate
