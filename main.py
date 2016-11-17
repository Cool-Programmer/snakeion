import pygame
import time
import random

pygame.init()  # Initialize pygame

# Variables
displayWidth = 800
displayHeight = 600
gameTitle = 'Snakeion'
FPS = 8  # Frames Per Second (30 is the more used)
snakeDir = 'right'

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# General Settings
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # Game window
pygame.display.set_caption(gameTitle)  # Set title
clock = pygame.time.Clock()  # Clock object return
smFont = pygame.font.SysFont(None, 35)  # Small font object
mdFont = pygame.font.SysFont(None, 69)  # Medium font object
lgFont = pygame.font.SysFont(None, 80)  # Large font object
snakeBg = pygame.image.load('images/snakebg.png')  # Gameover screen background
snakeHead = pygame.image.load('images/snakeHead.png')  # Snake head picture. Sorry.

# Snake long
def snake(blockSize, snakelist): # Adding to snake
    if snakeDir == 'right':
        head = pygame.transform.rotate(snakeHead, 270)
    elif snakeDir == 'left':
        head = pygame.transform.rotate(snakeHead, 90)
    elif snakeDir == 'up':
        head = snakeHead
    elif snakeDir == 'down':
        head = pygame.transform.rotate(snakeHead, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][-1]))  # Head of the snake
    for elem in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, black, [elem[0], elem[1], blockSize, blockSize])  # Draw snake

# textObj return
def textObj(text, color, size):
    if size == 'small':
        textSurface = smFont.render(text, True, color)  # Set the small text surface
    elif size == 'medium':
        textSurface = mdFont.render(text, True, color)  # Set the medium text surface
    elif size == 'big':
        textSurface = lgFont.render(text, True, color)  # Set the large text surface

    return textSurface, textSurface.get_rect()  # Get the rectangle that's around the text


# Message on the screen
def msg2scr(msg, color, y_displace=0, size = 'small'):
    textSurface, textRect = textObj(msg, color, size)  # Setup the text's surface and the rectangle around it
    textRect.center = (displayWidth/2), (displayHeight/2)+y_displace  # Center the text
    gameDisplay.blit(textSurface, textRect)  # Display

# Main loop
def gameLoop():
    global snakeDir
    # Game Exit | Game Over
    gameExit = False  # constant-like variable for controlling exiting
    gameOver = False  # constant-like variable for controlling ending the game
    blockSize = 20 # Size of the snake

    # Block's position
    lead_x = displayWidth / 2  # Number 1 block position X
    lead_y = displayHeight / 2  # Number 1 block position Y
    lead_x_change = 10  # Initial change X. Whenever the game is started the snake is already moves
    lead_y_change = 0  # Initial change Y
    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(0, displayWidth-blockSize))  # Apple location X (random)
    randAppleY = round(random.randrange(0, displayHeight-blockSize)) # Apple location Y (random)

    while not gameExit:
        # If gameover
        while gameOver == True:
            gameDisplay.blit(snakeBg, (0, 0))
            msg2scr('Game Over!', white, -128, 'big')
            msg2scr('Press W to play again or Q to quit', blue, -70, 'small')
            pygame.display.update()

            for event in pygame.event.get():  # Gameover event handling loop
                if event.type == pygame.QUIT:  # Game Exit
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:  # Keypress
                    if event.key == pygame.K_w:
                        gameLoop()
                    elif event.key == pygame.K_ESCAPE:  # Exit via Esc
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_q:  # Exit via Q
                        gameOver = False
                        gameExit = True


        for event in pygame.event.get():  # Main event handling loop
            if event.type == pygame.QUIT:  # Close the window by X
                gameExit = True
            if event.type == pygame.KEYDOWN:  # KEYPRESS
                if event.key == pygame.K_LEFT:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                    snakeDir = 'left'
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = blockSize
                    lead_y_change = 0
                    snakeDir='right'
                elif event.key == pygame.K_UP:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                    snakeDir='up'
                elif event.key == pygame.K_DOWN:
                    lead_y_change = blockSize
                    lead_x_change = 0
                    snakeDir='down'
                elif event.key == pygame.K_ESCAPE:  # Exit via Esc
                    gameExit = True
                elif event.key == pygame.K_q:  # Exit via Q
                    gameOver = True
            # This is kinda simulation that the key hold is real event. Will make the game too easy, but:
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0

        # BORDER OBSTACLES
        if lead_x >= displayWidth or lead_x < 0 or lead_y >= displayHeight or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change  # Sum lead_x & lead_x_change
        lead_y += lead_y_change  # Sum lead_y & lead_y_change



        gameDisplay.fill(green)  # Set background color to green
        appleSize = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleSize, appleSize]) # Draw apple

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        # Clear list
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Snakes touches itself :D
        for each_part in snakeList[:-1]:
            if each_part == snakeHead:
                gameOver = True

        # Draw snake
        snake(blockSize, snakeList)
        pygame.display.update()

        # THIS WILL WORK ONLY IF THE APPLE SIZE AND THE SNAKE SIZE ARE EXACTLY THE SAME
        # if lead_x == randAppleX and lead_y == randAppleY:  # If the snake and the apple touch each other, generate another apple
        #     randAppleX = round(random.randrange(0, displayWidth - blockSize) / 10.0) * 10.0  # Apple location X (random)
        #     randAppleY = round(random.randrange(0, displayHeight - blockSize) / 10.0) * 10.0  # Apple location Y (random)
        #     snakeLength+=1

        # IF THE SIZE OF THE SNAKE IS 10px X 10px, AND THE APPLE SIZE IS WHATEVER
        # if lead_x >= randAppleX and lead_x <= randAppleX+appleSize:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + appleSize:
        #         randAppleX = round(random.randrange(0, displayWidth - blockSize))  # Apple location X (random)
        #         randAppleY = round(random.randrange(0, displayHeight - blockSize)) # Apple location Y (random)
        #         snakeLength+=1

        # Collisions
        if lead_x > randAppleX and lead_x < randAppleX+appleSize or lead_x+blockSize > randAppleX and lead_x+blockSize < randAppleX+appleSize:
            if lead_y > randAppleY and lead_y < randAppleY+appleSize or lead_y+blockSize > randAppleY and lead_y+blockSize < randAppleY+appleSize:
                randAppleX = round(random.randrange(0, displayWidth - blockSize)) # Apple location X (random)
                randAppleY = round(random.randrange(0, displayHeight - blockSize))  # Apple location Y (random)
                snakeLength += 1




        clock.tick(FPS)  # Frames per second

    pygame.display.update()  # Update flip
    # msg2scr('Game Over', blue)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()  # Uninitialize pygame
    quit()  # Quit

gameLoop()