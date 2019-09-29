import pygame

# Initialise Pygame
pygame.init()

# Définit background comme étant une couleur sans rouge, vert et bleu
background = (0, 0, 0)

# Crée une fenêtre de 960 pixels de largeur sur 720 pixels de hauteur
width, height = 960, 720
screen = pygame.display.set_mode((width, height))

# Crée une horloge qui sera utilisée pour limiter le nombre d'images par seconde
clock = pygame.time.Clock()

# Charge le fichier ball.png dans pygame
ball = pygame.image.load("ball.png")
# Crée un rectangle de la taille de l'image
# Le coin du rectangle sera dans le coin de la fenêtre
ballrect = ball.get_rect()

ballrect.x = 100
ballrect.y = 500

# Vitesse de déplacement de la balle en x et y
speed_x = 3
speed_y = 3


#Definition d ela couleur de la raquette
paddle_color = (255,0,0)
paddle_width = 10
paddle_height = 80

paddle1 = pygame.Surface([paddle_width, paddle_height])
paddle1.fill(paddle_color)
paddlerect1 = paddle1.get_rect()
paddlerect1.x = width / 10
paddlerect1.y = height / 2

paddle2 = pygame.Surface([paddle_width, paddle_height])
paddle2.fill((0,0,255))
paddlerect2 = paddle2.get_rect()
paddlerect2.x = width * 0.9
paddlerect2.y = height / 2


# On commence une boucle infinie
while True:
    # Lorsqu'un évènement de fermeture se produit, le programme est quitté
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Le rectangle se déplace
    # d’un pixel à droite et d’un pixel en bas
    ballrect.x = ballrect.x + speed_x
    ballrect.y = ballrect.y + speed_y
    if ballrect.bottom > height:
        speed_y = -1
    if ballrect.top < 0:
        speed_y = 1
    if ballrect.right > width:
        speed_x = - 1
    if ballrect.left < 0:
        speed_x = 1
    # Remplit la fenêtre par la couleur background
    screen.fill(background)
    # Copie le contenu de l'image dans le rectangle
    screen.blit(ball, ballrect)
    screen.blit(paddle1, paddlerect1)
    screen.blit(paddle2, paddlerect2)
    # Rend visible tout ce qui a été fait
    pygame.display.flip()
    # Récupère la liste des touches pressées
    keys=pygame.key.get_pressed()
    # Regarde si la flèche du bas est pressée
    if keys[pygame.K_DOWN]:
        paddlerect1.y = paddlerect1.y -  2 * abs(speed_y)
    if keys[pygame.K_UP]:
        paddlerect1.y = paddlerect1.y +  2 * abs(speed_y)
    if ( (paddlerect1.x + paddle_width) == ballrect.left ) and ( paddlerect1.y + 40 > ballrect.centery) and (paddlerect1.y - 40 < ballrect.centery) :
        speed_x = -1 * speed_x
    # Limite la vitesse pour ne pas parcourir la boucle plus de 30 fois par seconde
    clock.tick(30)
