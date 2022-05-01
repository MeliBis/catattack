import pygame, random
pygame.init()
BLACK=(0,0,0)

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("./meterorito.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y +=1

		if self.rect.y > 600:
			self.rect.y = -10
			self.rect.x = random.randrange(900)
		

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("./cata.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, x):
		self.speed_x += x

	def update(self):
		self.rect.x += self.speed_x
		player.rect.y = 510
	

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("./laser.png").convert()
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 4

class Game(object):
	def __init__(self):
		self.game_over = False

		self.score = 0

		self.meteor_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()


WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("catAttack")
icono = pygame.image.load("./prueba3-cata.png").convert()
pygame.display.set_icon(icono)


clock = pygame.time.Clock()
done = False
score = 0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

meteor = Meteor()
for i in range(20):
	meteor = Meteor()
	meteor.rect.x = random.randrange(WIDTH - 20)
	meteor.rect.y = random.randrange(450) 

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()
def run_logic(self):

		if not self.game_over:
			self.all_sprites_list.update()

			meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

			for meteor in meteor_hit_list:
				self.score += 1
				print(self.score)

			if len(self.meteor_list) == 0:
				self.game_over = True

def display_frame(self, screen):
		screen.fill(WHITE)

		if self.game_over:
			font = pygame.font.SysFont("serif", 25) # Fuente
			text = font.render("Game Over, Click To Continue", True, BLACK) # Texto
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) # posicion text
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.blit(text, [center_x, center_y]) # ponerlo en pantalla

		if not self.game_over:
			self.all_sprites_list.draw(screen)


player = Player()

background= pygame.image.load("./backgroud-luna.png").convert()
pygame.mixer.music.load('./kim-lightyear-angel-eyes-chiptune-edit-110226.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

all_sprite_list.add(player)

sound = pygame.mixer.Sound('./LaserBlastQuick PE1095107.mp3')



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(3)
			if event.key == pygame.K_SPACE:
				laser = Laser()
				laser.rect.x = player.rect.x + 45
				laser.rect.y = player.rect.y - 20

				laser_list.add(laser)
				all_sprite_list.add(laser)
				sound.play()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(-3)
	all_sprite_list.update()

	meteor_hit_list= pygame.sprite.spritecollide(player, meteor_list, True)


	for meteor in meteor_list:
		meteor.rect.y +=1
	all_sprite_list.update() 

	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)	
		for meteor in meteor_hit_list:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
			score += 1
			print(score)
		if laser.rect.y < -10:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)


	#screen.fill([255, 255, 255])
	screen.blit(background,[0,0])

	all_sprite_list.draw(screen)

  

	pygame.display.flip()
	clock.tick(60)

pygame.quit()




