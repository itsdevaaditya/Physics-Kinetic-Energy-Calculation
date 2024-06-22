import math

g = 0

def energi_potensial(massa, g, ketinggian):
    return massa * g * ketinggian

def energi_kinetik(massa, kecepatan):
    return 0.5 * massa * kecepatan ** 2

def hitung_kecepatan(energi_kinetik, massa):
    return math.sqrt(2 * energi_kinetik / massa)

def hitung_massa_alternatif(energi_kinetik, ketinggian):
    return energi_kinetik / (g * ketinggian)

def hitung_ketinggian(energi_potensial, massa):
    return energi_potensial / (massa * g)

def main():
    # Input dari pengguna
    print("Silakan pilih apa yang ingin Anda cari:")
    print("1. Energi Kinetik A")
    print("2. Energi Kinetik B")
    print("3. Massa")
    print("4. Ketinggian A")
    print("5. Kecepatan A")
    print("6. Ketinggian B")
    print("7. Kecepatan B")
    
    pilihan = int(input("Masukkan pilihan (1-7): "))

    if pilihan == 1:
        # Pengguna ingin mencari energi kinetik di titik A
        g = int(input("Masukkan nilai gravitasi: "))
        massa = float(input("Masukkan massa bola (kg): "))
        ketinggian_A = float(input("Masukkan ketinggian titik A (m): "))

        # Hitung energi kinetik di titik A
        EK_A = energi_potensial(massa, ketinggian_A)

        print(f"Energi Kinetik A: {EK_A} Joule")

    elif pilihan == 2:
        # Pengguna ingin mencari energi kinetik di titik B
        g = int(input("Masukkan nilai gravitasi: "))
        massa = float(input("Masukkan massa bola (kg): "))
        ketinggian_A = float(input("Masukkan ketinggian titik A (m): "))
        ketinggian_B = float(input("Masukkan ketinggian titik B (m) (0 apabila tidak ada hB): "))
        # Hitung energi potensial di titik A dan B
        EP_A = energi_potensial(massa, g, ketinggian_A)
        EP_B = energi_potensial(massa, g, ketinggian_B)

        # Energi kinetik di titik B
        EK_B = EP_A - EP_B

        print(f"Energi Kinetik B: {EK_B} Joule")

    elif pilihan == 3:
        # Pengguna ingin mencari massa
        g = int(input("Masukkan nilai gravitasi: "))
        EK_A = float(input("Masukkan energi kinetik titik A (Joule): "))
        kecepatan_A = float(input("Masukkan kecepatan titik A (m/s): "))

        if kecepatan_A == 0:
            ketinggian_A = float(input("Masukkan ketinggian titik A (m): "))
            massa = hitung_massa_alternatif(EK_A, ketinggian_A)
        else:
            massa = 2 * EK_A / kecepatan_A ** 2

        print(f"Massa: {massa} kg")

    elif pilihan == 4:
        # Pengguna ingin mencari ketinggian A
        g = int(input("Masukkan nilai gravitasi: "))
        massa = float(input("Masukkan massa bola (kg): "))
        EK_A = float(input("Masukkan energi kinetik titik A (Joule): "))

        # Hitung ketinggian A
        ketinggian_A = EK_A / (massa * g)

        print(f"Ketinggian A: {ketinggian_A} m")

    elif pilihan == 5:
        # Pengguna ingin mencari kecepatan A
        massa = float(input("Masukkan massa bola (kg): "))
        EK_A = float(input("Masukkan energi kinetik titik A (Joule): "))

        # Hitung kecepatan A
        kecepatan_A = hitung_kecepatan(EK_A, massa)

        print(f"Kecepatan A: {kecepatan_A} m/s")

    elif pilihan == 6:
        # Pengguna ingin mencari ketinggian B
        g = int(input("Masukkan nilai gravitasi: "))
        massa = float(input("Masukkan massa bola (kg): "))
        ketinggian_A = float(input("Masukkan ketinggian titik A (m): "))
        EK_B = float(input("Masukkan energi kinetik titik B (Joule): "))

        # Hitung energi potensial di titik A
        EP_A = energi_potensial(massa, ketinggian_A)

        # Hitung energi potensial di titik B
        EP_B = EP_A - EK_B

        # Hitung ketinggian B
        ketinggian_B = EP_B / (massa * g)

        print(f"Ketinggian B: {ketinggian_B} m")

    elif pilihan == 7:
        # Pengguna ingin mencari kecepatan B
        g = int(input("Masukkan nilai gravitasi: "))
        massa = float(input("Masukkan massa bola (kg): "))
        ketinggian_A = float(input("Masukkan ketinggian titik A (m): "))
        EK_B = float(input("Masukkan energi kinetik titik B (Joule): "))

        # Hitung energi potensial di titik A
        EP_A = energi_potensial(massa, ketinggian_A)

        # Hitung kecepatan B
        kecepatan_B = hitung_kecepatan(EK_B, massa)

        print(f"Kecepatan B: {kecepatan_B} m/s")

    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
