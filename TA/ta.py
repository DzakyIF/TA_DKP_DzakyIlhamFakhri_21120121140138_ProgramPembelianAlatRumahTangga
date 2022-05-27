from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from PIL import ImageTk, Image

#1. Modul 1 = Variabel
#2. Modul 2 = Pengkondisian
#3. Modul 4 = Fungsi
#4. Modul 5 = OOP 1 (Class)
#5. Modul 6 = OOP 2 (Setter, Getter)
#6. Modul 8 = GUI


root = Tk()
root.geometry("950x540")
root.title("Program Pembelian Alat Rumah Tangga")
root.resizable(width = 0, height = 0)
bg1 = ImageTk.PhotoImage(Image.open("C:/Coding/Code/Python/TA/Image1.png").resize((950, 540), Image.ANTIALIAS))
labelbg = Label(root, image=bg1)
labelbg.place(x=0, y=0)

label1 = Label(root, text="SELAMAT DATANG DI", font=("times new roman", 22), bg='#c2feff')
label1.place(x=555, y=145)
label2 = Label(root, text="TOKO ALAT RUMAH TANGGA", font=("times new roman", 22), bg='#c2feff')
label2.place(x=505, y=180)
label3 = Label(root, text="Informasi Pembeli :", font=("times new roman", 16), bg='#c2feff')
label3.place(x=425, y=250)
label4 = Label(root, text="Nama                    :", font=("times new roman", 12), bg='#c2feff')
label4.place(x=425, y=300)
label5 = Label(root, text="Alamat pengiriman :", font=("times new roman", 12), bg='#c2feff')
label5.place(x=425, y=330)
enama = Entry(root, width=35)
enama.place(x=560, y=305)
ealam = Entry(root, width=35)
ealam.place(x=560, y=335)

main_menu = Menu(root)
root.config(menu=main_menu)


class katakatabk:
    def __init__(self, kata = 0):
        self.katta = kata

    def setkatta(self, x):
        self.katta = x

    def getkatta(self):
        return self.katta


class fungsiframe1:
    def beli_click():
        bsapu = int(frame1.qsapu.get())
        bpel = int(frame1.qpel.get())
        bsetrika = int(frame1.qsetrika.get())
        bjemba = int(frame1.qjemba.get())
        totalbelanja = str((bsapu*30000)+(bpel*32500)+(bsetrika*125000)+(bjemba*115000))
        
        ynbeli = messagebox.askyesno("Konfirmasi", "Apakah Barang Yang Dibeli Sudah Benar")
        if ynbeli == 1:
            messagebox.showinfo("Shipping", "Name : "+enama.get()+"\nAlamat : "+ealam.get()+"\nTotal Harga : Rp."+totalbelanja)
            root.destroy()


class taroframe:
    def new_frame_1():
        taroframe.hide_frame()
        frame1.frame_1.pack(fill="both", expand=1)

    def hide_frame():
        frame1.frame_1.pack_forget()


class menus:
    menu_0 = Menu(main_menu)
    main_menu.add_cascade(label="Homepage", command=taroframe.hide_frame)


    menu_1 = Menu(main_menu)
    main_menu.add_cascade(label="Catalogue", command=taroframe.new_frame_1)

    menu_3 = Menu(main_menu)
    main_menu.add_cascade(label="Exit", command=root.quit)


class frame1:
    frame_1 = Frame(root, width=950, height=540)
    fbg = ImageTk.PhotoImage(Image.open("C:/Coding/Code/Python/TA/Image1.png").resize((950, 540), Image.ANTIALIAS))
    labelbg = Label(frame_1, image=fbg)
    labelbg.place(x=0, y=0)

    fsapu = ImageTk.PhotoImage(Image.open("C:/Coding/Code/Python/TA/sapu.png").resize((100, 150), Image.ANTIALIAS))
    labelbg = Label(frame_1, image=fsapu)
    labelbg.place(x=50, y=50)
    lsapu = Label(frame_1, text="Sapu : Rp.30.000", font=("times new roman", 12), bg='#c2feff')
    lsapu.place(x=44, y=25)
    qlsapu = Label(frame_1, text="Beli : ", bg='#c2feff')
    qlsapu.place(x=67, y=203)
    qsapu = Entry(frame_1, width=5)
    qsapu.place(x=102, y=204)

    fpel = ImageTk.PhotoImage(Image.open("C:/Coding/Code/Python/TA/pel.png").resize((100, 150), Image.ANTIALIAS))
    labelbg = Label(frame_1, image=fpel)
    labelbg.place(x=200, y=50)
    lpel = Label(frame_1, text="Pel : Rp.32.500", font=("times new roman", 12), bg='#c2feff')
    lpel.place(x=201, y=25)
    qlpel = Label(frame_1, text="Beli : ", bg='#c2feff')
    qlpel.place(x=220, y=203)
    qpel = Entry(frame_1, width=5)
    qpel.place(x=252, y=204)

    fsetrika = ImageTk.PhotoImage(Image.open("C:/Coding/Code/Python/TA/setrika.png").resize((125, 95), Image.ANTIALIAS))
    labelbg = Label(frame_1, image=fsetrika)
    labelbg.place(x=350, y=100)
    lsetrika = Label(frame_1, text="Setrika : Rp.125.000", font=("times new roman", 12), bg='#c2feff')
    lsetrika.place(x=347, y=75)
    qlsetrika = Label(frame_1, text="Beli : ", bg='#c2feff')
    qlsetrika.place(x=379, y=199)
    qsetrika = Entry(frame_1, width=5)
    qsetrika.place(x=411, y=200)

    fjemba = ImageTk.PhotoImage(Image.open("C:/Coding/Code/Python/TA/jemuran.png").resize((145, 145), Image.ANTIALIAS))
    labelbg = Label(frame_1, image=fjemba)
    labelbg.place(x=545, y=50)
    ljemba = Label(frame_1, text="Jemuran : Rp.115.000", font=("times new roman", 12), bg='#c2feff')
    ljemba.place(x=549, y=25)
    qljemba = Label(frame_1, text="Beli : ", bg='#c2feff')
    qljemba.place(x=589, y=198)
    qjemba = Entry(frame_1, width=5)
    qjemba.place(x=621, y=200)

    tombolbeli = Button(frame_1, text="BELI", command= fungsiframe1.beli_click, font=("times new roman", 30))
    tombolbeli.place(x=790, y=425)

    katakata = katakatabk()
    katakata.setkatta("Mohon Untuk Masukkan Angka Bukan Alfabet Di Kolom Belinya")
    katakata = Label(frame_1, text=katakata.getkatta(), bg="#c2feff")
    katakata.place(x=580, y=515)


root.mainloop()