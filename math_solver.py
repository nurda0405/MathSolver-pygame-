import random
# fill the grid with numbers and figures, after that trace a path until the last cell.

class Game:
    def find_path(self, x, y, path):
        #stop if reached the end cell
        if (x == self.i - 1 and y == self.j - 2) or (x == self.i - 2 and y == self.j - 1):
            self.reached = True
            self.path = path + [[x,y], [7,7]]
            return
        
        #shuffling the directions to avoid repeated paths
        random.shuffle(self.directions)

        #seeking the last cell
        if not self.reached:
            for d in self.directions:
                if not self.reached:        
                    i = d[0]
                    j = d[1]
                    if -1 < x + i < 8 and -1 < y + j < 8:
                        if not [x+i, y+j] in path:
                            self.find_path(x + i, y + j, path + [[x, y]])
            #the reason why my previous program didn't worked correctly is that I had to not save the values in the variable within function as the path of wrong way interference with the traced path, instead, I had give the new value as a parameter of the next recursion function. Also, I had to know the working principle of the recursion call, for example, in the 'for' cycle the first called function executes until it reaches its end case and other called functions waits until the first is executed. For example, in my code I had to swap the order of if clause and for cycle to check whether the path reached the end cell, otherwise, it will continue working after reaching the end cell. 
    
   #tracing the path and finding the end value
    def trace_path(self, x, y, i, sum):
        figure = self.grid[x][y]
        i += 1
        x, y = self.path[i][0], self.path[i][1]
        print(figure, self.grid[x][y])

        if figure == '+':
            sum += self.grid[x][y]
        elif figure == '-':
            sum -= self.grid[x][y]

        if i < self.length - 4: #why the last two elements are executed when I put -2, why does it work when I put -4?
            self.trace_path(self.path[i + 1][0], self.path[i + 1][1], i + 1, sum)
        else:
            self.grid[7][7] = sum
    
    def __init__(self):
        self.i = 8
        self.j = 8
        self.path = []
        self.reached = False
        self.grid = [[0 for i in range(self.i)] for j in range(self.j)]        
        self.directions = [[0,1],[0,-1],[-1,0],[1,0]]        
        
                
        #filling the grid with random values
        for i in range(self.i):
            for j in range(self.j):
                if (i + j) % 2:    
                    self.grid[i][j] = random.choice(['+', '-'])
                else:
                    self.grid[i][j] = random.randint(1,15)
        self.grid[7][6], self.grid[6][7] = "=", "="

        #finding a path until the last cell
        self.find_path(0, 0, [])
        self.length = len(self.path)

        #tracing the path
        self.trace_path(self.path[1][0], self.path[1][1], 1, self.grid[0][0])

        self.problem = ''
        for cell in self.path:
            self.problem += str(self.grid[cell[0]][cell[1]])

        
         
game = Game()
for i in range(8):
    print(game.grid[i],'\n')
print(game.path,'\n')
print(game.problem)