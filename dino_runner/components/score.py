import pygame

from dino_runner.utils.constants import FONT_STYLE

class Score():
    
    def __init__(self):
        self.current_score = 0
        self.max_score = 0

    def update(self, game):
        self.current_score += 1
        if self.current_score % 100 == 0:
            game.game_speed += 2
        if self.max_score < self.current_score:
            self.max_score = self.current_score

    def draw(self, screen):
        POS_MAX_SCORE_X = 700
        POS_MAX_SCORE_Y = 50
        POS_SCORE_X = 970
        POS_SCORE_Y = 50
        font = pygame.font.Font(FONT_STYLE, 30)
        message = font.render(f'Score: {self.current_score}', True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (POS_SCORE_X, POS_SCORE_Y)
        screen.blit(message, message_rect)

        font = pygame.font.Font(FONT_STYLE, 30)
        message = font.render(f'Max Score: {self.max_score}', True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (POS_MAX_SCORE_X, POS_MAX_SCORE_Y)
        screen.blit(message, message_rect)