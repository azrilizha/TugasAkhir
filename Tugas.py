import csv
import os

nama_file = "data servis Virtual Komputer.csv"

def blank_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#1 : Membuat file data baru dalam format csv
def buat_baru():
    blank_screen()
    with open(nama_file, 'w', newline='') as csv_file: 
        header = ["Tanggal","Nama Barang","Jumlah","Estimasi","Biaya Total"]
        tulis = csv.writer(csv_file, delimiter=';')
        tulis.writerow(header)
    print("File Berhasil Dibuat")
    kembali()

#2 : Menambah atau menulis file data baru
def tambahkan():
    blank_screen() 
    with open(nama_file, 'a', newline='') as csv_file:

        print("TAMBAHKAN BARANG".center(90))
        print("SERVIS ELEKTRONIK DAN KOMPUTER".center(90))
        print("="*90)      
        tanggal = input('Tanggal : ')
        nama = input('Nama Barang : ') 
        jumlah = int(input('Jumlah : ')) 
        biaya = int(input('Estimasi : Rp.')) 
        biaya_sementara = jumlah*biaya
        print("Estimasi Biaya Servis Anda : Rp.", biaya_sementara)
        data = [tanggal,nama,jumlah,biaya,biaya_sementara]
        tulis = csv.writer(csv_file, delimiter=';')
        tulis.writerow(data)
    print("Data sukses ditambahkan..")
    kembali() 

#3 : Menampilkan data dari file sebelumnya
def tampil_data():
    blank_screen()
    barang = []
    with open(nama_file) as csv_file:
        read_data = csv.reader(csv_file, delimiter=";")
        for row in read_data:
            barang.append(row)
    print("TAMPILKAN BARANG".center(90))
    print("SERVIS ELEKTRONIK DAN KOMPUTER".center(90))
    print("_"*90)
    if len(barang) > 1:
        number = -1
        for dt in barang:
            number += 1
            print (f"{str(number)} \t {dt[0]:<15} {dt[1]:<18} {dt[2]:^17} {dt[3]:<19} {dt[4]:<18}")
            print ("="*85)
        kembali()
    elif len(barang) <=1 :
        print("TIDAK ADA BARANG".center(90))
        kembali()

#4 : Menghapus data yang ingin dihapus
def hapus():
    blank_screen()
    barang = []
    with open(nama_file) as csv_file: 
        read_data = csv.reader(csv_file, delimiter=";")
        for row in read_data:
            barang.append(row)
    print("HAPUS DATA BARANG".center(90))
    print("SERVIS ELEKTRONIK DAN KOMPUTER".center(90))
    print("="*90)
    if len(barang)>1:
        number = 0
        for dt in barang:
         print (f"{str(number)} \t {dt[0]:<15} {dt[1]:<18} {dt[2]:^17} {dt[3]:<19} {dt[4]:<18}")
        number += 1
        print ("_"*90)
    elif len(barang) <= 1:
        print("TIDAK ADA BARANG".center(90))
        kembali()
    number = int(input('Pilih nomer : '))
    del barang[number]
    with open(nama_file, 'w', newline='') as csv_file:
        tulis = csv.writer(csv_file, delimiter=';')
        for dt in barang:
            data = [dt[0],dt[1],dt[2],dt[3],dt[4]]
            tulis.writerow(data)
    print("Data sukses dihapus..")
    kembali()

#5 mengedit data
def edit_data():
    blank_screen()
    barang = [] 
    with open(nama_file, mode="r") as csv_file:
        read_data = csv.reader(csv_file, delimiter=";")
        for row in read_data:
             barang.append(row)
        print("UBAH DATA BARANG".center(90))
        print("SERVIS ELEKTRONIK DAN KOMPUTER".center(90))
        print("="*90)
        if len(barang) > 1:
            number = 0
            for dt in barang:
                print (f"{str(number)} \t {dt[0]:<15} {dt[1]:<18} {dt[2]:^17} {dt[3]:<19} {dt[4]:<18}")
                number += 1
                print ("_"*90)
            number = int(input('Pilih nomer : '))
            tanggal = input('\nTanggal : ')
            nama = input('Nama Barang : ') 
            jumlah = int(input('Jumlah : ')) 
            biaya = int(input('Estimasi : Rp.')) 
            biaya_sementara = jumlah*biaya
            
            barang[number][0] = tanggal
            barang[number][1] = nama
            barang[number][2] = jumlah
            barang[number][3] = biaya
            barang[number][4] = biaya_sementara
                    
            with open(nama_file, 'w', newline='') as csv_file:
                tulis = csv.writer(csv_file, delimiter=';')
                for dt in barang:
                    data = [dt[0],dt[1],dt[2],dt[3],dt[4]]
                    tulis.writerow(data)
            print("Data sukses diubah..")
            kembali()

        elif len(barang) <= 1:
            print("TIDAK ADA BARANG".center(90))
            kembali()

def beranda():
    blank_screen()
    print("="*72)
    print("SELAMAT DATANG".center(72))
    print('APLIKASI PENCATATAN SERVIS ELEKTRONIK DAN KOMPUTER'.center(72))
    print("="*72)
    print(''' 
    |99| Keluar
    |1|  Buat daftar Servis [.csv] 
    |2|  Tambah data Servis
    |3|  Lihat data Servis
    |4|  Hapus data Servis (Jika sudah)
    |5|  Edit data Servis''') 
    print("="*72)
    pilihan_menu = input(" Pilih tindakan : ")
    if(pilihan_menu == "1"):
        buat_baru() 
    elif(pilihan_menu == "2"): 
        tambahkan() 
    elif(pilihan_menu == "3"):
        tampil_data() 
    elif(pilihan_menu == "4"):
        hapus()  
    elif(pilihan_menu == "5"):
        edit_data()
    elif(pilihan_menu == "99"): 
        exit()
    else:
        kembali()

def kembali():
    input("\n Tekan enter untuk kembali ke beranda..")
    beranda()

if __name__== "__main__":
    while True:
        beranda()
