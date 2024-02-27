import pygame

pygame.init()
class Cell(pygame.sprite.Sprite):
    def __init__(self):
        self.x = "achivable"
array = [[0]]
cell = Cell()
array[0][0] = cell
print(array[0][0].x)
screen = pygame.display.set_mode((640,640))
rect = pygame.Surface((50,50))
rect.fill((0,0,255))
rectangle = rect.get_rect()
screen.fill((255,255,255))
screen.blit(rect, (0,0))

font = pygame.font.Font('freesansbold.ttf', 14)
position = font.render(str(0) + " "+str(0), True,(0,0,0))
pos_rect = position.get_rect()
pos_rect.center = (200,200)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            screen.fill((255,255,255))
            if 0 <= mouseX <= 50 and 0 <= mouseY <= 50:
                rect.fill((255,0,0))
            position = font.render(str(mouseX)+" "+str(mouseY), True,(0,0,0))
            screen.blit(rect, (0,0))
            screen.blit(position, pos_rect)
            
    pygame.display.update()

