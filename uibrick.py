import pygame
#  막대 및 벽돌 클래스
class Block(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img.convert_alpha()
        self.image2 = None
        self.image3 = None
        self.rect = img.get_rect()
        self.life = 3

    def add_image(self, img2, img3):
        self.image2 = img2
        self.image3 = img3


# 농구공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img.convert_alpha()
        self.rect = img.get_rect()
        self.mask = pygame.mask.from_surface(img)
        self.velx = 0.0
        self.vely = 0.0
        # self.radius = 20
        # self.speed = random.randint(10, 16)