import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()
screen.blit(background, (0,0))

#done = False
mainloop = True

FPS = 30
playtime = 0.0

n = 0 #assigned number n for prototype use ONLY.
score = 0
counter = 0
imgLog = {} #{round1: 'cat02.jpeg', round2: 'cat05.jpeg'...}
posLog = {} #{round1: (row,col), round2: (row,col),...}
#row,col is ichoice,jchoice


clock = pygame.time.Clock()

catImgs = ['cat01.jpeg', 'cat02.jpeg', 'cat03.jpeg']

#catImgs = ['cat01.jpeg', 'cat02.jpeg', 'cat03.jpeg', 'cat04.jpeg', 'cat05.jpeg', 'cat06.jpeg', 'cat07.jpeg', 'cat08.jpeg', 'cat09.jpeg']

first = True

def condition1(currentRound):
    return posLog[currentRound] == posLog[currentRound-n]

def condition2(currentRound):
    return imgLog[currentRound] == imgLog[currentRound-n]

while mainloop:
    counter += 1
    if first:
        randChosen = random.choice(catImgs)
        ichoice = random.choice([x for x in range(3)])
        jchoice = random.choice([x for x in range(3)])
        first = False
        
    imgLog[counter] = randChosen
    posLog[counter] = (ichoice,jchoice)
    
    prevNum = int(playtime)
    milliseconds = clock.tick(FPS)
    playtime += milliseconds/1000.0
  
    if int(playtime)==(prevNum+1):
        screen.blit(background, (0,0)) #resets background
        ichoice = random.choice([x for x in range(3)])
        jchoice = random.choice([x for x in range(3)])
        randChosen = random.choice(catImgs)
        imgLog[counter] = randChosen #overwrites prev randChosen so its fine.
        posLog[counter] = (ichoice,jchoice)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            elif counter>n:
                res1 = condition1(counter)
                res2 = condition2(counter) #is it the same cat as in prev n round?
                #res3 = condition3(counter)
                #ans = [res1,res2,res3].count(True)
                ans = [res1, res2].count(True)
                
                #if at least 1 condition true
                if event.key == pygame.K_1 and 1==ans: #and 1==ans 
                    score += 1

                #if at least 2 conditions true
                elif event.key == pygame.K_2 and 2==ans: #and 2==ans
                    score += 1
                    
                #if at least 3 conditions true
                elif event.key == pygame.K_3 and 3==ans: #and 3==ans
                    score += 1
                else:
                    pass
                
    squareStart = 40
    squareSize = 125
    squarePadding = 20

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
                pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(squareStart + i*(squareSize+squarePadding), squareStart + j*(squareSize+squarePadding), squareSize, squareSize))
    pygame.display.flip()
    
pygame.quit()
print('Score: '+str(score))
