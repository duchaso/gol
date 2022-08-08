from pygame import Surface, Rect, draw

class Board:
    def __init__(self, board_width: int, board_height: int) -> None:
        self.BOARD_W = board_width
        self.BOARD_H = board_height

        self.board = [[False for i in range(self.BOARD_H)] for row in range(self.BOARD_W)]
        self.commands = dict()

    def change_cell(self, x: int, y: int) -> None:
        self.board[x][y] = True if self.board[x][y] == False else False

    def tick(self) -> None:
        for key, value in self.commands.items():
            self.board[key[0]][key[1]] = value

        self.commands.clear()
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board[0])):
                neighbours = self.count_neighbours(x, y)
                if self.board[x][y] == True:
                    #if alive and doesn't have 2 or 3 neighbours - die
                    if neighbours != 2 and neighbours != 3:
                        self.commands[(x, y)] = False                
                #if dead and has 3 neighbours - live
                elif self.board[x][y] == False and neighbours == 3:
                    self.commands[(x, y)] = True

    def count_neighbours(self, x: int, y: int) -> int:
        cnt = 0
        for j in range(y - 1, y + 2):
            if j >= len(self.board[0]) or j < 0: continue
            for i in range(x - 1, x + 2):
                if i >= len(self.board) or i < 0: continue
                elif i == x and j == y: continue
                elif self.board[i][j] == True: cnt += 1
        return cnt

    def draw(self, surface: Surface, square_size: int) -> None:
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[0])):
                if self.board[row][col] == True:
                    draw.rect(surface, (255, 255, 255), Rect(row * square_size, col * square_size, square_size, square_size))