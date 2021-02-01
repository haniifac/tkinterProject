# Setting
from tkinter import *
root = Tk()
root.title("Haniif's Garage")
root.minsize(500,500)
root.maxsize(500,500)
root.config(bg="#dff0c5")
root.iconbitmap("C:/Users/Hans/Desktop/coding python/img/tire.ico")

###################################  CODE  ###############################################

############################# List Mobil
mobilList = []

####### Login Menu
#> Function
def loginTombol():
    nama = login_id.get()
    if nama == "a":
        labelgagal.place_forget()
        labelberhasil.place(x=220,y=290)
        tombol_login.after(1100, lambda : menu_hapus())
        tombol_login.after(1150, lambda : mainMenu())
    else:
        labelgagal.place(x=220,y=290)


#> Define
line = Label(root, text="===============================", font=("Courier",20), bg="#dff0c5")
line2 = Label(root, text="===============================", font=("Courier",20), bg="#dff0c5")
heading = Label(root, text="Selamat Datang di Garasi Haniif", font=("Courier",18), bg="#dff0c5")
login_id_label = Label(root, text="Username", bg="#dff0c5")
login_id = Entry(root, width=20)
tombol_login = Button(root, text="Login", padx=50, pady=10, command=loginTombol)
labelberhasil = Label(root, text="Login berhasil!", bg="green", fg="white", padx=10, pady=10)
labelgagal = Label(root, text="Login gagal!", bg="red", fg="white", padx=10, pady=10)

#> Place
def menu_taruh():
    line.grid(row=0,column=0)
    heading.grid(row=1,column=0)
    line2.grid(row=2,column=0)
    login_id_label.place(x=160,y=200)
    login_id.place(x=230,y=200)
    tombol_login.place(x=200,y=230)
    
def menu_hapus():
    line.grid_forget()
    heading.grid_forget()
    line2.grid_forget()
    login_id_label.place_forget()
    login_id.place_forget()
    tombol_login.place_forget()
    labelberhasil.place_forget()
    root.config(bg="white")

menu_taruh()


##############################  Menu Tambah Mobil
#> Fuction


#> Define
tambahEntry = Entry(root, width=20)
tambahButton = Button(root, text="Tambahkan!",font=("Courier",16),bg="white")

#> Place
def tambahmobilMenu():
    tambahEntry.place(x=100,y=100)
    tambahButton.place(x=100, y=120)




########################### Main Menu
#> Function
def tomboltambahfungsi():
    hapusMainMenu()
    tambahmobilMenu()

#> Place
def mainMenu():
    headingMenu.place(x=150,y=40)
    lineMainmenu.place(x=40,y=70)
    tombolTambahMobil.place(x=130,y=140)
    tombolHapusMobil.place(x=270,y=140)
    tombolListMobil.place(x=109,y=190)

def hapusMainMenu():
    headingMenu.forget()
    lineMainmenu.forget()
    tombolTambahMobil.forget()
    tombolHapusMobil.forget()
    tombolListMobil.forget()
    root.config(bg="white")
    
#> Define
headingMenu = Label(root, text="Pilih tombol",font=("Courier",20),bg="white")
lineMainmenu = Label(root, text="===============================", font=("Courier",16), bg="white")
tombolTambahMobil = Button(root, text="Tambah",font=("Courier",16),command=hapusMainMenu)
tombolHapusMobil = Button(root, text="Hapus",font=("Courier",16))
tombolListMobil = Button(root, text="List Mobil",font=("Courier",16),padx=60, pady=5)




######################################  END  #####################################
root.mainloop()