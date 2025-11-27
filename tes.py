# Soal 1 - Membaca Dataset dan Eksplorasi Awal [cite: 14]

# 1. Impor library pandas
import pandas as pd
import matplotlib.pyplot as plt # Kita impor ini juga buat Soal 9 nanti

# Baca file csv ke dalam DataFrame bernama df 
# Pastikan file csv ada di folder yang sama dengan kodingan kamu ya!
df = pd.read_csv('jumlah_sampah_jabar.csv')

# 2. Tampilkan 5 baris pertama [cite: 16]
print("--- 5 Baris Pertama Data ---")
print(df.head())

# 3. Tampilkan informasi struktur DataFrame [cite: 17]
print("\n--- Informasi Data ---")
print(df.info())