import time
import sys
import pygame

from .board import Board

class Game:
    WIDTH, HEIGHT = 800, 600
    SQUARE_S = 10

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

        self.board = Board(Game.WIDTH // Game.SQUARE_S, Game.HEIGHT // Game.SQUARE_S)
        self.start = False

        #Draw net
        self.rect_list = list()
        for y in range(0, Game.HEIGHT, Game.SQUARE_S):
            for x in range(0, Game.WIDTH, Game.SQUARE_S):
                self.rect_list.append(pygame.Rect(x, y, Game.SQUARE_S, Game.SQUARE_S))

    def run(self) -> None:
        while True:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif not self.start:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_player_input(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = True
    
    def handle_player_input(self, clicked_point: tuple) -> None:
        self.board.change_cell(clicked_point[0] // Game.SQUARE_S, clicked_point[1] // Game.SQUARE_S) 

    def update(self) -> None:
        if self.start:
            self.board.tick()
            time.sleep(0.5)

    def render(self) -> None:
        self.screen.fill((0, 0, 0))

        # for i in range(16):
        #     pygame.draw.rect(screen , (255, 255, 255), pygame.Rect(20 * SQUARE_S, (20 + i) * SQUARE_S, SQUARE_S, SQUARE_S))
        # for rect in self.rect_list:
        #     pygame.draw.rect(self.screen, (255, 255, 255), rect, width=1)
        
        self.board.draw(self.screen, Game.SQUARE_S)





    