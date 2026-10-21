# You will build a Mini Sprite Adventure using Python and Pygame. You will draw a moving rectangle sprite, compare solid and outlined shapes, use arrow keys to move the sprite, keep it inside the screen, and change its color when it touches different screen edges.

# Step 1: Create the Pygame Screen Create a new Python file. Import pygame, initialize it, and create a screen using pygame.display.set_mode(). Add a caption for the game window.

# Step 2: Set the Sprite Position and Size Create x and y variables for the sprite position. Also create sprite_width, sprite_height, and speed so the rectangle can be drawn and moved.

# Step 3: Define Colors Create color variables using RGB values. These colors will be used for the background, circles, and moving sprite.

# Step 4: Create the Game Loop Use a while loop so the game window stays open until the player closes it. Handle pygame.QUIT inside the event loop.

# Step 5: Check Arrow Keys with get_pressed() Use pygame.key.get_pressed() to check which arrow keys are being held down. Update x and y when the user presses left, right, up, or down.

# Step 6: Keep the Sprite Inside the Screen Use min() and max() to stop the sprite from moving outside the screen boundaries.

# Step 7: Change Color Based on Position Use if, elif, and else statements to change the sprite color when it touches the left, right, top, or bottom edge.

# Step 8: Draw Shapes and Sprite Fill the screen with a background color, draw one solid circle and one outlined circle, then draw the moving rectangle using pygame.Rect.

# Step 9: Run and Explore Run the program and move the sprite using arrow keys. Touch each edge of the screen and observe how the sprite color changes.

# Mini Sprite Adventure
 
import pygame
 
def main():
    pygame.init()
 
    # PART 1: Create the game screen
    screen_width, screen_height = 500, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mini Sprite Adventure")
 
    # PART 2: Set sprite position and size
    x, y = 50, 50
    sprite_width, sprite_height = 60, 60
    speed = 4
 
    # PART 3: Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 125, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
 
    current_color = WHITE
 
    clock = pygame.time.Clock()
    running = True
 
    # PART 4: Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        # PART 5: Check which arrow keys are held down
        pressed = pygame.key.get_pressed()
 
        if pressed[pygame.K_LEFT]:
            x -= speed
        if pressed[pygame.K_RIGHT]:
            x += speed
        if pressed[pygame.K_UP]:
            y -= speed
        if pressed[pygame.K_DOWN]:
            y += speed
 
        # PART 6: Keep the sprite inside the screen
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)
 
        # PART 7: Change color based on sprite position
        if x == 0:
            current_color = BLUE
        elif x == screen_width - sprite_width:
            current_color = YELLOW
        elif y == 0:
            current_color = RED
        elif y == screen_height - sprite_height:
            current_color = GREEN
        else:
            current_color = WHITE
 
        # PART 8: Draw the background
        screen.fill(BLACK)
 
        # PART 9: Draw solid and outlined shapes
        pygame.draw.circle(screen, GREEN, (420, 320), 35)
        pygame.draw.circle(screen, BLUE, (80, 320), 35, 4)
 
        # PART 10: Draw the moving sprite using pygame.Rect
        sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)
        pygame.draw.rect(screen, current_color, sprite_rect)
 
        pygame.display.flip()
        clock.tick(60)
 
    pygame.quit()
 
 
if __name__ == "__main__":
    main()