import pygame
import sys
import time
import random

from pygame.locals import *


class Planet:
    def __init__(self, mass, density, posx, posy):
        self.mass = mass;
        self.density = density;
        self.x = posx;
        self.y = posy;
        
    def draw(self, surface):
        pygame.draw.circle(surface, (100,  100, 100), (self.x, self.y), self.density);


class Universe:
    def __init__(self, lightSpeed):
        self.planets = [];
        print("creating universe");
        
    def addPlanet(self, p):
        self.planets.append(p);

        
    def run(self, surface):
        for p in self.planets:
            p.draw(surface);
            

    

fpsClock = pygame.time.Clock()
FPS = 60;
if __name__ == '__main__':

    pygame.init();
    a = Planet(10, 10, 500, 600);
    b = Planet(10, 30, 400, 200);
    screen = pygame.display.set_mode((1024, 768), 0, 32);
    surface = pygame.Surface(screen.get_size());
    surface = surface.convert();
    # surface.fill((255,255,255));
    print("before un");
    un = Universe(3*10**8);
    un.addPlanet(a);
    un.addPlanet(b);
    print("after un");
    while(True):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit();
                sys.exit();
                # elif event.type == KEYDOWN:
                #     if event.key == K_UP:

            #     elif event.key == K_DOWN:

            #     elif event.key == K_LEFT:

            #     elif event.key == K_RIGHT:
        surface.fill((0,0,50));

        un.run(surface)
        screen.blit(surface, (0, 0));
        
        pygame.display.flip();
        pygame.display.update();
        fpsClock.tick(FPS)
