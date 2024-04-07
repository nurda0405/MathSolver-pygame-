import random
import pygame

# fill the grid with numbers and figures, after that trace a path until the last cell.
class Game:
    def find_path(self, x, y, path):
        #stop if reached the last cell
        if (x == self.row - 1 and y == self.col - 2) or (x == self.row - 2 and y == self.col - 1):
            self.reached = True
            self.path = path + [[x, y], [self.row - 1, self.col - 1]]
            return
        
        #shuffling the directions to avoid repeated paths
        random.shuffle(self.directions)

        #seeking the last cell
        if not self.reached:
            for d in self.directions:
                if not self.reached:        
                    i = d[0]
                    j = d[1]
                    if -1 < x + i < self.row and -1 < y + j < self.col:
                        if not [x + i, y + j] in path:
                            self.find_path(x + i, y + j, path + [[x, y]])
            #the reason why my previous program didn't worked correctly is that I had to not save the values in the variable within function as the path of wrong way interference with the traced path, instead, I had give the new value as a parameter of the next recursion function. Also, I had to know the working principle of the recursion call, for example, in the 'for' cycle the first called function executes until it reaches its end case and other called functions waits until the first is executed. For example, in my code I had to swap the order of if clause and for cycle to check whether the path reached the end cell, otherwise, it will continue working after reaching the end cell. 
    
   #tracing the path and finding the end value
    def trace_path(self, x, y, i, sum):
        figure = self.grid[x][y]
        i += 1
        x, y = self.path[i][0], self.path[i][1]

        if figure == '+':
            sum += self.grid[x][y]
        elif figure == '-':
            sum -= self.grid[x][y]

        if i < self.length - 4: #why the last two elements are executed when I put -2, why does it work when I put -4? At least it works!
            self.trace_path(self.path[i + 1][0], self.path[i + 1][1], i + 1, sum)
        else:
            self.grid[self.row - 1][self.col - 1] = sum
    
    def __init__(self, row, col, minNumber, maxNumber):
        self.row = row
        self.col = col
        self.path = []
        self.reached = False
        self.grid = [[0 for i in range(self.col)] for j in range(self.row)]        
        self.directions = [[0,1],[0,-1],[-1,0],[1,0]]        
        
                
        #filling the grid with random values
        for i in range(self.row):
            for j in range(self.col):
                if (i + j) % 2: 
                    self.grid[i][j] = random.choice(['+', '-'])
                else:
                    self.grid[i][j] = random.randint(minNumber, maxNumber)
        self.grid[self.row - 1][self.col - 2], self.grid[self.row - 2][self.col - 1] = "=", "="

        #finding a path until the last cell
        self.find_path(0, 0, [])
        self.length = len(self.path)

        #tracing the path
        self.trace_path(self.path[1][0], self.path[1][1], 1, self.grid[0][0])

class Cell(pygame.sprite.Sprite):
    def __init__(self, gridX, gridY, screenY, screenX, value, width):
        pygame.sprite.Sprite.__init__(self)
        self.value = str(value)
        self.width = width
        self.gridRow, self.gridCol = gridX, gridY
        self.screenX, self.screenY = screenX, screenY
        self.rect = (self.screenX, self.screenY)
        self.ticked = False
        
        self.image = pygame.Surface((80,80))
        self.image.fill((255,255,255))
         #drawing the cell on the screen
        self.text = font.render(self.value, True, (0,0,0))
        self.textX, self.textY = self.screenX + self.width // 2 - 10, self.screenY + self.width // 2 - 10
        self.draw()
        
    def click(self):
        if not self.ticked and self.isAdjacent():
            self.image.fill((0,255,0))
            player_path.append([self.gridRow, self.gridCol])
            self.ticked = True
            self.draw()
            if self.gridRow == row - 1 and self.gridCol == col - 1:
                if player_path == game.path:
                    print("Correct. You win!")
                else:
                    print("Wrong. Try again...")
            
    def isAdjacent(self):
        lastRow, lastCol = player_path[-1][0], player_path[-1][1]
        if abs(lastRow - self.gridRow) <= 1 and abs(lastCol - self.gridCol) <= 1:
            if not (abs(lastRow - self.gridRow) == 1 and abs(lastCol - self.gridCol) == 1):
                return True
        return False 

    def draw(self):
        screen.blit(self.image, (self.screenX, self.screenY))
        screen.blit(self.text, (self.textX, self.textY))

#F5 button
def restart():
    game.__init__(row, col, minNumber, maxNumber)
    for i in range(len(player_path) - 1):
        player_path.pop()
    for i in range(row): #creating cells
        for j in range(col):
            cell = Cell(i, j, coordinates[i], coordinates[j], game.grid[i][j], width)
            cells[i][j] = cell
    cells[0][0].click()
    player_path.pop()

#Enter button 
def show_path(list_cells):
    global picture
    previous = cells[0][0]
    next = cells[game.path[1][0]][game.path[1][1]]
    previous = opposite_directions[direction(previous, next)]
    l = len(list_cells)
    for i in range(l):
        coordinate = list_cells[i]
        if i != l - 1:
            next = cells[list_cells[i+1][0]][list_cells[i+1][1]]
        else:
            next = cells[row - 1][col - 1]
        cell = cells[coordinate[0]][coordinate[1]]
        #the problem is that it will give an error while proceeding previous cell from final cell
        #I have to make the cycle stop when it reaches the previous cell from the final cell, and make 
        next = direction(cell, next)
        if previous == 'left' or previous == 'right':
            if next == 'left' or next == 'right':
                if previous == 'left':
                    picture = folder + previous + '-' + next + '.png'
                else:
                    picture = folder + next + '-' + previous + '.png'
            else:
                picture = folder + previous + '-' + next + '.png'
        elif next == 'up' or next =='down':
            if next == 'up':
                picture = folder + next + '-' + previous + '.png'
            else:
                picture = folder + previous + '-' + next + '.png'
        else:
            picture = folder + next + '-' + previous + '.png'
        
        cell.image = pygame.image.load(picture)
        cell.draw()
        previous = opposite_directions[next]
        
def direction(current, next):
    currentRow = current.gridRow
    currentCol = current.gridCol
    nextRow = next.gridRow
    nextCol = next.gridCol

    rowDifference = nextRow - currentRow 
    colDifference = nextCol - currentCol 

    if rowDifference == 0:
        if colDifference == 1:
            return 'right'
        else:
            return 'left'
    elif rowDifference == 1:
        return 'down'
    else:
        return 'up'

def visible(list_cells, toShow):
    if toShow:
        for coordinate in list_cells:
            cell = cells[coordinate[0]][coordinate[1]]
            cell.image.fill((0,255,0))
            cell.ticked = True
            cell.draw()
    else:
        for coordinate in list_cells:
            cell = cells[coordinate[0]][coordinate[1]]
            cell.image.fill((255,255,255))
            cell.ticked = False
            cell.draw()

        
pygame.init()
row = 8
col = 8
width = 80
minNumber = 1
maxNumber = 20
coordinates = [10 + 90 * i for i in range(row)]

#this is the variables I use to store the names of pictures in the folder.
opposite_directions = {}
opposite_directions['right'] = 'left'
opposite_directions['left'] = 'right'
opposite_directions['up'] = 'down'
opposite_directions['down'] = 'up'

picture = ''
folder = './pictures/' 



screen = pygame.display.set_mode((coordinates[row - 1] + width + 10, coordinates[col - 1] + width + 10))
font = pygame.font.Font('freesansbold.ttf',24)

game = Game(row, col, minNumber, maxNumber)
player_path = [[0, 0]]
cells = [[0 for i in range(col)] for j in range(row)]
previous = 'unknown'
restart()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            for i in range(row):
                for j in range(col):
                    if coordinates[i] <= mouseY <= coordinates[i] + width and coordinates[j] <= mouseX <= coordinates[j] + width: 
                        cells[i][j].click()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if len(player_path) > 1:
                    gridX, gridY = player_path[-1][0], player_path[-1][1]
                    player_path.pop()
                    cells[gridX][gridY].ticked = False
                    visible([[gridX, gridY]], False)
            if event.key == pygame.K_F5:
                restart()
            if event.key == pygame.K_SPACE:
                visible(player_path[1:], False) #making all player cells invisible except the first one
                player_path = player_path[0:1] 
            if event.key == pygame.K_KP_ENTER:
                visible(player_path, False) #making the player path invisible
                show_path(game.path[1:-1]) #showing the path
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER:
                visible(game.path, False) 
                visible(player_path, True)


                    
    pygame.display.update()