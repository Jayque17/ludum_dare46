#!/usr/bin/env python3

from pygame_functions import *
from random import randint

WIDTH = 1000
HEIGHT = 800


class Butterfly:
    """
    Class to build a butterfly
    """
    def __init__(self, speed):

        self.x = WIDTH//20 
        self.y = 3*(HEIGHT//4) 
        self.h = 65
        self.w = 60
        self.speed = speed
        self.sprite = makeSprite("images/butterfly3.png")
        self.dead = False
        
    def move(self):
        
        if keyPressed("left"):
            
            if self.x - self.w/2 > 0:
                self.x -= self.speed
        
        elif keyPressed("right"):
            
            if self.x + self.w/2 < WIDTH:
                self.x += self.speed
        
        elif keyPressed("up"):
            
            if self.y - self.h/2 > 0:
                self.y -= self.speed
        
        elif keyPressed("down"):
            
            if self.y + self.h/2 < HEIGHT:
                self.y += self.speed
        
    def draw(self):

        showSprite(self.sprite)
        moveSprite(self.sprite, self.x, self.y, True)
        

class Bird:
    """
    Class to build a bird.
    """
    def __init__(self, speed):
        
        self.x = WIDTH
        self.y = 3*HEIGHT/5
        self.w = 100
        self.h = 140
        self.speed = speed
        self.spritebi = makeSprite("images/bird.png")
        self.spriteb = makeSprite("images/lbeak1.png")
        addSpriteImage(self.spriteb, "images/lbeak2.png")
        addSpriteImage(self.spriteb, "images/lbeak3.png")
        addSpriteImage(self.spriteb, "images/beak4.png")
        self.spi = 0
        self.eat = False
    
    def draw(self):

        showSprite(self.spriteb)
        showSprite(self.spritebi)
        changeSpriteImage(self.spriteb, self.spi)            
        moveSprite(self.spriteb, self.x - 50, self.y - 35)
        moveSprite(self.spritebi, self.x + 40, self.y - 30)
        
    def moveUpDown(self, but):

        if but.x < self.x:

                if self.y  > 0 and self.y > but.y - but.h: 
                    self.y -= self.speed
                    self.spi = 1
                
                elif self.y + self.h < HEIGHT and self.y + self.h < but.y + but.h:
                    self.y += self.speed
                    self.spi = 2
                
                elif self.y <  but.y + but.h < self.y + self.h:
                    self.spi = 0

    def moveForward(self):

        self.x -= self.speed

    def catch(self, but):

        if (self.x < but.x < (self.x + self.w)) and \
        ((self.y < (but.y + but.h/2 - 5) < (self.y + self.h)) \
        or (self.y < (but.y - but.h/2 + 5) < (self.y + self.h))):
            but.dead = True
            self.eat = True
            self.spi = 3


class Spider:
    """
    Class to build a spider.
    """
    def __init__(self, speed):

        self.x = WIDTH
        self.y = 0
        self.w = 100
        self.h = 80
        self.speed = speed
        self.fall = True 
        self.sprite = makeSprite("images/spider.png")
        addSpriteImage(self.sprite, "images/spider2.png")
        self.eat = False
    
    def draw(self):
        
        if self.eat:
            changeSpriteImage(self.sprite, 1)
            moveSprite(self.sprite, self.x, 0)
        
        else:
            drawLine(self.x + self.w/2, 0, self.x + self.w/2, self.y, "white")
            moveSprite(self.sprite, self.x, self.y)

        showSprite(self.sprite)
        
    def fallRise(self):

        if self.fall:
            self.y += self.speed

            if self.y + self.h >= HEIGHT/2:
                self.fall = False
        else:
            self.y -= self.speed

            if self.y == 0:
                self.fall = True
    
    def eatButterfly(self, but):
        
        if (self.x < but.x < (self.x + self.w)) and \
        ((self.y < (but.y + but.h/2 - 5) < (self.y + self.h)) \
        or (self.y < (but.y - but.h/2 + 5) < (self.y + self.h))):
           but.dead = True
           self.eat = True


class Frog:
    """
    Class to build a frog
    """
    def __init__(self, speed):

        self.x = WIDTH
        self.y = 8.5*HEIGHT//10
        self.w = 120
        self.h = 130
        self.sprite = makeSprite("images/frog.png")
        addSpriteImage(self.sprite, "images/frog2.png")
        self.speed = speed 
        self.mx = 0
        self.my = 0
        self.tx = 0
        self.ty = 0
        self.tongue = []
        self.max = False
        self.sprite_t = makeSprite("images/tongue.png")
        self.eat = False

    def findNorme(self, but):

        self.tongue.append([self.mx, self.my])
        norme = (((self.mx - but.x)**2 + (self.my - but.y)**2))**(1/2)
        self.tx = (self.mx/norme) - (but.x/norme)
        self.ty = (self.my/norme) - (but.y/norme)

    def stickOutTongue(self, but):

        if self.max == False:

            if len(self.tongue) == 0:
                self.findNorme(but)

            else:
                self.tongue.append([self.tongue[-1][0] - self.tx*self.speed, \
                self.tongue[-1][1] - self.ty*self.speed])
                
                if (self.tongue[0][0] - self.tongue[-1][0] >= HEIGHT//3 \
                and but.x <= self.mx) \
                or (self.tongue[-1][0] - self.tongue[0][0] >= HEIGHT//3 \
                and but.x > self.mx) \
                or (self.tongue[0][1] - self.tongue[-1][1] >= HEIGHT//3 \
                and but.y <= self.my) \
                or (self.tongue[-1][1] - self.tongue[0][-1] >= HEIGHT//3 \
                and but.y > self.my) \
                or (self.tongue[-1][1] >= HEIGHT):
                    self.max = True
                                                
    def swallowButterfly(self, but):

        if len(self.tongue) > 0:

            for i in self.tongue:

                if ((but.x - but.w/2 < i[0] < but.x + but.w/2) \
                and (but.y - but.h/2 < i[1] < but.y + but.h/2)) \
                or ((self.x < but.x < (self.x + self.w)) and \
                ((self.y < (but.y + but.h/2 - 5) < (self.y + self.h)) \
                or (self.y < (but.y - but.h/2 + 5) < (self.y + self.h)))):
                    but.dead = True
                    self.eat = True

    def closeMouth(self):

        if self.max == True:
            self.tongue.pop(-1)

            if len(self.tongue) == 0:
                self.max = False

    def draw(self):

        if self.eat:
            changeSpriteImage(self.sprite, 1)
        showSprite(self.sprite)
        moveSprite(self.sprite, self.x - 40, self.y - 50)

    def drawT(self, but):

        self.mx = self.x + (self.w)/2
        self.my = self.y + 25
        self.stickOutTongue(but)
        self.closeMouth()

        if len(self.tongue) > 0:
            
            drawLine(self.tongue[0][0], self.tongue[0][1], \
            self.tongue[-1][0], self.tongue[-1][1], "red", 5)
            showSprite(self.sprite_t)
            moveSprite(self.sprite_t, self.tongue[-1][0], self.tongue[-1][1], True)


def scrollEnemy(speed, enemy):
    
    enemy.x -= speed

def scrollTongue(speed, frog):

    if len(frog.tongue) > 0:
        for i in frog.tongue:
            i[0] -= speed

def addPredators(predators):

    speed = randint(1, 5)
    pred = randint(0, 100)

    if pred == 0:
        
        if len(predators) > 0:
            
            if (predators[-1].x + predators[-1].w + 15) <= WIDTH:
                    predators.append(Frog(speed))
        
        else:
            predators.append(Frog(speed))

    elif pred == 1:
        
        if len(predators) > 0:
            
            if (predators[-1].x + predators[-1].w + 15) <= WIDTH:
                    predators.append(Spider(speed))
        
        else:
            predators.append(Spider(speed))

def useSkillPredators(predators, sp_scroll):

    if len(predators) > 0:

        for pred in predators:
            scrollEnemy(sp_scroll, pred)
            pred.draw()
            
            if type(pred) == Spider:
                pred.fallRise()
                pred.eatButterfly(but)
            
            else:
                scrollTongue(sp_scroll, pred)
                pred.swallowButterfly(but)
                pred.drawT(but)

def emptyPredators(predators):

    if len(predators) > 0:

        for pred in predators:

            if pred.x + pred.w <= 0:
                killSprite(pred.sprite)
                if type(pred) == Frog:
                    killSprite(pred.sprite_t)
                predators.pop(predators.index(pred))

def summonbird(bird):

    if bird.x + bird.w <= 0:
        bird.x += WIDTH


if __name__ == "__main__":

    setAutoUpdate(False)
    
    screenSize(WIDTH, HEIGHT)
    setBackgroundImage(["images/perfect_bkgd.png"])
    
    but = Butterfly(5)
    bird = Bird(2.5)
    predators = []

    fps = 90
    sp_scroll = 2

    keyLabel = makeLabel("Esc for exit, Arrows for move, Space for hide", 20, 0, 0, "orange")
    showLabel(keyLabel)

    while not(but.dead):

        if keyPressed("space"):
            hideLabel(keyLabel)

        if keyPressed("esc"):
            break

        scrollBackground(-sp_scroll, 0)

        emptyPredators(predators)
        addPredators(predators)
        useSkillPredators(predators, sp_scroll)
        summonbird(bird)
        
        bird.draw()
        but.draw()

        bird.moveForward()
        bird.moveUpDown(but)
        bird.catch(but)
        
        but.move()

        tick(fps)
        updateDisplay()

    hideAll()

    scrollBackground(-sp_scroll, 0)
    
    if bird.eat == True:
        bird.draw()
    
    else:
        for pred in predators:
            if pred.eat == True:
                pred.draw()

    endWait()
