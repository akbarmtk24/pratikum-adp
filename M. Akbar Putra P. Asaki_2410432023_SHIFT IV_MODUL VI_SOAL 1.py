huruf = ["A", "A-", "B+", "B", "B-", "C+", "C", "D", "E"]
angka = [4.00, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0.00]

mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
matkul = int(input("Masukkan jumlah mata kuliah: "))

data = []  

i = 0
while i < mahasiswa:
    print("Mahasiswa ke-", i + 1)
    nama = input("Nama mahasiswa: ")
    nilai = [nama]
    
    j = 0
    while j < matkul:
        nilai_input = input("Nilai mata kuliah ke-{}: ".format(j + 1)).upper()
        if nilai_input in huruf:
            nilai.append(nilai_input)
            j += 1
        else:
            print("Nilai tidak valid! Gunakan A, A-, B+, B, B-, C+, C, D, E.")
    
    data.append(nilai)
    i += 1

ip = []  

i = 0
while i < mahasiswa:
    total = 0
    j = 1
    while j <= matkul:
        nilai_huruf = data[i][j]
        
        k = 0
        while k < len(huruf):
            if nilai_huruf == huruf[k]:
                total += angka[k]
            k += 1
        
        j += 1
    
    ip_mahasiswa = total / matkul
    ip.append([data[i][0], ip_mahasiswa])
    i += 1

i = 0
while i < mahasiswa - 1:
    j = i + 1
    while j < mahasiswa:
        if ip[i][1] < ip[j][1]:
            sementara = ip[i]
            ip[i] = ip[j]
            ip[j] = sementara
        j += 1
    i += 1

print("Daftar Indeks Prestasi Mahasiswa:")
print("----------------------------------")
i = 0
while i < mahasiswa:
    print(f"Nama : {ip[i][0]}")
    print("Nilai tiap matkul")
    ke = 0
    while ke < matkul:
        nilai_huruf = data[i][ke + 1]
        k = 0
        while k < len(huruf):
            if nilai_huruf == huruf[k]:
                nilai_angka = angka[k]
                break
            k += 1
        print(f"Mata Kuliah ke-{ke + 1} : {nilai_angka}")
        ke += 1
    print(f"IP   : {ip[i][1]}")
    print("----------------------------------")
    i += 1
    