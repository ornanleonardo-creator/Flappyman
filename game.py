import pygame, random, sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Couleurs
WHITE = (255, 255, 255)

# Images
bird = pygame.image.load("assets/bird.png")
coin = pygame.image.load("assets/coin.png")
background = pygame.image.load("assets/background.png")

# Variables
bird_x, bird_y = 50, HEIGHT//2
bird_speed = 0
gravity = 0.5
coins = [(random.randint(100, WIDTH-50), random.randint(50, HEIGHT-50)) for _ in range(5)]
score = 0

# Boucle principale
while True:
    screen.blit(background, (0,0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -10

    # Mouvement de l'oiseau
    bird_speed += gravity
    bird_y += bird_speed
    screen.blit(bird, (bird_x, bird_y))

    # Affichage des pièces et collision
    for c in coins[:]:
        screen.blit(coin, c)
        coin_rect = pygame.Rect(c[0], c[1], coin.get_width(), coin.get_height())
        bird_rect = pygame.Rect(bird_x, bird_y, bird.get_width(), bird.get_height())
        if bird_rect.colliderect(coin_rect):
            coins.remove(c)
            score += 1

    # Texte score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
