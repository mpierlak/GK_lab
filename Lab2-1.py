import pygame
import sys
import math

class Transforms2D:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Transforms")

        
        self.transform_select = 0

    def apply_transforms(self, point):
        # funkcje transformacji
        def transform_0(x, y):
            return x, y
        
        def transform_1(x, y):
            return x * 0.5 + 1, y * 0.5 + 1
        
        def transform_2(x, y):
            return x * math.cos(math.radians(45)) - y * math.sin(math.radians(45)), \
                   x * math.sin(math.radians(45)) + y * math.cos(math.radians(45))
        
        def transform_3(x, y):
            return x * 0.5, y
        
        def transform_4(x, y):
            return x + 0.4 * y, y
        
        def transform_5(x, y):
            return x, y * 0.5 - 200
        
        def transform_6(x, y):
            return -y * 0.7, x
        
        def transform_7(x, y):
            return x * 0.5, y
        
        def transform_8(x, y):
            return x * math.cos(math.radians(30)) - (y * 0.5 + 110) * math.sin(math.radians(30)), \
                   x * math.sin(math.radians(30)) + (y * 0.5 + 170) * math.cos(math.radians(30))
        
        def transform_9(x, y):
            return x + 150, -y * 0.50
        
        transforms = [transform_0, transform_1, transform_2, transform_3, transform_4,
                      transform_5, transform_6, transform_7, transform_8, transform_9]

        return transforms[self.transform_select](*point)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    
                    if pygame.K_0 <= event.key <= pygame.K_9:
                        self.transform_select = event.key - pygame.K_0

            self.screen.fill((255, 255, 255))

            # tworzenie wielokata
            n = 10
            points = [(150 * math.cos((2 * math.pi / n) * i), 150 * math.sin((2 * math.pi / n) * i)) for i in range(n)]
            transformed_points = [self.apply_transforms(point) for point in points]

            # przesuniecie punktow do srodka ekranu
            center_x, center_y = self.width // 2, self.height // 2
            transformed_points = [(x + center_x, y + center_y) for x, y in transformed_points]

            # rysowanie wielokata
            pygame.draw.polygon(self.screen, (0, 0, 200), transformed_points, 0)

            pygame.display.flip()

if __name__ == "__main__":
    app = Transforms2D()
    app.run()
