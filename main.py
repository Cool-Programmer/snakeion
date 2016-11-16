import pygame
import time

pygame.init()  # Initialize pygame

# Variables
displayWidth = 800
displayHeight = 600
gameTitle = 'Snakeion'
FPS = 15  # Frames Per Second (30 is the more used)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# General Settings
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # Game window
pygame.display.set_caption(gameTitle)  # Set title
clock = pygame.time.Clock()  # clock object return
font = pygame.font.SysFont(None, 33)  # font object
snakeBg = pygame.image.load('images/snakebg.png')


# Message on the screen
def msg2scr(msg, color):
    scr_txt = font.render(msg, True, color)
    gameDisplay.blit(scr_txt, [displayWidth/2, displayHeight/2])  # Show

# Main loop
def gameLoop():

    # Game Exit | Game Over
    gameExit = False  # constant-like variable for controlling exiting
    gameOver = False  # constant-like variable for controlling ending the game
    blockSize = 10

    # Block's position
    lead_x = displayWidth / 2  # Number 1 block position X
    lead_y = displayHeight / 2  # Number 1 block position Y
    lead_x_change = 0  # Initial change X
    lead_y_change = 0  # Initial change Y

    while not gameExit:
        # If gameover
        while gameOver == True:
            gameDisplay.blit(snakeBg, (0, 0))
            msg2scr('Game Over! Press W to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():  # Gameover event handling loop
                if event.type == pygame.QUIT:  # Game Exit
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:  # Keypress
                    if event.key == pygame.K_q:
                        gameExit = True
                    elif event.key == pygame.K_w:
                        gameLoop()
                    elif event.key == pygame.K_ESCAPE:
                        gameExit = True


        for event in pygame.event.get():  # Main event handling loop
            if event.type == pygame.QUIT:  # Close the window by X
                gameExit = True
            if event.type == pygame.KEYDOWN:  # KEYPRESS
                if event.key == pygame.K_LEFT:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = blockSize
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = blockSize
                    lead_x_change = 0
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
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, blockSize, blockSize])  # Draw box

        pygame.display.update()
        clock.tick(FPS)  # Frames per second

    pygame.display.update()  # Update flip
    # msg2scr('Game Over', blue)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()  # Uninitialize pygame
    quit()  # Quit

gameLoop()