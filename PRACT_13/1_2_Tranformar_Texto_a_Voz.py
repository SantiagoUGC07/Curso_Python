import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

#Escuchar nuestro Microfono y devolver el audio como Texto
def transformar_audio_en_texto():
    #alamacenar recognizer en variable
    r = sr.Recognizer()
    #Configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de esperar
        r.pause_threshold = 0.8
        #informar que comenzo la grabacion
        print("ya puedes hablar")
        #guardar lo que escuche como audio
        audio = r.listen(origen)
        #manejor de errores
        try:
            #buscar en google
            pedido = r.recognize_google(audio, language = "es-es")
            #prueba de que pudo ingresar
            print("Dijiste: " +  pedido)
            #devolver pedido
            return pedido
        #en caso de que no comprenda
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print("no entendi, me repites porfa")
            return "sigo esperando"
        except sr.RequestError:
            #prueba de que no compredio el audio
            print("No hay servicio")
            #devolver error
            return "sigo esperando"
        except:
            #prueba de que no comprendio el audio
            print("algo ha salido mal")
            return "sigo esperando"
#transformar_audio_en_texto()

#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)#para que se tome la primera voz.
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
#hablar("Hola mundo")

#voces de las que se dispone en las librerias
'''
engine = pyttsx3.init()
    for voz in engine.getProperty('voices'):
    print(voz) #se MUESTRAN LAS VOCES que se tienen disponibles
'''
    #ESTE LINK para descargar nuevas voces
    #https://support.microsoft.com/es-es/topic/descargar-idiomas-y-voces-para-lector-inmersivo-el-modo-lectura-y-lectura-en-voz-alta-4c83a8d8-7486-42f7-8e46-2b0fdf753130
#Opciones de voz / idioma
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


#informar dia de la semana
def pedir_dia():
    #crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)
    #crear una variable para el dai de semana
    dia_semana = dia.weekday()
    print(f"hoy es {dia_semana}")
    #diccionario con nombres de dias
    calendario = {0: 'lunes',
                  1: 'martes',
                  2: 'miercoles',
                  3: 'jueves',
                  4: 'viernes',
                  5: 'sabado',
                  6: 'domingo'}
    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')
#hablar("Hola uriel, espero que tengas un buen dia") #para que diga el texto

#Informar que hora es
def pedir_hora():
    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos  y {hora.second} segundos '#se reproduce el texto
    print(hora)
    #decir la hora
    hablar(hora)


#funcion saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:#definir que horario es.
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'
    #decir el saludo
    hablar(f"{momento}, soy Helena, tu asistente personal, por favor, dime en que te puedo ayudar")



#funcion central del asistente
def pedir_cosas():
    #activar el saludo inicial
    saludo_inicial()
    #variable de corte
    comenzar = True
    #loop central
    while comenzar:
        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar("con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir google' in pedido:
            hablar('claro, estoy en eso')
            webbrowser.open('https://www.google.com.mx')
            continue
        elif 'qué día es hoy' in pedido:#es importante poner los acentos para que detecte bien
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('claro, Buscando en wikipedia')
            pedido = pedido.replace('buscar en wikipedia', '')#el string vacio es para almacenar la busqueda. de wikipedia.
            wikipedia.set_lang('es')#para decirle que busque en indioma español
            resultado = wikipedia.summary(pedido, sentences=1)#sentences que lea solo el parrafo 1
            hablar("Wikipedia dice lo siguiente: ")
            hablar(resultado)
        elif 'buscar en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('buscar en internet','')#solo colocar la palabra que se dease buscar
            pywhatkit.search(pedido)#para buscar en google
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('buena idea, ya comeinzo a reproducirlo')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))#contar chiste en es español
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()#el "de" para marcar un stop el -1 para que vaya hasta el ultimo elemento de la lista y strip para eliminar el espacio en blanco
            cartera = {'apple': 'APPL',#para realizar la busqueda de la aacion
                       'amazon': 'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]#se guarda el valor del string que buscaremos
                accio_buscada = yf.Ticker(accion_buscada)#yf es yahoo finance que nos ayudara a buscar la accion
                precio_actual = accion_buscada.info['regularMarketPrice']#buscaremos dentro del diccionario que regresa accion_buscada.info la clave regularmarketprice para obtener esa info en especifico
                hablar(f"la encontre, el precio de {accion} es { precio_actual}")#con esto obtenemos la respuesta del precio
                continue
            except:
                hablar("perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()
