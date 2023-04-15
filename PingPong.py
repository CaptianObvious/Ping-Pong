from pygame import *
from random import *
mixer.init()

score = 0
lost = 0
win_width = 700
win_height = 500
finish = False

#создай окно игры
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")


#задай фон сцены
background = transform.scale(image.load("fon.png"), (win_width, win_height))
#mixer.music.load("space.ogg")

font.init()
font2 = font.SysFont("verdana", 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 445:
            self.rect.y += self.speed
        elif keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update_R(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y < 445:
            self.rect.y += self.speed
        elif keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
 

player1 = Player('horizontal-line.png',10, 200, 5, 65, 65)
player2 = Player('horizontal-line.png',650, 200, 5, 65, 65)
sharik = GameSprite("sharik.png",250, 250, 0, 33, 75)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))

    player1.reset()
    player2.reset()
    sharik.reset()
    player1.update_L()
    player2.update_R()

    display.update()
