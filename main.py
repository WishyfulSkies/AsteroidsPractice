import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	AsteroidField.containers = (updatable,)
	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
                	if event.type == pygame.QUIT:
                        	return

		screen.fill((0,0,0))

		for object in drawable:
			object.draw(screen)

		for object in updatable:
			object.update(dt)

		for asteroid in asteroids:
			if asteroid.CollisionCheck(player):
				exit("Game over!")

			for shot in shots:
				if asteroid.CollisionCheck(shot):
					asteroid.split()
					shot.kill()
				

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
