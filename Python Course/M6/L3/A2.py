# You will build a Smart Traffic Signal Simulator using Python and Pygame. You will create a moving car as a sprite, store it inside a sprite group, make it move with a velocity, and use custom events to change the car colour and traffic signal whenever the car reaches a road boundary.

# Step 1: Import and Initialize Pygame Create a new Python file. Import pygame and random, then call pygame.init().

# Step 2: Create the Custom Event IDs Use pygame.USEREVENT + 1 and pygame.USEREVENT + 2 to create separate events for changing the car and signal colours.

# Step 3: Define the Colours Create road, car, and traffic-light colours using pygame.Color().

# Step 4: Create the Car Sprite Class Define Car as a child of pygame.sprite.Sprite. Call super().__init__() inside the constructor.

# Step 5: Give the Car an Image, Rect, and Velocity Create the car surface with pygame.Surface(), store its position with get_rect(), and set a horizontal velocity.

# Step 6: Move the Car and Detect Boundaries Inside update(), move the Rect with move_ip(). Reverse the horizontal velocity when the car touches the left or right edge.

# Step 7: Post the Custom Events When a road boundary is reached, use pygame.event.post() to add the car-colour and signal-change events to the event queue.

# Step 8: Create and Use the Sprite Group Create pygame.sprite.Group(), add the car, then call update() and draw() on the group inside the game loop.

# Step 9: Handle Custom Events in the Game Loop Check event.type for the two custom event IDs. Change the car colour and switch the signal between red and green.

# Step 10: Draw and Test the Simulator Draw the road, divider lines, traffic signal, and car. Run the program and observe the colour changes at the screen boundaries.



# Smart Traffic Signal Simulator
 
# Import necessary libraries
import pygame
import random
 
# Initialize Pygame
pygame.init()
 
# Custom event IDs
CAR_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
SIGNAL_CHANGE_EVENT = pygame.USEREVENT + 2
 
# Define colours
ROAD = pygame.Color("darkgray")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
BLUE = pygame.Color("blue")
ORANGE = pygame.Color("orange")
 
RED = pygame.Color("red")
GREEN = pygame.Color("green")
 
 
# Create a Car sprite class
class Car(pygame.sprite.Sprite):
 
    # Constructor method
    def __init__(self, color, width, height):
        # Call the parent Sprite constructor
        super().__init__()
 
        # Give the car an image
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Give the car a rectangular position
        self.rect = self.image.get_rect()
 
        # Give the car a horizontal velocity
        self.velocity = [3, 0]
 
    # Update the car's position
    def update(self):
        # Move the car using its velocity
        self.rect.move_ip(self.velocity)
 
        sensor_triggered = False
 
        # Check whether the car reaches either road boundary
        if self.rect.left <= 0 or self.rect.right >= 600:
            # Reverse the car's direction
            self.velocity[0] = -self.velocity[0]
 
            sensor_triggered = True
 
        # Post custom events when a boundary sensor is triggered
        if sensor_triggered:
            pygame.event.post(
                pygame.event.Event(CAR_COLOR_CHANGE_EVENT)
            )
 
            pygame.event.post(
                pygame.event.Event(SIGNAL_CHANGE_EVENT)
            )
 
    # Change the car's colour
    def change_color(self):
        self.image.fill(
            random.choice([WHITE, YELLOW, BLUE, ORANGE])
        )
 
 
# Function to change the traffic signal
def change_signal():
    global signal_color
 
    # Switch between red and green
    if signal_color == RED:
        signal_color = GREEN
    else:
        signal_color = RED
 
 
# Create a sprite group
all_sprites = pygame.sprite.Group()
 
# Create the car sprite
car = Car(WHITE, 70, 35)
 
# Position the car on the road
car.rect.x = 50
car.rect.y = 300
 
# Add the car to the sprite group
all_sprites.add(car)
 
# Create the game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Smart Traffic Signal Simulator")
 
# Set the starting signal colour
signal_color = RED
 
# Create a clock to control the frame rate
clock = pygame.time.Clock()
 
# Control the game loop
running = True
 
while running:
 
    # Handle events
    for event in pygame.event.get():
 
        # Close the application
        if event.type == pygame.QUIT:
            running = False
 
        # Handle the custom car colour event
        elif event.type == CAR_COLOR_CHANGE_EVENT:
            car.change_color()
 
        # Handle the custom traffic signal event
        elif event.type == SIGNAL_CHANGE_EVENT:
            change_signal()
 
    # Update all sprites in the group
    all_sprites.update()
 
    # Draw the road background
    screen.fill(ROAD)
 
    # Draw road divider lines
    for x in range(0, 600, 80):
        pygame.draw.rect(
            screen,
            WHITE,
            (x, 345, 45, 5)
        )
 
    # Draw the traffic-signal box
    pygame.draw.rect(
        screen,
        pygame.Color("black"),
        (275, 40, 50, 90)
    )
 
    # Draw the active traffic-signal light
    pygame.draw.circle(
        screen,
        signal_color,
        (300, 85),
        20
    )
 
    # Draw all sprites
    all_sprites.draw(screen)
 
    # Refresh the display
    pygame.display.flip()
 
    # Limit the frame rate
    clock.tick(60)
 
# Close Pygame
pygame.quit()
