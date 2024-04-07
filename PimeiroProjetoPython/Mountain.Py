import turtle
import time

# Configurações iniciais da tela
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Carro Subindo uma Montanha")

# Criando uma tartaruga para representar o carro
carro = turtle.Turtle()
carro.shape("square")
carro.color("red")
carro.penup()

# Função para desenhar a montanha com curvas
def desenhar_montanha():
    carro.goto(-300, -250)  # Posição inicial
    carro.pendown()
    for _ in range(4):  # Loop para desenhar a montanha com curvas
        carro.left(45)
        carro.forward(50)
        carro.right(45)
        carro.forward(100)
        carro.right(45)
        carro.forward(50)
        carro.left(45)
    carro.penup()

# Função para mover o carro pela montanha
def subir_montanha():
    for _ in range(10):  # Loop para simular 10 segundos
        carro.setx(carro.xcor() + 10)  # Movendo o carro para frente
        carro.sety(0.01 * (carro.xcor() ** 2))  # Movendo o carro para cima
        time.sleep(1)  # Aguardando 1 segundo entre cada movimento

# Chamando a função para desenhar a montanha com curvas
desenhar_montanha()

# Chamando a função para mover o carro pela montanha
subir_montanha()

# Mantém a janela aberta até que seja fechada pelo usuário
screen.mainloop()
