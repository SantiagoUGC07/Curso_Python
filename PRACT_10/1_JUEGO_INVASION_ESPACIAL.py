#JUEGO INVASION ESPACIAL
'''
Se requiere instalar la libreria de pygame por cmd con el sig comando
    pip install pygame
'''
import pygame
import random
import math
from pygame import mixer#para poder agregar musica
import pylint

#se inicializar a pygame
pygame.init()

#crear el display de la pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e icono de la ventana
pygame.display.set_caption("Inavasion Espacial")
icono = pygame.image.load("Icono_esfera_32px_es_recomendable.jpg")#aqui cargamos la imagen, lo recomendable es un icono de 32px png
pygame.display.set_icon(icono)#colocar el icono en la pantalla

#AGREGAR MUSICA
mixer.music.load('fondo_music_dragon_ball.mp3')
mixer.music.set_volume(0.2)# 0.2 para bajar el volumen a la quita parte de su volumen
mixer.music.play(-1)# -1 se pone para que se repita cuando acabe

#VARIABLES PERSONAJE
img_jugador = pygame.image.load("goku_64px_sin_fondo.png")
jugador_x=344#poscicion del jugandor en pantalla, se dividio 800 que es el anocho de pantalla 400 y se le resto la mitad del ancho del personaje 56 =344
jugador_y=440#se resta 600 de la pantalla menos 150 del alto de la imagen
jugador_x_cambio=0

#VARIABLES ENEMIGO
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio= []
enemigo_y_cambio= []
cantidad_enemigos = 8
#CREACION DE LOS ENEMIGOS CON LOOP
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("nave_sin_fondo.png"))
    enemigo_x.append(random.randint(0,680))#se resto 120px de la imagen enemigo menos el ancho de pantalla 800px para tener un aprox del rango
    enemigo_y.append(random.randint(50,200))#con random y randint le decimos a los ejes que la imagen puede aparecer aleatoriamente en un rango  de 50, 200 px en pantalla
    enemigo_x_cambio.append(3.5)# la taza de cambio en px, para que se mueva el enemigo, debe ser igual alas que se tienen en los limites de pantalla
    enemigo_y_cambio.append(50)

#VARIABLE MUNDO
fondo=pygame.image.load(("mundo_sin_fondo.png"))

#VARIABLE KAMEHAME
img_kamehame=pygame.image.load("kameha_sin_fondo.png")
kamehame_x = 0 #poscicion donde iniciara el kame
kamehame_y = 400#posicion donde comienza el kamehame
kamehame_x_cambio= 0#no se ocupa esta dado a que no tienen movimiento en x
kamehame_y_cambio= 8 #velocidad de movimiento
kamehame_visible= False#se coloca en falso dado que al inicio del juego no se vera

#FUNCION PARA MOSTRAR JUGADOR
def jugador(x,y):#se le envian parametros para mover al personaje
    pantalla.blit(img_jugador,(x,y))#blit arroja o muestra al jugador en pantalla

#FUNCION PARA MOSTRAR ENEMIGO
def enemigo(x,y,E):#se le envian parametros para mover al personaje
    pantalla.blit(img_enemigo[E],(x,y))#blit arroja o muestra al jugador en pantalla, se coloca [E] para generar distintos enegmigos

#FUNCION LANZAR KAMEHAME HA
def lanzar_kamehame(x,y):#se le envian parametros para mover el kamehame
    global kamehame_visible #la variable es tipo global, para que pueda ser visible
    kamehame_visible = True#y una vez que se lance cambia a True para que se pueda ver
    pantalla.blit(img_kamehame,(x+29, y+15))#se les suman pixeles a X y Y para que aparezcan en medio de goku

#FUNCION DETECTAR COLISION
def hay_colision(x_1,y_1,x_2,y_2):

    distancia= math.sqrt(math.pow(x_1-x_2,2)+math.pow(y_2-y_1,2))#esta es la formula de distancia entre dos objetos en un plano bidimensional
    if distancia < 27:
        return True
    else:
        return False
#PUNTAJE POR COLISION
puntaje = 0 #llevar el puntaje de los enemigos que matamos
#fuente = pygame.font.Font("freesansbold.ttf", 32)#esta fuete viene incorporada en pygame para textos, font sirve para incluir fuentes
fuente = pygame.font.Font("Gerlyonz Jimakes.otf", 32)#para importar una fuente descargada de internet
texto_x = 10 #para posicionarlos en la pantalla
texto_y = 10 #para poscicionarlos en la pantalla

#TEXTO FINAL DE JUEGO importando la fuente descargada
fuente_final = pygame.font.Font('Flanela.TTF.ttf',40)#el tamaño de 40 px
def texto_final():#funcion del texto final
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(280,250))#280 y 250 para que el texto quede centrado

#FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    #render significar renderizar o mostrar en pantalla el texto, mas un antialias y el color de la fuente a mostrar
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))# se coloca True por que pide un booleano o antialias y el color blanco en RGB
    pantalla.blit(texto,(x,y))#Monstrar en pantalla el texto con el color y la fuente


'''
evento: todo lo que ocurra en una pantalla de pygame es un evento
'''
#LOOP PARA MANTENER LA PANTALLA ABIERTA Y JUEGO
se_ejecuta = True
while se_ejecuta:
    #ASIGNAR
    #AQUI SE AGINA EL COLOR DE LA PANTALLA RGB, se coloca al inicio del loop para evitar que tape lo demas
    #pantalla.fill((242, 142, 55))#para poner un fondo RGB
    pantalla.blit(fondo,(0,0))#como queremos que abarque toda la pantalla se pone la coordenada (0,0)
    #jugador_x -=0.1#la resta hace que el jugador se mantenga moviendo ala izq
    #EVENTOS
    for evento in pygame.event.get():#event.get() cuando alguien de click
        #EVENTO PARA SALIR DE LA PANTALLA
        if evento.type == pygame.QUIT:#QUIT sirve para salir de la pantalla, cuando se de click en la X de la ventana
            se_ejecuta = False#se cambia a false y se sale del loop, asi nos salimos de la pantalla
        #EVENTO PRESIONAR TECLA
        if evento.type == pygame.KEYDOWN:#ENVENTO TECLAS MOVIMIENTO
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio=-6#para mover en 0.3 a la izq el jugador, se cambio a 2.5 por que se agrego una imagen de fondo
            if evento.key == pygame.K_RIGHT:#EVENTO TECLAS MOVIMIENTO
                jugador_x_cambio= 6
            if evento.key == pygame.K_SPACE:#EVENTO KAMEHAME ESPACIO
                sonido_kamehame=mixer.Sound('kamehame.mp3')#se agrega el sonido aqui para cuando aprietes space se reproduzca el sonido
                sonido_kamehame.set_volume(0.1)#disminuir el sonido del kamehame
                sonido_kamehame.play()#para reproducir el sonido
                if kamehame_visible == False: #solo se aplican si el kamehame no esta en la pantalla
                    kamehame_x = jugador_x#de esta manera el kamehame no sigue al jugador
                    lanzar_kamehame(kamehame_x,kamehame_y)#
        #EVENTO SUELTA TECLA
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0#para que no se mueva el jugador cuando se suelten las flechas

    #LLAMANDO FUNCIONES O EVENTOS
    #MOVIMIENTO JUGADOR
    jugador_x+=jugador_x_cambio#SUMAR O RESTAR VALORES A LAS CORDENADAS X
    #MANETENER AL JUGADOR EN LOS LIMITES DE LA PANTALLA
    if jugador_x <= 0:
        jugador_x=0
    elif jugador_x >= 675:#se resta el ancho de goku menos el de la pantalla 150px-800px=650 para hacer un calculop aprox
        jugador_x=675
    #MANETENER AL ENEMIGO EN LOS LIMITES DE LA PANTALLA y CAMBIARMOVIMIENTO AUTOMATICO
    for e in range(cantidad_enemigos):#PARA GENERAR MAS ENEMIGOS Y QUE LOS MOVIMIENTOS SE ASIGNEN POR SU POSICION EN LA LISTA [e]
        #FIN DE JUEGO
        if enemigo_y[e] > 450:# e para revisar si algun enemigo alcanzo el final de la pantalla
            for k in range(cantidad_enemigos):#k Para tomar en cuenta a todos los enemigos
                enemigo_y[k] = 1000# k para posicionar a todos los enemigos fuera de la pantalla y asi terminar el juego
            texto_final()
            break
        #MOVIMIENTO ENEMIGO
        enemigo_x[e] += enemigo_x_cambio[e]
        if enemigo_x[e] <= 0: #cuando el enemigo llegue al limite cambia de direccion y aumentan los px en los ejes de Y
            enemigo_x_cambio[e]=3.5#el movimiento que tendra automatico el enemigo, sin necesidad de apretar teclas
            enemigo_y[e] +=enemigo_y_cambio[e]
        elif enemigo_x[e] >= 680:#se resta el ancho de la nave menos el de la pantalla 120px-800px=680 para hacer un calculop aprox
            enemigo_x_cambio[e]=-3.5
            enemigo_y[e] += enemigo_y_cambio[e]
        #COLISION KAMEHAME Y NAVE, esta dentro del for para que las colisiones se posicionen con los enemigos por eso solo se pone el indice [e] a los enemigos
        colision = hay_colision(enemigo_x[e],enemigo_y[e],kamehame_x,kamehame_y)
        if colision:
            sonido_colision = mixer.Sound("explosion.mp3")#agregar sonido cuando colisionen
            sonido_colision.set_volume(0.3)#bajar el sonido de explosion
            sonido_colision.play()#reproducir el sonido de explosion
            kamehame_y=400#cuando hay una colision restablecer kamehame a su posicion inicial
            kamehame_visible=False#y dejar de ser visible
            puntaje += 1
            enemigo_x[e] = random.randint(0,680)#se colocan los valores iniciales del enemigo para restablecerlo una vez muerto
            enemigo_y[e] = random.randint(50, 200)
        # MOSTRAR ENEMIGO
        enemigo(enemigo_x[e],enemigo_y[e],e)#para mostrar distintos enemigos con sus diferentes posiciones
    #MOVIMIENTO KAMEHAME
    if kamehame_y <= -60:#la cantidad de pixeles de alto del kamehame, asi saber si desaparecio de la pantalla y no siga en los ejes de la y
        kamehame_y=400 #donde iniciara de nuevo el kamehame
        kamehame_visible=False #dejara de ser visible, hasta que se dispare
    if kamehame_visible:#si kamehame es ==True
        lanzar_kamehame(kamehame_x,kamehame_y)#llamamos a la funcion
        kamehame_y -= kamehame_y_cambio

    #MOSTRAR JUGADOR
    jugador(jugador_x,jugador_y)#MOSTRAR al jugador en pantalla
    #MOSTRAR PUNTAJE
    mostrar_puntaje(texto_x,texto_y)
    #MANTENER LA PANTALLA ACTUALIZANDOSE
    pygame.display.update()#para que la pantalla se actualice y se muestre



