#afterhoursprogramming.com/tutorial/python/writing-to-files
#startup
import pygame
from network import Network
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
SALMON = (255,140,105)
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
x_direction = 4
y_direction = 4
padd_length = 60
padd_width = 15
x_padd = 0
y_padd = 120
x_padd_2 = size[0] - padd_width
y_padd_2 = 25
scoreA = 0
scoreB = 0
#DISPLAY SCORES
def draw_score(screen, x, y, score):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 50, True, False)
    # Render the text. "True" means anti-aliased text.
    # SALMON is the colour. The variable SALMON was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render(str(score), True, SALMON)
    # Puts the image of the text on the screen at x,y
    screen.blit(text, (x, y))
#ENDDEF
def paddle_on_screen(y_paddle):
    #THIS STOPS PADDLE FROM MOVING OFF SCREEN
    if y_paddle >= size[1]:
        print(padd_length)
        y_paddle = 0 - padd_length
    elif y_paddle <= (0 - padd_length):
        y_paddle = (size[1])
    #End if
    return y_paddle
#ENDDEF
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
# -- User input and controls
    #MAKES BALL MOVE
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    #CHECKS IF BALL HAS HIT THE PADDLE
    if x_val <= padd_width and y_val < (y_padd + padd_length) and y_val > (y_padd - padd_length):
        #SPEEDS UP BALL ON IMPACT
        x_direction = (x_direction * -1) + 2
    #THIS BOUNCES BALL OF OTHER PADDLE
    elif (x_val + ball_width) >= (size[0] - padd_width) and y_val < (y_padd_2 + padd_length) and y_val > (y_padd_2 - padd_length):
        x_direction = x_direction * -1
    #CHECKS IF PLAYER A DIES 
    elif x_val <= 0:
        #RESETS POSITION
        x_val = 150
        y_val = 200
        x_direction = 3
        #GIVES PLAYER B A POINT
        scoreB = scoreB + 1
    #CHECKS IF PLAYER B DIES
    elif x_val >= size[0]:
        #RESETS POSITION
        x_val = 150
        y_val = 200
        x_direction = 3
        #GIVES PLAYER A A POINT
        scoreA = scoreA + 1
    #CHECKS IF TOP OR BOTTOM SCREEN HAS BEEN HIT
    elif y_val >= (size[1] - ball_width) or y_val <= 0 :
        y_direction = y_direction * -1
    #ENDIF
    #FIRST TO FIVE POINTS WINS
    #if scoreA == 5 or scoreB == 5:
    #    pygame.draw.rect(screen, WHITE, (50, 50, 100, 1000))
    
    keys = pygame.key.get_pressed()
    #PLAYER A CONTROLS
    if keys[pygame.K_w]:
    # -- write logic that happens on key press here
        y_padd = y_padd - 5
    elif keys[pygame.K_s]:
        # -- write logic that happens on key press here
        y_padd = y_padd + 5
    #ENDIF
    #PLAYER B CONTROLS
    if keys[pygame.K_UP]:
    # -- write logic that happens on key press here
        y_padd_2 = y_padd_2 - 5
    elif keys[pygame.K_DOWN]:
        # -- write logic that happens on key press here
        y_padd_2 = y_padd_2 + 5 
    #End If

    #THIS STOPS PADDLE FROM MOVING OFF SCREEN
    y_padd = paddle_on_screen(y_padd)
    y_padd_2 = paddle_on_screen(y_padd_2)      
    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    #Ball
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    #LEFT PADDLE
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_width, padd_length))
    #RIGHT PADDLE
    pygame.draw.rect(screen, WHITE, (x_padd_2, y_padd_2, padd_width, padd_length))
    #LEFT SCORE
    draw_score(screen, 290, 30, scoreA)
    #RIGHT SCORE
    draw_score(screen, 350, 30, scoreB)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
#End While - End of game loop
pygame.quit()
