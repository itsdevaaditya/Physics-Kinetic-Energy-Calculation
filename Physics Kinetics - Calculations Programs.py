import math
import tkinter as tk
from tkinter import messagebox

def calc_massa(energi_potensial, g, ketinggian):
    return (energi_potensial / g) / ketinggian

def alt_massacalc(energi_kinetik, percepatan):
    return (2 * energi_kinetik) / percepatan ** 2

def calc_velocity(energi_kinetik, massa):
    return math.sqrt(2 * energi_kinetik / massa)

def calc_height(energi_potensial, massa, g):
    return energi_potensial / (massa * g)

def alt_heightcalc(ketinggian_b, percepatan_b, percepatan_a, g):
    return ketinggian_b + ((1 * ((percepatan_b ** 2) - (percepatan_a ** 2))) / (2 * g))

def calc_ep(massa, g, ketinggian):
    return massa * g * ketinggian

def calc_ek(massa, percepatan):
    return 0.5 * massa * percepatan ** 2

def calc_em(massa, g, ketinggian, percepatan):
    return (massa * g * ketinggian) + (0.5 * massa * percepatan ** 2)

def update_fields():
    for widget in input_frame.winfo_children():
        widget.grid_remove()

    choice = int(option.get())

    if choice == 1:
        tk.Label(input_frame, text="Energi Potensial (Ep)").grid(row=0, column=0)
        entry_ep.grid(row=0, column=1)
        tk.Label(input_frame, text="Gravitasi (g)").grid(row=1, column=0)
        entry_g.grid(row=1, column=1)
        tk.Label(input_frame, text="Ketinggian (h)").grid(row=2, column=0)
        entry_h.grid(row=2, column=1)
        tk.Label(input_frame, text="Energi Kinetik (Ek) - Optional").grid(row=3, column=0)
        entry_ek.grid(row=3, column=1)
        tk.Label(input_frame, text="Percepatan (v) - Optional").grid(row=4, column=0)
        entry_v.grid(row=4, column=1)

    elif choice == 2:
        tk.Label(input_frame, text="Energi Kinetik (Ek)").grid(row=0, column=0)
        entry_ek.grid(row=0, column=1)
        tk.Label(input_frame, text="Massa (m)").grid(row=1, column=0)
        entry_m.grid(row=1, column=1)

    elif choice == 3:
        tk.Label(input_frame, text="Energi Potensial (Ep)").grid(row=0, column=0)
        entry_ep.grid(row=0, column=1)
        tk.Label(input_frame, text="Massa (m)").grid(row=1, column=0)
        entry_m.grid(row=1, column=1)
        tk.Label(input_frame, text="Gravitasi (g)").grid(row=2, column=0)
        entry_g.grid(row=2, column=1)
        tk.Label(input_frame, text="Ketinggian B (hB) - Optional").grid(row=3, column=0)
        entry_hb.grid(row=3, column=1)
        tk.Label(input_frame, text="Percepatan B (vB) - Optional").grid(row=4, column=0)
        entry_vb.grid(row=4, column=1)
        tk.Label(input_frame, text="Percepatan A (vA) - Optional").grid(row=5, column=0)
        entry_va.grid(row=5, column=1)

    elif choice == 4:
        tk.Label(input_frame, text="Energi Potensial (Ep)").grid(row=0, column=0)
        entry_ep.grid(row=0, column=1)
        tk.Label(input_frame, text="Massa (m)").grid(row=1, column=0)
        entry_m.grid(row=1, column=1)
        tk.Label(input_frame, text="Gravitasi (g)").grid(row=2, column=0)
        entry_g.grid(row=2, column=1)
        tk.Label(input_frame, text="Ketinggian A (hA) - Optional").grid(row=3, column=0)
        entry_ha.grid(row=3, column=1)
        tk.Label(input_frame, text="Percepatan A (vA) - Optional").grid(row=4, column=0)
        entry_va.grid(row=4, column=1)
        tk.Label(input_frame, text="Percepatan B (vB) - Optional").grid(row=5, column=0)
        entry_vb.grid(row=5, column=1)

    elif choice == 5:
        tk.Label(input_frame, text="Massa (m)").grid(row=0, column=0)
        entry_m.grid(row=0, column=1)
        tk.Label(input_frame, text="Gravitasi (g)").grid(row=1, column=0)
        entry_g.grid(row=1, column=1)
        tk.Label(input_frame, text="Ketinggian (h)").grid(row=2, column=0)
        entry_h.grid(row=2, column=1)

    elif choice == 6:
        tk.Label(input_frame, text="Massa (m)").grid(row=0, column=0)
        entry_m.grid(row=0, column=1)
        tk.Label(input_frame, text="Percepatan (v)").grid(row=1, column=0)
        entry_v.grid(row=1, column=1)

    elif choice == 7:
        tk.Label(input_frame, text="Massa (m)").grid(row=0, column=0)
        entry_m.grid(row=0, column=1)
        tk.Label(input_frame, text="Gravitasi (g)").grid(row=1, column=0)
        entry_g.grid(row=1, column=1)
        tk.Label(input_frame, text="Ketinggian (h)").grid(row=2, column=0)
        entry_h.grid(row=2, column=1)
        tk.Label(input_frame, text="Percepatan (v)").grid(row=3, column=0)
        entry_v.grid(row=3, column=1)

def calculate():
    choice = int(option.get())
    try:
        if choice == 1:
            ep = float(entry_ep.get())
            if ep != 0 or None:
                g = float(entry_g.get())
                h = float(entry_h.get())
                massa = calc_massa(ep, g, h)
            else:
                ek = float(entry_ek.get())
                percepatan = float(entry_v.get())
                massa = alt_massacalc(ek, percepatan)
            messagebox.showinfo("Result", f"Massa: {round(massa, 4)} kg")

        elif choice == 2:
            ek = float(entry_ek.get())
            massa = float(entry_m.get())
            kecepatan = calc_velocity(ek, massa)
            messagebox.showinfo("Result", f"Kecepatan: {round(kecepatan, 4)} m/s")

        elif choice == 3:
            ep = float(entry_ep.get())
            if ep != 0 or None:
                massa = float(entry_m.get())
                g = float(entry_g.get())
                h = calc_height(ep, massa, g)
            else:
                hb = float(entry_hb.get())
                vb = float(entry_vb.get())
                va = float(entry_va.get())
                g = float(entry_g.get())
                h = alt_heightcalc(hb, vb, va, g)
            messagebox.showinfo("Result", f"Ketinggian A: {round(h, 4)} m")

        elif choice == 4:
            ep = float(entry_ep.get())
            if ep != 0 or None:
                massa = float(entry_m.get())
                g = float(entry_g.get())
                h = calc_height(ep, massa, g)
            else:
                ha = float(entry_ha.get())
                va = float(entry_va.get())
                vb = float(entry_vb.get())
                g = float(entry_g.get())
                h = alt_heightcalc(ha, va, vb, g)
            messagebox.showinfo("Result", f"Ketinggian B: {round(h, 4)} m")

        elif choice == 5:
            massa = float(entry_m.get())
            g = float(entry_g.get())
            ketinggian = float(entry_h.get())
            ep = calc_ep(massa, g, ketinggian)
            messagebox.showinfo("Result", f"Energi Potensial: {round(ep, 4)} Joule (J)")

        elif choice == 6:
            massa = float(entry_m.get())
            percepatan = float(entry_v.get())
            ek = calc_ek(massa, percepatan)
            messagebox.showinfo("Result", f"Energi Kinetik: {round(ek, 4)} Joule (J)")

        elif choice == 7:
            massa = float(entry_m.get())
            g = float(entry_g.get())
            ketinggian = float(entry_h.get())
            percepatan = float(entry_v.get())
            em = calc_em(massa, g, ketinggian, percepatan)
            messagebox.showinfo("Result", f"Energi Mekanik: {round(em, 4)} Joule (J)")

    except ValueError:
        messagebox.showerror("NDAK MANUK AKAL", f"Masukkin angka yang masuk akal dong....")

root = tk.Tk()
root.title("Kalkulasi Energi Mekanik Fisika")

option = tk.StringVar(value="1")

tk.Label(root, text="Pilih apa yang ingin anda hitung:").grid(row=0, column=0, columnspan=2)
tk.Radiobutton(root, text="Massa (m)", variable=option, value=1, command=update_fields).grid(row=1, column=0, columnspan=2)
tk.Radiobutton(root, text="Kecepatan (v)", variable=option, value=2, command=update_fields).grid(row=2, column=0, columnspan=2)
tk.Radiobutton(root, text="Ketinggian A", variable=option, value=3, command=update_fields).grid(row=3, column=0, columnspan=2)
tk.Radiobutton(root, text="Ketinggian B", variable=option, value=4, command=update_fields).grid(row=4, column=0, columnspan=2)
tk.Radiobutton(root, text="Energi Potensial (EP)", variable=option, value=5, command=update_fields).grid(row=5, column=0, columnspan=2)
tk.Radiobutton(root, text="Energi Kinetik (EK)", variable=option, value=6, command=update_fields).grid(row=6, column=0, columnspan=2)
tk.Radiobutton(root, text="Energi Mekanik (EM)", variable=option, value=7, command=update_fields).grid(row=7, column=0, columnspan=2)

input_frame = tk.Frame(root)
input_frame.grid(row=8, column=0, columnspan=2)

entry_ep = tk.Entry(input_frame)
entry_m = tk.Entry(input_frame)
entry_g = tk.Entry(input_frame)
entry_h = tk.Entry(input_frame)
entry_ek = tk.Entry(input_frame)
entry_v = tk.Entry(input_frame)
entry_hb = tk.Entry(input_frame)
entry_vb = tk.Entry(input_frame)
entry_va = tk.Entry(input_frame)
entry_ha = tk.Entry(input_frame)

tk.Button(root, text="Hitung", command=calculate).grid(row=9, column=0, columnspan=2)

# Initialize fields to the first option
update_fields()

root.mainloop()


# Code by Deva Aditya, and ChatGPT.