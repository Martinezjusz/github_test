import turtle
import random
import time


class Zolw:
    def __init__(self, color, start_x, start_y):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(start_x, start_y)
        self.turtle.zakres_losowania = [2, 6]
        self.turtle.showturtle()

    def move(self):
        self.turtle.forward(random.randint(self.turtle.zakres_losowania[0], self.turtle.zakres_losowania[1]))

    def get_position(self):
        return self.turtle.position()

    def get_color(self):
        return self.turtle.color()[0]

    def zwieksz_zakres(self):
        self.turtle.zakres_losowania[0] += 1
        self.turtle.zakres_losowania[1] += 1


class Wyscig:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Wyścig żółwi")
        self.screen.bgcolor("lightblue")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.zolwie = []
        self.wygrany = None
        self.odpowiedz = None

    def rysuj_mete(self):
        kolor_linii_mety = ['white', 'black']
        kolor = 0

        meta = turtle.Turtle()
        meta.penup()
        meta.color('black')
        meta.pensize(10)
        meta.goto(283, 300)
        meta.pendown()
        meta.speed(0)
        meta.setheading(270)

        for _ in range(100):
            meta.color(kolor_linii_mety[kolor])
            meta.forward(9)
            kolor = 1 - kolor

    def stworz_zolwie(self):
        kolory = ['red', 'green', 'blue', 'brown', 'pink']
        for i in range(len(kolory)):
            zolw = Zolw(kolory[i], -280, -220 + i * 100)
            self.zolwie.append(zolw)

    def zwiekszanie_zakresu(self):
        for zolw in self.zolwie:
            if zolw.get_color() == self.odpowiedz:
                zolw.zwieksz_zakres()

    def gra(self):
        self.rysuj_mete()
        self.stworz_zolwie()

        self.odpowiedz = self.screen.textinput("Zakład", "Na którego żółwia obstawiasz? (red/green/blue/brown/pink)")

        self.screen.listen()
        self.screen.onkey(self.zwiekszanie_zakresu, "a")

        game_on = True

        while game_on:
            self.screen.update()
            for zolw in self.zolwie:
                zolw.move()
                time.sleep(0.015)
                if zolw.get_position()[0] > 275:
                    self.wygrany = zolw.get_color()
                    game_on = False

        if self.odpowiedz == self.wygrany:
            print("Gratulacje! Wygrałeś!")
        else:
            print(f"Niestety, przegrałeś. Wygrał żółw o kolorze {self.wygrany}")

        self.screen.exitonclick()


wyscig = Wyscig()
wyscig.gra()