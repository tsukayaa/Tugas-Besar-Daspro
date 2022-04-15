# Deskripsi : Register

# Admin dapat mendaftarkan pengguna baru dengan memasukkan nama, username,
# dan password. Pengguna yang mendaftar otomatis memiliki role “user”.
# Pastikan username bersifat unik. Fungsi ini tidak dapat membuat user dengan
# role admin; untuk membuat user admin dapat mengedit file penyimpanan.
# Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”,
# dan angka 0-9.

# akses: admin
# >>> register
from array_csv import user
from perpustakaan_fungsi import length

def validasi_reg(username_user):
    for i in range(length(username_user)):
        kondisi_salah = 0 <= ord(username_user[i]) <= 44 or 46 <= ord(username_user[i]) <= 47 or 58 <= ord(username_user[i]) <= 64 or 91 <= ord(username_user[i]) <= 94 or ord(username_user[i]) == 96 or 123 <= ord(username_user[i]) <= 127:
        if kondisi_salah:
            return False
        else:
            return True

def regis(nama, username, password):
    while validasi_reg(username) == False:
        print("Username hanya boleh mengandung alfabet (A-Z & a-z), underscore (_), strip (-), dan angka (0-9)")
        nama = input("Masukkan nama: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    else:
        for row in user:
            if user[row][1] == username :
                print('Username', username, 'sudah terpakai, silakan menggunakan username lain')
                break
            else:
                user_baru = [[nama,username,password]]
    return (user + user_baru)


# nama = input("Masukkan nama: ")
# username = input("Masukkan username: ")
# password = input("Masukkan password: ")