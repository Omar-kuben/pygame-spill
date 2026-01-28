import pygame as pg
pg.init()
class Ball:
    def __init__(self, x_pos:int, y_pos:int, radius:float, fart:int, vindu:pg.surface.Surface, farge:tuple):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._radius = radius
        self._fart = fart
        self._vindu = vindu
        self._farge = farge

    def tegne(self):
        pg.draw.circle(self._vindu, self._farge, (self._x_pos, self._y_pos), self._radius)
    def flytt(self,trykkede_taster):
        
        if trykkede_taster[pg.K_UP] and self._y_pos > self._radius:
            self._y_pos -= self._fart
        
        elif trykkede_taster[pg.K_DOWN] and self._y_pos < self._vindu.get_height() - self._radius:
            self._y_pos += self._fart

        elif trykkede_taster[pg.K_LEFT] and self._x_pos  > self._radius:
            self._x_pos -= self._fart

        elif trykkede_taster[pg.K_RIGHT] and self._x_pos < self._vindu.get_width() - self._radius:
            self._x_pos += self._fart

class Rektangel:
    def __init__(self, x, y, bredde, hoyde, fart, vindu):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.hoyde = hoyde
        self.fart = fart
        self.vindu = vindu

    def tegne(self):
        pg.draw.rect(self.vindu, (255,0,0), (self.x,self.y,self.bredde,self.hoyde)) #xpos ypos bredde høyde
    def flytt(self):
        if self.y <= 0  or self.y >= self.vindu.get_height() - self.hoyde: 
            self.fart = -self.fart
        self.y -= self.fart


class Sluttested:
    def __init__(self, x, y, bredde, hoyde, vindu):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.hoyde = hoyde
        self.vindu = vindu

    def tegne(self):
        pg.draw.rect(self.vindu, (0,0,0), (self.x,self.y,self.bredde,self.hoyde))        



VINDU_BREDDE = 700
VINDU_HOYDE  = 650
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
 
pg.display.flip()
 
ball = Ball(25, 350, 25, 0.1, vindu,(255,0,0))
firekant = Rektangel(350,350,50,50,0.1,vindu)
sluttAreal = Sluttested(650, 300, 80, 80, vindu)

fortsett = True 
while fortsett:
    vindu.fill((255,255,255))
    ball.tegne()
    firekant.tegne()
    sluttAreal.tegne()
    pg.display.flip()
 
    trykkede_taster = pg.key.get_pressed()
    ball.flytt(trykkede_taster)
    firekant.flytt()
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False  
pg.quit()

