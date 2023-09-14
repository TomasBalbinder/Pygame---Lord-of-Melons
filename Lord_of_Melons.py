import pygame
import random

pygame.init()

# display settings 
width = 1024
height = 1024
my_screen = pygame.display.set_mode((width, height))

# music
pygame.mixer.music.load('hero.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
sword = pygame.mixer.Sound('heavy_sword.wav')

# title 
pygame.display.set_caption('LEVEL1')
picture = pygame.image.load('snowman.png')
pygame.display.set_icon(picture)

# font
font = pygame.font.SysFont('cambria',30)

# header text
header_render = font.render("Lord of Melons",True,'black')
header_rect = header_render.get_rect()
header_rect.center = (width // 2, 30)

# counter
score_number = 0
score = font.render(f"Score {score_number}",True,'black')
score_rect = header_render.get_rect()
score_rect.center = (120, 30)

# image_warrior
warrior = pygame.image.load('warrior.PNG')
warrior_x, postava_y = warrior.get_size()
warrior_rect = warrior.get_rect()
warrior_rect.center = (width // 2, height // 2)

# movment + fps
value = 10
fps = 60
clock = pygame.time.Clock()
top_underline = 23

# image_fruit
fruit = pygame.image.load('fruit.PNG')
fruit_size_x, fruit_size_y = fruit.get_size()
fruit_rect = fruit.get_rect()
fruit_rect.center = (random.randint(0 + fruit_size_x,(width - fruit_size_x)), random.randint(0 + fruit_size_y,(height - fruit_size_y)))


# main loop of game
main_game = True
while main_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game = False

    my_screen.fill('grey')

    my_screen.blit(score, score_rect)
    my_screen.blit(header_render,header_rect)
    my_screen.blit(fruit, fruit_rect)
    my_screen.blit(warrior, warrior_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and warrior_rect.y >= header_rect.center[1] + top_underline:
        warrior_rect.y -= value

    if keys[pygame.K_s] and warrior_rect.y <= width - postava_y:
        warrior_rect.y += value

    if keys[pygame.K_d] and warrior_rect.x < height - warrior_x:
        warrior_rect.x += value

    if keys[pygame.K_a] and warrior_rect.x >= 0:
        warrior_rect.x -= value

    if warrior_rect.colliderect(fruit_rect):
        pygame.mixer.Sound.play(sword)
        score_number = score_number + 1
        score = font.render(f"Score {score_number}",True,'black')
        fruit_rect.center = (random.randint(0 + fruit_size_x,(width - fruit_size_x)), random.randint(0 + fruit_size_y,(height - fruit_size_y)))

    pygame.draw.line(my_screen,'black', (0,header_rect.center[1] + 20), (width,header_rect.center[1] + 20),3) #podtrzeni
    pygame.display.update()

    clock.tick(fps)
pygame.quit()