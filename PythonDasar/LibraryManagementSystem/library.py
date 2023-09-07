from tkinter import *
import tkinter as tk #mengimport module tkinter
from tkinter import ttk #import ttk() widget
from tkinter import messagebox
import mysql.connector


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1440x850+0+0")

        #================================================== Variabel ==================================================
        self.member_var=StringVar()
        self.nis_var=StringVar()
        self.id_var=StringVar()
        self.nama_var=StringVar()
        self.kelas_var=StringVar()
        self.jurusan_var=StringVar()
        self.nohp_var=StringVar()
        self.idbuku_var=StringVar()
        self.judulbuku_var=StringVar()
        self.penulis_var=StringVar()
        self.tglpinjam_var=StringVar()
        self.tglkembali_var=StringVar()
        self.denda_var=StringVar()
 
        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM", bg="orange", fg="black", bd=20,relief=RIDGE, font=("times new roman",50,"bold"),padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="orange")
        frame.place(x=0, y=130, width=1440, height=400)

        #================================================== DataFrameLeft Frame ==================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="orange", fg="black", bd=7,relief=RIDGE, font=("times new roman",16,"bold"),padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=800, height=350)

        lblMember=Label(DataFrameLeft,text="Member Type", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=2)
        lblMember.grid(row=0,column=0,sticky=W)
        cbMember=ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.member_var, width=27,state="readonly")
        cbMember["value"]=("Admin Staff","Student","Teacher")
        cbMember.grid(row=0,column=1)

        lblNis=Label(DataFrameLeft,text="NIS", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNis.grid(row=1,column=0,sticky=W)
        txtNis=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.nis_var,width=29)
        txtNis.grid(row=1, column=1)
        
        lblName=Label(DataFrameLeft,text="Full Name", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblName.grid(row=2,column=0,sticky=W)
        txtName=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.nama_var, width=29)
        txtName.grid(row=2, column=1)

        lblKelas=Label(DataFrameLeft,text="Kelas", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=2)
        lblKelas.grid(row=3,column=0,sticky=W)
        cbKelas=ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.kelas_var, width=27,state="readonly")
        cbKelas["value"]=("X","XI","XII")
        cbKelas.grid(row=3,column=1)
        
        lblJurusan=Label(DataFrameLeft,text="Jurusan", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=2)
        lblJurusan.grid(row=4,column=0,sticky=W)
        cbJurusan=ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.jurusan_var, width=27,state="readonly")
        cbJurusan["value"]=("Broadcasting","Multimedia","Rekayasa Perangkat Lunak", "Multimedia")
        cbJurusan.grid(row=4,column=1)

        lblNohp=Label(DataFrameLeft,text="No. HP", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNohp.grid(row=5,column=0,sticky=W)
        txtNohp=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.nohp_var, width=29)
        txtNohp.grid(row=5, column=1)

        lblIdBuku=Label(DataFrameLeft,text="ID Buku", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblIdBuku.grid(row=0,column=2,sticky=W)
        txtIdBuku=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.id_var, width=29)
        txtIdBuku.grid(row=0, column=3)

        lblJudulBuku=Label(DataFrameLeft,text="Judul Buku", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblJudulBuku.grid(row=1,column=2,sticky=W)
        txtJudulBuku=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.judulbuku_var, width=29)
        txtJudulBuku.grid(row=1, column=3)

        lblPenulis=Label(DataFrameLeft,text="Penulis", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPenulis.grid(row=2,column=2,sticky=W)
        txtPenulis=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.penulis_var, width=29)
        txtPenulis.grid(row=2, column=3)

        lblTglPinjam=Label(DataFrameLeft,text="Tanggal Peminjaman", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblTglPinjam.grid(row=3,column=2,sticky=W)
        txtTglPinjam=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.tglpinjam_var, width=29)
        txtTglPinjam.grid(row=3, column=3)

        lblTglKembali=Label(DataFrameLeft,text="Tanggal Pengembalian", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblTglKembali.grid(row=4,column=2,sticky=W)
        txtTglKembali=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.tglkembali_var, width=29)
        txtTglKembali.grid(row=4, column=3)

        lblDenda=Label(DataFrameLeft,text="Denda", bg="orange", fg="black", font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDenda.grid(row=5,column=2,sticky=W)
        txtDenda=Entry(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.denda_var, width=29)
        txtDenda.grid(row=5, column=3)

        #================================================== DataFrameRight ==================================================

        DataFrameRight=LabelFrame(frame,text="Book Details", bg="orange", fg="black", bd=7,relief=RIDGE, font=("times new roman",16,"bold"),padx=20)
        DataFrameRight.place(x=810, y=5, width=570, height=350)

        self.txtBox=Text(DataFrameRight, font=("arial", 12, "bold"), width=35, height=18, padx=0, pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar = Scrollbar(DataFrameRight) 
        listScrollbar.grid (row=0, column=1, sticky="ns")

        ListBooks=["Atomic Habit","How To Win Friends & Influence People", "Think Fast and Slow", "Meditations", "Good Vibes Good Life", "Man Search for Meaning",
                   "Autobiography M.K Gandhi", "Meditations","Letter from Stoic","Filosofi Teras","Laut Bercerita","You Do You","Healing is the New High","Now and Again",
                   "7 Habit of Highly Effective People","101 Essays that Will Change the Way You Think","Psychology of Money"]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="Atomic Habit"):
                self.judulbuku_var.set("Atomic Habit")
                self.booktitle_var.set("")

        listBox = Listbox(DataFrameRight, font=("times new roman", 15, "bold"), width=30, height=15)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in ListBooks:
            listBox.insert(END,item)

        #================================================== Button Frame ==================================================

        FrameButton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="orange")
        FrameButton.place(x=0, y=530, width=1440, height=100)

        btnShowData = Button(FrameButton, text="Show Data", font=("times new roman", 15, "bold"), width=23, bg="orange", fg="black")
        btnShowData.grid(row=0, column=0)
        btnAddData = Button(FrameButton, comman=self.add_data, text="Add Data", font=("times new roman", 15, "bold"), width=23, bg="orange", fg="black")
        btnAddData.grid(row=0, column=1)
        btnUpdateData = Button(FrameButton, text="Update Data", font=("times new roman", 15, "bold"), width=23, bg="orange", fg="black")
        btnUpdateData.grid(row=0, column=2)
        btnDeleteData = Button(FrameButton, text="Delete Data", font=("times new roman", 15, "bold"), width=23, bg="orange", fg="black")
        btnDeleteData.grid(row=0, column=3)
        btnResetData = Button(FrameButton, text="Reset", font=("times new roman", 15, "bold"), width=23, bg="orange", fg="black")
        btnResetData.grid(row=0, column=4)
        btnExit = Button(FrameButton, text="Exit", font=("times new roman", 15, "bold"), width=23, bg="orange", fg="black")
        btnExit.grid(row=0, column=5)

        #================================================== Information Frame ==================================================

        FrameDetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="orange")
        FrameDetails.place(x=0, y=600, width=1440, height=245)

        Table_frame=Frame(FrameDetails, bd=6,relief=RIDGE, bg="orange")
        Table_frame.place(x=0, y=2, width=1370, height=190)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame, column=("membertype", "nis", "nama", "kelas", "jurusan", "nohp",
                                                             "idbuku", "judulbuku", "penulis","tglpinjam","tglkembali","denda"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(comman=self.library_table.yview)

        
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("nis", text="NIS")
        self.library_table.heading("nama", text="Nama")
        self.library_table.heading("kelas", text="Kelas")
        self.library_table.heading("jurusan", text="Jurusan")
        self.library_table.heading("nohp", text="No HP")
        self.library_table.heading("idbuku", text="ID Buku")
        self.library_table.heading("judulbuku", text="Judul Buku")
        self.library_table.heading("penulis", text="Penulis")
        self.library_table.heading("tglpinjam", text="Tanggal Peminjaman")
        self.library_table.heading("tglkembali", text="Tanggal Pengembalian")
        self.library_table.heading("denda", text="Denda")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("nis", width=100)
        self.library_table.column("nama", width=100)
        self.library_table.column("kelas", width=100)
        self.library_table.column("jurusan", width=100)
        self.library_table.column("nohp", width=100)
        self.library_table.column("idbuku", width=100)
        self.library_table.column("judulbuku", width=100)
        self.library_table.column("penulis", width=100)
        self.library_table.column("tglpinjam", width=100)
        self.library_table.column("tglkembali", width=100)
        self.library_table.column("denda", width=100)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="", database="db_satu")
        my_cursor=conn.cursor()
        my_cursor.execute("inser into library values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            self.member_var.get(), 
            self.nis_var.get(),
            self.nama_var.get(),
            self.kelas_var .get(),
            self.jurusan_var.get(),
            self.nohp_var.get(),
            self.idbuku_var.get(),
            self.judulbuku_var.get(),
            self.penulis_var.get(),
            self.tglpinjam_var.get(),
            self.tglkembali_var.get(),
            self.denda_var.get()
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")
        

if __name__ == "__main__":
    root = tk.Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()