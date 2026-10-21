# You will build a Wildlife Information Display using Python and Pygame. You will create a display window, load a background and wildlife image, scale and position the images, render a heading and wildlife fact, keep the application running with a game loop, and control its frame rate.

# Step 1: Prepare the Project Files Create a new Python file. Save background.png and tiger.png in the same folder as the program.

# Step 2: Import and Initialize Pygame Import pygame and call pygame.init() so the required Pygame modules are ready to use.

# Step 3: Create the Display Window Set the screen width and height to 500. Use pygame.display.set_mode() to create the window and set its caption.

# Step 4: Load and Scale the Images Load background.png and tiger.png with pygame.image.load(). Use pygame.transform.scale() to resize them.

# Step 5: Position the Wildlife Image Use get_rect(center=...) to place the tiger near the centre of the screen.

# Step 6: Create and Render the Text Create two Font objects. Use render() to make the heading and fact surfaces, then position them with get_rect().

# Step 7: Create the Game Loop Define game_loop(). Use a while loop and pygame.event.get() so the application stays open until the close button is clicked.

# Step 8: Draw Everything on the Screen Use blit() to draw the background, tiger image, heading, and fact. Call pygame.display.flip() to show the completed frame.

# Step 9: Control the Frame Rate Create pygame.time.Clock() and call clock.tick(30) once per loop to limit the application to 30 frames per second.

# Step 10: Run and Test the Application Run the program. Confirm that both images and both text lines appear and that the window closes correctly.




# Wildlife Information Display
 
# Import necessary library
import pygame
 
# Initialize Pygame
pygame.init()
 
# Set screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
 
# Create the display window
display_surface = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
 
# Set the window title
pygame.display.set_caption(
    "Wildlife Information Display"
)
 
# Load and scale the background image
background_image = pygame.transform.scale(
    pygame.image.load("wildlife_background.webp").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
 
# Load and scale the wildlife image
wildlife_image = pygame.transform.scale(
    pygame.image.load("tiger.webp").convert_alpha(),
    (220, 220)
)
 
# Position the wildlife image at the centre
wildlife_rect = wildlife_image.get_rect(
    center=(
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2 - 30
    )
)
 
# Create fonts for the heading and information
heading_font = pygame.font.Font(None, 42)
fact_font = pygame.font.Font(None, 28)
 
# Render the heading text
heading_text = heading_font.render(
    "Wildlife Spotlight: Tiger",
    True,
    pygame.Color("white")
)
 
# Position the heading
heading_rect = heading_text.get_rect(
    center=(SCREEN_WIDTH // 2, 45)
)
 
# Render the wildlife fact
fact_text = fact_font.render(
    "Tigers are powerful wild cats.",
    True,
    pygame.Color("white")
)
 
# Position the fact text
fact_rect = fact_text.get_rect(
    center=(SCREEN_WIDTH // 2, 420)
)
 
 
# Main game loop
def game_loop():
    # Create a clock to control the frame rate
    clock = pygame.time.Clock()
 
    running = True
 
    while running:
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        # Draw the background
        display_surface.blit(
            background_image,
            (0, 0)
        )
 
        # Draw the wildlife image
        display_surface.blit(
            wildlife_image,
            wildlife_rect
        )
 
        # Display the heading and fact
        display_surface.blit(
            heading_text,
            heading_rect
        )
 
        display_surface.blit(
            fact_text,
            fact_rect
        )
 
        # Update the screen
        pygame.display.flip()
 
        # Limit the game to 30 frames per second
        clock.tick(30)
 
    # Close Pygame
    pygame.quit()
 
 
# Run the application
if __name__ == "__main__":
    game_loop()
