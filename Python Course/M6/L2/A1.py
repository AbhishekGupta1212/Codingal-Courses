import pygame 

# Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.

# Step 1: Import pygame and call pygame.init() to start it up.

# Step 2: Create a 400x300 display window using pygame.display.set_mode() and store it in screen.

# Step 3: Set done to False to control the main loop.

# Step 4: Start a while not done loop that keeps the window open.

# Step 5: Inside the loop, check every event with pygame.event.get(), setting done to True if the event type is pygame.QUIT.

# Step 6: Draw a rectangle on screen using pygame.draw.rect(), the color (0, 125, 255), and pygame.Rect(30, 30, 60, 60).

# Step 7: Call pygame.display.flip() to show the rectangle on the window.

pygame.init()  
screen = pygame.display.set_mode((400, 300))  
done = False  
  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))    
  
    pygame.display.flip()  