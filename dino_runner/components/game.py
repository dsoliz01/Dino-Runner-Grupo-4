import pygame
from dino_runner.components.dinosaur import Dinosuar
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import FONT_STYLE, Score
from dino_runner.utils.constants import BG, CLOUD, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.text_utils import draw_message_component


INITIAL_GAME_SPEED = 20
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosuar()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.death_count = 0
        self.executing = False

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.initialize_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def initialize_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score.current_score = 0
        self.game_speed = INITIAL_GAME_SPEED
        self.player_heart_manager.reset_heart_count()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)
        self.power_up_manager.update(self.score.current_score, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        if self.score.current_score <= 1000:
            self.screen.fill((255, 255, 255))
        else:
            self.screen.fill((0, 0, 0))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.check_power_up(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):


        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        pass

    def place_text(self, font_sizes, pos_x, pos_y, text_message, color):
        font = pygame.font.Font(FONT_STYLE, font_sizes)
        text = font.render(text_message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (pos_x, pos_y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
    # poner color al fondo
        self.screen.fill((255, 255, 255))
    # mostrar mensaje de inicio
        half_screen_width= SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            draw_message_component("PRESS A KEY TO GAME", self.screen)
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height - 100))
            self.screen.blit(CLOUD, (half_screen_width +60, half_screen_height - 100))  
            #tarea
        else:
            #mostrar mensaje de reinicio
            self.place_text(35, 550, 400, "PRESS A KEY TO PLAY AGAIN",(0, 0, 0))
            #mostrar puntos obtenidos
            self.place_text(22, 120, 50,f'MAX SCORE: {self.score.max_score}', (240, 0, 0))
            #mostrar muertes totales
            self.place_text(22, 120, 100, f'DEAHT COUNT: {self.death_count}', (240, 0, 0))
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height - 100))
            self.screen.blit(CLOUD, (half_screen_width +60, half_screen_height - 100))   
            

            
            
            print(self.death_count)
    # mostrar imagen como icono
        self.screen.blit(DINO_START, (half_screen_width - 50, half_screen_height -140))
    # actualizar pantalla
        pygame.display.flip()
    # manejar eventos
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

