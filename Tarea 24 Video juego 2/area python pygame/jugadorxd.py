from gzip import WRITE
import pygame, random

#------------------------------------------------------------------------configuracion de ventana-------------------------------------------------------------------


#tamaño de la ventana

WIDTH = 1280
HEIGHT = 990

#Defino colores que seran utilizado mas adelante
BLACK = (0, 0, 0)
MORADO = (139, 69, 144)
WHITE = (225 , 225, 225)
AZUL = (60, 133, 223)


#inicializo el pygame

pygame.init()
pygame.mixer.init()

#Creacion de la ventana y su nombre ademas incluyendo las variables del tamaño indicadas anteriormente para la pantalla 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#nombre de la ventana
pygame.display.set_caption("Destruir tarea xd")

#Creacion del reloj del Control de FPS por segundo 
clock = pygame.time.Clock()


#Creacion del texto del marcador
def draw_text(surface, text, size, x, y):

	#indique tipo de letra
	font = pygame.font.SysFont("arial", size)
	#indique el color --------------------   ⬇   ---------------------------- segun la definicion colores con los numeros en la parte de arriba
	text_surface = font.render(text, True, MORADO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)


def draw_shield_bar(surface, x, y, percentage):
	
	#largo de la barra
	BAR_LENGHT = 150
	#Altura de la barra
	BAR_HEIGHT = 25
	#que tan llena sera la barra
	fill = (percentage / 100) * BAR_LENGHT

	#creo el borde de la barra
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)

	#creo el lleno de la barra
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)

	#indico que el color de la barra de  salud ya este siendo definidido en la parte superior
	pygame.draw.rect(surface, AZUL, fill)

	#indico que color tendra la barra y el tamaño de este
	pygame.draw.rect(surface, WHITE, border, 4)

#--------------------------------------------------------creacion del jugador------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
	
	#inicializo la clase
	def __init__(self):
		super().__init__()
		
		#Imagen del jugador
		self.image = pygame.image.load("cosas/nave.png").convert()

		#Remover borde y fondo negro de la imagen
		self.image.set_colorkey(BLACK)

		#obtener el cuadro de mi sprite (indica la posicion de la nave) 
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10

		#----------variable del escudo

		self.shield = 100

		#--------------------------------------movimiento del jugador

		#Variable de la velocidad
		self.speed_x = 0
		
	def update(self):
		#Variable de la velocidad
		self.speed_x = 0
		

		#Indicamos que se esta presionando teclado con la variable --keystate-- con las condiciones de pygame
		keystate = pygame.key.get_pressed()
		
		
		#Esto ira verificando que si la tecla a sido presionada haga la accion que le indiquemos

		#En Este Caso estamos indicando que si presionamos ← →  vaya a una cierta velocidad como en el eje tipo plano Cartesiano		
		if keystate[pygame.K_LEFT]:
			self.speed_x = -10
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 10
		
		#Le estoy sumando la velocidad que se le aplicara a cada eje segun lo que haiga puesto a cada letra del teclado
		self.rect.x += self.speed_x

		#Aqui se le agregan los limites de la ventana a la nave (esto para que no se salga fuera del limite visto por la ventana)

		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0


		#metodo del disparo del laser	(este indicando que saldra del centro de la imagen)
	def shoot(self):
		laser = Bala_Laser(self.rect.centerx, self.rect.top)  #(centerx = el centro de la imagen,      Top= el borde de la parte de arriba de la imagen)
		
		#indico que se agregue el contenido a los contendor de los sprites y tambien a la clase

		all_sprites.add(laser)
		Balas.add(laser)

		#agrego el sonido del laser (se creo la funcion de cargar la musica entre las ultimas partes del documento,  aqui en esta area solo estamos indicando que se reproduzca cada vez que dispare)
		sonido_laser.play()






#---------------------------------------------creacion de enemigo-------------------------------------------------------------

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		#imagen del enemigo (esta seleccionando de manera random de una lista creada en la parte de abajo en la linea 194)
		self.image = random.choice(imagenes_de_enemigos)


		#Remover borde y fondo negro de la imagen
		self.image.set_colorkey(BLACK)

		#obtener el cuadro de mi sprite (indica la posicion de enemigo en este caso aleatoreo)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-150, -110)
		
		#Velocidad de donde viene el enemigo de manera aleatorea
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)
	
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		
		#indico que si pasa el limite de la pantalla se repita sus acciones

		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)







#---------------------------------------------------------------------creacion de la bala laser -------------------------------------------------------------------------


class Bala_Laser(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("cosas/laser.png")
		
		#Remover borde y fondo negro de la imagen
		self.image.set_colorkey(BLACK)

		#obtener el cuadro de mi sprite 
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		
		#velocidad del disparo (indicando negativo para que vaya hacia arriba)
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy

		#con esto eliminimos el laser cuando llegue al limite para que no ocupe mas memoria
		if self.rect.bottom < 0:
			self.kill()


#----------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------crear la clase de la explosion------------------------------------------------------------------

class Explosion(pygame.sprite.Sprite):
	
	#la inicializion indicando el center  para que aparezca en el centro de la cosision de la imagen del enemigo
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # cuánto tiempo esperar para el siguiente cuadro "VELOCIDAD DE LA EXPLOSIÓN"

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill() # indicamos que  cuando llegamos al final de la animación no continuamos para no ocuapr memoria.
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

def show_go_screen():
    draw_text(screen, "Destructor de Tarea", 65, WIDTH// 2, HEIGHT // 4)
    draw_text(screen, "Hecho por Angel Steven #16", 27, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Presione la tecla espacio para empezar ", 20, WIDTH // 2, HEIGHT * 3/4)
    pygame.display.flip()

#-----------------------------------------------------------------Acciones de contencion del funcionamiento del juego-----------------------------------------------------------------------------------------

# Cargar fondo.
background = pygame.image.load("cosas/Fondo.png").convert()



#------------------------------------contenedor de imagenes de todos los enemigos esta para ser cargada en la clase meteor-------------------------------

#creo una area vacia para enemigos
imagenes_de_enemigos = []
#creo una variable con el contenido de todos los enemigos
lista_de_enemigos = ["cosas/e1.png","cosas/e2.png","cosas/e3.png","cosas/e4.png","cosas/e5.png","cosas/e6.png","cosas/e7.png","cosas/e8.png","cosas/e9.png","cosas/e10.png","cosas/e11.png","cosas/e12.png","cosas/e13.png","cosas/e14.png","cosas/e15.png","cosas/e16.png","cosas/e17.png"]
#creo un bucle que indica(que "img" es la "lista de enemigos", y que "img" se le agregue al area vacia de la variable" imagenes de enemigos" )
for img in lista_de_enemigos:
	imagenes_de_enemigos.append(pygame.image.load(img).convert())


#------------------------------------contenedor de imagenes de todos las explosiones---------------------------------------------------------------------

#creo una area vacia para las imagenes
explosion_anim = []
#indico cuantas imagenes hay en el rango (en total son 8 pero ponemos 9 para un espacio vacio)
for i in range(9):
	#ubicamos donde estan las imagenes---------------------⬇------- segun esto buscara todas las imagenes que tengan el mismo texto pero con la parte señalada como variante todas las variantes
	imagenes_de_animacion = "cosas/explo/regularExplosion0{}.png".format(i)
	#cargamos las imagenes
	img = pygame.image.load(imagenes_de_animacion).convert()
	#le quitamos el fondo negro
	img.set_colorkey(BLACK)

	#cambiar la escala o tamaño de la imagen
	img_scale = pygame.transform.scale(img, (100, 100))

	#lo agrego al area vacia para formar la lista
	explosion_anim.append(img_scale)



#------------------------------------Efecto de musica y sonidos-----------------------------------------------

sonido_laser = pygame.mixer.Sound("cosas/laser_efecto.ogg")
sonido_explosion = pygame.mixer.Sound("cosas/explosion.wav")
sonido_choque = pygame.mixer.Sound("cosas/choque.mp3")
sonido_muerte = pygame.mixer.Sound("cosas/muerte.mp3")
pygame.mixer.music.load("cosas/musica.mp3")
#volumen de la musica de fondo
pygame.mixer.music.set_volume(0.3)


#---------------------------------------------------------

#--------------------------------------------------------Creo la variable para el fin del juego

gameover = True

#---------------------------------------------------------reproduzco la musica de fondo
#con el loop indicamos cuantas veces queremos que se reproduzca, aunque si lo ponemos con menos uno {-1} la repetira infinitamente
pygame.mixer.music.play(loops =-1)

# Bucle del juego
running = True
while running:

	if gameover:
		gameover = False
		
		#Contenedor de las acciones del sprite
		all_sprites = pygame.sprite.Group()
		meteor_list = pygame.sprite.Group()
		Balas = pygame.sprite.Group()

		#indico que se agregue el contenido a los contendores
		player = Player()
		all_sprites.add(player)


		# en el rango indique la cantidad que quiero que aparezca de enemigos
		for i in range(15):
			meteor = Meteor()
			all_sprites.add(meteor)
			meteor_list.add(meteor)

			#--------------------------------------creo esta variable para el marcador
		score = 0


	#Indica la velocidad de los FPS segun el reloj que creamos anteriormente
	# Mantenga el bucle funcionando a la velocidad correcta
	clock.tick(60)

	
	# Entrada de proceso (eventos)
	for event in pygame.event.get():
		
		#Evento de cierre o de cargar el fin del juego (game over)
		if event.type == pygame.QUIT:
			running = False
		

		#evento de teclado dicho con el 'KEYDOWN'(Con el "K.SPACE"  decimos que es la tecla "espacio")
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:      
				player.shoot()   #con eso indicamos que dispare

	# Indicamos la actualizacion de todas las acciones de los sprites en la ventana
	
	all_sprites.update()



	#-----------------------------------------------------------------Colisiones-----------------------------------------------------------------------------------------
	#colisiones del meteoro y la nave

	golpe_nave =pygame.sprite.spritecollide(player, meteor_list, True)
	for si_me_golpea in golpe_nave:
		
		sonido_choque.play()

		#variable del escudo le estoy

		#Estoy indicando que el escudo que vale 100 segun la variable creada en el area del jugardor esta se le vaya bajanndo segun la cantidad que le indicamos:
		player.shield -= 25
		# que despues de cada golpe se repita el meteoro
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)

		#indico que inicie la explosion y que se guarde en el contenedor de todos los  sprites

		explosion1 = Explosion(si_me_golpea.rect.center)
		all_sprites.add(explosion1)

		
		#indico que cuando el escudo lleque a 0 haga lo siguiente:
		
		if player.shield <= 0:
			sonido_muerte.play()
			gameover = True

	#colisiones del meteoro y el laser

	golpes_meteoro_laser = pygame.sprite.groupcollide(meteor_list, Balas, True, True)
	for golpesito in golpes_meteoro_laser:
		
		#indico que cada vez que haga la colision con el laser, la variable "score" = el marcador se le vaya sumando uno
		score+= 1
		#indico que inicie la explosion y que se guarde en el contenedor de todos los  sprites

		explosion = Explosion(golpesito.rect.center)
		all_sprites.add(explosion)

		#cargo el sonido de la explosion con cada colision con el laser y los enemigos
		sonido_explosion.play()
		#osea cada vez que lo elimine vuelva aparecer arriba esto ocurriendo por yo estar llamando la clase meteoro
		
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)
	#----------------------------------------------------------------------------------------------------------------------------------------------------------------------





	#Dibujar / Renderizar
	#estamos indicando que todos los sprite aparescan en la ventana
	
	#En esta area estamos indicando que aparezca el fondo en la ventana segun la variable , ademas indicando la pocision de esta, en este caso (0,0) para que quede en el centro
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)

	#indicando el marcador segun la funcion creada y que aparezca en pantalla dandole su posicion

	draw_text(screen, str(score), 30, WIDTH//2, 10 )

	#indicando el la barra de salud segun la funcion creada y que aparezca en pantalla dandole su posicion de cordenadas

	draw_shield_bar(screen, 565, 50, player.shield)

	# *después* de dibujar todo, voltea la pantalla.
	pygame.display.flip()

pygame.quit()


               


       