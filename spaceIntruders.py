import pygame as pyg
import random
import sys
windowX = 500
windowY = 500
windowHeight = 500
windowWidth = 650
screen = pyg.display.set_mode((windowWidth, windowHeight))
title = "Space Invader"
windowTitle = pyg.display.set_caption(title)
icon = pyg.image.load("images/invaderGameIcon.ico")
goodGuy = pyg.image.load("images/GoodGuy.png")
enemy = pyg.image.load("images/Enemy.png")
bullet = pyg.image.load("images/Bullet.png")
displayIcon = pyg.display.set_icon(icon)

class player():
    def __init__(self):
        super().__init__()
        self.goodGuyX = windowWidth / 2
        self.goodGuyY = windowHeight*0.8
        self.moveX = 0.1
        self.moveY = 0
        self.displayPlayer()

    def displayPlayer(self): 
        screen.blit(goodGuy, (self.goodGuyX, self.goodGuyY))

class Enemy():
    def __init__(self):
        self.enemyModel = enemy
        self.enemyX = random.uniform(10, windowWidth - 50)
        self.enemyY = windowHeight * random.uniform(0.1, 0.2)
        self.moveX = 0.05
    def displayEnemy(self):
        screen.blit(self.enemyModel, (self.enemyX, self.enemyY))
        self.movement()
    def movement(self):
        self.enemyX += self.moveX
        if self.enemyX >= windowWidth - 50:
            self.enemyX -= 0.1
            self.enemyY += 50
            self.moveX = -0.05
        elif self.enemyX <= 0:
            self.enemyX += 0.1
            self.enemyY += 50
            self.moveX = 0.05
        if self.enemyY <= 0:
            self.enemyY += 50
        self.trick = random.randint(1, 10000)
        if self.trick == 20:
            self.moveX = random.uniform(-0.09, 0.09)
            self.secondTrick = random.randint(1, 10)
            if self.secondTrick == 1:
                self.enemyY += random.randint(-50, 50)






running = True
if __name__ == "__main__":
    pyg.init()
    defender = player()
    intruder = Enemy() 
    army = []
    for i in range(1, 11):
        intruder = Enemy()
        army.append(intruder)
    armyList = [i for i in sys.modules.values() if i is not None]
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_d:
                    defender.moveX = 0.1
                    defender.moveY = 0
                elif event.key == pyg.K_a:
                    defender.moveX = -0.1
                    defender.moveY = 0
                elif event.key == pyg.K_w:
                    defender.moveX = 0
                    defender.moveY = -0.1
                elif event.key == pyg.K_s:
                    defender.moveX = 0
                    defender.moveY = 0.1
        if defender.goodGuyX >= windowWidth - 50:
            defender.moveX = 0
            defender.goodGuyX -= 0.1
        elif defender.goodGuyX <= 0:
            defender.moveX = 0
            defender.goodGuyX += 0.1
        elif defender.goodGuyY >= windowHeight - 100:
            defender.moveY = 0
            defender.goodGuyY -= 0.1
        elif defender.goodGuyY <= 0:
            defender.moveY = 0
            defender.goodGuyY += 0.1
        
        screen.fill((49, 28, 79))
        for i in range(len(army)):
            army[i].displayEnemy()
        intruder.displayEnemy()
        defender.displayPlayer()
        defender.goodGuyX += defender.moveX
        defender.goodGuyY += defender.moveY
        pyg.display.update()