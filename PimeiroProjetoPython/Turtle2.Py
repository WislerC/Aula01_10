import turtle

# Configurações iniciais da tela
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Tartaruga Colorida")

# Criando uma tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(1)  # Define a velocidade da tartaruga (1 a 10)

# Função para desenhar o corpo da tartaruga
def desenhar_corpo():
    tartaruga.penup()
    tartaruga.goto(0, -90)
    tartaruga.pendown()
    tartaruga.fillcolor("black")
    tartaruga.begin_fill()
    tartaruga.circle(90)
    tartaruga.end_fill()

# Função para desenhar a boca da tartaruga
def desenhar_boca():
    tartaruga.penup()
    tartaruga.goto(20, -30)
    tartaruga.pendown()
    tartaruga.fillcolor("#8B4513")  # Marrom
    tartaruga.begin_fill()
    tartaruga.circle(10, 180)
    tartaruga.end_fill()

# Função para desenhar os olhos da tartaruga
def desenhar_olhos():
    # Olho direito
    tartaruga.penup()
    tartaruga.goto(10, 10)
    tartaruga.pendown()
    tartaruga.fillcolor("blue")
    tartaruga.begin_fill()
    tartaruga.circle(5)
    tartaruga.end_fill()
    
    # Olho esquerdo
    tartaruga.penup()
    tartaruga.goto(-10, 10)
    tartaruga.pendown()
    tartaruga.fillcolor("blue")
    tartaruga.begin_fill()
    tartaruga.circle(5)
    tartaruga.end_fill()

# Função para desenhar a boca cinza da tartaruga
def desenhar_boca_cinza():
    tartaruga.penup()
    tartaruga.goto(0, -30)
    tartaruga.pendown()
    tartaruga.fillcolor("gray")
    tartaruga.begin_fill()
    tartaruga.circle(5)
    tartaruga.end_fill()

# Chamando as funções para desenhar os componentes da tartaruga
desenhar_corpo()
desenhar_boca()
desenhar_olhos()
desenhar_boca_cinza()

# Mantém a janela aberta até que seja fechada pelo usuário
screen.mainloop()
