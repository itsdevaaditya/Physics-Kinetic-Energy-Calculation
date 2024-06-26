import math
import os

# KALKULASI MASSA ###########################################################
def calc_massa(energi_potensial, g, ketinggian):
    return (energi_potensial / g) / ketinggian

def alt_massacalc(energi_kinetik, percepatan):
    return (2 * energi_kinetik) / percepatan **2
#############################################################################
# KALKULASI PERCEPATAN ######################################################
def calc_velocity(energi_kinetik, massa):
    return math.sqrt(2 * energi_kinetik / massa)
#############################################################################
# KALKULASI KETINGGIAN A ####################################################
def calc_height(energi_potensial, massa, g):
    return energi_potensial / (massa * g)

def alt_heightcalc(ketinggian_b, percepatan_b, percepatan_a, g):
    return ketinggian_b + ((1 * ((percepatan_b ** 2) - (percepatan_a ** 2))) / (2 * g)) # hb + (1/2g vb **2 - va **2)
#############################################################################
# KALKULASI KETINGGIAN B ####################################################
def calc_height(energi_potensial, massa,g ):
    return energi_potensial / (massa * g)

def alt_heightcalc(ketinggian_a, percepatan_a, percepatan_b, g):
    return ketinggian_a + ((1 * ((percepatan_a ** 2) - (percepatan_b ** 2))) / (2 * g)) # ha + (1/2g va **2 - vb **2)
#############################################################################
# KALKULASI ENERGI POTENSIAL ################################################
def calc_ep(massa, g, ketinggian):
    return massa * g * ketinggian
#############################################################################
# KALKULASI ENERGI KINETIK ##################################################
def calc_ek(massa, percepatan):
    return 0.5 * massa * percepatan**2
#############################################################################
# KALKULASI ENERGI MEKANIK ####################################################
def calc_em(massa, g, ketinggian, percepatan):
    return (massa * g * ketinggian) + (0.5 * massa * percepatan**2)
#############################################################################

def main():
    print("Pilih apa yang ingin anda hitung:")
    print('''    1. Massa (m)
    2. Kecepatan (v)
    3. Ketinggian A
    4. Ketinggian B
    5. Energi Potensial (EP)
    6. Energi Kinetik (EK)
    7. Energi Mekanik (EM)
      ''')
    pilihan = int(input("Masukkan Pilihan (1-7): "))

    ############    MENGHITUNG MASSA    ###########################################################
    if pilihan == 1:
        energi_potensial_a = float(input("Masukkan nilai dari Energi Potensial titik A (EpA): ")) 

        if energi_potensial_a != 0: #apabila EP = 0 maka eksekusi program ini:
            g = float(input("Masukkan nilai gravitasi (m/s): ")) 
            ketinggian_a = float(input("Masukkan nilai dari Ketinggian titik A (hA): ")) 

        if energi_potensial_a == 0 or ketinggian_a == 0:
            energi_kinetik_b = float(input("Masukkan Nilai dari Energi Kinetik B: "))
            percepatan = float(input("Masukkan Nilai dari Percepatan B: ")) 
        
            massa = alt_massacalc(energi_kinetik_b, percepatan)
            print(f"Massa: {round(massa, 4)} kg")
        else: # apabila EP dan Ketinggian A tidak kosong, maka eksekusi program ini
            massa = calc_massa(energi_potensial_a, g, ketinggian_a)
            print(f"Massa: {round(massa, 4)} kg")

    ############    MENGHITUNG KECEPATAN    ########################################################
    elif pilihan == 2:
        energi_kinetik = float(input("Masukkan nilai dari Energi Kinetik (EK): "))
        massa = float(input("Masukkan Massa dari sebuah Benda (M): "))
        percepatan = calc_velocity(energi_kinetik, massa)
        print(f"Kecepatan (v) benda tersebut: {round(percepatan, 4)} m/s")

    ############    MENGHITUNG KETINGGIAN A    #####################################################
    elif pilihan == 3:
        energi_potensial = int(input("Masukkan nilai Energi Potensial (Ep): "))

        if energi_potensial == 0: # nilai ep = 0 atau tidak ada, eksekusi program ini
            ketinggian_b = float(input("Masukkan nilai ketinggian B (hB): ")) 
            percepatan_b = float(input("Masukkan nilai percepatan B (vB): ")) 
            percepatan_a = float(input("Masukkan nilai percepatan A (vA) ")) 
            g = float(input("Masukkan nilai gravitasi (m/s): ")) 

            ketinggian_a = alt_heightcalc(ketinggian_b, percepatan_b, percepatan_a)
            print(f"Ketinggian A: {round(ketinggian_a, 4)} m")

        else: # nilai ep bukan 0, eksekusi program ini
            massa = float(input("Masukkan nilai Massa benda (m): "))
            g = float(input("Masukkan nilai gravitasi (m/s): "))

            ketinggian_a = calc_height(energi_potensial, massa)
            print(f"Ketinggian A: {round(ketinggian_a, 4)} m")

    ############    MENGHITUNG KETINGGIAN B    #####################################################
    elif pilihan == 4:
        energi_potensial = float(input("Masukkan nilai Energi Potensial (Ep): "))

        if energi_potensial == 0: # nilai ep = 0 atau tidak ada, eksekusi program ini
            ketinggian_a = float(input("Masukkan nilai ketinggian A (hB): ")) 
            percepatan_a = float(input("Masukkan nilai percepatan A (vB): ")) 
            percepatan_b = float(input("Masukkan nilai percepatan B (vA): ")) 
            g = float(input("Masukkan nilai gravitasi (m/s): ")) 

            ketinggian_b = alt_heightcalc(ketinggian_a, percepatan_a, percepatan_a)
            print(f"Ketinggian B: {round(ketinggian_b, 4)} m")

        else: # nilai ep bukan 0, eksekusi program ini
            massa = float(input("Masukkan nilai Massa benda (m): "))
            g = float(input("Masukkan nilai gravitasi (m/s): "))

            ketinggian_a = calc_height(energi_potensial, massa)
            print(f"Ketinggian B: {round(ketinggian_a, 4)} m")

    ############    MENGHITUNG ENERGI POTENSIAL    ###################################################
    elif pilihan == 5:
        massa = float(input("Masukkan nilai Massa benda (m): "))
        g = float(input("Masukkan nilai gravitasi (m/s): "))
        ketinggian = float(input("Masukkan nilai ketinggian  (h): ")) 

        energi_potensial = calc_ep(massa, g, ketinggian)
        print(f"Energi Potensial: {round(energi_potensial, 4)} Joule (J)")

    ############    MENGHITUNG ENERGI KINETIK    #####################################################
    elif pilihan == 6:
        massa = float(input("Masukkan nilai Massa benda (m): "))
        percepatan = float(input("Masukkan nilai percepatan (v): "))  

        energi_kinetik = calc_ek(massa, percepatan)
        print(f"Energi Kinetik: {round(energi_kinetik, 4)} Joule (J)")

    ############    MENGHITUNG ENERGI MEKANIK    #####################################################
    elif pilihan == 7:
        massa = float(input("Masukkan nilai Massa benda (m): "))
        g = float(input("Masukkan nilai gravitasi (m/s): "))
        ketinggian = float(input("Masukkan nilai ketinggian  (h): "))
        percepatan = float(input("Masukkan nilai percepatan (v): "))   

        energi_mekanik = calc_em(massa, g, ketinggian, percepatan)
        print(f"Energi Mekanik: {round(energi_mekanik, 4)} Joule (J)")

    
    lagi = input("Hitung lagi? [y/n]: ")
    if lagi == "y":
        os.system('cls')
        main()
    else:
        exit()

main()


# Code by Deva Aditya