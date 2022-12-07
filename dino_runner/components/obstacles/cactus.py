import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    Y_POS_LARGE_CACTUS = 320

    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        self.rect.y = self.Y_POS_LARGE_CACTUS

class SMALL_CACTUS(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        self.rect.y = 325
