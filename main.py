import pygame
from constants import *
from logger import log_state
from player import Player
from circleshape import CircleShape





def main():
    pygame.init()
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Jerry = Player(x,y,PLAYER_RADIUS)
    updatable.add(Jerry)
    drawable.add(Jerry)
    
    


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass

        screen.fill("black")
        dt = Clock.tick(60)
        dt= dt/1000
        for thing in updatable:
            thing.update(dt)
            thing.move(dt)
        for thing in drawable:
            thing.draw(screen)

        
        pygame.display.flip()
        
        

        







if __name__ == "__main__":
    main()


