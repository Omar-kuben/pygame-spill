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

    
   

        
 
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
 
pg.display.flip()
 
ball = Ball(30, 255, 25, 0.1, vindu,(255,0,0))
 
fortsett = True
while fortsett:
    vindu.fill((255,255,255))
    ball.tegne()
    pg.display.flip()
 
    trykkede_taster = pg.key.get_pressed()
    ball.flytt(trykkede_taster)
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False  
pg.quit()

