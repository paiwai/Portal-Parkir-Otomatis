
print("APLIKASI PARKIR OTOMATIS")

def cariparkir(x,y,m,nk_fix,n):
    kosong = True
    pilih = 0
    for i in range (x):
        for j in range (y):
            if (m[i][j] == "*" and kosong == True):
                seat = (chr(64+i))
                print("Tempat parkir anda di titik ", seat , (j))
                pilih = input("(Y/T)\n")
                if (pilih == "Y"):
                    m[i][j] = "x"
                    a_brs = i
                    a_klm = j
                    nk_fix = a_brs*100000+a_klm*10000+n
                    kosong = False
                    return (nk_fix)

def sisaparkir(l,x,y,m):
    print()
    print("   Sisa Tempat Parkir yang Tersedia \n               di Lantai", l)
    for i in range (x):
        for j in range (y):
            print(str(m[i][j]) + " ", end="")
        print()

    print("="*40)
    print()

def karcis(l,ken,n,k,j):
    print("="*40)
    print("          ~~~ KARCIS PARKIR ~~~")
    print("Lokasi Parkir   : Lantai", l)
    print("Jenis Kendaraan :", ken)
    print("Nomor polisi    :", n)       # menampilkan nopol
    print("No. Karcis      :", k)       # menampilkan no.karcis
    print("jam Masuk       :", j)       # menampilkan jam masuk
    print("          ~SELAMAT PARKIR~")
    print("="*40)

def keluar(x,y,data,ext,m):
    # mencari nilai no karcis pada array
    # dan mengembalikannya menjadi 0 (kondisi kosong)
    for i in range (x):
        for j in range (y):
            ()
    i = 0
    n = x*y
    arr_nk = ""
    found = False
    while (i<n and found == False):
        if (data[i] == ext):
            arr_nk = str(ext)
            found = True
        else:
            i += 1
    
    data[i] = 0

    # mendeklarasikan nilai arr_nk sebagai koordinat
    koordinat1 = int(arr_nk[0])
    koordinat2 = int(arr_nk[1])

    # mencari koordinat parkir dari no. karcis 
    # dan mengembalikan nilai x menjadi * sebagai indikator kosong
    for i in range (x):
        for j in range (y):
            m[koordinat1][koordinat2] = "*"

def karcis_out(k,d,bi):
    print("="*40)
    print("          ~~~ KARCIS KELUAR ~~~")
    print("Lokasi Parkir   : Lantai 2")
    print("Jenis Kendaraan : Mobil")
    print("No. Karcis      :", k)          # menampilkan no.karcis
    print("Durasi Parkir   :", d)          # menampilkan durasi parkir
    print("Biaya Parkir    : Rp", int(bi), ",00") # menampilkan biaya parkir
    print("          ~TERIMA KASIH~")
    print("="*40)

# sub program penghitungan biaya parkir
def biaya(jenis,ext):
    k = ext
    print("="*40)
    print()
    print("PORTAL KELUAR")
    print()
    print("format jam (jam.menit)")
    a = float(input("Masukkan Jam Masuk :"))
    a = a*60
    z = float(input("Masukkan Jam Keluar :"))
    z = z*60
    print()

    b = z-a
    d = b

    # jika yang keluar adalah mobil
    if (jenis == 1):
        if (b%60 != 0): 
            b = b//60
            b = b + 1
            if (b <= 1):
                b = b*3000
                karcis_out(k,d,b)
            elif (b > 1):
                b = b*5000
                karcis_out(k,d,b)
                
        elif (b%60 == 0):
                b = b/60
                if (b <= 1):
                    b = b*3000
                    karcis_out(k,d,b)
                elif (b > 1):
                    b = b*5000
                    karcis_out(k,d,b)

    # jika yang keluar adalah motor                
    elif (jenis == 2):
        if (b%60 != 0): 
            b = b//60
            b = b + 1
            if (b <= 1):
                b = b*2000
                karcis_out(k,d,b)
            elif (b > 1):
                b = b*3000
                karcis_out(k,d,b)
                
        elif (b%60 == 0):
                b = b/60
                if (b <= 1):
                    b = b*3000
                    karcis_out(k,d,b)
                elif (b > 1):
                    b = b*5000
                    karcis_out(k,d,b)

    # jika angka pilihan yg dimasukkan salah
    else:
        print("Input salah.")

    

# data matrix dan array mobil
mb = [["*" for j in range (5)] for i in range (5)]
data_mb = [0 for i in range (15)]
def masuk1():
    ken = "Mobil"
    nk_fix = 0
    nopol = input("Masukan nomor polisi : ")
    print("Format Jam : jam.menit | _ _ . _ _")
    jam_parkir = str(input("Jam masuk : "))
    no_karcis = int(nopol[3])*1000 + int(nopol[4])*100 + int(nopol[5])*10 + int(nopol[6])
    print()
    print("SILAHKAN PARKIR DI LANTAI 2")
    print("Tempat Parkir yang Tersedia\n * : kosong | x : terisi")

    #menampilkan matrix tempat parkir mobil
    for i in range (5):
        for j in range (5):
            mb [0][0] = "x"
            mb [0][1] = 1
            mb [0][2] = 2
            mb [0][3] = 3
            mb [0][4] = 4
            mb [1][0] = "A"
            mb [2][0] = "B"
            mb [3][0] = "C"
            mb [4][0] = "D"
            print(str(mb[i][j]) + " ", end="")
        print()

    # memanggil program cariparkir
    nk_fix = cariparkir(5,5,mb,nk_fix,no_karcis)

    # menginput no karcis ke array
    data_mb.append(nk_fix)

    # memanggil program karcis
    karcis(2,ken,nopol, nk_fix, jam_parkir)

    # memanggil program sisaparkir
    sisaparkir(2,5,5,mb)


mt = [["*" for j in range (6)] for i in range (5)]
data_mt = [0 for i in range (19)]
def masuk2():
    ken = "Motor"
    nk_fix = 0
    nopol = input("Masukan nomor polisi : ")
    jam_parkir = str(input("Masukan Jam masuk : "))
    no_karcis = int(nopol[3])*1000 + int(nopol[4])*100 + int(nopol[5])*10 + int(nopol[6])
    print()
    print("SILAHKAN PARKIR DI LANTAI 2")
    print("Tempat Parkir yang Tersedia\n * : kosong | x : terisi")

    #menampilkan matrix tempat parkir mobil
    for i in range (5):
        for j in range (6):
            mt [0][0] = "x"
            mt [0][1] = 1
            mt [0][2] = 2
            mt [0][3] = 3
            mt [0][4] = 4
            mt [0][5] = 5
            mt [1][0] = "A"
            mt [2][0] = "B"
            mt [3][0] = "C"
            mt [4][0] = "D"
            print(str(mt[i][j]) + " ", end="")
        print()

    # memanggil program cariparkir
    nk_fix = cariparkir(5,6,mt,nk_fix,no_karcis)

    # menginput no karcis ke array
    data_mt.append(nk_fix)

    # memanggil program karcis
    karcis(1,ken,nopol, nk_fix, jam_parkir)

    # memanggil program sisaparkir
    sisaparkir(1,5,6,mt)

# PROGRAM UTAMA
maxmobil = 16
maxmotor = 20
while (True):
    pil_prog = int(input("Pilih Program : \n[1] Masuk \n[2] Keluar\nPilih : " ))
    while (pil_prog == 1):
        jenis = int(input("Jenis Kendaraan : \n[1] Mobil \n[2] Motor \npilih : "))
        while (jenis == 1):
            if (maxmobil > 0):
                masuk1()
                maxmobil-=1
                break
            
            else:
                print("Mohon maaf, tempat parkir penuh.")
                break

        while (jenis == 2):
            if (maxmotor > 0):
                masuk2()
                maxmotor-=1
                break
            else:
                print("Mohon maaf, tempat parkir penuh.")
        break
        
    while (pil_prog == 2):
        jenis = int(input("Jenis Kendaraan : \n[1] Mobil \n[2] Motor \npilih : "))
        # ketika memilih program keluar motor
        while (jenis == 1):
            if (maxmobil >= 16):
                print ("Tidak ada kendaraan terparkir.")
                break
            else:
                k_ext = int(input("Masukan No. Karcis Anda : "))
                if (k_ext in data_mb):
                    keluar(5,5,data_mb,k_ext,mb)
                    biaya(jenis,k_ext)
                    maxmobil += 1
                    sisaparkir(2,5,5,mb)
                    break
                else:
                    print("No Karcis salah.")
                    break
        
        # ketika memilih program keluar motor
        while (jenis == 2):
            if (maxmobil >= 20):
                print ("Tidak ada kendaraan terparkir.")
                break
            else:
                k_ext = int(input("Masukan No. Karcis Anda : "))
                if (k_ext in data_mb):
                    keluar(5,5,data_mb,k_ext,mb)
                    biaya(jenis,k_ext)
                    maxmobil += 1
                    sisaparkir(2,5,5,mb)
                    break
                else:
                    print("No Karcis salah.")
                    break
        break