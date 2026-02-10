from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

def Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__()

    def draw(self,screen,color):
        pygame.draw.circle(screen,self.position(),"white",self.radius(),LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity()*dt

