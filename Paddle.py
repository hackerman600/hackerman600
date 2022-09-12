import pygame

class Paddle:
    width = 20
    height = 100
    vel = 5
    white = (255,255,255)

    def __init__(self, x,y):
        self.x = self.og_x = x
        self.y = self.og_y = y

    def move(self, up = True):
        if up:
            self.y -= Paddle.vel

        else:
            self.y += Paddle.vel

    def draw(self, window):
        pygame.draw.rect(window, Paddle.white,pygame.Rect(self.x, self.y, Paddle.width, Paddle.height))

    def reset(self):
        self.x = self.og_x
        self.y = self.og_y