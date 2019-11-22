import pygame

size = (640, 480)
screen = pygame.display.set_mode(size)

BLUE = (50, 50, 255)
BLACK = (0,0,0)

pygame.init()

# -- Title of new window/screen
pygame.display.set_caption("Maps")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

my_map = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]

## -- Define the class tile which is a sprite
class tile(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref


# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()
# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
        if my_map[x][y] == 1:
            my_wall = tile(BLUE, 20, 20, x*20, y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)
        #Endif
    #Nextx
#Nexty
            
### -- Game Loop
while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


# -- Screen background is BLACK
    screen.fill (BLACK)

    all_sprites_list.draw(screen)
    
# -- flip display to reveal new position of objects
    pygame.display.flip()
# - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()



