def main():
    print('My first git program')
    print('And I change it every day')


if __name__ == '__main__':
    main()import pygame
import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.board2 = [[0] * width for _ in range(height)]
        self.xod = 0
        self.top = 30
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                c = self.board[j][i]
                if self.board2[j][i] == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (self.left + i * self.cell_size,
                self.top + j * self.cell_size, self.cell_size,self.cell_size), 0)
                elif self.board2[j][i] == 1:
                    pygame.draw.rect(screen, a, (self.left + i * self.cell_size,
                 self.top + j * self.cell_size, self.cell_size, self.cell_size),0)
                else:
                    pygame.draw.rect(screen, b, (self.left + i * self.cell_size,
                 self.top + j * self.cell_size, self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (255, 255, 255), (self.left + i * self.cell_size,
            self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse):
        if self.left <= mouse[0] <= self.left + self.cell_size * len(self.board[0]) \
                and self.top <= mouse[1] <= self.top + self.cell_size * len(self.board):
            c = self.cell_size
            return (mouse[0] - self.left) // c, (mouse[1] - self.top) // c
        else:
            return None

    def get_click(self, mouse):
        cell = self.get_cell(mouse)
        if cell is not None:
            self.on_click(cell)

    def on_click(self, xy):
        x, y = xy
        for i in range(self.width):
            if self.xod % 2 == 1:
                self.board2[y][i] = 1
            else:
                self.board2[y][i] = 2
            if self.xod % 2 == 1:
                self.board2[i][x] = 1
            else:
                self.board2[i][x] = 2
        self.xod += 1


n = int(input())
board = Board(n, n)
board.set_view(30, 30, 30)
clock = pygame.time.Clock()
size = n * 37, n * 37
screen = pygame.display.set_mode(size)
running = True
were = []
for i in range(256):
    were.append(i)
a = (random.choice(were), random.choice(were), random.choice(were))
b = (random.choice(were), random.choice(were), random.choice(were))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
    clock.tick(60)
