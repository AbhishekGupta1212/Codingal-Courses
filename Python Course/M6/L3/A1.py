# This activity, "Colorful Bounce," involves a moving rectangle (sprite) that bounces off the window edges. Each bounce changes its color and the window's background color, creating a dynamic display of colors.

# Step 1: Import pygame to build the game, and random to generate random colors, directions, and positions.

# Step 2: Initialize Pygame using pygame.init().

# Step 3: Create two custom event IDs, SPRITE_COLOR_CHANGE_EVENT and BACKGROUND_COLOR_CHANGE_EVENT, using pygame.USEREVENT + 1 and + 2.

# Step 4: Define background colors (BLUE, LIGHTBLUE, DARKBLUE) and sprite colors (YELLOW, MAGENTA, ORANGE, WHITE) using pygame.Color().

# Step 5: Create a Sprite class that inherits from pygame.sprite.Sprite.

# Step 6: In the constructor, call super().__init__(), then create self.image as a Surface, fill it with color, and create self.rect from it.

# Step 7: Give the sprite a random starting velocity using self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])].

# Step 8: Define an update() method that moves the sprite using self.rect.move_ip(self.velocity).

# Step 9: Inside update(), check whether the sprite has touched the left/right or top/bottom edges, and reverse the matching velocity value if so.

# Step 10: If a boundary was touched, post both SPRITE_COLOR_CHANGE_EVENT and BACKGROUND_COLOR_CHANGE_EVENT using pygame.event.post().

# Step 11: Define a change_color() method on the sprite that fills it with a random sprite color, and a change_background_color() function that picks a random background color.

# Step 12: Create a Group with all_sprites_list = pygame.sprite.Group(), create one Sprite named sp1 at a random position, and add it to the group.

# Step 13: Create the game window with set_mode((500, 400)), set its title with set_caption(), and fill it with the initial background color.

# Step 14: Start the main loop, checking pygame.QUIT to exit, and the two elif branches to handle the custom events.

# Step 15: Each pass, update and redraw every sprite in the group using all_sprites_list.update(), screen.fill(), and all_sprites_list.draw(screen), then refresh with flip() and limit speed with clock.tick(240).

# Step 16: When the loop ends, close Pygame using pygame.quit().


import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

  # Constructor method
  def __init__(self, color, height, width):
    # Call to the parent class (Sprite) constructor
    super().__init__()
    # Create the sprite's surface with dimensions and color
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    # Get the sprite's rect defining its position and size
    self.rect = self.image.get_rect()
    # Set initial velocity with random direction
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

  # Method to update the sprite's position
  def update(self):
    # Move the sprite by its velocity
    self.rect.move_ip(self.velocity)
    # Flag to track if the sprite hits a boundary
    boundary_hit = False
    # Check for collision with left or right boundaries and reverse direction
    if self.rect.left <= 0 or self.rect.right >= 500:
      self.velocity[0] = -self.velocity[0]
      boundary_hit = True
    # Check for collision with top or bottom boundaries and reverse direction
    if self.rect.top <= 0 or self.rect.bottom >= 400:
      self.velocity[1] = -self.velocity[1]
      boundary_hit = True

    # If a boundary was hit, post events to change colors
    if boundary_hit:
      pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
      pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

  # Method to change the sprite's color
  def change_color(self):
    self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


# Function to change the background color
def change_background_color():
  global bg_color
  bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)
# Randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
# Add the sprite to the group
all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption("Boundary Sprite")
# Set the initial background color
bg_color = BLUE
# Apply the background color
screen.fill(bg_color)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True
    # If the sprite color change event is triggered, change the sprite's color
    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.change_color()
    # If the background color change event is triggered, change the background color
    elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
      change_background_color()

  # Update all sprites
  all_sprites_list.update()
  # Fill the screen with the current background color
  screen.fill(bg_color)
  # Draw all sprites to the screen
  all_sprites_list.draw(screen)

  # Refresh the display
  pygame.display.flip()
  # Limit the frame rate to 240 fps
  clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()
