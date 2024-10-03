# Submission "Belajar Analisis Data dengan Python" Dicoding

# Deskripsi Project

Proyek ini menyajikan dashboard analisis data kualitas udara, dengan fokus pada tingkat PM10 di daerah Huairou. Tujuannya adalah untuk mengidentifikasi pola, variasi musiman, serta pengaruh kondisi cuaca terhadap kualitas udara. Wawasan dari analisis ini dapat bermanfaat bagi penelitian lingkungan, pemantauan kesehatan masyarakat, serta mendukung pengambilan keputusan terkait kebijakan lingkungan dan mitigasi polusi.

# Struktur Direktori
- **/dashboard**: Direktori ini berisi main.py yang digunakan untuk membuat dashboard hasil analisis data.
- **/data**: Direktori ini berisi data yang digunakan dalam proyek, dalam format .csv.
- **notebook.ipynb**: File ini yang digunakan untuk melakukan analisis data.
- **READ.md**: Ini adalah file dokumentasi.

# Installasi
1. Membuat dan Mengaktifkan Python Environment:
```
conda create --name airquality-ds python=3.9
conda activate airquality-ds
```
2. Install Paket yang Diperlukan:
```
pip install pandas numpy scipy matplotlib seaborn streamlit statsmodels
```

# Run Streamlit App
```
streamlit run dashboard.py
```
**Penggunaan**
1. Masuk ke direktori proyek (local):
 ```shell
    cd air-quality/dashboard/
    streamlit run dashboard.py
    ```

**Kunjungi Link Berikut**
(https://air-quality-annisaairsa.streamlit.app/)
