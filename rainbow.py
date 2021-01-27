import pygame
import random

#:)

pygame.init()

#win settings
width = 1500
height = 900

x = 0
y = 0
z = 1

y1 = height
x1 = 0

r1 = random.randint(0, 255)
g1 = random.randint(0, 255)
b1 = random.randint(0, 255)

r2 = random.randint(0, 255)
g2 = random.randint(0, 255)
b2 = random.randint(0, 255)

#r1 = 0
#g1 = 0
#b1 = 0

#r2 = 255
#g2 = 255
#b2 = 255

countR = r2 - r1
countG = g2 - g1
countB = b2 - b1

numberR = countR / width
numberG = countG / width
numberB = countB / width

#other settings
run = True

#functions

win = pygame.display.set_mode((width, height))
pygame.display.flip()

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if x <= width and x >= 0:
		pygame.draw.line(win, [round(r1), round(g1), round(b1)], [x, y], [x, y1], 1)

		x = x + z
		
		r1 = r1 + numberR
		g1 = g1 + numberG
		b1 = b1 + numberB
	else:
		x = x - z
		z = z - z * 2
		r1 = r2
		g1 = g2
		b1 = b2

		r2 = random.randint(0, 255)
		g2 = random.randint(0, 255)
		b2 = random.randint(0, 255)

		countR = r2 - r1
		countG = g2 - g1
		countB = b2 - b1

		numberR = countR / width
		numberG = countG / width
		numberB = countB / width

	pygame.display.update()