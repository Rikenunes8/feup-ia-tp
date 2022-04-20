import pygame
import UnequalLengthMazes as ULM
from boards import boardsULM

# Number of rows and columns of the grid according to the number of boards to display
boardsGrid = {
  0 : (0, 0), 1 : (1, 1), 2 : (1, 2), 3 : (2, 2), 4 : (2, 2), 5 : (2, 3), 
  6 : (2, 3), 7 : (2, 4), 8 : (2, 4), 9 : (3, 3), 10: (3, 4), 11: (3, 4), 12: (3, 4) 
}

BG_COLOR = '#888888'
# Board Colors
EMPTY_COLOR = '#DDDDDD'
BLOCK_COLOR = '#000000'
PATH_COLOR = '#FF0000'
# Menu Colors
TITLE_COLOR = '#000000'
BUTTON_COLOR = '#FFFFFF'
TEXT_COLOR = '#000000'

WIDTH, HEIGHT, FONT_SIZE = 800, 600, 40  


class Drawer:
  def __init__(self):
    pygame.display.set_caption('Unequal Length Mazes')
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  
    self.font = pygame.font.SysFont(None, FONT_SIZE)

  def drawText(self, text, color, x, y):
    textObj = self.font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    self.screen.blit(textObj, textRect)

  def drawOptionMenu(self, menu):
    (title, values) = menu
    indexes = list(range(1, len(values), 1)) + [0]
    options = [str(op[0]) + ' - ' + op[1] for op in list(zip(indexes, values))]

    self.screen.fill(BG_COLOR)

    btn_innerX, btn_innerY = 20, 10
    btn_sizeX = self.font.size(max(options, key = len))[0] + btn_innerX*2
    btn_sizeY = self.font.size(title)[1] + btn_innerY*2
    offset_x, offset_y = WIDTH/2 - btn_sizeX/2, 30
    
    self.drawText(title, TITLE_COLOR, WIDTH/2 - self.font.size(title)[0]/2, offset_y)

    offset_y += self.font.size(title)[1] + FONT_SIZE/2
    for op in options:
      pygame.draw.rect(self.screen, BUTTON_COLOR, (offset_x, offset_y, btn_sizeX, btn_sizeY)) #offX, offY, sizeX, sizeY
      self.drawText(op, TEXT_COLOR, WIDTH/2 - self.font.size(op)[0]/2, offset_y + btn_innerY)
      offset_y += btn_sizeY + FONT_SIZE/3

    pygame.display.update()

  def drawChooseBoardMenu(self):
    self.screen.fill(BG_COLOR)

    offset_x, offset_y = 20, 30

    title = "Choose Board"
    self.drawText(title, TITLE_COLOR, WIDTH/2 - self.font.size(title)[0]/2, offset_y)

    offset_y += self.font.size(title)[1] + FONT_SIZE/2
    
    grid_marginX, grid_marginY = 30, 5
    (grid_nRows, grid_nCols) = boardsGrid[len(boardsULM)]
    row_size = (HEIGHT - offset_y - grid_marginY) / grid_nRows
    col_size = (WIDTH - grid_marginX) / grid_nCols

    boardIdx = 0
    for row in range(grid_nRows):
      offset_x = grid_marginX
      for col in range(grid_nCols):
        if (boardIdx >= len(boardsULM)) : break
        board = ULM.boards.initBoards[boardsULM[boardIdx]]
        self.drawBoard(board, offset_x, offset_y + FONT_SIZE, row_size - FONT_SIZE, col_size - grid_marginX)
        legend = pygame.key.name(pygame.K_a + boardIdx)
        self.drawText(legend, TEXT_COLOR, offset_x + col_size/2 - self.font.size(legend)[0]*1.5, offset_y + (FONT_SIZE - self.font.size(legend)[1]))
        boardIdx += 1
        offset_x += col_size
      offset_y += row_size

    pygame.display.update()

  def drawBoard(self, board, offX=0, offY=0, height=HEIGHT, width=WIDTH):
    rows = len(board)
    cols = len(board[0])
    size = min(height/rows, width/cols)

    for i in range(rows):
      y = size*i + offY
      for j in range(cols):
        x = size*j + offX
        value = board[i][j]
        if value == ULM.BC:
          pygame.draw.rect(self.screen, BLOCK_COLOR, (x, y, size, size))
        else: 
          pygame.draw.rect(self.screen, EMPTY_COLOR, (x, y, size, size))
        pygame.draw.rect(self.screen, "black", (x, y, size, size), 2)
    for i in range(rows):
      y = size*i + offY
      for j in range(cols):
        x = size*j + offX
        value = board[i][j]
        if value == ULM.UP:
          pygame.draw.rect(self.screen, PATH_COLOR, (x+size/3, y+size*2/6, size/3, size*8/6))
        elif value == ULM.DOWN:
          pygame.draw.rect(self.screen, PATH_COLOR, (x+size/3, y-size*4/6, size/3, size*8/6))
        elif value == ULM.LEFT:
          pygame.draw.rect(self.screen, PATH_COLOR, (x+size*2/6, y+size/3, size*8/6, size/3))
        elif value == ULM.RIGHT:
          pygame.draw.rect(self.screen, PATH_COLOR, (x-size*4/6, y+size/3, size*8/6, size/3))

  def drawSolutionAI(self, solutionAI, algorithm, heuristic):
    self.screen.fill(BG_COLOR)

    offset_x, offset_y = 20, 30

    heurStr = " [h() : " + str(heuristic) + "]" if (algorithm == "greedy" or algorithm == "A*") else ""
    title = "Solution Found by " + algorithm + heurStr
    self.drawText(title, TITLE_COLOR, WIDTH/2 - self.font.size(title)[0]/2, offset_y)

    offset_y += self.font.size(title)[1] + FONT_SIZE/2

    (path, depth, nodes) = solutionAI 
    board = None if path == None else path[-1][0]
    depthStr = "Solution Depth: " + str(depth)
    nodesStr = "Nodes Visited: " + str(nodes)
    textsize = self.font.size(max([depthStr, nodesStr], key = len))[0] + offset_x

    if (board == None): self.drawText("No Solution Found", TEXT_COLOR, offset_x, offset_y + (HEIGHT - offset_y - offset_x)/2 - FONT_SIZE)
    else: self.drawBoard(board, offset_x, offset_y, HEIGHT - offset_y - offset_x, WIDTH - offset_x*2 - textsize)
    self.drawText(depthStr, TEXT_COLOR, WIDTH - textsize, offset_y + FONT_SIZE)
    self.drawText(nodesStr, TEXT_COLOR, WIDTH - textsize, offset_y + FONT_SIZE*2)

    pygame.display.update()

  def drawResolveState(self, board):
    self.screen.fill(BG_COLOR)
    self.drawBoard(board)
    pygame.display.update()

  def drawSolveState(self, algorithm, heuristic):
    self.screen.fill(BG_COLOR)
    heurStr = " [h() : " + str(heuristic) + "] ..." if (algorithm == "greedy" or algorithm == "A*") else "..."
    message = "Calculating " + algorithm + " solution " + heurStr
    self.drawText(message, TITLE_COLOR, WIDTH/2 - self.font.size(message)[0]/2, HEIGHT/2 - self.font.size(message)[1]/2)
    pygame.display.update()

  def drawLimitState(self, limit):
    self.screen.fill(BG_COLOR)
    title = "Introduce the Limit:"
    self.drawText(title, TITLE_COLOR, WIDTH/2 - self.font.size(title)[0]/2, HEIGHT/2 - self.font.size(limit)[1]*2)
    self.drawText(limit, TEXT_COLOR, WIDTH/2 - self.font.size(limit)[0]/2, HEIGHT/2 - self.font.size(limit)[1]/2)
    pygame.display.update()