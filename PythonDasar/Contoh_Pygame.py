import pygame

# Menginisialisasi Pygame
pygame.init()

# Mengatur lebar dan tinggi jendela
width, height = 800, 600

# Membuat jendela tampilan
screen = pygame.display.set_mode((width, height))

# Mengatur judul jendela
pygame.display.set_caption("Contoh Pygame")

# Loop utama permainan
running = True
while running:
    # Mendapatkan daftar event yang terjadi
    for event in pygame.event.get():
        # Keluar dari permainan jika tombol 'x' pada jendela ditutup
        if event.type == pygame.QUIT:
            running = False

    # Mengisi latar belakang jendela dengan warna putih
    screen.fill((255, 255, 255))

    # Memperbarui tampilan
    pygame.display.flip()

# Menutup Pygame
pygame.quit()
