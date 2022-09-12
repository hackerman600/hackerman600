import pygame
from ball import Ball
from Paddle import Paddle
pygame.init()

class Game:

    width = 700
    height = 500

    def __init__(self, win, width,height):
        self.win = win 
        self.height = height
        self.width = width 
        
        self.left_paddle = Paddle(100, Game.height//2 - Paddle.height//2)
        self.right_paddle = Paddle(Game.width-100-Paddle.width, Game.height//2 - Paddle.height//2)
        self.ball = Ball(Game.width//2,Game.height//2)

        self.left_score = 0
        self.right_score = 0


    def _draw_border(self,win):
        for i in range(20,Game.height,40):
            pygame.draw.rect(win, Paddle.white, pygame.Rect(Game.width//2 - 3, i, 6,20))


    def move_paddles(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.right_paddle.y + Paddle.vel >= 0:
            self.right_paddle.move(up = True)

        if keys[pygame.K_DOWN] and self.right_paddle.y - Paddle.vel <= Game.height:
            self.right_paddle.move(up = False)

        if keys[pygame.K_w] and self.left_paddle.y + Paddle.vel >= 0:
            self.left_paddle.move(up = True)
        
        if keys[pygame.K_s] and self.left_paddle.y - Paddle.vel<= Game.height:
            self.left_paddle.move(up = False)


    def draw(self, win):
        win.fill((0,0,0))
        self.ball.draw(win)
        self.left_paddle.draw(win)
        self.right_paddle.draw(win)
        self._draw_border(win)

    def reflect_ball(self):

        if self.ball.y + Ball.radius >= self.height:
            self.ball.y_vel *= -1
        if self.ball.y - Ball.radius <= 0:
            self.ball.y_vel *= -1

        if self.ball.x_vel > 0:
            if self.ball.y >= self.right_paddle.y and self.ball.y <= self.right_paddle.y + Paddle.height:
                if self.ball.x + self.ball.radius >= self.right_paddle.x:
                    self.ball.x_vel *= -1

                    right_centre = self.right_paddle.y + Paddle.height//2
                    dist = (self.ball.y - right_centre)//10
                    self.ball.y_vel = dist


        else:
            if self.ball.y >= self.left_paddle.y and self.ball.y <= self.left_paddle.y + Paddle.height:
                if self.ball.x - self.ball.radius <= self.left_paddle.x+Paddle.width:
                    self.ball.x_vel *= -1

                    left_centre = self.left_paddle.y + Paddle.height//2
                    dist = (self.ball.y - left_centre)//10
                    self.ball.y_vel = dist



        if self.ball.x > self.width or self.ball.x < 0:
            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()


    def loop(self,win):
        self.draw(win)
        self.ball.move()
        self.move_paddles()
        self.reflect_ball()



def main():
    width,height = 700, 500
    win = pygame.display.set_mode((width,height))
    game = Game(win,width,height)
    clock = pygame.time.Clock()
    

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game.loop(win)
        pygame.display.update()

    
    pygame.display.quit()
main()






