#Startup
import pygame
import random
import math
import webbrowser

# -- Global Constants
size = (640,480)
player_score = 0
pleasework = False
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255, 0, 0)
# -- Initialise PyGame
pygame.init()
#Load music
pygame.mixer.music.load('The-Avengers-Theme-Song.mp3')
#Play music
pygame.mixer.music.play()
# -- Blank Screen
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Space Invaders Lite")

#Displays game stats
def draw_stats(screen, x, y, stats):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 30, True, False)
    # Render the text. "True" means anti-aliased text.
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render(str(stats), True, YELLOW)
    # Puts the image of the text on the screen at x,y
    screen.blit(text, (x, y))
#Endproc

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for Player
    def __init__(self, color, width, height, lives, score, bullet_count):
        
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1] - height
        self.speed = 0
        self.lives = lives
        self.score = 0
        self.bullet_count = bullet_count
    #Endwhat?

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x >= size[0]:
            self.rect.x = 0
        elif self.rect.x <= 0:
            self.rect.x = size[0]
        #Endif
    #Endmethod


    def player_set_speed(self, val):
        self.speed = val
    #Endmethod
        
    def increase_score(self, val):
        self.score += val
    #Endmethod
        
    def decrease_bcount(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
        #Endif
    #Endmethod
            
#Endclass

class Invader(pygame.sprite.Sprite):
    # Define the constructor for Invader
    def __init__(self, color, width, height, speed, enemy):

        #Why can i not have xpos atribute that holds self.rect.x and change it when i call the class?
        
        # Call the sprite constructor
        super().__init__()
        self.image = pygame.image.load(enemy)
        # Set the position of the sprite
        self.height = height
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-self.height, (-150 - self.height), -1)
        self.speed = speed
        
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= size[1]:
            invader_group.remove(self)
        #Endif
    #Endmethod

    def centralise(self):
        while self.rect.x > 0:
            self.rect.x -= 1
        #Endwhile
    #Endmethod
            
#Endclass

class Bullet(pygame.sprite.Sprite):
    # Define the constructor for Bullet
    def __init__(self, color, width, height):
        
        # Call the sprite constructor
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = my_player.rect.x + (0.5 * my_player.width)
        self.rect.y = my_player.rect.y
        self.speed = 3
        
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 0:
            bullet_group.remove(self)
        #Endif
    #Endmethod
            
#Endclass
            
# -- Exit game flag set to false
done = False

# Create a sprite group of the invaders
invader_group = pygame.sprite.Group()
# Create a sprite group of the bullets
bullet_group = pygame.sprite.Group()
# Create a sprite group of all sprites
all_sprites_group = pygame.sprite.Group()

# Create the Objects

number_of_invaders = 10
for count in range (number_of_invaders):
    my_invader = Invader(BLUE, 30, 30, 1, "enemy.jpg") # Invaders are blue with size 30 x 30 px
    invader_group.add(my_invader) # Adds the new invader to the group of invaders
    all_sprites_group.add(my_invader) # Adds it to the group of all Sprites
#Next count
    
    
my_invader2 = Invader(BLUE, 30, 30, 0, "enemy.jpg")
my_invader3 = Invader(BLUE, 30, 30, 0, "enemy.jpg")
my_invader4 = Invader(BLUE, 30, 30, 0, "enemy.jpg")
my_invader5 = Invader(BLUE, 30, 30, 0, "enemy.jpg")
my_invader6 = Invader(BLUE, 30, 30, 0, "enemy.jpg")
    
my_player = Player(YELLOW, 15, 15, 5, 0, 200)
all_sprites_group.add(my_player) # Adds it to the group of all Sprites

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done and my_player.lives > 0:
    
    # -- User inputs here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - A key is down
            if event.key == pygame.K_LEFT: # - If the left key pressed
                my_player.player_set_speed(-4) # - Speed set to -4
            elif event.key == pygame.K_RIGHT: # - If the right key pressed
                my_player.player_set_speed(4) # - Speed set to 4
            elif event.key == pygame.K_UP: # - If up key is pressed, Alex's github opens
               #webbrowser.open_new_tab('https://github.com/alex-silcock/silcockaw-Y12-Computer-Science/commit/e7228fab2c1dd2e32832b558ee0dd0479c6049ba')
                pass
            elif event.key == pygame.K_SPACE: # - If space key is pressed
                if my_player.bullet_count > 0:
                    my_bullet = Bullet(RED, 2, 2) # - Bullet is created
                    bullet_group.add(my_bullet) # - Bullet is added to bullet_group
                    my_player.decrease_bcount() # - Bullet count decreases
                    all_sprites_group.add(my_bullet) # - Adds bullets to all sprites group
                #Endif
        elif event.type == pygame.KEYUP: # - A key released            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                my_player.player_set_speed(0) # Speed set to 0
                #Endif
            #Endif
        #Endif
    #Nextevent

    # -- Game logic goes after this comment
    if my_invader.rect.y == size[1] + 150:
        print("round2")
        number_of_invaders = 30
        for count in range (number_of_invaders):
            my_invader2 = Invader(BLUE, 30, 30, 1, "enemy.jpg") # Invaders are blue with size 30 x 30 px
            invader_group.add(my_invader2) # Adds the new invader to the group of invaders
            all_sprites_group.add(my_invader2) # Adds it to the group of all Sprites
        #Next count
    #Endif

    if my_invader2.rect.y == size[1] + 150:
        print("round3")
        number_of_invaders = 10
        for count in range (number_of_invaders):
            my_invader3 = Invader(BLUE, 50, 50, 2, "enemy.jpg") # Invaders are blue with size 30 x 30 px
            invader_group.add(my_invader3) # Adds the new invader to the group of invaders
            all_sprites_group.add(my_invader3) # Adds it to the group of all Sprites
        #Next count
    #Endif

    if my_invader3.rect.y == size[1] + 150 or my_invader3.rect.y == size[1] + 151:
        print("round3")
        number_of_invaders = 10
        for count in range (number_of_invaders):
            my_invader4 = Invader(BLUE, 45, 60, 1, "fiona.jpg") # Invaders are blue with size 30 x 30 px
            invader_group.add(my_invader4) # Adds the new invader to the group of invaders
            all_sprites_group.add(my_invader4) # Adds it to the group of all Sprites
        #Next count
    #Endif

    if my_invader4.rect.y == size[1] + 150:
        print("round4")
        number_of_invaders = 10
        for count in range (number_of_invaders):
            my_invader5 = Invader(BLUE, 56, 75, 2, "Spence.jpg") # Invaders are blue with size 30 x 30 px
            invader_group.add(my_invader5) # Adds the new invader to the group of invaders
            all_sprites_group.add(my_invader5) # Adds it to the group of all Sprites
        #Next count
    #Endif

    if my_invader5.rect.y == size[1] + 150 or my_invader5.rect.y == size[1] + 151:
        print("round5")
        pleasework = True
        number_of_invaders = 1
        for count in range (number_of_invaders):
            clock.tick(1)
            my_invader6 = Invader(BLUE, 636, 478, 1, "piano.jpeg") # Invaders are blue with size 30 x 30 px
            my_invader6.centralise()
            invader_group.add(my_invader6) # Adds the new invader to the group of invaders
            all_sprites_group.add(my_invader6) # Adds it to the group of all Sprites
        #Next count
    #Endif
        
    # -- When invader hits the player add 5 to score.
    player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)
    for p in player_hit_group: #how does this work!?
        my_player.lives = my_player.lives - 1
    #nextp
    for b in bullet_group:
        invader_hit_group = pygame.sprite.spritecollide(b, invader_group, True)
        #if len(invader_hit_group) >= 2:
        #   invader_destroy_group = pygame.sprite.spritecollide(b, invader_group, True)
        for b in invader_hit_group:
            my_player.increase_score(5)
        #Nextb
    #Nextb

            
    all_sprites_group.update()
    
# -- Screen background is BLACK
    screen.fill(BLACK)
    
# -- Draw here
    all_sprites_group.draw(screen)
    draw_stats(screen, 10, 10, "Lives: %d" % my_player.lives)
    draw_stats(screen, 10, 40, "Score: %d" % my_player.score)
    draw_stats(screen, 10, 70, "Bullets: %d" % my_player.bullet_count)
    
# -- Flip display to reveal new position of objects
    pygame.display.flip()
    
# - The clock ticks over
    clock.tick(60)
    if pleasework == True:
        clock.tick(20)
#End While - End of game loop

pygame.quit()

#Shmuck's assemble ... we're shmuck's 1, 2 and 3, i like being me, and i like being free!
#Shmuck's assemble ... this is a little freestyle eee. We're shmuck's 1, 2 and 3, i like being me, and i like being free!
