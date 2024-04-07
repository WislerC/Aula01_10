import turtle

# Configurações iniciais da tela
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Desenhando com Tartaruga")

# Criando uma tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(1)  # Define a velocidade da tartaruga (1 a 10)

# Função para desenhar um quadrado
def desenhar_quadrado():
    for _ in range(4):
        tartaruga.forward(100)
        tartaruga.right(90)

# Chamando a função para desenhar um quadrado
desenhar_quadrado()

# Mantém a janela aberta até que seja fechada pelo usuário
screen.mainloop()

