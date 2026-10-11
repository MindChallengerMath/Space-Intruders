import pygame as pyg

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




running = True
if __name__ == "__main__":
    pyg.init()
    defender = player()
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
        if defender.goodGuyX >= 600:
            defender.moveX = 0
            defender.goodGuyX -= 0.1
        elif defender.goodGuyX <= 0:
            defender.moveX = 0
            defender.goodGuyX += 0.1
        elif defender.goodGuyY >= 400:
            defender.moveY = 0
            defender.goodGuyY -= 0.1
        elif defender.goodGuyY <= 0:
            defender.moveY = 0
            defender.goodGuyY += 0.1
        
        screen.fill((49, 28, 79))
        defender.displayPlayer()
        defender.goodGuyX += defender.moveX
        defender.goodGuyY += defender.moveY
        pyg.display.update()