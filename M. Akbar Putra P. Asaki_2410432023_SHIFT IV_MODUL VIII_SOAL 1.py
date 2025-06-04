def hitungnilai(wawancara, pengalaman, pilihan):
    tambahan = 0

    if "ketua" in pengalaman.lower():
        tambahan += 2
    if pilihan.lower() in pengalaman.lower():
        tambahan += 3
    return wawancara + tambahan

def bacadata(namafile):
    file = open(namafile, "r")

    databidang = {
        "Acara": [],
        "Danus": [],
        "Pubdok": [],
        "Perlengkapan": []
    }

    for baris in file:
        bagian = baris.strip().split(",")
        nama = bagian[0]
        nim = bagian[1]
        kelas = bagian[2]
        pengalaman = bagian[3]
        wawancara = int(bagian[4])
        pilihan = bagian[5].capitalize()
        
        nilaiakhir = hitungnilai(wawancara, pengalaman, pilihan)

        cakoor = {
            "nama": nama,
            "nim": nim,
            "kelas": kelas,
            "pengalaman": pengalaman,
            "nilai": nilaiakhir
        }

        if pilihan in databidang:
            databidang[pilihan].append(cakoor)

    file.close()
    return databidang

def semua(databidang):
    print("Semua Cakoor per Bidang")
    for bidang in databidang:
        print(" ")
        print(f"Bidang: {bidang}")
        print("======================================================================")
        print("|              Nama              |     NIM    | Kelas |  Nilai Akhir |")
        print("======================================================================")
        for cakoor in databidang[bidang]:
            print(f"| {cakoor['nama']:<30} | {cakoor['nim']} | {cakoor['kelas']:<5} | {cakoor['nilai']:<12} |")
        print("======================================================================")

def terbaik(databidang):
    print("2 Cakoor Terbaik per Bidang")
    for bidang in databidang:
        print(f"Bidang: {bidang}")
        cakoorbidang = databidang[bidang]

        terbaik1 = None
        terbaik2 = None

        for koor in cakoorbidang:
            if terbaik1 is None or koor["nilai"] > terbaik1["nilai"]:
                terbaik2 = terbaik1
                terbaik1 = koor
            elif terbaik2 is None or koor["nilai"] > terbaik2["nilai"]:
                terbaik2 = koor
        
        print("===================================================================")
        print("| No |           Nama          |     NIM    | Kelas | Nilai Akhir |")
        print("===================================================================")        
        if terbaik1:
            print(f"| 1. | {terbaik1['nama']:<23} | {terbaik1['nim']} | {terbaik1['kelas']:<5} | {terbaik1['nilai']:<11} |")
        if terbaik2:
            print(f"| 2. | {terbaik2['nama']:<23} | {terbaik2['nim']} | {terbaik2['kelas']:<5} | {terbaik2['nilai']:<11} |")
        print("===================================================================")

def output():
    namafile = "OrPSB22.txt"
    data = bacadata(namafile)

    while True:
        print("1. Tampilkan semua cakoor per bidang")
        print("2. Tampilkan 2 cakoor terbaik per bidang")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            semua(data)
        elif pilihan == "2":
            terbaik(data)
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

output()
