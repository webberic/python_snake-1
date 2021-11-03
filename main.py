"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame

# initialize the game
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# set the screen size
dis = pygame.display.set_mode((800, 600))

# draw the screen
pygame.display.update()

# set a caption on the screen
pygame.display.set_caption('Snake game by Edureka')

# variables to hold different colors
blue   = (   0,   0,   255)
red    = (   255,   0,   0)

# create a variable to keep track of whether or not the game is over
game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis,blue,[x1,y1,10,10])

    pygame.display.update()

    clock.tick(30)

# the main game loop. this loop will run infinitely until the value
# of `game_over` changes from `False` to `True`
while not game_over:
        # loops over all of the events (like keypresses and mouse moves
        # and button clicks) that happen during one game loop cycle
        for event in pygame.event.get():
            # if someone clicks the red X in the upper right
            if event.type==pygame.QUIT:
                game_over=True
                #print(event)    #prints out all the actions that take place on the screen
        pygame.draw.rect(dis,blue,[200,150,10,10])
        pygame.display.update()


# quit the game
pygame.quit()
quit()
