import pygame
import time
import random
from enemy import Enemy
from pygame.locals import *

width = 916
height = 587

# setup pygame
pygame.init()
pygame.font.init()
random.seed()
myFont = pygame.font.SysFont('Arial', 20)
root = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Legend of Runner : Call of the waste of time")

title = pygame.image.load("title.png").convert_alpha()
alphaCount = 0
alpha = 255

# loading runner animations
runnerIdle = [pygame.image.load("player/idle-00.png").convert_alpha(),
              pygame.image.load("player/idle-01.png").convert_alpha(),
              pygame.image.load("player/idle-02.png").convert_alpha(),
              pygame.image.load("player/idle-03.png").convert_alpha()]

runnerIdle2 = [pygame.image.load("player/idle-2-00.png").convert_alpha(),
              pygame.image.load("player/idle-2-01.png").convert_alpha(),
              pygame.image.load("player/idle-2-02.png").convert_alpha(),
              pygame.image.load("player/idle-2-03.png").convert_alpha()]

runnerRun = [pygame.image.load("player/run-00.png").convert_alpha(),
             pygame.image.load("player/run-01.png").convert_alpha(),
             pygame.image.load("player/run-02.png").convert_alpha(),
             pygame.image.load("player/run-03.png").convert_alpha(),
             pygame.image.load("player/run-04.png").convert_alpha(),
             pygame.image.load("player/run-05.png").convert_alpha()]

runnerJump = [pygame.image.load("player/jump-00.png").convert_alpha(),
              pygame.image.load("player/jump-01.png").convert_alpha(),
              pygame.image.load("player/jump-02.png").convert_alpha(),
              pygame.image.load("player/jump-03.png").convert_alpha(),
              pygame.image.load("player/fall-00.png").convert_alpha(),
              pygame.image.load("player/fall-01.png").convert_alpha()]

runnerAttack1 = [pygame.image.load("player/attack1-00.png").convert_alpha(),
                 pygame.image.load("player/attack1-01.png").convert_alpha(),
                 pygame.image.load("player/attack1-02.png").convert_alpha(),
                 pygame.image.load("player/attack1-03.png").convert_alpha(),
                 pygame.image.load("player/attack1-04.png").convert_alpha(),
                 pygame.image.load("player/attack2-00.png").convert_alpha()]

runnerAttack2 = [pygame.image.load("player/attack2-00.png").convert_alpha(),
                 pygame.image.load("player/attack2-01.png").convert_alpha(),
                 pygame.image.load("player/attack2-02.png").convert_alpha(),
                 pygame.image.load("player/attack2-03.png").convert_alpha(),
                 pygame.image.load("player/attack2-04.png").convert_alpha(),
                 pygame.image.load("player/attack2-05.png").convert_alpha()]

runnerAttack3 = [pygame.image.load("player/attack3-00.png").convert_alpha(),
                 pygame.image.load("player/attack3-01.png").convert_alpha(),
                 pygame.image.load("player/attack3-02.png").convert_alpha(),
                 pygame.image.load("player/attack3-03.png").convert_alpha(),
                 pygame.image.load("player/attack3-04.png").convert_alpha(),
                 pygame.image.load("player/attack3-05.png").convert_alpha()]

runnerSlide = [pygame.image.load("player/stand-02.png").convert_alpha(),
               pygame.image.load("player/stand-01.png").convert_alpha(),
               pygame.image.load("player/stand-00.png").convert_alpha(),
               pygame.image.load("player/slide-00.png").convert_alpha(),
               pygame.image.load("player/slide-01.png").convert_alpha()]

runnerStand = [pygame.image.load("player/stand-00.png").convert_alpha(),
               pygame.image.load("player/stand-01.png").convert_alpha(),
               pygame.image.load("player/stand-02.png").convert_alpha()]

runnerDie = [pygame.image.load("player/die-00.png").convert_alpha(),
             pygame.image.load("player/die-01.png").convert_alpha(),
             pygame.image.load("player/die-02.png").convert_alpha(),
             pygame.image.load("player/die-03.png").convert_alpha(),
             pygame.image.load("player/die-04.png").convert_alpha(),
             pygame.image.load("player/die-05.png").convert_alpha(),
             pygame.image.load("player/die-06.png").convert_alpha()]

# loading enemies animations
slimeRun = [pygame.image.load("enemies/Slime/slime_run_00.png").convert_alpha(),
            pygame.image.load("enemies/Slime/slime_run_01.png").convert_alpha(),
            pygame.image.load("enemies/Slime/slime_run_02.png").convert_alpha(),
            pygame.image.load("enemies/Slime/slime_run_03.png").convert_alpha()]

# loading objects
obelisk = [pygame.image.load("obelisk/obelisk_000.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_001.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_002.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_003.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_004.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_005.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_006.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_007.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_008.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_009.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_010.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_011.png").convert_alpha(),
           pygame.image.load("obelisk/obelisk_012.png").convert_alpha()]
# loading emotes
emoteAlerted = [pygame.image.load("reactions/tile016.png").convert_alpha(),
                pygame.image.load("reactions/tile017.png").convert_alpha(),
                pygame.image.load("reactions/tile018.png").convert_alpha(),
                pygame.image.load("reactions/tile019.png").convert_alpha(),
                pygame.image.load("reactions/tile020.png").convert_alpha(),
                pygame.image.load("reactions/tile021.png").convert_alpha(),
                pygame.image.load("reactions/tile022.png").convert_alpha(),
                pygame.image.load("reactions/tile023.png").convert_alpha()]

# loading sound effects
sound_emote = pygame.mixer.Sound('sounds/emote sound.mp3')
sound_emote.set_volume(0.05)
sound_obelisk = pygame.mixer.Sound('sounds/obelisk.wav')
sound_obelisk.set_volume(0.05)
sound_slash1 = pygame.mixer.Sound('sounds/sword_slash_1.mp3')
sound_slash1.set_volume(0.05)
sound_slash2 = pygame.mixer.Sound('sounds/sword_slash_2.mp3')
sound_slash2.set_volume(0.05)

# loading musics
pygame.mixer.music.load('musics/chrono-cross-ost-times-scar.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# loading bars
staminaBar = []

# resizing (temporary)
animations = [runnerIdle, runnerIdle2, runnerRun, runnerJump, runnerAttack1, runnerDie, runnerSlide, runnerStand, runnerAttack2,
              runnerAttack3]

for animation in animations:
    for i in range(len(animation)):
        animation[i] = pygame.transform.scale(animation[i], (100, 74))

for i in range(len(obelisk)):
    obelisk[i] = pygame.transform.scale(obelisk[i], (120, 240))



runnerAttacks = [runnerAttack1, runnerAttack2, runnerAttack3]
attackSounds = [sound_slash1, sound_slash2]

background = pygame.image.load("background.png")
xBg = 0
relX = 0
xObelisk = width + 5
xDouble = 700
yDouble = 485

isPlaying = False
isAttacking = False
isSliding = False
isStand = True
isJump = False
isIdling = False

x = 160
y = 485
vel = 1
scrollingSpeed = 2
slowing = 0

enemies = []
spawnDelay = 240

jumpCount = 25
walkCount = 0
walkCountDouble = 0
emoteCount = 0
actionCount = 0
animationCount = 0

attackDelay = 0
currentAttack = 1

health = 100
stamina = 100
score = 0
highScore = 0

titleScreen = True
scene1 = False

pause = False
pauseText = myFont.render("Running", False, (241, 196, 15))
run = True
clock = pygame.time.Clock()


def attack_animation(speed, animation_number):
    global walkCount, isAttacking
    if walkCount + 1 >= 6 * speed:
        walkCount = 0
        isAttacking = False
        root.blit(animation_number[5], (x, y))
    else:
        root.blit(animation_number[walkCount // speed], (x, y))
        walkCount += 1


def slide_animation(speed):
    global walkCount, isStand
    if walkCount + 1 >= speed * 5:
        walkCount = 15
        isStand = False
    root.blit(runnerSlide[walkCount // speed], (x, y))
    walkCount += 1


def stand_animation(speed):
    global walkCount, isStand
    if walkCount + 1 >= speed * 3:
        isStand = True
        walkCount = 0
        root.blit(runnerStand[2], (x, y))
    else:
        root.blit(runnerStand[walkCount // speed], (x, y))
        walkCount += 1


def jump_animation(speed):
    global walkCount
    if walkCount + 1 >= speed * 6:
        walkCount = 32
    root.blit(runnerJump[walkCount // speed], (x, y))
    walkCount += 1


def run_animation(speed):
    global walkCount
    if walkCount + 1 > speed * 6:
        walkCount = 0
    root.blit(runnerRun[walkCount // speed], (x, y))
    walkCount += 1


def run_animation_double(speed):
    global walkCountDouble, xDouble, yDouble
    if walkCountDouble + 1 > 42:
        walkCountDouble = 0
    root.blit(runnerRun[walkCountDouble // speed], (xDouble, yDouble))
    walkCountDouble += 1


def idle_animation(speed):
    global walkCount
    if walkCount + 1 >= speed * 4:
        walkCount = 0
    root.blit(runnerIdle[walkCount // speed], (x, y))
    walkCount += 1

def idle2_animation(speed):
    global walkCount
    if walkCount + 1 >= speed * 4:
        walkCount = 0
    root.blit(runnerIdle2[walkCount // speed], (x, y))
    walkCount += 1

def idle_animation_double(speed):
    global walkCountDouble, xDouble, yDouble
    if walkCountDouble + 1 >= speed * 4:
        walkCountDouble = 0
    root.blit(runnerIdle[walkCountDouble // speed], (xDouble, yDouble))
    walkCountDouble += 1


def play_emote(liste: list):
    global emoteCount
    if emoteCount == 0:
        sound_emote.play()
    if emoteCount + 1 > 40:
        return True
    root.blit(liste[emoteCount // 5], (x + 55, y - 25))
    emoteCount += 1


def obelisk_animation(speed):
    global animationCount, xObelisk
    if animationCount + 1 > speed * 13:
        animationCount = 0
    root.blit(obelisk[animationCount // speed], (xObelisk, 330))
    animationCount += 1


'''
def Respawn(speed):

'''


# fade_in()  function

def fade_out(source, location):
    global alphaCount, alpha
    if alphaCount + 1 == 17:
        return True
    else:
        alpha -= 15
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(root, (-location[0], -location[1]))
        temp.blit(source, (0, 0))
        temp.set_alpha(alpha)
        root.blit(temp, location)
        alphaCount += 1


# gameloop
def redraw_game_window():
    global walkCount, jumpCount, isJump, xBg, isAttacking, isSliding, score, emoteCount, isPlaying, scene1, isStand, \
        titleScreen, actionCount, attackDelay, currentAttack, xObelisk, vel, x, slowing, walkCountDouble, xDouble

    rel_x = xBg % background.get_rect().width
    if rel_x < width:
        root.blit(background, (rel_x, 0))
    root.blit(background, (rel_x - background.get_rect().width, 0))

    if isPlaying:
        xBg -= scrollingSpeed
        xObelisk -= scrollingSpeed
        obelisk_animation(6)

        if isJump:
            jump_animation(8)

        elif isAttacking:
            attack_animation(4, runnerAttacks[currentAttack])
            attackDelay = 30

        elif isSliding:
            slide_animation(5)
            if x <= vel:
                isSliding = False
            else:
                if slowing < 2:
                    x -= slowing
                    slowing += 0.005

        elif not isStand and not isSliding:
            stand_animation(6)
            slowing = 0

        elif isIdling:
            idle2_animation(8)

        else:
            run_animation(7)
        score += 0.5

        for enemy in enemies:
            root.blit(slimeRun[0],(enemy.position,500))
            enemy.move(-scrollingSpeed)

    else:
        if titleScreen:
            xBg -= 1
            root.blit(title, (190, 70))
            run_animation(8)
        if scene1:
            fade_out(title, (190, 70))
            actionCount += 0.25
            if actionCount < 60:
                xBg -= 1
                run_animation(8)
                xObelisk -= 1
                obelisk_animation(6)
            elif 60 <= actionCount < 80:
                idle_animation(8)
                obelisk_animation(6)
                idle_animation_double(8)
            elif 80 <= actionCount < 110:
                idle_animation(8)
                obelisk_animation(6)
                run_animation_double(8)
                xDouble += 2
            elif actionCount >= 110:
                if play_emote(emoteAlerted):
                    isPlaying = True
                    pygame.mixer.music.load('musics/chrono-trigger-music-extended-corridors-of-time.mp3')
                    pygame.mixer.music.play(-1)
                idle_animation(10)
                obelisk_animation(6)

    score_text = myFont.render("Score : " + str(round(score)), False, (241, 196, 15))
    root.blit(score_text, (0, 0))
    root.blit(pauseText, (200, 0))
    pygame.display.update()


# eventloop
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not pause:
        if isPlaying:
            if keys[pygame.K_ESCAPE]:
                pause = True
                pauseText = myFont.render("Pause", False, (241, 196, 15))
                pygame.mixer.music.set_volume(0.01)
                time.sleep(0.1)
            if not isAttacking:
                if not isSliding:
                    if isStand:
                        if keys[pygame.K_RIGHT] and x < width - vel - 100:
                            x += vel
                        if not isJump:
                            if keys[pygame.K_a]:
                                isAttacking = True
                                attackSounds[random.randint(0, 1)].play()
                                walkCount = 0
                                if attackDelay > 0 and currentAttack < 2:
                                    currentAttack += 1
                                else:
                                    currentAttack = 0
                                    attackDelay = 15
                            if not isIdling:
                                if keys[pygame.K_LEFT] and x > vel:
                                    isIdling = True
                                    walkCount = 0

                                if keys[pygame.K_UP]:
                                    isJump = True
                                    walkCount = 0
                                if keys[pygame.K_DOWN] and x> vel:
                                    isSliding = True
                                    walkCount = 0

                            elif event.type == pygame.KEYUP and not keys[pygame.K_LEFT]:
                                isIdling = False
                            elif x > vel:
                                x -= scrollingSpeed
                            else:
                                isIdling = False

                        else:
                            if jumpCount >= -25:
                                y -= (jumpCount * abs(jumpCount)) * 0.02
                                jumpCount -= 1
                            else:
                                jumpCount = 25
                                isJump = False
                                x -= vel

                elif event.type == pygame.KEYUP and not keys[pygame.K_DOWN]:
                    isSliding = False
                    walkCount = 0
            elif x > vel:
                x -= scrollingSpeed

            if attackDelay > 0:
                attackDelay -= 1

            if spawnDelay == 0:
                spawnDelay = 240
                enemies.append(Enemy(20,500))
            else:
                spawnDelay -= 1
        else:
            if keys[pygame.K_e]:
                if not scene1:
                    titleScreen = False
                    scene1 = True

        redraw_game_window()
    else:
        if keys[pygame.K_ESCAPE]:
            pause = False
            pauseText = myFont.render("Running", False, (241, 196, 15))
            time.sleep(0.5)
            pygame.mixer.music.set_volume(0.1)
pygame.quit()
