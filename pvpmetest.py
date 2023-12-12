import pygame
from pygame.sprite import Group, Sprite

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Game constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Player class
class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = 0
        self.vel_y = 0
        self.jumping = False
        self.health = 100
        self.ammo = 30
        self.weapon = "pistol"
        self.frame = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0

        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.vel_y = -15

        if keys[pygame.K_RETURN]:  # Press Enter to shoot
            self.shoot()

        self.vel_y += 1

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.die()

        self.frame += 1
        if self.frame % 10 == 0:
            self.image.fill(RED if self.frame % 20 < 10 else BLUE)

    def shoot(self):
        if self.ammo > 0:
            projectile = Projectile(self.rect.centerx, self.rect.centery, "right")
            projectiles.add(projectile)
            self.ammo -= 1

    def die(self):
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - 50
        self.vel_x = 0
        self.vel_y = 0
        self.health = 100
        self.ammo = 30

# Enemy class
class Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = 2

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vel_x = -self.vel_x

# Projectile class
class Projectile(Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction  # "left" or "right"
        self.speed = 8

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

# Platform class
class Platform(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

# Game initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Complex Pygame Shooter")
clock = pygame.time.Clock()

# Create game objects
player = Player(WIDTH // 2, HEIGHT - 50)
platforms = Group()
enemies = Group()
projectiles = Group()

# Create a platform at the bottom of the screen
platform = Platform(0, HEIGHT - 20, WIDTH, 20)
platforms.add(platform)

# Create an enemy
enemy = Enemy(WIDTH // 4, HEIGHT - 50)
enemies.add(enemy)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    # Check collisions with platforms
    if pygame.sprite.spritecollide(player, platforms, False):
        player.jumping = False
        player.rect.y -= player.vel_y
        player.vel_y = 0

    # Update and draw enemies
    enemies.update()
    for enemy in enemies:
        if pygame.sprite.collide_rect(player, enemy):
            player.die()
        screen.blit(enemy.image, enemy.rect.topleft)

    # Update and draw projectiles
    projectiles.update()
    for projectile in projectiles:
        if pygame.sprite.spritecollide(projectile, platforms, False):
            projectiles.remove(projectile)
        else:
            screen.blit(projectile.image, projectile.rect.topleft)

    # Draw everything on the screen
    screen.fill(BLACK)
    platforms.draw(screen)
    screen.blit(player.image, player.rect.topleft)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
