import random
import pygame
from dino_runner.components.power_ups.hammer import Hammer



from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups= []
        self.when_appears = 0

    def generate_power_up(self, current_score):
        if len(self.power_ups) == 0 and self.when_appears == current_score:
            self.when_appears += random.randint(200, 300)
            choice = random.randint(0, 1)
            if choice == 0:
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Hammer())

    def update(self, current_score, game_speed, player):
        self.generate_power_up(current_score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups( self):
        self.power_ups = []
        self.when_appears = random.randint(300, 400)

