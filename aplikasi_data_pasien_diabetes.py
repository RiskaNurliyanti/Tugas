print("========== Aplikasi Data Pasien Diabetes ==========")
nama = []
umur = []
jenisKelamin = []
tingkatGulaDarah = []
beratBadan = []
tinggiBadan = []
keturunanDiabetes = []
gejalaLemas = []
gejalaPandanganKabur = []
gejalaLukaSulitSembuh = []
gejalaSeringHaus = []
banyakGejala = []
status = []
pengobatan = []
stop = True


while (stop) :
    print("================ Input Data Pasien ================")
    gejala = 0
    s = 0
    addnama = input("Nama                             : ")
    nama.append(addnama)
    addUmur = int(input("Umur                             : "))
    umur.append(addUmur)
    addJenisKelamin = input("Jenis Kelamin [L/P]              : ")
    jenisKelamin.append(addJenisKelamin)
    addKeturunanDiabetes = input("Memiliki keturunan diabetes [y/n]: ")
    keturunanDiabetes.append(addKeturunanDiabetes)
    addGulaDarah = int(input("Tingkat Gula Darah (mg/dL)       : "))
    tingkatGulaDarah.append(addGulaDarah)
    addBeratBadan = int(input("Berat Badan (kg)                 : "))
    beratBadan.append(addBeratBadan)
    addTinggiBadan = int(input("Tinggi Badan (cm)                : "))
    tinggiBadan.append(addTinggiBadan)
    print("Gejala Gejala                    : ")
    addLemas = input("  - Lemas [y/n]                  : ")
    gejalaLemas.append(addLemas)
    addPandanganKabur = input("  - Pandangan Kabur [y/n]        : ")
    gejalaPandanganKabur.append(addPandanganKabur)
    addLukaSulitSembuh = input("  - Luka Sulit Sembuh [y/n]      : ")
    gejalaLukaSulitSembuh.append(addLukaSulitSembuh)
    addSeringHaus = input("  - Sering Merasa Haus [y/n]     : ")
    gejalaSeringHaus.append(addSeringHaus)
    print()

    if addGulaDarah < 70 :
        addStatus = "Hipoglikemia / Gula Darah Rendah"
    elif (addGulaDarah >= 70) and (addGulaDarah <= 200) :
        addStatus = "Sehat"
    elif addGulaDarah > 200 and addGulaDarah <=300 :
        addStatus = "Hiperglikemia / Diabetes"
        s = 1
    elif addGulaDarah > 300 :
        addStatus = "Hiperglikemia / Diabetes Tingkat Tinggi"
        s = 2

    status.append(addStatus)

    if addLemas == "y":
        gejala += 1
    
    if addPandanganKabur == "y":
        gejala += 1

    if addLukaSulitSembuh == "y":
        gejala += 1

    if addSeringHaus == "y":
        gejala += 1

    if s == 1 and gejala <= 2:
        addPengobatan = "Tidak perlu dirawat inap"
    elif s == 2 or gejala >= 2:
        addPengobatan = "Perlu dirawat inap"
    else :
        addPengobatan = "Tidak perlu pengobatan"
    
    pengobatan.append(addPengobatan)

    tanya = input("Masukan data pasien lagi [y/n] : ")
    if tanya == "n" :
        stop = False

for i in range(len(nama)):
    print("=================== Data Pasien ===================")
    print("Nama                             :", nama[i])
    print("Umur                             :", umur[i])
    print("Jenis Kelamin                    :", jenisKelamin[i])
    print("Kadar Gula Darah                 : " + str(tingkatGulaDarah[i]) + " Mg/dL")
    print("Berat Badan                      : " + str(beratBadan[i]) + " Kg")
    print("Tinggi Badan                     : " + str(tinggiBadan[i]) + " Cm")
    print("Memiliki Keturunan Diabetes      :", keturunanDiabetes[i])
    print("Mengalami Lemas                  :", gejalaLemas[i])
    print("Mengalami Pandangan Kabur        :", gejalaPandanganKabur[i])
    print("Mengalami Luka Sulit Sembuh      :", gejalaLukaSulitSembuh[i])
    print("Mengalami Sering Haus            :", gejalaSeringHaus[i])
    print("Status                           :", status[i])
    print("Pengobatan                       :", pengobatan[i])

