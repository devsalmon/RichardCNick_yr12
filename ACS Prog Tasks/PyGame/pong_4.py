#startup
import pygame
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
pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False
ball_width = 20
x_val = 150
y_val = 200
x_direction = 3
y_direction = 3
x_padd = 0
y_padd = 20
padd_length = 15
padd_width = 60
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
# -- User input and controls
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    #CHECKS IF BALL HAS HIT THE PADDLE
    if x_val == padd_length and y_val < (y_padd + padd_width) and y_val > (y_padd - padd_width):
        #SPEEDS UP BALL ON IMPACT
        x_direction = (x_direction * -1) + 1
    elif x_val >= (size[0] - ball_width):
        x_direction = x_direction * -1
    elif x_val <= 0:
        x_val = 150
        y_val = 200
        x_direction = 3
    elif y_val >= (size[1] - ball_width) or y_val <= 0 :
        y_direction = y_direction * -1
    keys = pygame.key.get_pressed()
    ## - the up key or down key has been pressed
    if keys[pygame.K_UP]:
    # -- write logic that happens on key press here
        y_padd = y_padd - 5
    elif keys[pygame.K_DOWN]:
        # -- write logic that happens on key press here
        y_padd = y_padd + 5
    #End If

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    # -- Game logic goes after this comment
    #THIS STOPS PADDLE FROM MOVING OFF SCREEN
    if y_padd >= (size[1]):
        y_padd = (0 - padd_width)
    elif y_padd <= (0 - padd_width):
        y_padd = (size[1])
    #End if
    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
# - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
