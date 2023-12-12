import pygame
from pygame.locals import *
from pygame.locals import *

import numpy as np

class Sprite:
    def __init__(self, file=None, pos=(0, 0), size=None):
        self.parent = None
        self.size = size
        self.rect = Rect(pos, (20, 20))
        self.position = np.array(pos, dtype=float)
        self.velocity = np.array([1.5, 0.5], dtype=float)

        self.angle = 0
        self.angular_velocity = 0

        self.color = 'red'
        self.speed = [0, 0]
        if file:
            self.image = pygame.image.load(file)
            if self.size:
                self.image = pygame.transform.scale(self.image, size)
                self.rect.size = self.image.get_size()
        else:
            self.image = pygame.Surface(self.rect.size)
            self.image.fill(self.color)
        self.image0 = self.image.copy()

    def set_pos(self, pos):
        self.position = np.array(pos, dtype=float)
        self.rect.center = pos
 
    def set_angle(self, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.image0, self.angle)
        self.rect.size = self.image.get_size()

    def do(self, event):
        pass

    def update(self):
        self.move()

    def move(self):
        self.position += self.velocity

        if self.angular_velocity:
            self.angle += self.angular_velocity
            self.image = pygame.transform.rotate(self.image0, self.angle)
            self.rect.size = self.image.get_size()

        self.rect.center = self.position
    
    def draw(self, surf):
        class Brick(Sprite):
            def __init__(self, pos, size):
                super().__init__(None, pos, size)
                self.color = 'blue'
                self.image.fill(self.color)

            def hit(self):
                self.parent.remove(self)


        class Ball(Sprite):
            def __init__(self, pos, size):
                super().__init__(None, pos, size)
                self.color = 'white'
                self.image.fill(self.color)
                self.velocity = np.array([2, -2], dtype=float)

            def update(self):
                self.move()
                if self.rect.left < 0 or self.rect.right > self.parent.rect.right:
                    self.velocity[0] = -self.velocity[0]
                if self.rect.top < 0:
                    self.velocity[1] = -self.velocity[1]
                if self.rect.bottom > self.parent.rect.bottom:
                    self.parent.game_over()

        class Sprite(pygame.sprite.Sprite):
            def __init__(self, image, pos, size):
                super().__init__()
                self.image0 = pygame.Surface(size)
                self.image0.fill('white')
                self.rect = self.image0.get_rect()
                self.position = pos.copy()
                self.velocity = [0, 0]
                self.angular_velocity = 0
                self.angle = 0
                if image:
                    self.load_image(image)

            def load_image(self, image):
                self.image0 = pygame.image.load(image).convert_alpha()
                self.rect = self.image0.get_rect()

            def move(self):
                self.position[0] += self.velocity[0]

class Ball(Sprite):
    def __init__(self, pos, size):
        super().__init__(None, pos, size)
        self.image0 = pygame.Surface(size)
        self.image0.fill('white')
        pygame.draw.ellipse(self.image0, 'red', self.image0.get_rect())
        self.image = self.image0
        self.rect = self.image.get_rect()
        self.velocity = [5, -5]
        self.angular_velocity = 0

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def update(self):
        self.move()
        if self.angular_velocity:
            self.angle += self.angular_velocity
            self.image = pygame.transform.rotate(self.image0, self.angle)
            self.rect.size = self.image.get_size()

        self.rect.center = self.position

    def collide(self, other):
        if self.rect.colliderect(other.rect):
            if self.rect.center[1] < other.rect.top or self.rect.center[1] > other.rect.bottom:
                self.velocity[1] = -self.velocity[1]
            else:
                self.velocity[0] = -self.velocity[0]
            return True
        return False


class Paddle(Sprite):
    def __init__(self, pos, size):
        super().__init__(None, pos, size)
        self.image = pygame.Surface(size)
        self.image.fill('white')
        pygame.draw.rect(self.image, 'green', self.image.get_rect(), 2)
        self.rect = self.image.get_rect()
        self.position = pos
        self.rect.center = self.position
        self.speed = 5

    def move(self):
        self.position[0] += self.speed
        self.rect.center = self.position

    def update(self):
           self.move()
class Ball(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
    self.image0 = pygame.Surface(size)
    self.image0.fill('white')
    pygame.draw.ellipse(self.image0, 'red', self.image0.get_rect())
    self.image = self.image0
    self.rect = self.image.get_rect()
    self.position = position
    self.rect.center = self.position
    self.velocity = [5, -5]
    self.angular_velocity = 0

                            def move(self):
                                self.position[0] += self.velocity[0]
                                self.position[1] += self.velocity[1]

                            def collide(self, other):
                                return self.rect.colliderect(other.rect)

                            def update(self):
                                self.move()
                                if self.rect.left < 0 or self.rect.right > self.parent.rect.right:
                                    self.velocity[0] = -self.velocity[0]
                                if self.rect.top < 0:
                                    self.velocity[1] = -self.velocity[1]
                                elif self.rect.bottom > self.parent.rect.bottom:
                                    self.parent.game_over()

                                if self.angular_velocity:
                                    self.angle += self.angular_velocity
                                    self.image = pygame.transform.rotate(self.image0, self.angle)
                                    self.rect.size = self.image.get_size()

                                self.rect.center = self.position

                        class Brick(pygame.sprite.Sprite):
                            def __init__(self, position, size):
                                super().__init__()
                                self.image = pygame.Surface(size)
                                self.image.fill('white')
                                pygame.draw.rect(self.image, 'blue', self.image.get_rect(), 2)
                                self.rect = self.image.get_rect()
                                self.position = position
                                self.rect.center = self.position
                                self.hits = 0

                            def hit(self):
                                self.hits += 1
                                if self.hits == 1:
                                    self.image.fill('yellow')
                                elif self.hits == 2:
                                    self.image.fill('orange')
                                elif self.hits == 3:
                                    self.kill()

                        class Paddle(pygame.sprite.Sprite):
                            def __init__(self, position, size):
                                super().__init__()
                                self.image = pygame.Surface(size)
                                self.image.fill('white')
                                pygame.draw.rect(self.image, 'green', self.image.get_rect(), 2)
                                self.rect = self.image.get_rect()
                                self.position = position
                                self.rect.center = self.position
                                self.speed = 5

                            def move(self):
                                self.position[0] += self.speed
                                self.rect.center = self.position

                            def update(self):
                                self.move()
                                import pygame
                                from pygame.locals import (
                                    K_SPACE,
                                    K_a,
                                    K_b,
                                    QUIT,
                                    KEYDOWN,
                                    RESIZABLE,
                                )


                                class Ball:
                                    def __init__(self, position, size):
                                        self.position = position
                                        self.velocity = [0, 0]
                                        self.size = size
                                        self.color = 'white'
                                        self.angular_velocity = 0
                                        self.angle = 0
                                        self.image0 = pygame.Surface(self.size)
                                        self.image0.fill(self.color)
                                        self.image0.set_colorkey('black')
                                        pygame.draw.ellipse(self.image0, self.color, self.image0.get_rect())
                                        self.image = self.image0
                                        self.rect = self.image.get_rect()
                                        self.rect.center = self.position

                                    def update(self):
                                        self.position[0] += self.velocity[0]
                                        self.position[1] += self.velocity[1]

                                        if self.rect.left < 0:
                                            self.velocity[0] = -self.velocity[0]
                                        elif self.rect.right > self.parent.rect.right:
                                            self.velocity[0] = -self.velocity[0]

                                        if self.rect.top < 0:
                                            self.velocity[1] = -self.velocity[1]
                                        elif self.rect.bottom > self.parent.rect.bottom:
                                            self.velocity[1] = -self.velocity[1]
                                            self.game_over()

                                        if self.angular_velocity:
                                            self.angle += self.angular_velocity
                                            self.image = pygame.transform.rotate(self.image0, self.angle)
                                            self.rect.size = self.image.get_size()

                                        self.rect.center = self.position

                                    def collide(self, other):
                                        return self.rect.colliderect(other.rect)


                                class Brick:
                                    def __init__(self, position, size):
                                        self.position = position
                                        self.size = size
                                        self.color = 'red'
                                        self.image = pygame.Surface(self.size)
                                        self.image.fill(self.color)
                                        self.rect = self.image.get_rect()
                                        self.rect.center = self.position
                                        self.hits = 1

                                    def hit(self):
                                        self.hits -= 1
                                        if self.hits == 0:
                                            self.parent.remove(self)

                                    def update(self):
                                        pass

                                    def draw(self, surf):
                                        surf.blit(self.image, self.rect)


                                class Paddle:
                                    def __init__(self, position, size):
                                        self.position = position
                                        self.size = size
                                        self.color = 'white'
                                        self.image = pygame.Surface(self.size)
                                        self.image.fill(self.color)
                                        self.rect = self.image.get_rect()
                                        self.rect.center = self.position
                                        self.velocity = [0, 0]

                                    def update(self):
                                        self.position[0] += self.velocity[0]
                                        self.position[1] += self.velocity[1]

                                        if self.rect.left < 0:
                                            self.rect.left = 0
                                        elif self.rect.right > self.parent.rect.right:
                                            self.rect.right = self.parent.rect.right

                                        if self.angular_velocity:
                                            self.angle += self.angular_velocity
                                            self.image = pygame.transform.rotate(self.image0, self.angle)
                                            self.rect.size = self.image.get_size()

                                        self.rect.center = self.position

                                    def draw(self, surf):
                                        surf.blit(self.image, self.rect)


                                class App:
                                    def __init__(self, file=None, caption='Pygame'):
                                        pygame.init()
                                        pygame.display.set_caption(caption)
                                        self.flags = RESIZABLE
                                        self.size = (640, 480)
                                        self.screen = pygame.display.set_mode(self.size, self.flags)
                                        self.running = True
                                        self.updating = True
                                        self.objects = []
                                        self.bg_color = 'black'
                                        if file:
                                            self.load_image(file)
                                        else:
                                            self.image = pygame.Surface(self.size)
                                            self.image.fill(self.bg_color)
                                            self.rect = self.image.get_rect()
                                        self.key_cmd = {}

                                    def load_image(self, file):
                                        self.image = pygame.image.load(file).convert()
                                        self.rect = self.image.get_rect()
                                        self.screen = pygame.display.set_mode(self.rect.size, self.flags)

                                    def run(self):
                                        while self.running:
                                            for event in pygame.event.get():
                                                self.do(event)
                                            self.update()
                                            self.draw()

                                    def add_cmd(self, key, cmd):
                                        self.key_cmd[key] = cmd
                                        print(self.key_cmd)

                                    def add(self, obj):
                                        self.objects.append(obj)
                                        obj.parent = self

                                    def remove(self, obj):
                                        self.objects.remove(obj)

                                    def do(self, event):
                                        if event.type == QUIT:
                                            self.running = False
                                            pygame.quit()
                                        elif event.type == KEYDOWN:
                                            if event.key == K_SPACE:
                                                self.updating = not self.updating

                                            if event.key in self.key_cmd:
                                                cmd = self.key_cmd[event.key]
                                                eval(cmd)

                                        for obj in self.objects:
                                            obj.do(event)

                                    def update(self):
                                        if self.updating:
                                            for obj in self.objects:
                                                obj.update()

                                            for ball in (obj for obj in self.objects if isinstance(obj, Ball)):
                                                for brick in (obj for obj in self.objects if isinstance(obj, Brick)):
                                                    if ball.collide(brick):
                                                        brick.hit()

                                                for paddle in (obj for obj in self.objects if isinstance(obj, Paddle)):
                                                    if ball.collide(paddle):
                                                        ball.velocity[1] = -ball.velocity[1]

                                    def draw(self):
                                        self.screen.blit(self.image, self.rect)
                                        for obj in self.objects:
                                            obj.draw(self.screen)
                                        pygame.display.update()

                                    def game_over(self):
                                        self.running = False
                                        print('Game over')


                                if __name__ == '__main__':
                                    app = App('space.png', 'Atari Breakout')

                                    paddle = Paddle((320, 460), (100, 20))
                                    app.add(paddle)

                                    for i in range(10):
                                        for j in range(5):
                                            brick = Brick((i * 64 + 32, j * 32 + 32), (60, 20))
                                            app.add(brick)

                                    ball = Ball((320, 240), (20, 20))
                                    app.add(ball)

                                    app.add_cmd(K_a, 'print(123)')
                                    app.add_cmd(K_b, "self.load_image('space.png')")
                                    app.run()
