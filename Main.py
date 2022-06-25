import pygame 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

font = pygame.font.SysFont("arialblack", 40)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

screen.fill((255, 255, 255))
draw_text("Main Menu", font, (0, 0, 0), SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2 - 200)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()