# Importación de todas las librerías necesarias
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

# Inicialización de pygame y carga de sonidos
pygame.init()
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.load("media/bajavida.ogg")
sonido_correcto = pygame.mixer.Sound("media/correcto.ogg")
sonido_correcto.set_volume(0.3)
sonido_incorrecto = pygame.mixer.Sound("media/incorrecto.ogg")
sonido_incorrecto.set_volume(0.1)

# Lista de listas de preguntas y respuestas
preguntasRespuestas = [
    ["¿Cuánto es 1 + 1?", "2"],
    ["¿Cuántos dedos tiene una mano?", "5"],
    ["¿Qué animal hace el sonido 'miau'?", "Gato"],
    ["¿Cuántas patas tiene una araña?", "8"],
    ["¿Cuántas estaciones del año hay?", "4"],
    ["¿Cómo se llama el astro rey alrededor del cual gira la Tierra?", "Sol"],
    ["¿Cuántos días tiene el mes de febrero en un año no bisiesto?", "28"],
    ["¿Cuál es el resultado de sumar todos los lados de un triángulo?", "180 grados"],
    ["¿Cómo se llama el líquido que cae del cielo en forma de gotas?", "Lluvia"],
    ["¿Cuál es el color del cielo en un día despejado?", "Azul"],
    ["¿Cuántos huesos tiene el cuerpo humano?", "206"],
    ["¿Cuántos dedos tiene un pie?", "5"],
    ["¿Cuál es el primer mes del año?", "Enero"],
    ["¿Cuál es el día que sigue a lunes?", "Martes"],
    ["¿Cómo se llama el objeto que usamos para ver objetos lejanos?", "Telescopio"],
    ["¿Cuántos minutos hay en una hora?", "60"],
    ["¿Cuál es el planeta más cercano al Sol?", "Mercurio"],
    ["¿Qué animal es famoso por ser el mejor amigo del hombre?", "Perro"],
    ["¿Cuántos lados tiene un cuadrado?", "4"],
    ["¿En qué temporada caen las hojas de los árboles?", "Otoño"],
    ["¿Cómo se llama el lugar donde vivimos?", "Casa"],
    ["¿Cuál es la capital de España?", "Madrid"],
    ["¿Cuál es el resultado de multiplicar 5 por 3?", "15"],
    ["¿Cómo se llama la parte del cuerpo que usamos para oler?", "Nariz"],
    ["¿Cuántos colores tiene un arco iris?", "7"],
    ["¿Cuál es la moneda oficial de Estados Unidos?", "Dólar"],
    ["¿Cuántas letras tiene la palabra 'gato'?", "4"],
    ["¿Qué número sigue después del 9?", "10"],
    ["¿Cómo se llama la persona que cuida nuestros dientes?", "Dentista"],
    ["¿Cuántos días tiene una semana?", "7"],
    ["¿Cuál es el resultado de restar 8 a 15?", "7"],
    ["¿Cuál es el país conocido como la Tierra del Sol Naciente?", "Japón"],
    ["¿Cómo se llama el cuerpo celeste que ilumina la noche?", "Luna"],
    ["¿Cuál es la capital de Francia?", "París"],
    ["¿Cuál es el resultado de dividir 10 entre 2?", "5"],
    ["¿Cómo se llama el líquido que bebemos para mantenernos hidratados?", "Agua"],
    ["¿Cuál es el animal más grande del mundo?", "Ballena azul"],
    ["¿Qué instrumento se utiliza para medir el tiempo?", "Reloj"],
    ["¿Cuántos dientes tiene un adulto?", "32"],
    ["¿Cuál es el resultado de sumar 2 más 3?", "5"],
    ["¿Cómo se llama el lugar donde estudiamos?", "Escuela"],
    ["¿Cuál es el resultado de sumar 6 más 4?", "10"],
    ["¿Cómo se llama la capa externa de la Tierra?", "Corteza"],
    ["¿Cuántos ojos tiene una persona?", "2"],
    ["¿Cuál es el resultado de multiplicar 4 por 5?", "20"],
    ["¿Cómo se llama la estación del año en la que hace más calor?", "Verano"],
]

# Inicialización de variables globales
numeroR = random.randrange(0, len(preguntasRespuestas))
puntuacionV = 0
vidas = 3
tiempoRestante = 11
cantidadPreguntas = len(preguntasRespuestas)
primerTurno = True

# Creación de la ventana principal
ventana = Tk()
ventana.title("El Juego del Gato Inteligente")
ventana.resizable(False, False)
ventana.iconphoto(True, PhotoImage(file="media/gatito.png"))

# Carga de imágenes y creación de labels para las mismas
gatoN = Image.open("media/NEUTRALCAT.png")
gatoN = gatoN.resize((600, 337))
gatoN = ImageTk.PhotoImage(gatoN)
gatoNL = Label(ventana, image=gatoN)

gatoF = Image.open("media/HAPPYCAT.png")
gatoF = gatoF.resize((600, 337))
gatoF = ImageTk.PhotoImage(gatoF)
gatoFL = Label(ventana, image=gatoF)

gatoV = Image.open("media/VOIDCAT.png")
gatoV = gatoV.resize((600, 337))
gatoV = ImageTk.PhotoImage(gatoV)
gatoVL = Label(ventana, image=gatoV)

tresV = Image.open("media/3v.png")
tresV = ImageTk.PhotoImage(tresV)
tresVL = Label(ventana, image=tresV)
tresVL.grid(row=4, column=0, columnspan=3)

dosV = Image.open("media/2v.png")
dosV = ImageTk.PhotoImage(dosV)
dosVL = Label(ventana, image=dosV)

unaV = Image.open("media/1v.png")
unaV = ImageTk.PhotoImage(unaV)
unaVL = Label(ventana, image=unaV)

ceroV = Image.open("media/0v.png")
ceroV = ImageTk.PhotoImage(ceroV)
ceroVL = Label(ventana, image=ceroV)

gatoNL.grid(row=0, column=0, columnspan=3)


# Función que comprueba si la respuesta es correcta o incorrecta
def comprobar():
    global gatoNL, gatoFL, gatoVL, primerTurno, puntuacionV, puntuacion, vidas, responder, tiempoRestante
    # Comprueba si es el primer turno, si es así, comienza la cuenta regresiva
    if primerTurno:
        primerTurno = False
        instruccion.config(text="¡¡¡ESCRIBE TU RESPUESTA!!!")
        cuentaRegresiva()
    else:
        # Comprueba si la respuesta es correcta o incorrecta
        gatoNL.grid_forget()
        if responder.get().lower() == preguntasRespuestas[numeroR][1].lower():
            preguntasRespuestas.pop(numeroR)
            gatoFL.grid(row=0, column=0, columnspan=3)
            puntuacionV += 1
            sonido_correcto.play()
            tiempoRestante = 11
            puntuacion.config(text="Puntuación: " + str(puntuacionV))
            instruccion.config(text="¡¡¡CORRECTO!!!")
        else:
            # Si la respuesta es incorrecta, se resta una vida y se cambia la imagen del gato
            gatoVL.grid(row=0, column=0, columnspan=3)
            preguntasRespuestas.pop(numeroR)
            vidas -= 1
            sonido_incorrecto.play()
            tiempoRestante = 11
            # Dependiendo de la cantidad de vidas, se cambia la imagen del gato y se muestra la cantidad de vidas restantes
            match vidas:
                case 2:
                    tresVL.grid_forget()
                    dosVL.grid(row=4, column=0, columnspan=3)
                case 1:
                    dosVL.grid_forget()
                    ventana.after(1000, musica)
                    unaVL.grid(row=4, column=0, columnspan=3)
                case 0:
                    unaVL.grid_forget()
                    ceroVL.grid(row=4, column=0, columnspan=3)
            # Si las vidas llegan a 0, se detiene la música, se desactiva el campo de respuesta y se muestra un mensaje de derrota
            if vidas == 0:
                pygame.mixer.music.stop()
                responder.config(state=DISABLED)
                tiempoRestante = 0
                pregunta.config(text="El Gato está decepcionado...")
                messagebox.showinfo(
                    "¡¡¡PERDISTE!!!", "Tu puntuación fue: " + str(puntuacionV)
                )
                reiniciarBtn.grid(row=5, column=0, columnspan=3)
            instruccion.config(text="¡¡¡INCORRECTO!!!")
    # Si las vidas son mayores a 0, se restaura la imagen del gato, la pregunta y el campo de respuesta
    if vidas > 0:
        ventana.after(1000, restaurar)


# Función que reproduce la música
def musica():
    pygame.mixer.music.play(-1)


# Función que restaura la imagen del gato, la pregunta y el campo de respuesta
def restaurar():
    global gatoNL, gatoFL, gatoVL, numeroR, btnSubirPuntuacion
    numeroR = random.randrange(0, len(preguntasRespuestas))
    gatoFL.grid_forget()
    gatoVL.grid_forget()
    gatoNL.grid(row=0, column=0, columnspan=3)
    responder.delete(0, END)
    responder.focus_set()
    pregunta.config(text=preguntasRespuestas[numeroR][0])
    instruccion.config(text="¡¡¡ESCRIBE TU RESPUESTA!!!")


# Función que reinicia el juego desde cero
def reiniciar():
    global gatoNL, gatoFL, gatoVL, numeroR, primerTurno, puntuacionV, puntuacion, vidas, responder
    global pregunta, instruccion, reiniciarBtn, tresVL, dosVL, unaVL, ceroVL, tiempoRestante, tiempoL, preguntasRespuestas

    # Lista de listas de preguntas y respuestas reinsertada para que no se quede sin preguntas al reiniciar
    preguntasRespuestas = [
        ["¿Cuánto es 1 + 1?", "2"],
        ["¿Cuántos dedos tiene una mano?", "5"],
        ["¿Qué animal hace el sonido 'miau'?", "Gato"],
        ["¿Cuántas patas tiene una araña?", "8"],
        ["¿Cuántas estaciones del año hay?", "4"],
        ["¿Cómo se llama el astro rey alrededor del cual gira la Tierra?", "Sol"],
        ["¿Cuántos días tiene el mes de febrero en un año no bisiesto?", "28"],
        [
            "¿Cuál es el resultado de sumar todos los lados de un triángulo?",
            "180 grados",
        ],
        ["¿Cómo se llama el líquido que cae del cielo en forma de gotas?", "Lluvia"],
        ["¿Cuál es el color del cielo en un día despejado?", "Azul"],
        ["¿Cuántos huesos tiene el cuerpo humano?", "206"],
        ["¿Cuántos dedos tiene un pie?", "5"],
        ["¿Cuál es el primer mes del año?", "Enero"],
        ["¿Cuál es el día que sigue a lunes?", "Martes"],
        ["¿Cómo se llama el objeto que usamos para ver objetos lejanos?", "Telescopio"],
        ["¿Cuántos minutos hay en una hora?", "60"],
        ["¿Cuál es el planeta más cercano al Sol?", "Mercurio"],
        ["¿Qué animal es famoso por ser el mejor amigo del hombre?", "Perro"],
        ["¿Cuántos lados tiene un cuadrado?", "4"],
        ["¿En qué temporada caen las hojas de los árboles?", "Otoño"],
        ["¿Cómo se llama el lugar donde vivimos?", "Casa"],
        ["¿Cuál es la capital de España?", "Madrid"],
        ["¿Cuál es el resultado de multiplicar 5 por 3?", "15"],
        ["¿Cómo se llama la parte del cuerpo que usamos para oler?", "Nariz"],
        ["¿Cuántos colores tiene un arco iris?", "7"],
        ["¿Cuál es la moneda oficial de Estados Unidos?", "Dólar"],
        ["¿Cuántas letras tiene la palabra 'gato'?", "4"],
        ["¿Qué número sigue después del 9?", "10"],
        ["¿Cómo se llama la persona que cuida nuestros dientes?", "Dentista"],
        ["¿Cuántos días tiene una semana?", "7"],
        ["¿Cuál es el resultado de restar 8 a 15?", "7"],
        ["¿Cuál es el país conocido como la Tierra del Sol Naciente?", "Japón"],
        ["¿Cómo se llama el cuerpo celeste que ilumina la noche?", "Luna"],
        ["¿Cuál es la capital de Francia?", "París"],
        ["¿Cuál es el resultado de dividir 10 entre 2?", "5"],
        ["¿Cómo se llama el líquido que bebemos para mantenernos hidratados?", "Agua"],
        ["¿Cuál es el animal más grande del mundo?", "Ballena azul"],
        ["¿Qué instrumento se utiliza para medir el tiempo?", "Reloj"],
        ["¿Cuántos dientes tiene un adulto?", "32"],
        ["¿Cuál es el resultado de sumar 2 más 3?", "5"],
        ["¿Cómo se llama el lugar donde estudiamos?", "Escuela"],
        ["¿Cuál es el resultado de sumar 6 más 4?", "10"],
        ["¿Cómo se llama la capa externa de la Tierra?", "Corteza"],
        ["¿Cuántos ojos tiene una persona?", "2"],
        ["¿Cuál es el resultado de multiplicar 4 por 5?", "20"],
        ["¿Cómo se llama la estación del año en la que hace más calor?", "Verano"],
    ]

    # Reinicialización de variables globales
    numeroR = random.randrange(0, len(preguntasRespuestas))
    primerTurno = True
    puntuacionV = 0
    vidas = 3
    gatoFL.grid_forget()
    gatoVL.grid_forget()
    gatoNL.grid(row=0, column=0, columnspan=3)
    responder.config(state=NORMAL)
    responder.delete(0, END)
    responder.focus_set()
    pregunta.config(text="Prepárate...")
    instruccion.config(text="Da enter en el campo para comenzar")

    ceroVL.grid_forget()
    tresVL.grid(row=4, column=0, columnspan=3)
    reiniciarBtn.grid_forget()
    puntuacion.config(text="Puntuación: 0")
    tiempoRestante = 11
    tiempoL.config(text="Tiempo restante: " + str(tiempoRestante))


# Función que inicia la cuenta regresiva y actualiza el tiempo restante
def cuentaRegresiva():
    global tiempoRestante

    if tiempoRestante > 0:
        tiempoRestante -= 1
        tiempoL.config(text="Tiempo restante: " + str(tiempoRestante))
        ventana.after(1000, cuentaRegresiva)
    elif tiempoRestante < 1 and vidas > 0:
        responder.config(state=DISABLED)
        pregunta.config(text="El Gato está decepcionado...")
        sonido_incorrecto.play()
        pygame.mixer.music.stop()
        messagebox.showinfo("¡¡¡PERDISTE!!!", "Tu puntuación fue: " + str(puntuacionV))
        tresVL.grid_forget()
        dosVL.grid_forget()
        unaVL.grid_forget()
        ceroVL.grid_forget()
        reiniciarBtn.grid(row=4, column=0, columnspan=3)


# Creación y colocación de los widgets
pregunta = Label(ventana, text="Prepárate...")
pregunta.grid(row=1, column=0, columnspan=3)

puntuacion = Label(ventana, text="Puntuación: 0")
puntuacion.grid(row=0, column=2, sticky=NE)

tiempoL = Label(ventana, text="Tiempo restante: ")
tiempoL.grid(row=0, column=0, sticky=NW)

instruccion = Label(ventana, text="Da enter en el campo para comenzar")
instruccion.grid(row=2, column=0, columnspan=3)

responder = Entry(ventana, width=60)
responder.bind("<Return>", lambda x: comprobar())
responder.grid(row=3, column=0, columnspan=3)

reiniciarBtn = Button(ventana, text="Reiniciar", command=lambda: reiniciar())

# Inicio de la ventana principal
mainloop()
