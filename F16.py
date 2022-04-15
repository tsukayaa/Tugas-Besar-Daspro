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
folder=str(input("Masukkan nama folder penyimpanan: "))
file_user=str(input('Masukan nama file user : '))
file_game=str(input('Masukan nama file game : '))
file_riwayat=str(input('Masukan nama file riwayat : '))
file_kepemilikan=str(input('Masukan nama file kepemilikan : '))

if find(folder):
    make(file_user, folder)
    make(file_game,folder)
    make(file_riwayat, folder)
    make(file_kepemilikan, folder)
    #Kemudian data yang telah diolah dari fungsi sebelumnya dipindahkan ke file yang telah dibuat
    
else: #Jika nama folder penyimpanan yang diinput belum ada di parent_dir, maka buat folder baru
    create(folder)
    make(file_user, folder)
    make(file_game,folder)
    make(file_riwayat, folder)
    make(file_kepemilikan, folder)
    #Kemudian data yang telah diolah dari fungsi sebelumnya dipindahkan ke file yang telah dibuat




