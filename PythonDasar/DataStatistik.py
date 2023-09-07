import numpy as np
import pandas as pd

# Membuat data contoh
data = np.random.randint(0, 100, size=(100))  # Data acak 100 angka antara 0 dan 100

# Membuat DataFrame dari data
df = pd.DataFrame(data, columns=['Angka'])

# Statistik deskriptif
mean = df['Angka'].mean()
median = df['Angka'].median()
min_value = df['Angka'].min()
max_value = df['Angka'].max()
std_deviation = df['Angka'].std()

# Menampilkan hasil statistik
print('Statistik Data')
print('--------------')
print('Rata-rata:', mean)
print('Median:', median)
print('Nilai Minimum:', min_value)
print('Nilai Maksimum:', max_value)
print('Standar Deviasi:', std_deviation)
