import pygame,sys,math,time
from pygame.locals import *
import Adafruit_BBIO.ADC as ADC
# set up a bunch of constants
WHITE= (255, 255, 255)
DARKRED = (128,0,0)
RED = (255,0,0)
BLACK= ( 0,0,0)
GREEN= ( 0, 255,0) ### HERE
BLUE= ( 0,0, 255) ### HERE
BGCOLOR = WHITE
WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2) # the midpoint for the width of the window
WIN_CENTERY = int(WINDOWHEIGHT / 2) # the midpoint for the height of the window
FPS = 160 # frames per second to run at
AMPLITUDE = 80 # how many pixels tall the waves with rise/fall.
# standard pygame setup code
pygame.init()
ADC.setup()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Waves')
#fontObj = pygame.font.Font('freesansbold.ttf', 16)
xPos = 0
yPos = 0
prevXpos = 0
prevYpos = 0
posRecord = {'wave':[]}
step = 0
while 1:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key== K_ESCAPE):
			pygame.quit()
			sys.exit()
	yPos = ADC.read("AIN0")*1.8*80
	xPos += 5
	posRecord['wave'].append((xPos,yPos))
	DISPLAYSURF.fill(BGCOLOR)
	for x,y in posRecord['wave']:
		pygame.draw.line(DISPLAYSURF,RED,(int(x),WIN_CENTERY-int(y)),(int(prevXpos),WIN_CENTERY-int(prevYpos)),1)
		prevXpos = int(x)
		prevYpos = int(y)
	prevXpos = 0
	prevYpos = 0
	if xPos > WINDOWWIDTH:
		xPos = 0
		posRecord['wave'] = []
	pygame.display.update()
	FPSCLOCK.tick(FPS)
	time.sleep(0.1)
