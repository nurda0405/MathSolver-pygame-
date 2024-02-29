The goal of the player: is to construct a path from the first cell until the last cell in which the result of
algebraic expression is the value of last cell.

Logic of the game:
1. The first cell should be always clicked;
2. Cell should be clicked only if it is the adjacent with the last clicked cell;
3. The coordinates of the cell should be added to the path and its color should be changed when it is clicked;
4. If the clicked cell is the cell in the right bottom in the grid, the path of the player should be checked with the right path of the game.
5. Ctrl + Z command should set the last cell to its default settings and its coordinate should be erased from the path;
6. Erase button should erase all cells except the cell at left top from path;
7. Show path button should blit the correct path;
8. Restart path should construct new grid and path.

Algorithm:

Create object of game class;
Create each cell in the grid as a sprite;
Group all cells into a sprite.Group;
Show cells in display;
Declare the player's path;

Set the color of cell at left top to yellow;
Add the coordinates of cell at left top to player's path;


Mouse click event for the group of cells:
    IF cell collides with mouse:
        IF cell is not picked:
            IF cell is adjacent with the last chosen cell:
                Change cell.color;
                Path += [cell[x], cell[y]];
        
        IF cell[x] == 7 and cell[y] = 7:
            IF Path == Game.Path:
                Print("You win!");
            ELSE:
                Print("Wrong path...");

Erase button:
    delete cells except the first;
    change the color of all cells except the first;

Ctrl + Z:
    delete the last cell from path if it is not the last cell;
    change the color of the last cell if it is not the first cell;

Restart button:
    Construct new grid;
    Construct new path;

Show path:
    iterate the cells of game's path;
    change the color of cell to yellow;

I want to show arrows while showing the path. For this I am foing to blit it on the screen by the coordinates of 
cell.
After stopping showing the path, I am going to draw the cells.

Error:
After finishing showing the path first cell is not colored.

I am going to replace arrows with lines and corners.
There are 2 lines and 4 corners:
When to use each of them:

Lines: when the previous and next cells on the line.

def where(current, anotherCell)
    previousCol = previousCol - CurrentCol;
    previousRow = previousRow - CurrentRow;
    if previousCol == 0:
        if previousRow == -1:
            previous = 'up'
        else:
            previous = 'down'
    elif previousCol == -1:
        previous = 'left'
    else:
        previous = 'right'

nextCol = nextCol - currentCol;
nextRow = nextRow - currentRow;


1. left-right:
    abs(previousRow) == abs(nextRow) == 0;
    abs(previousCol) == abs(nextCol) == 1 

2. up-down: 
    abs(previousRow) == abs(nextRow) == 1;
    abs(previousCol) == abs(nextCol) == 0 

Corners:
1. left-up: 
    previousCol = -1;
    previousRow = 0;

    nextRow = -1;
    nextCol = 0;
2. left - down:
    previousCol = -1;
    previousRow = 0;

    nextRow = -1;
    nextCol = 0;
