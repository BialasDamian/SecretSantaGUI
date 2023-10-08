import tkinter as tk
from tkinter import messagebox
from random import shuffle

lista_imion = []
lista_losujacych = []

    
def dodaj_imie():
    do_dodania = str.capitalize(str.strip(entry_imie.get()))
    if do_dodania in lista_imion:
        messagebox.showerror("Błąd", "Podane imię już znajduje się na liście. Podaj wartość unikatową.")
    elif len(do_dodania) == 0:
        messagebox.showerror("Błąd", "Należy podać imię.")
    else:
        lista_imion.append(do_dodania)
        
        entry_imie.delete(0, "end")
        update_label_imiona()

def losuj():
    if len(lista_imion) < 3:
        messagebox.showerror("Błąd", "Lista jest za krótka, aby móc losować osoby.")
    else:
        shuffle(lista_imion)
        for i in range(len(lista_imion)):
            if i != len(lista_imion) - 1:
                lista_losujacych.append(lista_imion[i + 1])
            else:
                lista_losujacych.append(lista_imion[0])
        mikolaj = {}
        for i in range(len(lista_imion)):
            mikolaj[lista_imion[i]] = lista_losujacych[i]
        lista_do_wyswietlenia = list(mikolaj.items())
        shuffle(lista_do_wyswietlenia)
        for i in range(len(lista_do_wyswietlenia)):
            messagebox.showwarning("!!!Uwaga!!!",f"{lista_do_wyswietlenia[i][0]}, Upewnij się że nikt nie patrzy poza Tobą! ")
            messagebox.showinfo("!!!Losowanie!!!", f"Teraz losować będzie {lista_do_wyswietlenia[i][0]}\n\n{lista_do_wyswietlenia[i][0]} kupujesz prezent dla {lista_do_wyswietlenia[i][1]}")
        messagebox.showinfo("Koniec", "To już wszyscy ;)")
        

def update_label_imiona():
    label_imiona.config(text=", ".join(lista_imion))

ekran = tk.Tk()
ekran.title("Mikolajkowy los")
ekran.geometry('480x320')
frame_dodaj_imie = tk.Frame(ekran)
frame_dodaj_imie.pack()
entry_imie = tk.Entry(ekran)
entry_imie.pack()
label_imiona = tk.Label(ekran,text="Imiona")
label_imiona.pack()


label_dodaj_imie = tk.Label(frame_dodaj_imie)
control_frame = tk.Frame(ekran)
control_frame.pack(side=tk.TOP)


add_button = tk.Button(control_frame, text="Dodaj", command=dodaj_imie)
add_button.pack(side=tk.TOP)

draw_button = tk.Button(control_frame, text="Losuj", command=losuj)
draw_button.pack(side=tk.TOP)

error_label = tk.Label(control_frame, text="", fg="red")
error_label.pack(side=tk.TOP)
def komenda():
    for i in range(1):
        lista_imion.clear()
        lista_losujacych.clear()
        entry_imie.delete(0,"end")
        label_imiona.config(text="Imiona")

clear_button = tk.Button(ekran,text="Wyczyść listę",command=komenda)
clear_button.pack(side=tk.TOP)
result_label = tk.Label(control_frame, text="", font=("Arial", 12))
result_label.pack(side=tk.BOTTOM)

ekran.mainloop()