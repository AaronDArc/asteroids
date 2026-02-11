import pygame
from constants import *
from logger import log_state
from player import Player
from circleshape import CircleShape
from asteroids import Asteroid
from asteroidfield import AsteroidField
from logger import log_event





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
    asteroids = pygame.sprite.Group()
    


    Player.containers = (updatable,drawable) # This basically just says all future instances of the player group will go to the updatable group and the drawable group via inheritance
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)


    jerry = Player(x,y,LINE_WIDTH)
    asteroid_field = AsteroidField()

    print(updatable)
    
    


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
            pass
        


        for thing in drawable:
            if thing != jerry and jerry.collideswith(thing):
                log_state()
                print("Player Hit!!!")
                return
            thing.draw(screen)
            pass

        
        pygame.display.flip()
        
        

        







if __name__ == "__main__":
    main()


