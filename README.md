# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam menghasilkan lulusan berkualitas. Namun demikian, dalam perjalanannya, institusi ini menghadapi tantangan signifikan berupa tingginya angka mahasiswa yang mengalami dropout (tidak menyelesaikan pendidikan).

Masalah dropout ini tidak hanya berdampak pada citra institusi tetapi juga secara langsung memengaruhi efektivitas dan efisiensi operasional pendidikan. Oleh karena itu, Jaya Jaya Institut berkomitmen untuk mendeteksi potensi mahasiswa yang akan dropout sejak dini agar bisa diberikan intervensi atau bimbingan lebih lanjut.

### Permasalahan Bisnis
Permasalahan bisnis yang diidentifikasi dalam proyek ini antara lain:
- Tingginya jumlah mahasiswa yang dropout setiap tahunnya.
- Tidak adanya sistem deteksi dini untuk memprediksi risiko dropout.
- Kurangnya data visualisasi untuk memahami faktor-faktor penyebab dropout.
- Keterbatasan dalam pengambilan keputusan berbasis data.

### Cakupan Proyek
Proyek ini akan mencakup beberapa bagian utama sebagai berikut:
- Pembuatan sistem visualisasi data (dashboard) untuk memberikan insight terkait mahasiswa dropout.
- Pengembangan model machine learning untuk memprediksi mahasiswa yang berisiko dropout.
- Implementasi prototipe sistem prediksi berbasis web menggunakan Streamlit.
- Rekomendasi actionable untuk institusi guna menanggulangi masalah dropout.

### Persiapan

Sumber data: [Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

📦 Setup Environment
**Opsi 1: Menggunakan anaconda**
```
conda create --name attrition-analysis python=3.9
conda activate attrition-analysis
pip install -r requirements.txt
```
**Opsi 2: Menggunakan Shell/Terminal**
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

**🐳 Menjalankan Metabase Menggunakan Docker**
Untuk memudahkan proses setup, Metabase dapat dijalankan menggunakan Docker. Ikuti langkah-langkah berikut:

1. Install Docker
   Unduh dan instal Docker sesuai sistem operasi Anda dari: https://www.docker.com/products/docker-desktop
2. Unduh Image Metabase
   Gunakan perintah berikut untuk mengunduh image Metabase versi 0.46.4:
   ```
   docker pull metabase/metabase:v0.46.4
   ```
3. Jalankan Container Metabase
   Gunakan perintah berikut untuk menjalankan Metabase dan menyimpan file database internal di folder lokal metabase-data:
   ```
   docker run -d -p 3000:3000 --name metabase \
   -v $PWD/metabase-data:/metabase-data \
   -e "MB_DB_FILE=/metabase-data/metabase.db" \
   metabase/metabase:v0.46.4
   ```
   Penjelasan:

   -v $PWD/metabase-data:/metabase-data: Menyimpan file konfigurasi Metabase secara lokal.

    -e "MB_DB_FILE=/metabase-data/metabase.db": Memberitahu Metabase untuk menyimpan database internal di lokasi tersebut.

4. Akses Metabase
   Buka browser dan akses Metabase pada URL berikut [](http://localhost:3000/setup)

   Gunakan akun login berikut:
   - Email: root@mail.com
   - Password: root123

5. Menghubungkan Metabase ke Supabase (PostgreSQL Cloud)
   Setelah login, pilih opsi untuk menambahkan database dan isi form koneksi berikut:

   - Database Type: PostgreSQL
   - Name: Supabase Attrition DB
   - Host: aws-0-ap-southeast-1.pooler.supabase.com
   - Port: 6543
   - Database Name: postgres
   - Username: postgres.kvcyzcbzhvxaxoorgwjz
   - Password: P82GkzdJEHx86cnk

   Klik Next dan tunggu hingga koneksi berhasil.

6. Lihat Dashboard 'Student Performance Dashboard'.
   

**⚙️ Setup Sistem Prediksi Dropout secara Lokal (Streamlit)**
1.  Pastikan Python 3 sudah terinstal.
2.  Instal pustaka tambahan (jika belum):
    ```bash
    pip install pandas scikit-learn streamlit joblib
    ```
3.  Pastikan file berikut tersedia dalam di direktori kerja Anda:
   - app.py → Aplikasi Streamlit
   - dropout_model.pkl → File model SVM yang sudah dilatih
   - scaler.pkl → StandardScaler untuk preprocessing data
   - label_encoder.pkl → Label Encoder untuk preprocessing data
   - selected_columns.pkl → Nama-nama kolom fitur
4.  Jalankan aplikasi Streamlit:
   ```
   streamlit run app.py
   ```
5. Akses aplikasi via browser di alamat:
   ```
   http://localhost:8501
   ```

## Business Dashboard
Dashboard ini dirancang untuk menganalisis faktor-faktor penyebab mahasiswa dropout. Komponen utama dari dashboard ini meliputi:
1. Ringkasan umum yang menampilkan jumlah mahasiswa berdasarkan statusnya (Dropout, Graduate, Enrolled).
   <img width="1439" alt="Screenshot 2025-05-24 at 21 34 44" src="https://github.com/user-attachments/assets/b3016f66-c066-4aaa-8400-f2d9fcedd7e9" />

2. Karakteristik dan Kinerja Akademik yang menampilkan Average Admission Grade (Rata-rata nilai masuk), Average 1st and 2nd semester grade (Rata-rata nilai semester 1 dan 2), dan Average of Curricular units 1st and 2nd semester approved (Rata-rata sks semester 1 dan 2).
   <img width="1440" alt="Screenshot 2025-05-24 at 21 35 08" src="https://github.com/user-attachments/assets/5cda3b2e-bdcc-4711-ab9a-940482f2fbde" />

3. Analisis demografi yang menampilkan gender, status pernikahan, dan umur saat mendaftar.
   <img width="1440" alt="Screenshot 2025-05-24 at 21 32 40" src="https://github.com/user-attachments/assets/41f5776c-4727-4d2b-8a36-c69506526108" />
   <img width="1440" alt="Screenshot 2025-05-24 at 21 33 03" src="https://github.com/user-attachments/assets/74f63e97-07e3-4607-96ca-a79e584aadb7" />

4. Faktor sosial ekonomi yang meliputi Debtor (berhutang atau tidak), Scholarship holder (pemegang beasiswa atau tidak), dan Tuition fees up to date (Pembayaran kuliah terkini).
   <img width="1440" alt="Screenshot 2025-05-24 at 21 33 27" src="https://github.com/user-attachments/assets/7e604f7e-e4c9-448b-8171-9f8bad1f1cba" />

5. Faktor eksternal (makroekonomi) yang meliputi tingkat pengangguran dan rata - rata GDP.
    <img width="1440" alt="Screenshot 2025-05-24 at 21 33 47" src="https://github.com/user-attachments/assets/163d1ad3-0918-4705-8ee5-34b379f788a2" />

## Menjalankan Sistem Machine Learning
Sistem prediksi dibangun menggunakan Python dengan model klasifikasi terbaik (SVM) berdasarkan evaluasi akurasi dan f1-score. Input fitur dapat dimasukkan oleh pengguna melalui antarmuka web Streamlit. Fitur yang dimasukkan antara lain: 
- Application Mode
- Debtor: Ya/ Tidak
- Tuition Fees Up to Date: Ya/ Tidak
- Gender: Laki-laki/ perempuan
- Penerima Beasiswa: Ya/ Tidak
- Usia saat mendaftar
- Mata kuliah disetujui semester 1
- Nilai rata-rata semester 1
- Mata kuliah disetujui semester 2
- Nilai rata-rata semester 2

Untuk menjalankan aplikasi prediksi dapat mengunjungi **Link ini:** [Link Streamlit App](https://students-performance-jaya-jaya-institut-9huucrgcgyawvxfwq5wwgw.streamlit.app/)

Untuk menjalankan secara lokal
```
streamlit run app.py
```

## Conclusion
📊 Dashboard
Dari dashboard yang telah dibuat, terdapat beberapa poin penting yang dapat disimpulkan:
1. Total mahasiswa dropout adalah 32.1% dari total 4.224 mahasiswa.
2. Rata rata nilai pada semester 1 dan semester 2 menunjukkan bahwa mahasiswa dropout memiliki rata - rata paling rendah, yaitu 7.26 pada semester 1 dan 5.9 pada semester 2. Selain itu, rata - rata sks yang diberikan pada semester 1 dan semester 2 untuk mahasiswa dropout hanya 1-3 sks, sedangkan untuk mahasiswa terdaftar 4 sks dan mahasiswa lulus 6 sks.
3. Usia saat pendaftaran 26 tahun keatas didominasi oleh mahasiswa yang dropout.
4. Mahasiswa yang dropout 32.16% nya tidak membayar uang kuliah terkini.
5. Mahasiswa yang dropout memiliki rata-rata GDP -0.15.

🤖 Model ML
Berdasarkan eksperimen dengan tiga model (Random Forest, Logistic Regression, dan SVM), didapatkan bahwa model Support Vector Machine (SVM) memberikan performa terbaik dengan akurasi 86.33% dan f1-score tertinggi untuk kelas dropout. Sistem ini dapat mendeteksi mahasiswa berisiko tinggi dengan cukup baik dan dapat menjadi alat bantu intervensi dini.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

1. Pemantauan Mahasiswa Risiko Tinggi Berdasarkan Indikator KunciGunakan dashboard untuk secara aktif memantau mahasiswa dengan karakteristik yang sering muncul pada kelompok dropout, seperti:
   - Nilai rendah pada semester 1 dan 2
   - Tidak membayar uang kuliah tepat waktu
   - Tidak menerima beasiswa
   - Usia lebih tua saat pendaftaran
   Fokus pada mahasiswa dengan kombinasi faktor ini untuk prioritas bimbingan.

2. Peningkatan Layanan Akademik dan Keuangan untuk Mahasiswa Berisiko
   - Berikan dukungan akademik tambahan (seperti remedial, tutoring, atau pembimbingan belajar) bagi mahasiswa dengan performa akademik rendah.
   - Evaluasi dan permudah akses bantuan keuangan atau beasiswa bagi mahasiswa yang tidak mampu, karena keterlambatan pembayaran muncul sebagai indikator dropout.

3. Konseling Terarah Berdasarkan Output Prediksi
   Implementasikan sesi konseling terjadwal bagi mahasiswa yang diprediksi berisiko dropout oleh model. Petakan intervensi berdasarkan tingkat probabilitas dropout yang dihasilkan model untuk memastikan pendekatan yang sesuai.

4. Pembuatan Sistem Early Warning Otomatis
   Kembangkan modul notifikasi atau dashboard khusus untuk bagian kemahasiswaan yang secara otomatis menampilkan mahasiswa dengan skor risiko dropout tinggi setiap awal semester.

