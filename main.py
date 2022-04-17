from tkinter import *

zliczanie_ocen = []
zliczanie_wag = []


class Application(Frame):
    column = 3

    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.waga = None
        self.ocena = None
        self.ilosc_ocen = None
        self.name_var = StringVar()
        self.txt1 = None
        self.grid()
        self.create_widgets()
        global zliczanie_wag
        global zliczanie_ocen

    def create_widgets(self):
        # utwórz etykietę z instrukcją

        Label(self,
              text="Program do liczenia średniej ważonej."
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Ilość ocen: "
              ).grid(row=1, column=0, sticky=W)

        self.ilosc_ocen = Entry(self, textvariable=self.name_var)

        self.ilosc_ocen.grid(row=1, column=1, sticky=W)

        Button(self,
               text="Dalej!",
               command=self.wyswietl_komorki
               ).grid(row=2, column=0, sticky=W)

    def wyswietl_komorki(self):
        ilosc = int(self.ilosc_ocen.get())
        if ilosc < 1:
            try:
                print("")

            except ValueError:
                print("To nie numer!")

        for widget in Frame.winfo_children(self):
            widget.destroy()
        self.create_widgets()

        for part in range(ilosc):
            Label(self,
                  text=f"Ocena nr{part + 1}:"
                  ).grid(row=self.column, column=0, sticky=W)
            self.ocena = (Entry(self))
            self.ocena.grid(row=self.column, column=1, sticky=W)

            Label(self,
                  text=f"Waga nr{part + 1}:"
                  ).grid(row=self.column, column=2, sticky=W)
            self.waga = (Entry(self))
            self.waga.grid(row=self.column, column=3, sticky=W)
            self.column += 1
            zliczanie_wag.append(self.waga)
            zliczanie_ocen.append(self.ocena)

        # utwórz przycisk akceptacji danych
        Button(self,
               text="Oblicz!",
               command=self.obliczanie
               ).grid(row=self.column + 1, column=0, sticky=W)

    def obliczanie(self):
        # pobierz wartości z interfejsu GUI

        suma_wag = 0
        suma = 0
        lista = []
        for entry in zliczanie_ocen:
            lista.append(float(entry.get()))
        for licznik, entry1 in enumerate(zliczanie_wag):
            suma_wag += int(entry1.get())
            lista[licznik] = lista[licznik] * int(entry1.get())
        zliczanie_ocen.clear()
        zliczanie_wag.clear()

        for numer in lista:
            suma += numer

        srednia1 = suma / suma_wag

        self.txt1 = Text(self, width=5, height=1, wrap=CHAR)
        Label(self,
              text="Średnia"
              ).grid(row=self.column + 2, column=0, sticky=W)
        Label(self,
              text="ważona:"
              ).grid(row=self.column + 3, column=0, sticky=W)
        self.txt1.grid(row=self.column + 3, column=1, sticky=W)

        wynik = round(srednia1, 2)
        self.txt1.delete(0.0, END)
        # noinspection PyTypeChecker
        self.txt1.insert(0.0, wynik)


root = Tk()
root.title("Średnia ważona")
root.geometry("400x600")

app = Application(root)

root.mainloop()
