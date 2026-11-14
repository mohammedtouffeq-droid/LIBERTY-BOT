import time
import random

try:
    import pygame
    PYGAME_READY = True
except ImportError:
    PYGAME_READY = False


class RobotFace:
    def __init__(self, width=480, height=320):
        self.width = width
        self.height = height
        self.state = "idle"
        self.last_blink = time.time()
        self.blinking = False

        if PYGAME_READY:
            pygame.init()
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Liberty-Bot Face")
            self.clock = pygame.time.Clock()
        else:
            self.screen = None

    def set_expression(self, mood):
        self.state = mood

    def draw_frame(self):
        if not PYGAME_READY or not self.screen:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        self.screen.fill((10, 14, 24))
        eye_color = (0, 225, 255)

        now = time.time()
        if not self.blinking and (now - self.last_blink) > random.uniform(3.0, 6.0):
            self.blinking = True
            self.last_blink = now
        elif self.blinking and (now - self.last_blink) > 0.14:
            self.blinking = False
            self.last_blink = now

        left_x = self.width // 2 - 110
        right_x = self.width // 2 + 20
        eye_y = self.height // 2 - 45
        eye_w = 90
        eye_h = 90

        if self.blinking:
            pygame.draw.rect(self.screen, eye_color, (left_x, eye_y + 40, eye_w, 10), border_radius=5)
            pygame.draw.rect(self.screen, eye_color, (right_x, eye_y + 40, eye_w, 10), border_radius=5)
        elif self.state == "happy":
            pygame.draw.rect(self.screen, eye_color, (left_x, eye_y + 15, eye_w, 55), border_radius=25)
            pygame.draw.rect(self.screen, eye_color, (right_x, eye_y + 15, eye_w, 55), border_radius=25)
            pygame.draw.rect(self.screen, (10, 14, 24), (left_x, eye_y + 45, eye_w, 40))
            pygame.draw.rect(self.screen, (10, 14, 24), (right_x, eye_y + 45, eye_w, 40))
        elif self.state == "thinking":
            offset = int((now * 8) % 20) - 10
            pygame.draw.rect(self.screen, eye_color, (left_x + offset, eye_y + 20, eye_w, 50), border_radius=14)
            pygame.draw.rect(self.screen, eye_color, (right_x + offset, eye_y + 10, eye_w, 65), border_radius=14)
        else:
            pygame.draw.rect(self.screen, eye_color, (left_x, eye_y, eye_w, eye_h), border_radius=20)
            pygame.draw.rect(self.screen, eye_color, (right_x, eye_y, eye_w, eye_h), border_radius=20)

        pygame.display.flip()
        self.clock.tick(30)
