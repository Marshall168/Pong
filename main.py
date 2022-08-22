import pygame, sys
from settings import *
import random


def animation():
	global SPEED_X, SPEED_Y, score, enemy_score
	
	# Move the ball
	ball.x += SPEED_X
	ball.y += SPEED_Y


	# Basic Wall Collision and Scores *FIX*
	if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
		SPEED_Y *= -1

	if ball.left <= 0:
		score += 1
		ball_restart()

	if ball.right >= SCREEN_WIDTH:
		enemy_score += 1
		ball_restart()

	# Rect Collisions
	if ball.colliderect(player) or ball.colliderect(enemy):
		SPEED_X *= -1
		
def player_animation():
	player.y += SPEED
	# Player Collision
	if player.top <= 0:
		player.top = 0
	if player.bottom >= SCREEN_HEIGHT:
		player.bottom = SCREEN_HEIGHT
def enemy_animation():
	if enemy.top < ball.y:
		enemy.top += ESPEED
	if enemy.bottom > ball.y:
		enemy.bottom -= ESPEED
	if enemy.top <= 0:
		enemy.top = 0
	if enemy.bottom >= SCREEN_HEIGHT:
		enemy.bottom = SCREEN_HEIGHT

def ball_restart():
	global SPEED_X, SPEED_Y

	ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	SPEED_Y *= random.choice((1,-1))
	SPEED_X *= random.choice((1,-1))

SPEED_X = SPEED_X * random.choice((1,-1))
SPEED_Y = SPEED_Y * random.choice((1,-1))

# Setup
pygame.init()
clock = pygame.time.Clock()

# Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Classic Pong')

# Rectangles
ball = pygame.Rect(SCREEN_WIDTH/2 -15, SCREEN_HEIGHT/2 -15, 30, 30)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 50, 10,100)
enemy = pygame.Rect(10, SCREEN_HEIGHT/2 - 50, 10,100)

player_color = pygame.Color('coral')
background_color = pygame.Color('grey5')

# Text
score = 0
enemy_score = 0
font = pygame.font.Font("freesansbold.ttf", 40)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit() 
		
		# Move Player
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				SPEED += 7
			if event.key == pygame.K_UP:
				SPEED -= 7

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				SPEED -= 7
			if event.key == pygame.K_UP:
				SPEED += 7

	animation()
	player_animation()
	enemy_animation()


# Drawings
	screen.fill(background_color)
	pygame.draw.rect(screen, player_color, player)
	pygame.draw.rect(screen, player_color, enemy)
	pygame.draw.ellipse(screen, player_color, ball)
	pygame.draw.aaline(screen, player_color, (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))


# Player Score
	player_text = font.render(f"{score}", False, 'coral')
	screen.blit(player_text, (700, 50))

# Enemy Score
	enemy_text = font.render(f"{enemy_score}", False, 'coral')
	screen.blit(player_text, (560, 50))

	pygame.display.flip()
	clock.tick(60)