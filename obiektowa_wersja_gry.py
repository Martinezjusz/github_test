class Pracownik:
    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja
    
    def przedstaw_sie(self):
        print(f"Imię: {self.imie}")
        print(f"Stanowisko: {self.stanowisko}")
        print(f"Pensja: {self.pensja} PLN")
    
    def oblicz_wynagrodzenie(self):
        return self.pensja

class PelnoetatowyPracownik(Pracownik):
    def __init__(self, imie, stanowisko, pensja, urlop):
        super().__init__(imie, stanowisko, pensja)
        self.urlop = urlop
    
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Przyznany urlop: {self.urlop} dni")
    
    def oblicz_wynagrodzenie(self):
        bonus = self.urlop * 50  # Za każdy dzień urlopu bonus 50 PLN
        return self.pensja + bonus

class Kontraktor(Pracownik):
    def __init__(self, imie, stanowisko, stawka_godzinowa, godziny_pracy):
        super().__init__(imie, stanowisko, 0)  # Kontraktor nie ma stałej pensji
        self.stawka_godzinowa = stawka_godzinowa
        self.godziny_pracy = godziny_pracy
    
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Stawka godzinowa: {self.stawka_godzinowa} PLN")
        print(f"Liczba godzin pracy: {self.godziny_pracy}")
    
    def oblicz_wynagrodzenie(self):
        return self.stawka_godzinowa * self.godziny_pracy

pracownik_etatowy = PelnoetatowyPracownik("Anna Kowalska", "Kierownik Projektu", 8000, 20)
kontraktor = Kontraktor("Jan Nowak", "Programista", 100, 160)

print("Pracownik etatowy:")
pracownik_etatowy.przedstaw_sie()
print(f"Wynagrodzenie: {pracownik_etatowy.oblicz_wynagrodzenie()} PLN\n")

print("Kontraktor:")
kontraktor.przedstaw_sie()
print(f"Wynagrodzenie: {kontraktor.oblicz_wynagrodzenie()} PLN")
