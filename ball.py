import pygame 

class Ball:
    radius = 7
    max_vel = 4
    red = (255,0,0)
    def __init__(self,x,y):
        self.x = self.og_x = x
        self.y = self.og_y = y 
        self.x_vel = Ball.max_vel
        self.y_vel = 0

    def move(self):
        self.x += self.x_vel 
        self.y += self.y_vel 

    def draw(self, window):
        pygame.draw.circle(window, Ball.red,(self.x, self.y),Ball.radius)

    def reset(self):
        self.x = self.og_x
        self.y = self.og_y
        self.x_vel = Ball.max_vel
        self.y_vel = 0


        