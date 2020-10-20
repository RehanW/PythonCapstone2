import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers.

#TASK 15 GAME

# I am going to use a lot of the code from the example file and will comment where I have used it.
# I am however retyping everything just so that I can get some practice on what needs to go where.
# Importing the libraries at the top to make the game work.

# First we need to initialize the module so that everything can start properly.
pygame.init()

# Now we need to create the game screen.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# Now we need to declare the player and enemies and we will give them images from the example folder.
player = pygame.image.load("image.png")
enemy1 = pygame.image.load("image.png")
enemy2 = pygame.image.load("image.png")
enemy3 = pygame.image.load("image.png")
prize = pygame.image.load("prize.jpg")

# Next we have to get the dimensions of the images used.
player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# Next we need to store the positions of the player and the enemy and the prize
playerXPosition = 100
playerYPosition = 50

# We will give the enemies random start positions off screen
enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

# Prize position
prizeXPosition = 300
prizeYPosition = 200

# Next we need to set the state of the buttons to False seeing that nothing is pressed
keyUp = False
keyRight = False
keyDown = False
keyLeft = False

# Now we will start with the game loop, we need to constantly run the loop and clear and update as we go on
# so that we can see that the game is running in real time.
while 1:
    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    # This updates the screen
    pygame.display.flip()

    # Now we will loop through events in the game.
    for event in pygame.event.get():

        # First we check if the user quits the program, then if so we exit the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Next we check for user presses down on a key.
        if event.type == pygame.KEYDOWN:

            # Now test if the key pressed is the one we want.
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        # Next we check for user not pressing a key.
        if event.type == pygame.KEYUP:

            # Now we test if the key we don't want to press is up.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # After events are checked for in the loop and values are set,
    # we check the key press values and move the player accordingly.

    # The coordinate system of the game window is that the top left corner is (0, 0).
    # This means that if you want to move the player down you have to increase the y position.
    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition < 0:
            playerXPosition += 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1

    # Next we check for collision with enemy players and prize.
    # We need bounding boxes around the images of the player and the enemy and the prize.
    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())

    # Now we need to update the playerBox to the player's position,
    # making the box stay around the player.
    playerBox.top = playerXPosition
    playerBox.right = (playerXPosition - (player_height / 2)) + player_width
    playerBox.bottom = playerYPosition
    playerBox.left = (playerYPosition + (player_height / 2))

    # Next we need to make the bounding boxes around the enemies.
    enemy1Box = pygame.Rect(enemy1.get_rect())

    enemy1Box.top = enemy1XPosition
    enemy1Box.right = (enemy1XPosition - (enemy1_height / 2)) + enemy1_width
    enemy1Box.bottom = enemy1YPosition
    enemy1Box.left = (enemy1YPosition + (enemy1_height / 2))

    enemy2Box = pygame.Rect(enemy2.get_rect())

    enemy2Box.top = enemy2XPosition
    enemy2Box.right = (enemy2XPosition - (enemy2_height / 2)) + enemy2_width
    enemy2Box.bottom = enemy2YPosition
    enemy2Box.left = (enemy2YPosition + (enemy2_height / 2))

    enemy3Box = pygame.Rect(enemy3.get_rect())

    enemy3Box.top = enemy3XPosition
    enemy3Box.right = (enemy3XPosition - (enemy3_height / 2)) + enemy3_width
    enemy3Box.bottom = enemy3YPosition
    enemy3Box.left = (enemy3YPosition + (enemy3_height / 2))

    # Next the bounding boxes around the prize
    prizeBox = pygame.Rect(prize.get_rect())

    prizeBox.top = prizeXPosition
    prizeBox.right = (prizeXPosition - (prize_height / 2)) + player_width
    prizeBox.bottom = prizeYPosition
    prizeBox.left = (prizeYPosition + (prize_height / 2))

    # Next we test collision of the boxes:
    if playerBox.colliderect(enemy1Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)

    # Next we set what happens with the enemies.
    if enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width:
        print("You win!")
        pygame.quit()
        exit(0)

    # Now we make the enemy approach the player.
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15