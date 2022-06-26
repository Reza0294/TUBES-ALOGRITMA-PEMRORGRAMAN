print("SELAMAT DATANG GAME QUESTION!!")

nama = input("Masukan Nama Anda: ")
poin = 0
chance = 1

print("Halo" + nama,",Selamat Datang")
print("Anda akan memulai menjawab quiz,dan mendapat nilai apabila benar")


playing = input("Apakah kamu sudah Siap? ")

while chance > 0:
    if poin  < 75:

        print("Anda harus mendapatkan nilai 75,agar berhasil")
        print("Anda mempunyai",chance,"kesempatan")
        
        mulai = input("Anda sudah Siap?")

        if mulai == "Siap" :
         poin  -=  poin
        chance -= 1

    print("Ayo kita mulai!!!")

print("1) Apa Nama ibukota Indonesia adalah?:  ")
jawaban = input ()
if jawaban == "Jakarta" :
    poin += 20
    print("Selamat anda mendapatkan 20 poin, poin anda", poin)
else :
    print("Maaf jawaban anda salah, poin anda", poin)

print("2)Apa nama ibukota jerman adalah?: ")
jawaban = input ()
if jawaban == "Berlin" :
    poin += 20
    print("Selamat anda mendapatkan 20 poin, poin anda", poin)
    
else:
    print("Maaf jawaban anda salah, poin anda",  poin)

print("3) Siapa Wakil Presiden pertama Repuvlik Indonesia?: ")
jawaban = input ()
if jawaban == "Moh.Hatta" :
    poin += 20
    print("Selamat anda mendapatkan 20 poin, poin anda", poin)
    
else:
    print("Maaf jawaban anda salah, poin anda",  poin)

print("4) Apa nama makanan khas Sumatera Barat?: ")
jawaban = input ()
if jawaban == "Rendang" :
    poin += 20
    print("Selamat anda mendapatkan 20 poin, poin anda", poin)
    
else:
    print("Maaf jawaban anda salah, poin anda",  poin)

print("5)Apa nama Universitas Swasta nomor satu di Indonesia?:  ")
jawaban = input ()
if jawaban == "Universitas Telkom" :
    poin += 20
    print("Selamat anda mendapatkan 20 poin, poin anda", poin)
    
else:
    print("Maaf jawaban anda salah, poin anda",  poin)
 
  
print("Selamat "+nama,"Anda telah selesai,poin yang anda miliki adalah",poin)
if poin >=75:
    print("Anda dinyatakan lulus")
else:
    print("Anda dinyatakan tidak lulus")

print("Terima kasih atas waktunya telah menyelsaikan game kami:))")

