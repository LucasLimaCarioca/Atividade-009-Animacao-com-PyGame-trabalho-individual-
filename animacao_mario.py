import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mario')

sprite_sheet_moving_image = pygame.image.load('sprites/mario movendo.png').convert_alpha()
sprite_sheet_jumping = pygame.image.load('sprites/mario pulando.png').convert_alpha()
sprite_sheet_moving = spritesheet.SpriteSheet(sprite_sheet_moving_image)


BG = (50, 50, 50)
BG_IMG = (146, 144, 255)


frame_0 = sprite_sheet_moving.get_image(0, 16, 16, 5, BG_IMG)
frame_1 = sprite_sheet_moving.get_image(1, 16, 16, 5, BG_IMG)
frame_2 = sprite_sheet_moving.get_image(2, 16, 16, 5, BG_IMG)

run = True
while run:
    screen.fill(BG)

    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (16*5, 0))
    screen.blit(frame_2, (16*2*5, 0))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()
