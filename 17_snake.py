import pygame
import random

def random_location():
    global SCREEN_SIZE, FOOD_LOCATION
    return (
        random.randint(0, SCREEN_SIZE[0]/10 - 1) * 10,
        random.randint(0, SCREEN_SIZE[1]/10 - 1) * 10
    )

# RGB (Red, Green, Blue)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255,255)

pygame.init()
SCREEN_SIZE = (800, 600)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Snake")
pygame.font.init()

czcionka = pygame.font.SysFont('Chiller', 30)
czcionka60 = pygame.font.SysFont('Freestyle Script', 30)

clock = pygame.time.Clock()

# aktualna pozycja weza
snake_x = 400
snake_y = 300

segments = [(snake_x, snake_y)]

# predkosc przesuwania
vx = 10
vy = 0

FOOD_LOCATION = None
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx = -10
                vy = 0
            elif event.key == pygame.K_RIGHT:
                vx = 10
                vy = 0
            elif event.key == pygame.K_UP:
                vx = 0
                vy = -10
            elif event.key == pygame.K_DOWN:
               vx = 0
               vy = 10
            elif event.key == pygame.K_RETURN:
                game_over = False
                segments = [segments[0]]

    if game_over:
        SCREEN.fill(BLACK)
        tekst_koniec = czcionka60.render(f'Twój wynik: {len(segments) - 1}', False, WHITE)
        tekst_reset = czcionka60.render('Wciśnij ENTER, aby zagrać ponownie', False, WHITE)

        SCREEN.blit(tekst_koniec, (10, 10))
        SCREEN.blit(tekst_reset, (10, 80))
    else:

        snake_x += vx
        snake_y += vy

        WIDTH, HEIGHT = SCREEN_SIZE
        if snake_x >=WIDTH:
            snake_x = 0
        elif snake_x < 0:
            snake_x = WIDTH - 10
        if snake_y >= HEIGHT:
            snake_y = 0
        elif snake_y < 0:
            snake_y = HEIGHT - 10

        if (snake_x, snake_y) in segments:
            game_over = True

        segments.insert(0, (snake_x, snake_y))      # dodaj na poczatku
        
        if (FOOD_LOCATION
            and snake_x == FOOD_LOCATION[0]
            and snake_y == FOOD_LOCATION[1]):
            FOOD_LOCATION = None
        else:
            segments.pop()      # usun na koncu listy

        if FOOD_LOCATION is None:
            FOOD_LOCATION = random_location()


        SCREEN.fill(BLACK)
        for x, y in segments:
            pygame.draw.rect(
                SCREEN ,WHITE, [x, y, 10, 10])
        pygame.draw.rect(
            SCREEN, RED, [FOOD_LOCATION[0], FOOD_LOCATION[1], 10, 10])

        tekst_punkty = czcionka.render(f'Punkty: {len(segments) - 1}', False, WHITE)
        SCREEN.blit(tekst_punkty, (10, 10))

    pygame.display.update()
    clock.tick(30)




    ##########################################################################################################
                # NA POZNIEJ DOPISAC KOD, KTORY ROBI DUZE PUNKTY!!!
    ##########################################################################################################