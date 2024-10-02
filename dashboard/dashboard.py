import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul halaman
st.set_page_config(page_title="Air Quality Dashboard")

# Judul aplikasi
st.title("Data Analysis Air Quality - Huairou")

# Deskripsi
st.markdown("""
<div style="text-align: justify;">
    Dashboard ini menyajikan analisis data kualitas udara, dengan fokus pada tingkat PM10 dari daerah Huairou. 
    Proyek ini bertujuan untuk mengidentifikasi pola, variasi musiman, dan pengaruh kondisi cuaca terhadap kualitas udara. 
    Wawasan yang diperoleh dari analisis ini dapat berguna untuk penelitian lingkungan dan pemantauan kesehatan masyarakat, 
    serta membantu dalam pengambilan keputusan terkait kebijakan lingkungan dan mitigasi polusi.
</div>
""", unsafe_allow_html=True)

# Memuat data dari file lokal
data = pd.read_csv("C:/Users/MY HP/Documents/air-quality/dashboard/PRSA_Data_Huairou_20130301-20170228.csv")  # Ganti dengan path yang sesuai

# Menambahkan gambar ikonik Huairou di bagian atas sidebar
st.sidebar.image("https://mediaim.expedia.com/destination/1/339748b6d2ac7e127e541e8e8d51a634.jpg", caption="Ikonik Huairou", use_column_width=True)

# Cek kolom yang ada
if 'year' in data.columns and 'month' in data.columns and 'day' in data.columns:
    # Menambahkan sidebar untuk input interaktif
    st.sidebar.header('Fitur Rentang Waktu')

    # Memungkinkan pengguna memilih tahun dan bulan untuk melihat data
    selected_year = st.sidebar.selectbox('Pilih Tahun', sorted(data['year'].unique()))
    selected_month = st.sidebar.selectbox('Pilih Bulan', sorted(data['month'].unique()))

    # Filter data berdasarkan tahun dan bulan yang dipilih
    data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

    # Menampilkan statistik data
    st.subheader('Tinjauan Data untuk Periode yang Dipilih')
    st.write(data_filtered.describe())

    # Line chart untuk tingkat PM10 selama bulan yang dipilih
    st.subheader('Tingkat PM10 Harian')
    fig, ax = plt.subplots()
    ax.plot(data_filtered['day'], data_filtered['PM10'])  # Ganti 'PM10' jika kolom berbeda
    plt.xlabel('Hari dalam Sebulan')
    plt.ylabel('Konsentrasi PM10')
    st.pyplot(fig)

    # Analisis Pola Musiman
    st.subheader('Analisis Pola Musiman')
    seasonal_trends = data.groupby('month')['PM10'].mean()  # Ganti 'PM10' jika kolom berbeda
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
        data['hour'] = data['hour'].astype(int)  # Ganti 'hour' jika kolom berbeda
        data['PM10'] = pd.to_numeric(data['PM10'], errors='coerce')  # Ganti 'PM10' jika kolom berbeda
        data['PM10'].ffill(inplace=True)

        # Menghitung rata-rata per jam
        hourly_avg = data.groupby('hour')['PM10'].mean()  # Ganti 'PM10' jika kolom berbeda

        # Plotting
        fig, ax = plt.subplots()
        sns.heatmap([hourly_avg.values], ax=ax, cmap='coolwarm', annot=False)  # Menonaktifkan anotasi
        plt.title('Rata-rata PM10 per jam')
        plt.xlabel('Jam')
        plt.yticks([])  # Menyembunyikan label y-axis
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error dalam memplotkan rata-rata per jam: {e}")

    # Membandingkan Curah Hujan dengan Kualitas Udara
    st.subheader('Membandingkan Curah Hujan dengan Tingkat PM10')
    fig, ax = plt.subplots()
    sns.scatterplot(x='RAIN', y='PM10', data=data_filtered, ax=ax)  # Ganti 'RAIN' dan 'PM10' jika kolom berbeda
    plt.title('Perbandingan Curah Hujan dengan Tingkat PM10')
    plt.xlabel('Curah Hujan')
    plt.ylabel('Konsentrasi PM10')
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
    - Dashboard ini menyajikan informasi penting mengenai tingkat PM10 di Huairou, menunjukkan variasi musiman yang signifikan. 
    - Tingkat PM10 cenderung lebih tinggi pada bulan tertentu, dipengaruhi oleh faktor lingkungan. 
    - Curah hujan memiliki efek positif dalam menurunkan konsentrasi PM10, menunjukkan pentingnya cuaca dalam mempengaruhi kualitas udara.
    - Temuan ini dapat mendukung kebijakan lingkungan dan strategi mitigasi polusi untuk meningkatkan kualitas udara di wilayah tersebut. 
    """)

else:
    st.error("Kolom 'year', 'month', atau 'day' tidak ditemukan di dataset.")

# About me
st.markdown(""" 
### About Me 
- **Name**: Annisaa Irsalina Razita
- **Email Address**: annisaairsalinarazita@gmail.com
- **Dicoding ID**: 
""")
