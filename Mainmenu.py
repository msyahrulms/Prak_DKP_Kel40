def customer(nama):
    orang = nama
    print('='*100)
    print('Halo Selamat Datang Di Pusat Rekomendasi HP Terbaik')
    print('Dengan ID:')
    return orang
a = customer(nama = input('Masukan nama anda : '))
print(a)

class HP() :   
    def merek(self, merk):
        merk = merk.capitalize()
        if merk == 'Samsung':
            print('Rekomendasi HP terbaik anda : Samsung Galaxy A01 Core')
        elif merk == 'Evercoss' :
            print('Rekomendasi HP terbaik anda : Evercoss M6A')
        elif merk == 'Nokia' :
            print("Rekomendasi HP terbaik anda : Nokia C1 2020")
        else :
            print ('Belum ada HP yang cocok')
    def merek1(self, merk1):
        merk1 = merk1.capitalize()
        if merk1 == 'Advan' :
            print ('Rekomendasi HP terbaik anda : Advan GX')
        elif merk1 == 'Infinix':
            print ('Rekomendasi HP terbaik anda : Infinix Hot 11s NFC')
        else :
            print ('Belum ada HP yang cocok')
    def merek2(self, merk2):
        merk2 = merk2.capitalize()
        if merk2 == 'Infinix' :
            print ('Rekomendasi HP terbaik anda : Infinix Note 10 pro')
        elif merk2 == ('POCO') :
            print ('Rekomendasi HP terbaik anda : Poco M3 Pro 5G')
        elif merk2 == 'Samsung' :
            print ('Rekomendasi HP terbaik anda : Samsung Galaxy A22 LTE')
        else :
            print ('Belum ada HP yang cocok')
    def merek3(self, merk3):
        merk3=merk3.capitalize()
        if merk3 == 'Iphone' :
            print ('Rekomendasi HP terbaik anda : Iphone 13 Pro')
        elif merk3 == 'Asus' :
            print ('Rekomendasi HP terbaik anda : ASUS ROG Phone 5')
        elif merk3 == 'Samsung' :
            print ('Rekomndasi HP terbaik untuk anda : Samsung Galaxy S22 Ultra')
        else :
            print ('Belum ada HP yang cocok')
n=1
while (n<=1):
    budget = float(input ("Masukan modal anda dalam Juta : "))
    
    if 0 < budget <= 1 :
        rekomendasi = HP()
        rekomendasi.merek(merk=input('Masukan nama merk: '))
    elif 1 < budget <= 2 :
        rekomendasi = HP()
        rekomendasi.merek1(merk1=input('Masukan nama merk: '))
    elif 2 < budget <= 3 :
        rekomendasi = HP()
        rekomendasi.merek2(merk2=input('Masukan nama merk: '))
    else :
        rekomendasi = HP()
        rekomendasi.merek3(merk3=input('Masukan nama merk: '))

    print('Apakah anda ingin rekomendasi lainnya')
    print ('1(Ya) / 2(Tidak)')
    n = int(input())
print('Sampai jumpa lagi',a)
