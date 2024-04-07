import turtle
import random
import time

# Configurações iniciais da tela
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Passarinhos Voando no Céu")

# Lista de cores para os pássaros
cores = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "pink", "gray", "black"]

# Função para desenhar um pássaro
def desenhar_passaro(cor):
    passaro = turtle.Turtle()
    passaro.speed(0)
    passaro.color(cor)
    passaro.shape("turtle")
    passaro.penup()
    return passaro

# Função para mover um pássaro aleatoriamente no céu
def voar(passaro):
    passaro.setx(random.randint(-380, 380))
    passaro.sety(random.randint(100, 250))

# Lista para armazenar os pássaros
passaros = []

# Criando 50 pássaros de cores diferentes
for _ in range(50):
    cor = random.choice(cores)
    passaro = desenhar_passaro(cor)
    voar(passaro)
    passaros.append(passaro)

# Função para mover os pássaros durante 20 segundos
def voar_durante_20_segundos():
    tempo_inicial = time.time()
    while time.time() - tempo_inicial < 20:
        for passaro in passaros:
            passaro.setx(passaro.xcor() + random.randint(-10, 10))
            passaro.sety(passaro.ycor() + random.randint(-5, 5))

# Chamando a função para mover os pássaros durante 20 segundos
voar_durante_20_segundos()

# Mantém a janela aberta até que seja fechada pelo usuário
screen.mainloop()
