import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def collideswith(self,other):
        x_diff = self.position.x - other.position.x
        y_diff = self.position.y - other.position.y
        c_diff = x_diff**2 + y_diff**2
        c_diff = c_diff**.5
        if c_diff >= self.radius + other.radius:
            return False
        return True

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass



    pass