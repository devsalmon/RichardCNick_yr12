#startup
import pygame
import random
import math
import webbrowser

# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")
player_score = 0

#DISPLAY SCORES
def draw_score(screen, x, y, score):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 50, True, False)
    # Render the text. "True" means anti-aliased text.
    # SALMON is the colour. The variable SALMON was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render(str(score), True, YELLOW)
    # Puts the image of the text on the screen at x,y
    screen.blit(text, (x, y))
#ENDDEF

## -- Define the class snow which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, -50, -1)
        self.speed = speed
    #End Procedure
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #End Procedure
#End Class
class Player(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(0, 600)
        #self.rect.y = random.randrange(0, -50, -1)
        self.rect.x = 300
        self.rect.y = size[1] - height
        self.speed = 0
    #End Procedure
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x >= size[0]:
            self.rect.x = 0
        elif self.rect.x <= 0:
            self.rect.x = size[0]
    #endproc
    def player_set_speed(self, val):
        self.speed = val
# -- Exit game flag set to false
done = False

# Create a list of the snow blocks
invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# Create the snowflakes
number_of_invaders = 10 # we are creating 50 snowflakes
for x in range (number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
    invader_group.add(my_invader) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add(my_invader) # adds it to the group of all Sprites
#Next x
my_player = Player(YELLOW, 10, 10)
all_sprites_group.add(my_player) # adds it to the group of all Sprites

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
    # -- User inputs here
   # keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down
            if event.key == pygame.K_LEFT: # - if the left key pressed
                my_player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                my_player.player_set_speed(3) # speed set to 3
            elif event.key == pygame.K_UP:
                import invaders_2
        elif event.type == pygame.KEYUP: # - a key released            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                my_player.player_set_speed(0) # speed set to 0
                #endif
            #endif
        #endif
    #next
#endproc
# -- Game logic goes after this comment
# -- when invader hits the player add 5 to score.
    player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)
    for ack in player_hit_group:
        player_score = player_score + 1
        print(player_hit_group)
    #next ack
    all_sprites_group.update()
# -- Screen background is BLACK
    screen.fill (BLACK)
# -- Draw here
    all_sprites_group.draw(screen)
    draw_score(screen, 290, 30, player_score)
# -- flip display to reveal new position of objects
    pygame.display.flip()
# - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

#Shmuck's assemble ... we're shmuck's 1, 2 and 3, i like being me, and i like being free!
#Shmuck's assemble ... this is a little freestyle eee. We're shmuck's 1, 2 and 3, i like being me, and i like being free!
