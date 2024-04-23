import turtle
import time
import random

Liste = []
skor = 0
maxSkor = 0

# çerçeve ayarları
w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600, 600)
w.bgcolor("white")
w.tracer(0)

# yılanın kafası
yn = turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("red")
yn.penup()
yn.goto(0, 0)
yn.yon = "dur"

# yem nesnesini tanımla
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("blue")
yem.penup()
yem.goto(0, 100)

def hareket():
    if yn.yon == "ust":
        y = yn.ycor()
        yn.sety(y + 20)
    if yn.yon == "alt":
        y = yn.ycor()
        yn.sety(y - 20)
    if yn.yon == "sag":
        x = yn.xcor()
        yn.setx(x + 20)
    if yn.yon == "sol":
        x = yn.xcor()
        yn.setx(x - 20)

def yukariGit():
    if yn.yon != "alt":
        yn.yon = "ust"

def asagiGit():
    if yn.yon != "ust":
        yn.yon = "alt"

def sagaGit():
    if yn.yon != "sol":
        yn.yon = "sag"

def solaGit():
    if yn.yon != "sag":
        yn.yon = "sol"

def ye():
    global skor, maxSkor
    if yn.distance(yem) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("red")
        kuyruk.penup()
        Liste.append(kuyruk)
        
        skor += 5
        if skor > maxSkor:
            maxSkor = skor
            w.title("Skor: {} En yüksek skor: {}".format(skor, maxSkor))
            
def kuyruğu_takip_et():
    uzunluk = len(Liste)
    for i in range(uzunluk - 1, 0, -1):
        prev_x = Liste[i - 1].xcor()
        prev_y = Liste[i - 1].ycor()
        Liste[i].goto(prev_x, prev_y)
    if uzunluk > 0:
        Liste[0].goto(yn.xcor(), yn.ycor())

def baslangic():
    global skor
    global maxSkor
    time.sleep(0.1)
    yn.goto(0, 0)
    yn.yon = "dur"
   
    for eklem in Liste:
        eklem.goto(1000, 1000)
    Liste.clear()
    skor = 0
    w.title("Skor: {} En yüksek puan:{}".format(skor, maxSkor))

w.listen()
w.onkeypress(yukariGit, "Up")
w.onkeypress(asagiGit, "Down")
w.onkeypress(sagaGit, "Right")
w.onkeypress(solaGit, "Left")

while True:
    w.update()
    hareket()
    ye()
    kuyruğu_takip_et()
    
    # Yılanın sınırlara çarpıp çarpmadığını kontrol et
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        baslangic()
    
    # Yılanın kuyruğuna çarpıp çarpmadığını kontrol et
    for eklem in Liste:
        if eklem.distance(yn) < 20:
            baslangic()

    time.sleep(0.1)

w.mainloop()
