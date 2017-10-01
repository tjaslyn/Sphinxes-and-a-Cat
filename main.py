import pygame
import random

pygame.init()

myfont = pygame.font.SysFont('Comic San MS', 3)

screen = pygame.display.set_mode((1000, 1000))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()
screen.blit(background, (0,0))

defaultTileColor = (0, 128, 255)
rightTileColor = (0, 255, 128)
wrongTileColor = (255, 0, 128)
tileColor = defaultTileColor

#done = False
mainloop = True

FPS = 30
playtime = 0.0

n = 2#assigned number n for prototype use ONLY.
score = 0
counter = 0
imgLog = {} #{round1: 'cat02.jpeg', round2: 'cat05.jpeg'...}
posLog = {} #{round1: (row,col), round2: (row,col),...}
meowLog = {}
#row,col is ichoice,jchoice


clock = pygame.time.Clock()

catImgs = ['cat01.jpeg', 'cat02.jpeg', 'cat03.jpeg', 'cat04.jpeg','cat05.jpeg', 'cat06.jpeg', 'cat08.jpeg', 'cat09.jpeg']
catMeows = ['meow01x.ogg', 'meow02x.ogg', 'meow03x.ogg', 'meow04x.ogg', 'meow05x.ogg', 'meow06x.ogg']
scoreCat = {4:'cat01.jpeg', 8:'cat02.jpeg', 12:'cat03.jpeg', 16:'cat04.jpeg', 20:'cat05.jpeg', 24:'cat06.jpeg', 28:'cat07.jpeg', 32:'cat08.jpeg', 36:'cat09.jpeg'}
first = True

def condition1(currentRound):
    return posLog[currentRound] == posLog[currentRound-n]

def condition2(currentRound):
    return imgLog[currentRound] == imgLog[currentRound-n]

def condition3(currentRound):
    return meowLog[currentRound] == meowLog[currentRound-n]

while mainloop:

    #counter += 1
    if first:
        randChosen = random.choice(catImgs)
        randMeow = random.choice(catMeows)
        meow = pygame.mixer.Sound(randMeow)
        pygame.mixer.Sound.play(meow)
        #pygame.mixer.Sound.play(meow)
        print(type(meow))
        ichoice = random.choice([x for x in range(3)])
        jchoice = random.choice([x for x in range(3)])
        first = False

    imgLog[counter] = randChosen
    posLog[counter] = (ichoice,jchoice)
    meowLog[counter] = randMeow

    prevNum = int(playtime)
    milliseconds = clock.tick(FPS)
    playtime += milliseconds/1000.0

    if int(playtime)==(prevNum+1):
        counter += 1
        screen.blit(background, (0,0)) #resets background
        tileColor = defaultTileColor #resets tile color
        ichoice = random.choice([x for x in range(3)])
        jchoice = random.choice([x for x in range(3)])
        randChosen = random.choice(catImgs)
        randMeow = random.choice(catMeows)
        meow = pygame.mixer.Sound(randMeow)
        pygame.mixer.Sound.play(meow)

        imgLog[counter] = randChosen #overwrites prev randChosen so its fine.
        posLog[counter] = (ichoice,jchoice)
        meowLog[counter] = randMeow
        if counter>n:
            res1 = condition1(counter)
            res2 = condition2(counter) #is it the same cat as in prev n round?
            res3 = condition3(counter)
            ans = [res1, res2, res3].count(True)
    #pygame.mixer.Sound.play(meow)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            elif counter>n:
                #res3 = condition3(counter)
                #ans = [res1,res2,res3].count(True)

                #if at least 1 condition true
                if event.key == pygame.K_1:
                    if ans == 1:
                        score += 1
                        tileColor = rightTileColor
                    else:
                        tileColor = wrongTileColor
                #if at least 2 conditions true
                elif event.key == pygame.K_2:
                    if ans == 2:
                        score += 1
                        tileColor = rightTileColor
                    else:
                        tileColor = wrongTileColor
                #if at least 3 conditions true
                elif event.key == pygame.K_3:
                    if ans == 3:
                        score += 1
                        tileColor = rightTileColor
                    else:
                        tileColor = wrongTileColor
                else:
                    pass
                

    squareStart = 75
    squareSize = 250
    squarePadding = 40

    #randomize the chosen square (to be printed with image instead)

    foundTile = False
    #print(ichoice,jchoice)
    for i in range(0, 3):
        for j in range(0, 3):
            if i==ichoice and j==jchoice:
                #print('test')

                img = pygame.image.load(randChosen)
                #screen.blit(img, (i,j))

                imgRect = pygame.Rect(squareStart + i*(squareSize+squarePadding), squareStart + j*(squareSize+squarePadding), squareSize, squareSize)
                #pygame.draw.rect(screen, img, pygame.Rect(squareStart + i*(squareSize+squarePadding), squareStart + j*(squareSize+squarePadding), squareSize, squareSize))
                #print(imgRect.width, imgRect.height)
                screen.blit(img, imgRect)
            else:
                #pygame.mixer.Sound.play(meow)
                pygame.draw.rect(screen, tileColor, pygame.Rect(squareStart + i*(squareSize+squarePadding), squareStart + j*(squareSize+squarePadding), squareSize, squareSize))

    
    myfont = pygame.font.SysFont("Ariel", 100)
    label = myfont.render("Score: " + str(score), 1, (0,0,0))
    screen.blit(label, (350,925))
    pygame.display.flip()
    #pygame.mixer.Sound.play(meow)

if score>=36:
    randpic = scoreCat[36]
elif score >=32:
    randpic = scoreCat[32]
elif score>=28:
    randpic = scoreCat[28]
elif score>=24:
    randpic = scoreCat[24]
elif score>=20:
    randpic = scoreCat[20]
elif score>=16:
    randpic = scoreCat[16]
elif score>=12:
    randpic = scoreCat[12]
elif score>=8:
    randpic = scoreCat[8]
else:
    randpic = scoreCat[4]

picture = pygame.image.load(randpic)
picture = pygame.transform.scale(picture, (1000, 1000))

endRect = picture.get_rect()
screen.blit(picture, endRect)
for i in range(10):
    
    pygame.display.flip()

pygame.quit()
print('Score: '+str(score))

