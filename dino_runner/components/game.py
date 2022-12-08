import pygame
from dino_runner.components.dinosaur import Dinosuar
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import FONT_STYLE, Score
from dino_runner.utils.constants import BG, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosuar()
        self.obstacle_manager = ObstacleManager()
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
        self.obstacle_manager.reset_obstacles()
        self.score.current_score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
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
        self.screen.fill((225, 225, 225))

    # mostrar mensaje de inicio
        half_screen_width= SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            self.place_text(30, half_screen_width, half_screen_height, "PRESS A KEY TO START", (0, 0, 20))
            #tarea
            
        else:
            #mostrar mensaje de reinicio
            self.place_text(35, 550, 400, "PRESS A KEY TO PLAY AGAIN",(0, 0, 0))
            #mostrar puntos obtenidos
            self.place_text(22, 120, 50,f'MAX SCORE: {self.score.max_score}', (240, 0, 0))
            #mostrar muertes totales
            self.place_text(22, 120, 100, f'DEAHT COUNT: {self.death_count}', (240, 0, 0))

            

            
            
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

