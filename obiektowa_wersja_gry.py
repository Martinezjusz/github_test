import turtle
import random
import time

Edit 1
Edit 2
Edit 3
Edit 4
Edit 5

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
