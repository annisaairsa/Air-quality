import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset dari file yang telah diunggah
data = pd.read_csv("/mnt/data/PRSA_Data_Huairou_20130301-20170228.csv")

# Deskripsi
st.write('Dasboard ini menyediakan cara interaktif untuk menjelajahi data kualitas udara, khususnya berfokus pada tingkat PM10 dan hubungannya dengan berbagai kondisi cuaca.')

# About me
st.markdown("""
### About Me
- **Name**: Annisaa Irsalina Razita
- **Email Address**: annisaairsalinarazita@gmail.com
- **Dicoding ID**: -

### Project Overview
Dashboard ini menyajikan analisis data kualitas udara, khususnya yang berfokus pada tingkat PM10 dari Huairou. Project ini bertujuan untuk mengungkap pola, variasi musiman, dan dampak kondisi cuaca yang berbeda terhadap kualitas udara. Wawasan dari analisis ini dapat bermanfaat untuk studi lingkungan dan pemantauan kesehatan masyarakat.
""")

# Menambahkan sidebar untuk input interaktif
st.sidebar.header('Fitur Input User')

# Pastikan kolom tanggal diubah menjadi tipe datetime untuk pemfilteran data
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']].astype(str).agg('-'.join, axis=1), format='%Y-%m-%d-%H')

# Menambahkan tahun dan bulan untuk dipilih user
selected_year = st.sidebar.selectbox('Pilih Tahun', data['year'].unique())
selected_month = st.sidebar.selectbox('Pilih Bulan', data['month'].unique())

# Filter data berdasarkan tahun dan bulan yang dipilih
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Menampilkan statistik data
st.subheader('Tinjauan Data untuk Periode yang Dipilih')
st.write(data_filtered.describe())

# Line chart untuk tingkat PM10 selama bulan yang dipilih
st.subheader('Tingkat PM10 Harian')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM10'])
plt.xlabel('Hari dalam Sebulan')
plt.ylabel('Konsentrasi PM10')
st.pyplot(fig)

# Analisis Pola Musiman
st.subheader('Analisis Pola Musiman')
seasonal_trends = data.groupby('month')['PM10'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='purple', ax=ax)
plt.title('Rata-rata Tingkat PM10 Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata PM10')
st.pyplot(fig)

# Rata-rata Heatmap per jam
st.subheader('Rata-rata PM10 per jam')
try:
    # Memastikan tipe data yang benar dan menangani nilai yang hilang
    data['hour'] = data['hour'].astype(int)
    data['PM10'] = pd.to_numeric(data['PM10'], errors='coerce')
    data['PM10'].ffill(inplace=True)

    # Menghitung rata-rata per jam
    hourly_avg = data.groupby('hour')['PM10'].mean()

    # Plotting
    fig, ax = plt.subplots()
    sns.heatmap([hourly_avg.values], ax=ax, cmap='coolwarm')
    plt.title('Rata-rata PM10 per jam')
    st.pyplot(fig)
except Exception as e:
    st.error(f"Error dalam memplotkan rata-rata per jam: {e}")

# Membandingkan Curah Hujan dengan Kualitas Udara
st.subheader('Membandingkan Curah Hujan dengan tingkat PM10')
fig, ax = plt.subplots()
sns.scatterplot(x='rain', y='PM10', data=data_filtered, ax=ax)
plt.title('Perbandingan Curah Hujan dengan tingkat PM10')
st.pyplot(fig)

# Korelasi Heatmap - Interaktif
st.subheader('Korelasi Heatmap Interaktif')
selected_columns = st.multiselect('Pilih Kolom untuk Korelasi', data.columns, default=['PM10', 'NO2', 'TEMP', 'PRES', 'DEWP'])
corr = data[selected_columns].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)

# Kesimpulan
st.subheader('Kesimpulan')
st.write("""
- Dashboard ini menyediakan analisis data kualitas udara yang mendalam dan interaktif.
- Berbagai visualisasi yang menawarkan wawasan tentang tingkat PM10, distribusinya, dan faktor-faktor yang mempengaruhinya.
- Pola musiman dan dampak kondisi cuaca dan polutan yang berbeda terhadap kualitas udara digambarkan dengan jelas.
- Pengguna dapat menjelajahi data secara dinamis untuk mendapatkan pemahaman yang lebih dalam tentang pola kualitas udara.
""")
