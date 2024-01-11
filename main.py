import pygame
import sys
import numpy as np

theta3 = np.deg2rad(45)

p0 = [0, 0]
p1 = [0, 0]
p2 = [0, 0]
p3 = [12, 5]

l1 = 4
l2 = 4
l3 = 4

x = 0
y = 0
theta1 = 0
theta2 = 0

pygame.init()
WIN = pygame.display.set_mode((800, 500))

scale = 20

clicked = False

while True:
    WIN.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        theta3+=0.0025
    if keys[pygame.K_RIGHT]:
        theta3-=0.0025
    
    if clicked:
        mouse_pos = pygame.mouse.get_pos()

        p3[0] = (mouse_pos[0] - 400)/scale
        p3[1] = (mouse_pos[1] - 250)/scale*-1

    p2[0] = p3[0] - (l3*np.cos(theta3))
    p2[1] = p3[1] - (l3*np.sin(theta3))

    theta2 = np.arccos(((p2[0]*p2[0]) + (p2[1]*p2[1]) - (l1*l1) - (l2*l2))/(2*l1*l2))
    theta1 = np.arctan2(p2[1], p2[0]) - np.arctan2((l2 * np.sin(theta2)), (l1 + l2 * np.cos(theta2)))

    p1[0] = l1*np.cos(theta1)
    p1[1] = l1*np.sin(theta1)

    print(f"{np.rad2deg(theta1)} {np.rad2deg(theta2)}")

    pygame.draw.line(WIN, (255,255,255), (p0[0]*scale + 400, p0[1]*scale*-1 + 250), (p1[0]*scale + 400, p1[1]*scale*-1 + 250), 2)
    pygame.draw.line(WIN, (255,255,255), (p1[0]*scale + 400, p1[1]*scale*-1 + 250), (p2[0]*scale + 400, p2[1]*scale*-1 + 250), 2)
    pygame.draw.line(WIN, (255,255,255), (p2[0]*scale + 400, p2[1]*scale*-1 + 250), (p3[0]*scale + 400, p3[1]*scale*-1 + 250), 2)

    pygame.draw.circle(WIN, (255,255,255), (p3[0]*scale + 400, p3[1]*scale*-1 + 250), 5)
    pygame.draw.circle(WIN, (155,155,155), (p0[0]*scale + 400, p0[1]*scale*-1 + 250), 3)
    pygame.draw.circle(WIN, (255,0,0), (p1[0]*scale + 400, p1[1]*scale*-1 + 250), 5)
    pygame.draw.circle(WIN, (155,155,155), (p2[0]*scale + 400, p2[1]*scale*-1 + 250), 3)

    pygame.display.flip()