import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Menggambar sebuah persegi
for i in range(4):
    t.forward(100)  # Maju sejauh 100 satuan
    t.right(90)    # Belok kanan sejauh 90 derajat

# Mengakhiri program saat layar di-klik
turtle.done()
