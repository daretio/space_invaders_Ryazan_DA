import pygame as pg

pg.init()
screen_widht, screen_heigh = 800, 600


FPS = 24
clock = pg.time.Clock()

#изображения
bg_img = pg.image.load('src/background.png')
icon_img = pg.image.load('src/ufo.png')

display = pg.display.set_mode((screen_widht, screen_heigh))
#display.fill('blue', (0, 0, screen_widht, screen_heigh))
pg.display.set_icon(icon_img)
pg.display.set_caption('Space invaders')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 48)

display.blit(bg_img, (0, 0))

text_img = sys_font.render('Score: 123', True, 'white')
display.blit(text_img, (0, 0))

dz_text = sys_font.render('Andreev Dmitry', True, 'white')
display.blit(dz_text, (595, 550))

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()
display.blit(game_over_text, (screen_widht/2 - w/2, screen_heigh/2 - h/2))

#igrok
player_img = pg.image.load('src/player.png')
player_widht, player_height = player_img.get_size()

running = True
while running:
    pg.display.update()
    for event in pg.event.get():
        #нажали крестик на окне
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False
        #tut nazhimaem na klavishi
        if event.type == pg.KEYDOWN:
            #nazhata q
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_SPACE:
                display.blit(bg_img, (0, 0))

    clock.tick(FPS)

pg.quit()


# import sys
#
# import pygame
# from pygame.locals import QUIT
#
# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')

# while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#    pygame.display.update()