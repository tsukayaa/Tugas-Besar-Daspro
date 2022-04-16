# Deskripsi: Login

# Saat masuk ke dalam aplikasi, pengguna bisa login dengan memasukkan username dan password.
# Bila username dan password yang diinput cocok dengan username dan password pada file user,
# maka pengguna berhasil login. Untuk alur login dibebaskan;
# tidak harus mengetik “login” dulu diperbolehkan (misal, ketika sistem menyala user diwajibkan login,
# namun pastikan kalau belum login tidak bisa melakukan apa-apa selain login).

# akses: admin dan user
# >>> login

from array_csv import user

def login(users):
    global aksesadmin
    global idcurrentuser
    while True:
        username_input = input("Masukkan username : ")
        password_input = cipher_pass(input("Masukkan password : "))

        for row in user:
            if row[1] == username_input and row[3] == password_input:
                print('Halo ' + username_input + '! Selamat datang di "Binomo".')

                if row[4] == 'Admin':
                    aksesadmin = True
                else:
                    aksesadmin = False
                idcurrentuser = data[0]
                #akses['akun'] = data
                return akses
