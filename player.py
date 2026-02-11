from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.rotation = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        points = self.triangle()
        pygame.draw.polygon(screen,"white",points,LINE_WIDTH)

    def update(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation += -PLAYER_TURN_SPEED*dt

        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED*dt

        self.move(dt)
        self.shoot()

    def move(self,dt):
        unit_vector = pygame.Vector2(0,1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            rotated_vector = unit_vector.rotate(self.rotation) * PLAYER_SPEED * dt
            self.position += rotated_vector
        if keys[pygame.K_s]:
            rotated_vector = unit_vector.rotate(self.rotation) * PLAYER_SPEED * -dt
            self.position += rotated_vector

    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
            shot_vector = pygame.Vector2(0,1) * PLAYER_SHOOT_SPEED
            shot_vector = shot_vector.rotate(self.rotation)
            shot.velocity = shot_vector

        #edge = random.choice(self.edges)
         #   speed = random.randint(40, 100)
          #  velocity = edge[0] * speed
           # velocity = velocity.rotate(random.randint(-30, 30))
            #position = edge[1](random.uniform(0, 1))

    #In your Player class, add a new method called shoot. This method takes no parameters and does the following:
#Creates a new Shot at the current position of the player.
#Sets the shot's .velocity attribute:
#Start with a pygame.Vector2 of (0, 1).
#.rotate() the vector in the direction the player is facing.
#Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster.

        


    

    

