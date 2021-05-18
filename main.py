import pygame
import time
import random
from classes import *
from pygame.locals import *

width = 916
height = 587

# setup pygame
pygame.init()

pygame.font.init()
root = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Legend of Runner : Call of the waste of time")
icon_50x50 = pygame.image.load("logo.png")
pygame.display.set_icon(icon_50x50)

player = Player(100, 100, 20)
random.seed()
font1 = pygame.font.Font('Triforce.ttf', 25)
font2 = pygame.font.Font('Triforce.ttf', 40)

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
slimeIdle = [pygame.image.load("enemies/slime/slime-idle-0.png").convert_alpha(),
             pygame.image.load("enemies/slime/slime-idle-1.png").convert_alpha(),
             pygame.image.load("enemies/slime/slime-idle-2.png").convert_alpha(),
             pygame.image.load("enemies/slime/slime-idle-3.png").convert_alpha()]

slimeDie = [pygame.image.load("enemies/slime/slime-die-0.png").convert_alpha(),
            pygame.image.load("enemies/slime/slime-die-1.png").convert_alpha(),
            pygame.image.load("enemies/slime/slime-die-2.png").convert_alpha(),
            pygame.image.load("enemies/slime/slime-die-3.png").convert_alpha()]

eyeIdle = [pygame.image.load("enemies/eyeball/tile000.png").convert_alpha(),
           pygame.image.load("enemies/eyeball/tile001.png").convert_alpha(),
           pygame.image.load("enemies/eyeball/tile002.png").convert_alpha(),
           pygame.image.load("enemies/eyeball/tile003.png").convert_alpha()]

eyeDie = [pygame.image.load("enemies/eyeball/tile016.png").convert_alpha(),
          pygame.image.load("enemies/eyeball/tile017.png").convert_alpha(),
          pygame.image.load("enemies/eyeball/tile018.png").convert_alpha(),
          pygame.image.load("enemies/eyeball/tile019.png").convert_alpha()]

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
pygame.mixer.music.load('musics/title-theme-the-legend-of-zelda-ocarina-of-time.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# loading bars
redBlueBar = pygame.image.load("hud/redblue.png").convert_alpha()
redBlueBar = pygame.transform.scale(redBlueBar, (345, 54))

# resizing
runner_animations = [runnerIdle, runnerIdle2, runnerRun, runnerJump, runnerAttack1, runnerDie, runnerSlide, runnerStand,
                     runnerAttack2,
                     runnerAttack3]

slime_animations = [slimeIdle, slimeDie]
eyeball_animation = [eyeIdle, eyeDie]

for animation in runner_animations:
    for i in range(len(animation)):
        animation[i] = pygame.transform.scale(animation[i], (100, 74))

for animation in slime_animations:
    for i in range(len(animation)):
        animation[i] = pygame.transform.scale(animation[i], (64, 50))

for animation in eyeball_animation:
    for i in range(len(animation)):
        animation[i] = pygame.transform.scale(animation[i], (48, 48))
    for i in range(len(animation)):
        animation[i] = pygame.transform.flip(animation[i], True, False)

for i in range(len(obelisk)):
    obelisk[i] = pygame.transform.scale(obelisk[i], (120, 240))

# variables/lists
runnerAttacks = [runnerAttack1, runnerAttack2, runnerAttack3]
attackSounds = [sound_slash1, sound_slash2]

background = pygame.image.load("background.png")
deathScreen = pygame.Surface((916, 587))
deathScreen.fill("black")
deathScreenTime = 0

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
isDead = False

x = 160
y = 485
vel = 1
scrollingSpeed = 2
slowing = 0
invincibilityTime = 0
swordDamage = True

enemies = []
spawnDelay = 240

jumpCount = 25
walkCount = 0
walkCountDouble = 0
walkCountEnemies = 0
DieCountEnemies = 0
emoteCount = 0
actionCount = 0
animationCount = 0

attackDelay = 0
currentAttack = 1

highScore = 0
score = 0

scene = 0

pause = False
startText = font1.render("appuyez sur e pour commencer", False, (255, 255, 255))
run = True
clock = pygame.time.Clock()


# animations personnage et ennemies
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


def die_animation(speed):
    global walkCount
    if walkCount + 1 >= speed * 7:
        root.blit(runnerDie[walkCount // speed], (x, y))
        return True
    root.blit(runnerDie[walkCount // speed], (x, y))
    walkCount += 1


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


def stranger_run_animation(speed):
    global walkCountDouble, xDouble, yDouble
    if walkCountDouble + 1 > 42:
        walkCountDouble = 0
    root.blit(runnerRun[walkCountDouble // speed], (xDouble, yDouble))
    walkCountDouble += 1


def stranger_idle_animation(speed):
    global walkCountDouble, xDouble, yDouble
    if walkCountDouble + 1 >= speed * 4:
        walkCountDouble = 0
    root.blit(runnerIdle[walkCountDouble // speed], (xDouble, yDouble))
    walkCountDouble += 1


def slime_idle_animation(speed, x, y):
    global walkCountEnemies
    if walkCountEnemies + 1 >= speed * 4:
        walkCountEnemies = 0
    root.blit(slimeIdle[walkCountEnemies // speed], (x, y))
    walkCountEnemies += 1


def slime_die_animation(speed, x, y):
    global DieCountEnemies
    if DieCountEnemies + 1 >= speed * 4:
        DieCountEnemies = 0
        return True
    root.blit(slimeDie[DieCountEnemies // speed], (x, y))
    DieCountEnemies += 1


def eyeball_idle_animation(speed, x, y):
    global walkCountEnemies
    if walkCountEnemies + 1 >= speed * 4:
        walkCountEnemies = 0
    root.blit(eyeIdle[walkCountEnemies // speed], (x, y))
    walkCountEnemies += 1


def eyeball_die_animation(speed, x, y):
    global DieCountEnemies
    if DieCountEnemies + 1 >= speed * 4:
        DieCountEnemies = 0
        return True
    root.blit(eyeDie[DieCountEnemies // speed], (x, y))
    DieCountEnemies += 1


# permet d'éffectuer un fondu
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
        alphaCount += 0.25


# écran titre
def title_screen():
    global xBg
    xBg -= 1
    root.blit(title, (190, 70))
    root.blit(startText, (315, 430))
    run_animation(8)


# cinématique de la rencontre avec son double
def cinematic():
    global actionCount, xDouble, xBg, xObelisk, isPlaying, scene
    fade_out(title, (190, 70))
    actionCount += 0.25
    if actionCount < 60:
        xBg -= 1
        run_animation(8)
        xObelisk -= 1
        obelisk_animation(6)
    elif 60 <= actionCount < 80:
        sound_obelisk.play()
        idle_animation(8)
        obelisk_animation(6)
        stranger_idle_animation(8)
    elif 80 <= actionCount < 110:
        sound_obelisk.stop()
        idle_animation(8)
        obelisk_animation(6)
        stranger_run_animation(8)
        xDouble += 2
    elif actionCount >= 110:
        if play_emote(emoteAlerted):
            isPlaying = True
            pygame.mixer.music.load('musics/chrono-trigger-music-extended-corridors-of-time.mp3')
            pygame.mixer.music.play(-1)
            scene = 2
        idle_animation(10)
        obelisk_animation(6)


# s'exécute lorsque le joeur meurt
def die():
    global x, y, enemies, score, xObelisk, scene, deathScreenTime, scene, alpha, alphaCount, enemies, scrollingSpeed
    if die_animation(9):
        root.blit(deathScreen, (0, 0))
        scene = 4
        alphaCount = 0
        alpha = 255
        del (enemies[:])
        score = 0
        scrollingSpeed = 2


# s'exécute une fois l'animation de mort finie
def respawn():
    global deathScreenTime, x, y, isPlaying, invincibilityTime, scene, xObelisk
    x = 100
    y = 485
    if fade_out(deathScreen, (0, 0)):
        isPlaying = True
        player.reset_stats()
        invincibilityTime = 0
        scene = 2
    sound_obelisk.play()
    pygame.mixer.music.load('musics/chrono-trigger-music-extended-corridors-of-time.mp3')
    pygame.mixer.music.play(-1)
    xObelisk = x - 18
    obelisk_animation(6)
    idle_animation(8)


# Boucle qui s'occupe de la partie affichage(animations etc..)
def redraw_game_window():
    global xBg, xObelisk, scrollingSpeed, enemies, isStand, isJump, isPlaying, isAttacking, invincibilityTime, \
        isSliding, isIdling, scene, highScore, enemyHitBox

    rel_x = xBg % background.get_rect().width
    if rel_x < width:
        root.blit(background, (rel_x, 0))
    root.blit(background, (rel_x - background.get_rect().width, 0))

    if isPlaying:
        xBg -= scrollingSpeed
        xObelisk -= scrollingSpeed
        obelisk_animation(6)

        # affichage des ennemies
        for enemy in enemies:
            if enemy.health <= 0:
                if enemy.type == "Slime":
                    if slime_die_animation(8, enemy.position, 510):
                        enemies.remove(enemy)
                elif enemy.type == "EyeBall":
                    if eyeball_die_animation(8, enemy.position, 465):
                        enemies.remove(enemy)
            else:
                if enemy.type == "Slime":
                    slime_idle_animation(8 * len(enemies), enemy.position, 510)
                elif enemy.type == "EyeBall":
                    eyeball_idle_animation(8 * len(enemies), enemy.position, 465)

        # affichage du joueur selon son action
        if round(invincibilityTime) % 2 == 0:
            if isJump:
                jump_animation(8)

            elif isAttacking:
                attack_animation(4, runnerAttacks[currentAttack])

            elif isSliding:
                slide_animation(5)

            elif not isStand and not isSliding:
                stand_animation(6)

            elif isIdling:
                idle2_animation(8)

            else:
                run_animation(7)

        if highScore < score:
            highScore = score

        # HUD affiche barre de vie, stamina et score
        pygame.draw.rect(root, pygame.Color(255, 0, 0), ((21, 19), (player.health * 3.3, 20)))
        pygame.draw.rect(root, pygame.Color(26, 35, 126), ((21, 37), (player.stamina * 3.3, 20)))
        score_text = font2.render("score : " + str(round(score)), False, (241, 196, 15))
        high_score_text = font1.render("meilleur score : " + str(round(highScore)), False, (241, 196, 15))
        root.blit(redBlueBar, (10, 10))
        root.blit(score_text, (680, 10))
        root.blit(high_score_text, (660, 55))

    else:
        if scene == 0:
            title_screen()
        elif scene == 1:
            cinematic()
        elif scene == 3:
            die()
        elif scene == 4:
            respawn()

    if 500 < score < 1000 and scrollingSpeed != 2.5:
        scrollingSpeed = 2.5
    elif score > 1000 and scrollingSpeed != 3:
        scrollingSpeed = 3
    pygame.display.update()


# eventloop (boucle s'occupant de la partie logique)
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if pause:
        # quitter le menu pause
        if keys[pygame.K_ESCAPE]:
            pause = False
            time.sleep(0.5)
            pygame.mixer.music.set_volume(0.1)
    else:
        if not isPlaying:
            if keys[pygame.K_e]:
                if scene == 0:
                    scene = 1
            if isDead:
                scene = 3
                isDead = False
        else:
            score += 0.2
            playerHitBox = pygame.Rect(x + 26, y + 15, 40, 55)
            if invincibilityTime > 0:
                invincibilityTime -= 0.1
            else:
                invincibilityTime = 0
            if player.stamina < 100:
                player.stamina_change(0.1)
            if keys[pygame.K_ESCAPE]:
                pause = True
                pygame.mixer.music.set_volume(0.01)
                time.sleep(0.1)
            if attackDelay > 0:
                attackDelay -= 1

            if spawnDelay == 0:
                spawnDelay = random.randint(200, 350)
                enemyType = random.randint(0, 1)
                if enemyType == 0:
                    enemies.append(Enemy("Slime", 20, width, (64, 30)))
                elif enemyType == 1:
                    enemies.append(Enemy("EyeBall", 15, width, (48, 48)))
            else:
                spawnDelay -= 1
            if isAttacking:
                attackDelay = 30
                playerHurtBox = pygame.Rect(x + 66, y + 15, 35, 55)
                if x > vel:
                    x -= scrollingSpeed
                # gestion collision épée-ennemies
                for enemy in enemies:
                    w, h = enemy.size
                    if enemy.type == "Slime":
                        enemyHitBox = Rect(enemy.position, 557 - h, w, h)
                    elif enemy.type == "EyeBall":
                        enemyHitBox = Rect(enemy.position + 5, 557 - h - 40, w - 10, h - 10)
                    if playerHurtBox.colliderect(enemyHitBox) and swordDamage:
                        enemy.health -= player.atk_points
                        swordDamage = False
            else:
                if isSliding:
                    if x <= vel:
                        isSliding = False
                    else:
                        if slowing < 2:
                            slowing += 0.005
                        x -= slowing
                    playerHitBox = pygame.Rect(x + 28, y + 40, 50, 35)
                    if event.type == pygame.KEYUP and not keys[pygame.K_DOWN]:
                        isSliding = False
                        walkCount = 0
                else:
                    slowing = 0
                    if isStand:
                        if isJump:
                            playerHitBox = pygame.Rect(x + 38, y + 15, 40, 55)
                            if keys[pygame.K_RIGHT] and x < width - vel - 100 and not isIdling:
                                x += vel
                            if jumpCount >= -25:
                                y -= (jumpCount * abs(jumpCount)) * 0.02
                                jumpCount -= 1
                            else:
                                jumpCount = 25
                                isJump = False
                                x -= vel
                        else:
                            if keys[pygame.K_a] and player.stamina >= 12:
                                swordDamage = True
                                isAttacking = True
                                player.stamina_change(-12)
                                attackSounds[random.randint(0, 1)].play()
                                walkCount = 0
                                if attackDelay > 0 and currentAttack < 2:
                                    currentAttack += 1
                                else:
                                    currentAttack = 0
                                    attackDelay = 15
                            if not isIdling:
                                playerHitBox = pygame.Rect(x + 38, y + 15, 40, 55)
                                if keys[pygame.K_LEFT] and x > vel:
                                    isIdling = True
                                    walkCount = 0
                                if keys[pygame.K_RIGHT] and x < width - vel - 100:
                                    x += vel
                                if keys[pygame.K_UP] and player.stamina >= 10:
                                    player.stamina_change(-10)
                                    isJump = True
                                    walkCount = 0
                                if keys[pygame.K_DOWN] and x > vel and player.stamina >= 10:
                                    player.stamina_change(-10)
                                    isSliding = True
                                    walkCount = 0
                            elif event.type == pygame.KEYUP and not keys[pygame.K_LEFT]:
                                isIdling = False
                            elif x > vel:
                                x -= scrollingSpeed
                            else:
                                isIdling = False

            if player.health <= 0:
                walkCount = 0
                isDead = True
                isPlaying = False

            # gestion collision ennemies-joueur
            for enemy in enemies:
                enemy.move(-scrollingSpeed)
                w, h = enemy.size
                if enemy.health > 0:
                    if enemy.type == "Slime":
                        enemyHitBox = Rect(enemy.position, 557 - h, w, h)
                    elif enemy.type == "EyeBall":
                        enemyHitBox = Rect(enemy.position + 5, 557 - h - 45, w - 10, h - 10)
                if playerHitBox.colliderect(enemyHitBox) and invincibilityTime == 0:
                    player.heal(-20)
                    invincibilityTime = 13
                if enemy.position <= -w:
                    enemies.remove(enemy)

        redraw_game_window()

pygame.quit()
