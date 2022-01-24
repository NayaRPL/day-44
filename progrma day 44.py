print("cara menggunakan break and continue dalam perulangan for")
print("menggunakan break")
for nilai in range(10):
    if nilai == 5:
      break
    print(nilai)
#penjelasannya: break artinya di sini adalah kita menghentikan secara paksa dari perulangan
#yang kita jalankan. oleh karena itu apa bila kita ingin di dalam perululangan tidak menampilkan
#semua nilai dari batsannya kita dapat menggunakan break
print("menggunakan continue")
for nilai in range(10):
    if nilai == 5:
      continue
    print(nilai)
#penpenjelasannya : continue artinya adalah kita menskip nilai dari yang di jalankan,jadi
    #apabila kita ingin di dalam perulangan kita tidak ingin menampilakan angka 5 maka kita
    #dapat mengginakan continue
print("for yang menggunakan list")
nama=["naya","awal","dina","lisa","luppi","salsa"]
for isi in(nama):
    print(isi)
print("menggunkan continue")
nama=["naya","awal","dina","lisa","luppi","salsa"]
for isi in nama:
    if isi == "awal" and "luppi":
        continue
    print(isi)
print("memakai fungsi enumerate dalam list")
kota=["majene","makassar","polewali","mamuju"]
for i,nilai in enumerate(kota):
    print(i,nilai)
#penjelasannya : fungsi enumerate dala data list adalah untuk
#memunculkan indeks da item dari data list   
print("memunculkan angka genap")
for i in range (20):
    if i /2 != 1:
        continue
    print(i)

kota=["majene","makassar","polewali","mamuju"]
nilai=input("masukkan kota yang ingin di cari:")
for indeks,i in enumerate (kota) :
    if i == nilai :
        print("kota yang anda cari berada pada indeks ",indeks,"yaitu:",i)
        break
else :
     print("kota yang anda cari tidak ada dalam dat list")


    
