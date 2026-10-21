"""
A rectangle sprite bounces around the window. Every time it hits an edge,
a custom pygame event is posted, which the game loop handles by picking
new random colors for both the sprite and the background.

Demonstrates:
1. Custom Sprite class (pygame.sprite.Sprite)
2. image / rect / velocity on a sprite
3. pygame.sprite.Group()
4. Custom events via pygame.USEREVENT
5. Posting custom events with pygame.event.post()
8. Handling custom events in the game loop
"""

import random
import pygame

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bounce")
clock = pygame.time.Clock()

RECT_SIZE = 60
SPEED = 5

# 4. Custom event: fired whenever the rectangle bounces off an edge
BOUNCE_EVENT = pygame.USEREVENT + 1


def random_color():
    return (random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))


# ---------------------------------------------------------------------------
# 1 & 2. Sprite class with image, rect, and velocity
# ---------------------------------------------------------------------------
class BouncingRect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = random_color()
        self.image = pygame.Surface((RECT_SIZE, RECT_SIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.velocity = pygame.Vector2(
            random.choice([-1, 1]) * SPEED,
            random.choice([-1, 1]) * SPEED,
        )

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        bounced = False

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity.x *= -1
            bounced = True

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.velocity.y *= -1
            bounced = True

        # keep the rect fully inside the window after reversing direction
        self.rect.clamp_ip(screen.get_rect())

        # 5. Post a custom event whenever a bounce happens
        if bounced:
            pygame.event.post(pygame.event.Event(BOUNCE_EVENT))

    def set_color(self, color):
        self.color = color
        self.image.fill(color)


# ---------------------------------------------------------------------------
# 3. Group the sprite(s) together
# ---------------------------------------------------------------------------
all_sprites = pygame.sprite.Group()
player_rect = BouncingRect()
all_sprites.add(player_rect)

bg_color = (10, 10, 30)

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
running = True
while running:
    # 8. Handle events, including our custom one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == BOUNCE_EVENT:
            bg_color = random_color()
            player_rect.set_color(random_color())

    all_sprites.update()

    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()