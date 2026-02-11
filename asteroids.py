from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen,color="white"):
        pygame.draw.circle(screen,color,(self.position.x,self.position.y),self.radius,LINE_WIDTH)

    def split(self):
        self.kill()
        old_radius = self.radius
        x = self.position.x
        y = self.position.y
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_velocity = self.velocity.rotate(angle)
        new_velocity_2 = self.velocity.rotate(-angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(x,y,new_radius)
        asteroid.velocity = new_velocity * 1.2
        asteroid2 = Asteroid(x,y,new_radius)
        asteroid2.velocity = new_velocity_2 * 1.2


        

        

    def update(self,dt):
        self.position += self.velocity*dt
        #self.y += self.velocity.y*dt


