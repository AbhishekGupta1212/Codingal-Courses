# Write a program that detects when keys are pressed and changes the color of a sprite when it touches the screen boundaries.

# Step 1: Define a main() function, initialize pygame, and create a 500x500 window with a caption.

# Step 2: Store five named colors in a colors dictionary, and set current_color to white.

# Step 3: Set the sprite's starting x, y position and its width and height, then create a clock to control frame rate.

# Step 4: Start the main loop, checking pygame.event.get() for the pygame.QUIT event.

# Step 5: Call pygame.key.get_pressed() and use four if checks on the arrow keys to adjust x and y.

# Step 6: Clamp x and y with min() and max() so the sprite stays fully inside the screen.

# Step 7: Use an if/elif chain on x and y to set current_color whenever the sprite touches an edge.

# Step 8: Fill the screen black, draw the sprite rectangle in current_color, flip the display, and tick the clock.


import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')

    # Mapping of color names to RGB values
    colors = {
        'purple': pygame.Color('purple'),
        'pink': pygame.Color('pink'),
        'gray': pygame.Color('gray'),
        'cyan': pygame.Color('cyan'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Change color based on boundary contact
        if x == 0: current_color = colors['gray']
        elif x == screen_width - sprite_width: current_color = colors['cyan']
        elif y == 0: current_color = colors['purple']
        elif y == screen_height - sprite_height:
            current_color = colors['pink']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()
