import pygame


pygame.init()  # Initialize pygame
gameDisplay = pygame.display.set_mode((800, 600))  # Game window
gameTitle = pygame.display.set_caption('Snakeion')  # Set title

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

gameExit = False  # constant-like variable for controlling exiting
gameOver = False  # constant-like variable for controlling ending the game

lead_x = 300  # Number 1 block position X
lead_y = 300  # Number 1 block position Y
lead_x_change = 0  #  Initial change X
lead_y_change = 0  #  Initial change Y

FPS = 15  # Frames Per Second (30 is the more used)
clock = pygame.time.Clock()  # clock object return

while not gameExit:
    for event in pygame.event.get():  # Event handling loop
        if event.type == pygame.QUIT:  # Close the window by X
            gameExit = True
        if event.type == pygame.KEYDOWN:  # KEYPRESS
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0
            elif event.key == pygame.K_ESCAPE:  # Exit via Esc
                gameExit = True
            elif event.key == pygame.K_q:  # Exit via Q
                gameExit = True
        # This is kinda simulation that the key hold is real event. Will make the game too easy, but:
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         lead_x_change = 0


    lead_x += lead_x_change  # Sum lead_x & lead_x_change
    lead_y += lead_y_change  # Sum lead_y & lead_y_change


    gameDisplay.fill(green)  # Set background color to green
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])  # Draw box

    pygame.display.update()
    clock.tick(FPS)
pygame.display.update()  # Update flip
pygame.quit()  # Uninitialize pygame
quit()  # Quit