import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import (LARGE_CACTUS, SMALL_CACTUS)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []


    def update(self, game):
        if len(self.obstacles) == 0:
            Cactus_size = random.randint(0,1)
            if Cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
        if game.player.dino_rect.colliderect(obstacle.rect):
            pygame.time.delay(2000)
            game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)