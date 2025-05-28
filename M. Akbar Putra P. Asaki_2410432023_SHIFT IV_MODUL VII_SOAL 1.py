def hitungglbb(vawal, a, t):
    vakhir = vawal + a * t
    jarak = vawal * t + 0.5 * a * t * t
    return vakhir, jarak

n = int(input("Masukkan jumlah data (n): "))

hasil = []

for i in range(n):
    print(f"Data ke-{i+1}")
    vawal = float(input("Masukkan kecepatan awal (m/s): "))
    a = float(input("Masukkan percepatan (m/s^2): "))
    t = float(input("Masukkan waktu (s): "))

    vakhir, jarak = hitungglbb(vawal, a, t)
    hasil.append([i+1, vawal, a, t, vakhir, jarak])

print("Hasil Perhitungan Gerak Lurus Berubah Beraturan (GLBB):")
print("===============================================================================")
print("| No | Kecepatan Awal | Percepatan | Waktu | Kecepatan Akhir | Jarak Tempuh   |")
print("===============================================================================")

for data in hasil:
    no, vawal, a, t, vakhir, jarak = data
    print(f"| {no:<2} | {vawal:<14} | {a:<10} | {t:<5} | {vakhir:<15} | {jarak:<14} |")

    print("===============================================================================")