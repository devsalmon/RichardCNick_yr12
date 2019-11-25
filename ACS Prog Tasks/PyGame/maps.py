import pygame

size = (640, 480)
screen = pygame.display.set_mode(size)

BLUE = (50, 50, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

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
    
    # Define the constructor for tile
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

class Player(pygame.sprite.Sprite):
    
    def __init__(self, color):
        
        super().__init__()
        width = 20
        height = 20
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 40

    def move(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val
    #Endmethod

#End class

# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()
# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
        if my_map[x][y] == 1:
            my_wall = tile(BLUE, 40, 40, x*40, y*40)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)

        #Endif
    #Nextx
#Nexty

my_pacman = Player(RED)

all_sprites_list.add(my_pacman)

                   
### -- Game Loop
while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_pacman.move(-2, 0)
    elif keys[pygame.K_RIGHT]:
        my_pacman.move(2, 0)
    elif keys[pygame.K_UP]:
        my_pacman.move(0, -2)
    elif keys[pygame.K_DOWN]:
        my_pacman.move(0, 2)
    #Endif

    # -- Check for collisions between pacman and wall tiles
    player_hit_list = pygame.sprite.spritecollide(my_pacman, wall_list, False)
    
    for foo in player_hit_list:
        my_pacman.move(0, 0)
        my_pacman.rect.x = my_pacman_old_x
        my_pacman.rect.y = my_pacman_old_y
    #Nextfoo
    #Run the update function for all sprites
    my_pacman_old_x = my_pacman.rect.x
    my_pacman_old_y = my_pacman.rect.y
    all_sprites_list.update()


# -- Screen background is BLACK
    screen.fill (BLACK)

    all_sprites_list.draw(screen)
    
# -- flip display to reveal new position of objects
    pygame.display.flip()
# - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
