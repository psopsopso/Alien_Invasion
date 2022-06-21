import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [2,2]
black =0,0,0

image = pygame.image.load('Images/alien.bmp')
rect = image.get_rect()


# Start each new alien near the top left of the screen
# rect.x = rect.width
# rect.y = rect.height




# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()

# print(f"Coord rectangle du screen: {screenrect}")
# print(f"Coord rectangle de l'image: {ballrect}")

# ballrect.midbottom = screenrect.midbottom

# print(f"Coord rectangle du screen: {screenrect}")
# print(f"Coord rectangle de l'image: {ballrect}")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#     screen.blit(ball,ballrect)
#     pygame.display.flip()