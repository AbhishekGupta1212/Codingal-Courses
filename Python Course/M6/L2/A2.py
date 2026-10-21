# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.


# Step 1: Import pygame and call pygame.init() to start it up.

# Step 2: Create a 400x400 display window using pygame.display.set_mode() and store it in window.

# Step 3: Fill the window with white using window.fill((255, 255, 255)).

# Step 4: Store the color green in a variable named GREEN.

# Step 5: Draw a solid circle with pygame.draw.circle(window, GREEN, (300, 300), 50).

# Step 6: Draw a hollow circle with pygame.draw.circle(window, GREEN, (100, 100), 50, 3), using width 3 for the outline.

# Step 7: Call pygame.display.update() to show both circles, then run an event loop that quits when the window closes.


import pygame

pygame.init()
# Create the display surface object of specific dimension.
window = pygame.display.set_mode((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
GREEN = (0, 255, 0)
# Draw solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)
# Draw outlined circle
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
# Draws the surface object to the screen.
pygame.display.update()
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()