import random
import pygame
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.components.obstacles.cactus import LargeCactus, SmallCactus
from dino_runner.utils.constants import (HAMMER_TYPE, LARGE_CACTUS, SMALL_CACTUS, BIRD)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type_list = [Bird(), SmallCactus(SMALL_CACTUS), LargeCactus(LARGE_CACTUS),] 
            self.obstacles.append(random.choice(self.obstacle_type_list))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            
            if not game.player.shield:
                if game.player.dino_rect.colliderect(obstacle.rect):
                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        self.obstacles.pop()
                    #elif game.player.type == HAMMER_TYPE:

                        #self.hammer_obstacle(game)
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                    

    def hammer_obstacle(self, game):
        for obstacle in self.obstacles:
            if game.player.dino_rect.colliderect(obstacle.rect):
                obstacle.rect.x += game.game_speed * 2
                obstacle.rect.y -= game.game_speed * 2
            if obstacle.rect.x > 1300:
                self.obstacles.pop()


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

