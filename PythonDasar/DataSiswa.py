import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Inisialisasi
window = tk.Tk()
window.title("Data Siswa")

nis = tk.StringVar()

# Fungsi untuk menampilkan data siswa
def tampilkan_data():
    nis = nis_entry.get()
    nama = nama_entry.get()
    jenis_kelamin = jenis_kelamin_var.get()
    jurusan = jurusan_combobox.get()
    hobi = [hobi_pilihan[i] for i in range(len(hobi_var)) if hobi_var[i].get() == 1]
    alamat = alamat_text.get("1.0", "end-1c")
    pesan = f"NIS: {nis}\nNama: {nama}\nJenis Kelamin: {jenis_kelamin}\nJurusan: {jurusan}\nHobi: {hobi}\nAlamat: {alamat}"
    messagebox.showinfo("Data Siswa", pesan)

# Frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# Label dan Entry NIS
nis_label = ttk.Label(input_frame, text="NIS:")
nis_label.grid(row=0, column=0, sticky="W")
nis_entry = ttk.Entry(input_frame, textvariable=nis)
nis_entry.grid(row=0, column=1)

# Label dan Entry Nama
nama_label = ttk.Label(input_frame, text="Nama:")
nama_label.grid(row=1, column=0, sticky="W")
nama_entry = ttk.Entry(input_frame)
nama_entry.grid(row=1, column=1)

# Label dan Radiobutton Jenis Kelamin
jenis_kelamin_label = ttk.Label(input_frame, text="Jenis Kelamin:")
jenis_kelamin_label.grid(row=2, column=0, sticky="W")
jenis_kelamin_var = tk.StringVar()
jenis_kelamin_frame = ttk.Frame(input_frame)
jenis_kelamin_frame.grid(row=2, column=1, sticky="W")
jenis_kelamin_pilihan = [("Laki-laki", "Laki-laki"), ("Perempuan", "Perempuan")]
for i, (text, value) in enumerate(jenis_kelamin_pilihan):
    rb = ttk.Radiobutton(jenis_kelamin_frame, text=text, value=value, variable=jenis_kelamin_var)
    rb.grid(row=0, column=i, padx=5)

# Label dan Combobox Jurusan
jurusan_label = ttk.Label(input_frame, text="Jurusan:")
jurusan_label.grid(row=3, column=0, sticky="W")
jurusan_combobox = ttk.Combobox(input_frame, values=["IPA", "IPS", "Bahasa"])
jurusan_combobox.grid(row=3, column=1)
jurusan_combobox.current(0)

# Label dan Checkbox Hobi
hobi_label = ttk.Label(input_frame, text="Hobi:")
hobi_label.grid(row=4, column=0, sticky="W")
hobi_frame = ttk.Frame(input_frame)
hobi_frame.grid(row=4, column=1, sticky="W")
hobi_var = []
hobi_pilihan = ["Membaca", "Olahraga", "Musik", "Seni"]
for i, hobi in enumerate(hobi_pilihan):
    var = tk.IntVar()
    checkbtn = ttk.Checkbutton(hobi_frame, text=hobi, variable=var)
    checkbtn.grid(row=i, column=0, sticky="W")
    hobi_var.append(var)

# Label dan Textarea Alamat
alamat_label = ttk.Label(input_frame, text="Alamat:")
alamat_label.grid(row=5, column=0, sticky="W")
alamat_text = tk.Text(input_frame, height=4)
alamat_text.grid(row=5, column=1)

# Tombol Tampilkan Data
tombol_tampilkan = ttk.Button(window, text="Tampilkan Data", command=tampilkan_data)
tombol_tampilkan.pack(pady=10)

window.mainloop()
