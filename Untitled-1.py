from pygame import *

win_width = 1000
win_height = 650

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_a(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_b(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
            
raketka1 = Player('raketka.jpg', 20, 400, 20, 100, 10)
raketka2 = Player('raketka.jpg', 970, 400, 20, 100, 10)
ball = GameSprite('ball (2).png', 500, 300, 80, 70, 5)
window = display.set_mode((win_width, win_height))
display.set_caption('пинг понг')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
speed = 10
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
game = True
clock = time.Clock()
FPS = 60
speed_x = 5
speed_y = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    raketka1.reset()
    raketka1.update_a()
    raketka2.reset()
    raketka2.update_b()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y >= 580:
        ball.rect.y *= -1
    elif ball.rect.y < 1:
        ball.rect.y *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 1000:
        finish = True
        window.blit(lose2, (200, 200))
    display.update()
    clock.tick(FPS)