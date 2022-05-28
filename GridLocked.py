from turtle import heading
import pygame
import random
import time
import math

#Initializing pygame
pygame.init()

#Set the screen sice
screen = pygame.display.set_mode((800, 800))

#Title of the pygame window
pygame.display.set_caption("GridLocked")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
level = 1
timer = 7
answer = letters[random.randint(0, 25)]
gridContents = []

font = pygame.font.Font('freesansbold.ttf', 24)

#Displays the score above the left corner of the grid
def disScore(x):
    score = font.render("Score: " + "{:.2f}".format(x), True, (255, 255, 255))
    screen.blit(score, (50, 20))

#Draws the entire grid
def makeGrid(x, grid):
    pygame.draw.line(screen, "WHITE", (50, 50), (750, 50))
    pygame.draw.line(screen, "WHITE", (50, 50), (50, 750))
    pygame.draw.line(screen, "WHITE", (50, 750), (750, 750))
    pygame.draw.line(screen, "WHITE", (750, 750), (750, 50))
    eachDistance = 700/(x+1)
    partitions = x + 1
    xCoord = 50 
    yCoord = 50
    if level <= 15:
        font = pygame.font.Font('freesansbold.ttf', 24)
    else:
        font = pygame.font.Font('freesansbold.ttf', 12)
    for i in range(1, partitions):
        xCoord = xCoord + eachDistance
        yCoord = yCoord + eachDistance
        pygame.draw.line(screen, "WHITE", (xCoord, 50), (xCoord, 750))
        pygame.draw.line(screen, "WHITE", (50, yCoord), (750, yCoord))
    counter = 0
    xCoord = 50
    yCoord = 50 + eachDistance//2
    for i in range(0, x+1):
        xCoord = 50 + eachDistance//2
        for j in range(0, x+1):
            letter = font.render(grid[counter], True, (255, 255, 255))
            screen.blit(letter, (xCoord, yCoord))
            counter = counter + 1
            xCoord = xCoord + eachDistance
        yCoord = yCoord + eachDistance    

#Picks a random letter from the list of leters that you have to find
def generateAnswer(listOfLetters, listOfNumbers):
    choice = random.randint(0, 1)
    if choice:
        index = random.randint(0,25)
        return listOfLetters[index]
    else:
        index = random.randint(0, 9)
        return listOfNumbers[index]
    
#Displays letter to be found above the grid
def displayAnswer(ans):
    score = font.render("Find " + ans, True, (255, 255, 255))
    screen.blit(score, (350, 20))

#This generates the letters and numbers of the entire grid
def generateGridValues(letters, numbers, ans, level):
    level = level + 1
    gridList = []
    gridList.append(ans);
    if level <= 5:
        for i in range(0, level * level - 1):

            index = random.randint(0, 25)
            while(letters[index] == ans):
                index = random.randint(0, 25)
            gridList.append(letters[index])
    else:
        for i in range(0, level * level - 1):
            choice = random.randint(0, 1)
            if choice == 0:
                index = random.randint(0, 25)
                while(letters[index] == ans):
                    index = random.randint(0, 25)
                gridList.append(letters[index])
            elif choice == 1:
                index = random.randint(0, 9)
                gridList.append(numbers[index])
    random.shuffle(gridList)
    return gridList

#This checks which box you clicked on the grid
def check(xPos, yPos, ans, list, lvl):
    row = (yPos - 50) // (700 // (lvl + 1))
    col = (xPos - 50) // (700 // (lvl + 1))
    location = (lvl + 1) * row + col
    if list[location] == ans:
        return 1
    else:
        return 0   

#This controls the colour changing of the timer
def getGreenToRed(percent):
    
    if(percent < 50):
        r = 255
        g = math.floor((percent*2)*255/100)
    else:
        g = 255
        r = math.floor(255-(percent*2-100)*255/100)
    
    return r, g

#This displays the time left for the level
def displayTime(time1, time2, totalTime):    
    time3 = totalTime - (time2 - time1)
    if(time3 < 0):
        time3 = 0

    percentage = (time3) * 100 / totalTime
    r, g = getGreenToRed(percentage)
    
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255

    score = font.render("{:.2f}".format(time3), True, (r, g, 0))
    screen.blit(score, (650, 20))
    return time3

#This updates your current score
def updateScore(time3, level, score):
    score = score + time3 * 100 * level / (100 - level)
    return score

#Main screen for the rules page
def rules():
    ruleScreen = pygame.display.set_mode((800, 800))
    x = 75
    y = 175
    flag = 1
    ruleFont = pygame.font.Font('freesansbold.ttf', 20)
    headingFont = pygame.font.Font('freesansbold.ttf', 36)
    rulesList = ["1. You will be asked to find a letter somewhere in the grid.", "2. Click on the correct box with the letter to go to the next level.", 
    "3. Your score also depends on how fast you find the letter.", "4. The sooner you find it the more points you get.", "5. Every level, the size of the grid increases and so does the time.", 
    "6. If you click on the wrong box or time runs out, the game is over.", "7. To access the main menu, click on the X button."]
    running = True
    while running:
        if flag:
            ruleScreen.fill("Black")
            flag = 0
            text = headingFont.render("Rules", True, (255, 255, 255))
            ruleScreen.blit(text, (350, 100))
            pygame.draw.line(screen, "WHITE", (50, 50), (750, 50))
            pygame.draw.line(screen, "WHITE", (50, 50), (50, 750))
            pygame.draw.line(screen, "WHITE", (50, 750), (750, 750))
            pygame.draw.line(screen, "WHITE", (750, 750), (750, 50))
            pygame.draw.line(screen, "WHITE", (55, 55), (745, 55))
            pygame.draw.line(screen, "WHITE", (55, 55), (55, 745))
            pygame.draw.line(screen, "WHITE", (55, 745), (745, 745))
            pygame.draw.line(screen, "WHITE", (745, 745), (745, 55))
            for rule in rulesList:
                text = ruleFont.render(rule, True, (255, 255, 255))
                ruleScreen.blit(text, (x, y))
                y = y + 75
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

#Main menu page
def mainMenu():
    mainScreen = pygame.display.set_mode((800, 800))
    mainFont = pygame.font.Font('freesansbold.ttf', 36)
    headingFont = pygame.font.Font('freesansbold.ttf', 55)
    running = True
    while running:
        mainScreen.fill("Black") 
        text = headingFont.render("GridLocked", True, (255, 255, 255))
        mainScreen.blit(text, (240, 125))
        text = mainFont.render("PLAY", True, (255, 255, 255))
        mainScreen.blit(text, (350, 300))
        text = mainFont.render("RULES", True, (255, 255, 255))
        mainScreen.blit(text, (335, 450))
        text = mainFont.render("QUIT", True, (255, 255, 255))
        mainScreen.blit(text, (350, 600))
        pygame.draw.line(screen, "WHITE", (50, 50), (750, 50))
        pygame.draw.line(screen, "WHITE", (50, 50), (50, 750))
        pygame.draw.line(screen, "WHITE", (50, 750), (750, 750))
        pygame.draw.line(screen, "WHITE", (750, 750), (750, 50))
        pygame.draw.line(screen, "WHITE", (55, 55), (745, 55))
        pygame.draw.line(screen, "WHITE", (55, 55), (55, 745))
        pygame.draw.line(screen, "WHITE", (55, 745), (745, 745))
        pygame.draw.line(screen, "WHITE", (745, 745), (745, 55))
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] >= 285 and mousePos[0] <= 500 and mousePos[1] >= 275 and mousePos[1] <= 357:
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 275), (500, 275))
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 357), (500, 357))
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 275), (285, 357))
            pygame.draw.line(mainScreen, (255, 255, 255), (500, 275), (500, 357))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 280), (495, 280))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 352), (495, 352))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 280), (290, 352))
            pygame.draw.line(mainScreen, (255, 255, 255), (495, 280), (495, 352))
        
        if mousePos[0] >= 285 and mousePos[0] <= 500 and mousePos[1] >= 425 and mousePos[1] <= 507:
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 425), (500, 425))
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 507), (500, 507))
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 425), (285, 507))
            pygame.draw.line(mainScreen, (255, 255, 255), (500, 425), (500, 507))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 430), (495, 430))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 502), (495, 502))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 430), (290, 502))
            pygame.draw.line(mainScreen, (255, 255, 255), (495, 430), (495, 502))

        if mousePos[0] >= 285 and mousePos[0] <= 500 and mousePos[1] >= 575 and mousePos[1] <= 657:
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 575), (500, 575))
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 657), (500, 657))
            pygame.draw.line(mainScreen, (255, 255, 255), (285, 575), (285, 657))
            pygame.draw.line(mainScreen, (255, 255, 255), (500, 575), (500, 657))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 580), (495, 580))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 652), (495, 652))
            pygame.draw.line(mainScreen, (255, 255, 255), (290, 580), (290, 652))
            pygame.draw.line(mainScreen, (255, 255, 255), (495, 580), (495, 652))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if mouseX >= 285 and mouseX <= 500 and mouseY >= 275 and mouseY <= 357:
                        play(level)
                    if mouseX >= 285 and mouseX <= 500 and mouseY >= 425 and mouseY <= 507:
                        rules()
                    if mouseX >= 285 and mouseX <= 500 and mouseY >= 575 and mouseY <= 657:
                        running = False
        pygame.display.update()

#This colours the box red or green based on whether your answer is correct or not
def colourCorrect(xPos, yPos, lvl, flag):
    eachDistance = 700/(lvl+1)
    row = ((yPos - 50) // (700 // (lvl + 1)))
    col = ((xPos - 50) // (700 // (lvl + 1)))
    x = 50
    y = 50
    colourX = x + eachDistance * (col)
    colourY = y + eachDistance * (row)
    if flag:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(colourX, colourY, eachDistance, eachDistance))
    else:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(colourX, colourY, eachDistance, eachDistance))
    pygame.display.update()

#This displays your score at the end screen    
def displayScore(score):
    screen.fill("BLACK")
    font = pygame.font.Font('freesansbold.ttf', 36)
    text = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(text, (250, 300))
    text = font.render("Your score: " + "{:.2f}".format(score), True, (255, 255, 255))
    screen.blit(text, (250, 350))
    pygame.display.update()

#The main body of the code which controls everything
def play(level):
    score = 0
    answer = generateAnswer(letters, numbers)
    gridContents = generateGridValues(letters, numbers, answer, level)
    screen.fill("BLACK")
    displayAnswer(answer)
    disScore(score)
    makeGrid(level, gridContents)
    running = True
    t1 = time.time()
    totalTimer = 5
    while running:
        
        t2 = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if mouseX >= 50 and mouseY >= 50 and mouseX <= 750 and mouseY <=750:
                        flag = check(mouseX, mouseY, answer, gridContents, level)
                        if flag:
                            colourCorrect(mouseX, mouseY, level, flag)
                            makeGrid(level, gridContents)
                            pygame.display.update()
                            time.sleep(2)
                            level = level + 1
                            t1 = time.time()
                            totalTimer = totalTimer + 0.25
                            answer = generateAnswer(letters, numbers)
                            gridContents = generateGridValues(letters, numbers, answer, level)
                            score = updateScore(time3, level, score)
                        else:
                            colourCorrect(mouseX, mouseY, level, flag)
                            makeGrid(level, gridContents)
                            pygame.display.update()
                            time.sleep(2)
                            displayScore(score)
                            pygame.display.update()
                            time.sleep(2)
                            running = False
        
        screen.fill("BLACK")
        displayAnswer(answer)
        disScore(score)
        makeGrid(level, gridContents)
        time3 = displayTime(t1, t2, totalTimer)
        if time3 == 0:
            displayScore(score)
            pygame.display.update()
            time.sleep(2)
            running = False
        pygame.display.update()


mainMenu()