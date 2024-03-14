import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

# Kolory
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Wymiary kwadratu
square_size = 300
square_x = (WIDTH - square_size) // 2
square_y = (HEIGHT - square_size) // 2

# Wymiary trójkąta
triangle_base = square_size
triangle_height = square_size / 2
triangle_x = square_x + square_size // 2
triangle_y = square_y + square_size // 2 + triangle_height / 2

# Obniżenie trójkąta
triangle_y += triangle_height

# Funkcja rysująca kwadrat
def draw_square():
    pygame.draw.rect(SCREEN, GREEN, (square_x, square_y, square_size, square_size))

# Funkcja rysująca trójkąt
def draw_triangle():
    triangle_points = [(triangle_x, triangle_y - triangle_height * 1.5),
                       (triangle_x - triangle_base / 2, triangle_y - triangle_height /2),
                       (triangle_x + triangle_base / 2, triangle_y - triangle_height/2)]
    pygame.draw.polygon(SCREEN, WHITE, triangle_points)


running = True
while running:
    SCREEN.fill(WHITE)  
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    draw_square()
    draw_triangle()

    pygame.display.flip()


pygame.quit()
sys.exit()
