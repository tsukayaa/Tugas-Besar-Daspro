import os

parent_dir = 'C:\\Users\\Haziq\\Desktop\\TUBES DASPRO' #Parent directory, letak semua file dan program terkait tubes, bisa disesuaikan 

# Mencari apakah folder (F) sudah ada di parent_dir, True jika sudah ada, dan False jika belum ada
def find(F):
    path=os.path.join(parent_dir, F)
    return (os.path.exists(path))  

# Membuat folder baru (jika diperlukan)
def create(NewFolder):
    path=os.path.join(parent_dir, NewFolder)
    os.makedirs(path)

# Membuat file baru  
def make(NewFile,FolderName):
    f=open(NewFile, 'w')
    f.close()

    FileLoc=parent_dir+'\\'+FolderName+'\\'+NewFile
    os.replace(NewFile, FileLoc)

#Algoritma
#input=save (admin menginput perintah 'save')
def save():
    folder=str(input("Masukkan nama folder penyimpanan: "))

    if find(folder):
        # Program akan membuat file kosong baru (user.csv, game.csv, riwayat.csv, kepemilikan.csv) di folder
        # File kosong tersebut akan menggantikan file lama yang sudah ada
        make("user.csv", folder)
        make("game.csv",folder)
        make("riwayat.csv", folder)
        make("kepemilikan.csv", folder)
        # program akan memindahkan data dari array ke file kosong baru dengan fungsi rewrite
        #rewrite("user.csv")
        #rewrite("game.csv")
        #rewrite("riwayat.csv")
        #rewrite("kepemilikan.csv")
        
    else: #Jika nama folder penyimpanan yang diinput belum ada di parent_dir, maka buat folder baru
        create(folder)
        #Program akan membuat file baru (user.csv, game.csv, riwayat.csv, kepemilikan.csv) di folder
        make("user.csv", folder)
        make("game.csv",folder)
        make("riwayat.csv", folder)
        make("kepemilikan.csv", folder)
        #rewrite("user.csv")
        #rewrite("game.csv")
        #rewrite("riwayat.csv")
        #rewrite("kepemilikan.csv")





