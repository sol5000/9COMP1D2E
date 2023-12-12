import pygame
import sys
import math

# Initialize the game
def initialize_game():
    pygame.init()
    screen_width = 1080
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hollen's Game")
    clock = pygame.time.Clock()

    # Load game assets
    background_image = pygame.image.load("background.png")
    player_image = pygame.image.load("player.png")
    enemy_image = pygame.image.load("enemy.png")
    bullet_image = pygame.image.load("sword.png")
    ground_image = pygame.image.load("ground.png")

    ground_rect = ground_image.get_rect()
    ground_rect.y = 551
    ground_rect.width = screen_width

    return screen, clock, background_image, player_image, enemy_image, bullet_image, ground_image, ground_rect

# Game loop
def game_loop(screen, clock, background_image, player_image, enemy_image, bullet_image, ground_image, ground_rect):
    game_over = False

    player_x = 200
    player_y = 550 - player_image.get_height()
    player_speed = 5
    player_rect = player_image.get_rect()

    enemy_x = 800
    enemy_y = 550 - enemy_image.get_height()
    enemy_speed = 5
    enemy_rect = enemy_image.get_rect()

    player_bullets = []
    enemy_bullets = []

    player_gravity = 2.0
    enemy_gravity = 2.0

    is_jumping = False
    jump_count = 0
    max_jump_count = 1
    jump_cooldown = 30  # Set the cooldown in frames
    current_cooldown = 0  # Initialize the cooldown counter

    ground_image = pygame.transform.scale(ground_image, (screen.get_width(), ground_image.get_height()))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player_bullet = {
                        "x": player_x,
                        "y": player_y,
                        "state": "fire"
                    }
                    player_bullets.append(player_bullet)
                if event.key == pygame.K_DOWN:
                    enemy_bullet = {
                        "x": enemy_x,
                        "y": enemy_y,
                        "state": "fire"
                    }
                    enemy_bullets.append(enemy_bullet)
                if event.key == pygame.K_SPACE and not is_jumping and jump_count < max_jump_count and current_cooldown == 0:
                    is_jumping = True
                    jump_count += 1
                    current_cooldown = jump_cooldown

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not is_jumping:
            player_y -= player_speed

        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed

        if keys[pygame.K_d] and player_x < screen.get_width() - player_image.get_width():
            player_x += player_speed

        if keys[pygame.K_UP] and enemy_y > 0:
            enemy_y -= enemy_speed

        if keys[pygame.K_LEFT] and enemy_x > 0:
            enemy_x -= enemy_speed

        if keys[pygame.K_RIGHT] and enemy_x < screen.get_width() - enemy_image.get_width():
            enemy_x += enemy_speed

        player_y += player_gravity
        enemy_y += enemy_gravity

        player_rect.x = player_x
        player_rect.y = player_y
        enemy_rect.x = enemy_x
        enemy_rect.y = enemy_y

        if player_rect.colliderect(ground_rect):
            if keys[pygame.K_w] and not is_jumping:
                player_y += player_speed
            player_gravity = 0
            is_jumping = False
            jump_count = 0
            if current_cooldown == 0:
                current_cooldown = jump_cooldown  # Reset the cooldown when on the ground
        else:
            player_gravity = 2.0

        if enemy_rect.colliderect(ground_rect):
            enemy_gravity = 0
        else:
            enemy_gravity = 2.0

        for bullet in player_bullets:
            if bullet["state"] == "fire":
                bullet_x = bullet["x"]
                bullet_y = bullet["y"]
                enemy_center_x = enemy_x + enemy_image.get_width() / 2
                enemy_center_y = enemy_y + enemy_image.get_height() / 2
                direction_x = enemy_center_x - bullet_x
                direction_y = enemy_center_y - bullet_y
                distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
                direction_x /= distance
                direction_y /= distance
                bullet_speed = 10
                bullet_x += direction_x * bullet_speed
                bullet_y += direction_y * bullet_speed
                bullet["x"] = bullet_x
                bullet["y"] = bullet_y
                if bullet["y"] <= 0:
                    bullet["state"] = "ready"
                elif enemy_rect.collidepoint(bullet_x, bullet_y):
                    bullet["state"] = "ready"

        for bullet in enemy_bullets:
            if bullet["state"] == "fire":
                bullet_x = bullet["x"]
                bullet_y = bullet["y"]
                player_center_x = player_x + player_image.get_width() / 2
                player_center_y = player_y + player_image.get_height() / 2
                direction_x = player_center_x - bullet_x
                direction_y = player_center_y - bullet_y
                distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
                direction_x /= distance
                direction_y /= distance
                bullet_speed = 10
                bullet_x += direction_x * bullet_speed
                bullet_y += direction_y * bullet_speed
                bullet["x"] = bullet_x
                bullet["y"] = bullet_y
                if bullet["y"] <= 0:
                    bullet["state"] = "ready"
                elif player_rect.collidepoint(bullet_x, bullet_y):
                    bullet["state"] = "ready"
                    bullet["state"] = "ready" 

        # Handle jumping cooldown
        if current_cooldown > 0:
            current_cooldown -= 1

        # Render the game
        screen.blit(background_image, (0, 0))
        screen.blit(ground_image, (0, 500))
        screen.blit(player_image, (player_x, player_y))
        screen.blit(enemy_image, (enemy_x, enemy_y))
        for bullet in player_bullets:
            if bullet["state"] == "fire":
                screen.blit(bullet_image, (bullet["x"], bullet["y"]))
        for bullet in enemy_bullets:
            if bullet["state"] == "fire":
                screen.blit(bullet_image, (bullet["x"], bullet["y"]))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Start the game
screen, clock, background_image, player_image, enemy_image, bullet_image, ground_image, ground_rect = initialize_game()
game_loop(screen, clock, background_image, player_image, enemy_image, bullet_image, ground_image, ground_rect)
