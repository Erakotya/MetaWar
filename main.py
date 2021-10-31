import pygame
import random
import math
from pygame import mixer
import pygame, sys
from camera import Auto
import time
import threading


pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
pygame.init()
clock = pygame.time.Clock()
#colors
BLACK = (0,0,0)
RED = (255,0,0)
Green = (0,255,0)
WHITE = (100,100,100)
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Meta-War")
#background = pygame.image.load("space.jpg")



meteor_img = pygame.image.load("meteor.png")
#background sound

font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 16)



def draw_text(text,font,color,surface,x,y,location):
    textobj = font.render(text,1, color)
    textrect = textobj.get_rect()
    if location == 1:
        textrect.center = (x,y)
        surface.blit(textobj,textrect)
    if location == 2:
        textrect.midleft = (x, y)
        surface.blit(textobj, textrect)

def loading():
    list = [".","..","..."]
    for n in range(5):
        box = pygame.Rect(150, 300, 200, 40)
        pygame.draw.rect(screen, (0, 0, 0), box)
        draw_text("Loading", font, (255, 255, 255), screen, 180.5, 300, 2)
        for i in list:
            draw_text(i, font, (255, 255, 255), screen, 308.5, 300,2)
            pygame.time.delay(300)
            pygame.display.update()



#screenfades out as a transition to the next screen
def fadeout(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)



pygame.mixer.init(4096, -16, 2, 64)
#main menu screen
def main_menu():
   pygame.mixer.music.load("song.mp3")
   pygame.mixer.music.play(-1)
   click = False
   running = True

   class time_click():
       variable = 0

        #creates a click sound when mouse hovers over button
       def check(self):
           if button_1.collidepoint(mx, my):
               explosion_sound = mixer.Sound("tap.wav")
               self.__class__.variable += 1
               explosion_sound.play(0)
               if self.__class__.variable >1:
                   explosion_sound.stop()
           if not button_1.collidepoint(mx, my):
               self.__class__.variable = 0


   aha = 0
   while running:

       screen.fill((0,0,0))
       background = pygame.image.load("space.jpg")
       screen.blit(background,(0,0))
       draw_text("main menu", font, (255,255,255), screen, 250,50,1)
       mx,my = pygame.mouse.get_pos()

       button_1 = pygame.Rect(160,247,180,46)          #clear rectangle with coordinate points, length & width
       button_2 = pygame.Rect(135, 347, 230, 46)

       if button_1.collidepoint(mx,my):
           if click:
               pygame.mixer.music.fadeout(1500)
               fadeout(800,600)
               game()
       if button_2.collidepoint(mx,my):
           if click:
               pygame.mixer.music.fadeout(1500)
               fadeout(800,600)
               instructions()




       if button_1.collidepoint(mx,my) or button_2.collidepoint(mx,my) :
           tap = mixer.Sound("taps.wav")
           aha += 1
           tap.play(0)
           if aha > 1:
               tap.stop()
       else:
           aha = 0



       pygame.draw.rect(screen,(0,0,255),button_1)      #u fill up the rectangle on the screen, color, and specify which rectangle
       draw_text("Play", font, (255, 255, 255), screen, 250, 270,1)

       pygame.draw.rect(screen,(0,0,255),button_2)
       draw_text("Instruction", font, (255, 255, 255), screen, 250, 370,1)

       click = False
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:
                  click = True

       pygame.display.update()

def instructions():
    paragraph = ["Welcome Captain!"," Here you will find how to navigate the game.","Your goal is to destroy as many meteors as possible.","To move, use the |W|, |A|, |D|, |S| keys."," Use you |SPACE| button to shoot."," Now, beware, after 8 shots you will need to reload."," To reload at any time press the |R| key,","and you will receive a fresh set of ammo."," If you wish to exit to the main menu, press the |ESC| key.","Good Luck, and may the power be with you, Captain!"]
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(-1)
    background = pygame.image.load("space.jpg")
    screen.blit(background, (0, 0))
    InstructionsFont = font
    y=70
    for line in paragraph:                                                     #prints the instruction line by line while changing the Y orientation value
        draw_text(line, font2, (255, 255, 255), screen, 250, y, 1)
        y+=20

    while True:
        #screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()


        pygame.display.update()


def game():
    level = 1
    hits_record = 0
    class Square1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((166, 50))
            self.image.set_colorkey(BLACK)
            #self.image.fill(Green)
            self.rect = self.image.get_rect()
            self.rect.topleft = (0,540)



    class Square2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((155, 50))
            #self.image.fill(RED)
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.topleft = (166,540)


    class Square3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((166, 50))
            self.image.set_colorkey(BLACK)
            #self.image.fill(Green)
            self.rect = self.image.get_rect()
            self.rect.topleft = (321,510)


    class GiantSpaceship(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("spaceshipGiant.png")
            self.image = pygame.transform.scale(self.image, (900, 300))
            self.rect = self.image.get_rect()
            self.x = 250
            self.y = 650
            self.rect.center = (self.x,self.y)
            self.timer = pygame.time.get_ticks()



        def shake(self):
            #print(now)
            #print(self.timer)
            #self.top_right = (270,630)
            self.listx = [-10,10]
            self.listy = [-10, 10]
            # random_num = random.randint(-30,30)
            # self.rect.center = (self.x, self.y)
            # print(self.rect.center)
            for x in range(30):
                for i in self.listx:
                    for n in self.listy:
                        self.rect.center = self.x + i,self.y +n

                        screen.blit(self.image, self.rect.center)

                    #print(self.rect.center)



    class Spaceship(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("spaceship.png")
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = (250, 700)
            self.posX = 0
            self.posY = 0
            self.shoot_delay = 200
            self.finalshot_delay = 2000# milliseconds
            self.last_shot = pygame.time.get_ticks()
            self.sixth_shot = pygame.time.get_ticks()
            self.reload_shot = pygame.time.get_ticks()
            self.reload_delay = pygame.time.get_ticks()
            self.shots = 0
            self.value = 1
            self.num = 0



        def come_back(self):
            self.rect.center = (250, 700)




        def update(self,):

            if self.rect.bottom > 500:
                self.posY -= 4
                self.rect.y += self.posY
            # spaceship movement
            self.posX = 0
            self.posY = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.posX = -4
            if keystate[pygame.K_RIGHT]:
                self.posX = 4
            self.rect.x += self.posX
            if keystate[pygame.K_UP]:
                self.posY = -4
            if keystate[pygame.K_DOWN]:
                self.posY = 4
            if keystate[pygame.K_r]:
               nows = pygame.time.get_ticks()
               reload = mixer.Sound("reload.wav")
               reload.play()
               if nows - self.reload_shot > self.finalshot_delay:
                   self.num = 0
                   self.value = 0
                   self.sixth_shot = nows
               else:
                   self.num = 0

            if keystate[pygame.K_SPACE]:
                if self.num == 0:           #dont shoot
                    nows = pygame.time.get_ticks()
                    if nows - self.sixth_shot > self.finalshot_delay:
                        self.sixth_shot = nows
                        self.num = 1
                else:                        #shoot
                    if self.num == 1:
                        self.test_value()

            self.rect.y += self.posY

            # checks boundaries
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > 600:
                self.rect.bottom = 600

            if self.rect.right > 500:
                self.rect.right = 500
            if self.rect.left < 0:
               self.rect.left = 0







        def shoot(self):
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                bullet = Bullet(self.rect.centerx - 16, self.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)
                #laser = mixer.Sound("laser.wav")
                #laser.play()
        def test_value(self):

            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.value += 1
                if self.value %12== 0:
                    self.shoot()
                    reload = mixer.Sound("reload.wav")
                    reload.play()
                    self.num = 0
                    #pygame.mixer.Sound.set_volume(reload_sound3, 5)
                    self.sixth_shot = now
                else:
                    if self.value % 12 != 0:
                        self.shoot()


    class Meteor(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = meteor_img
            self.image = self.image_orig.copy()
            self.rect = self.image.get_rect()
            self.radius = 30
            #pygame.draw.circle(self.image_orig, RED, self.rect.center, self.radius)
            self.rect.x = random.randint(0, 436)
            self.rect.y = random.randint(-300, -200)
            self.speed = random.uniform(1, 4)
            self.rot = 0
            self.rot_speed = random.randrange(-8, 8)
            self.last_update = pygame.time.get_ticks()

        def Rotation(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 40:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center

        def update(self):
            self.Rotation()
            self.rect.y += self.speed
            # checks boundaries
            if self.rect.top > 600:
                self.rect.x = random.randint(0, 736)
                self.rect.y = random.randint(-200, -100)
                self.speed = random.uniform(1, 6)



    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("rocket1.png")
            self.rect = self.image.get_rect()
            self.radius = 10
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = x
            self.rect.y = y
            self.speed = -5

        def update(self):
            self.rect.y += self.speed
            if self.rect.bottom < 0:
                self.kill()


    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center, size):
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = explosion_anim[self.size][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0  # frame is reffered to each explosion image
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    class Levels(pygame.sprite.Sprite):
        def __init__(self,):
            pygame.sprite.Sprite.__init__(self)
            for i in range(1):
                meteor = Meteor()
                all_sprites.add(meteor)
                meteors.add(meteor)







    meteor_images = []
    meteor_list = ["regularExplosion00.png", "regularExplosion01.png", "regularExplosion02.png",
                   "regularExplosion03.png", "regularExplosion04.png", "regularExplosion05.png",
                   "regularExplosion06.png", "regularExplosion07.png", "regularExplosion08.png"]
    for i in meteor_list:
        meteor_images.append(pygame.image.load(i))

    explosion_anim = {}
    explosion_anim["sml"] = []
    explosion_anim["lrg"] = []
    for i in range(9):
        filename = "regularExplosion0{}.png".format(i)
        img = pygame.image.load(filename)
        img.set_colorkey(BLACK)
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lrg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sml'].append(img_sm)

    # initializes pygame
    # create the screen

    # set up
    all_sprites = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    meteor = Meteor()
    state = 0
    spaceship = Spaceship()
    all_sprites.add(spaceship)
    Giantspaceship = GiantSpaceship()
    all_sprites.add(Giantspaceship)

    square1 = Square1()
    all_sprites.add(square1)
    square2 = Square2()
    all_sprites.add(square2)
    square3 = Square3()
    all_sprites.add(square3)
    gamelevel = Levels()




    mixer.music.load("background.wav")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    background = pygame.image.load("space.jpg")
    #background_rect = background.get_rect()
    initial = (0,0)
    second_screen = (-100,0)

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

                if event.key == pygame.K_a:
                    spaceship.come_back()

                if event.key == pygame.K_1:
                    auto = Auto(spaceship,meteors,meteor)
                    auto.scroll_spaceship()
                    auto.scroll_meteors()





        #update
        all_sprites.update()

        #spaceship.scroll()
        #checks for hits, use groupcollide for group v group and spritecollide for singular v group check.
        hits = pygame.sprite.groupcollide(meteors,bullets,True, True, pygame.sprite.collide_circle)
        for hit in hits:
            hits_record += 1
            if hits_record %3 == 0:
                Levels()
                level +=1
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            pygame.mixer.Sound.set_volume(explosion_sound, 0.5)
            expl = Explosion(hit.rect.center, 'lrg')
            all_sprites.add(expl)
            meteor = Meteor()  # the next three lines restart the functions bc meteors wont "recycle"
            all_sprites.add(meteor)
            meteors.add(meteor)


        hitsquare1 = pygame.sprite.spritecollide(square1, meteors, True,)
        for hits in hitsquare1:
            #for i in range (3):
            #Giantspaceship.shake()
            meteor = Meteor()  # the next three lines restart the functions bc meteors wont "recycle"
            all_sprites.add(meteor)
            meteors.add(meteor)


        hitsquare2 = pygame.sprite.spritecollide(square2, meteors, True,)
        for hits in hitsquare2:
            meteor = Meteor()  # the next three lines restart the functions bc meteors wont "recycle"
            all_sprites.add(meteor)
            meteors.add(meteor)
        hitsquare3 = pygame.sprite.spritecollide(square3, meteors, True,)
        for hits in hitsquare3:
            meteor = Meteor()  # the next three lines restart the functions bc meteors wont "recycle"
            all_sprites.add(meteor)
            meteors.add(meteor)

        #draw/render
        screen.fill(BLACK)
        screen.blit(background,initial)
        draw_text(str(level), font, (255, 255, 255), screen, 250, 50, 1)
        all_sprites.draw(screen)
        pygame.display.flip()



main_menu()
#game()
instructions()
pygame.quit()


#notes:
