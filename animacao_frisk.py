import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Frisk')

sprite_sheet_image = pygame.image.load('sprites/frisk.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)


BG = (50, 50, 50)
BG_IMG = (195, 134, 255)


animation_list = []
frames_count = [1, 4, 2, 2]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 400
frame = 0
step_counter = 0

for animation in frames_count:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 20, 30, 5, BG_IMG))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:
    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame == len(animation_list[action]):
            frame = 0

    screen.blit(animation_list[action][frame], (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                action = 1
                frame = 0
            if event.key == pygame.K_LEFT:
                action = 2
                frame = 0
            if event.key == pygame.K_RIGHT:
                action = 3
                frame = 0
        else:
            action = 0
            frame = 0

    pygame.display.update()

pygame.quit()
