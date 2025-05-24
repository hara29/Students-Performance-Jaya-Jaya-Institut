import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load model dan scaler
model = joblib.load('dropout_model.pkl')
scaler = joblib.load('scaler.pkl')
selected_columns = joblib.load('selected_columns.pkl')

st.title("Prediksi Dropout Mahasiswa")

# Input fitur
application_mode_dict = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
}

application_mode_label = st.selectbox("Application Mode", list(application_mode_dict.values()))
application_mode_value = [k for k, v in application_mode_dict.items() if v == application_mode_label][0]
debtor = st.radio("Debtor", ["Ya", "Tidak"])
tuition_paid = st.radio("Tuition Fees Up to Date", ["Ya", "Tidak"])
gender = st.radio("Gender", ["Laki-laki", "Perempuan"])
scholarship = st.radio("Penerima Beasiswa", ["Ya", "Tidak"])
age = st.number_input("Usia saat mendaftar", min_value=16, max_value=80)
cu1_approved = st.number_input("Mata kuliah disetujui semester 1", min_value=0)
cu1_grade = st.slider("Nilai rata-rata semester 1", min_value=0.0, max_value=20.0)
cu2_approved = st.number_input("Mata kuliah disetujui semester 2", min_value=0)
cu2_grade = st.slider("Nilai rata-rata semester 2", min_value=0.0, max_value=20.0)

# Konversi ke format numerik
input_dict = {
    'Application mode': application_mode_value,
    'Debtor': 1 if debtor == "Ya" else 0,
    'Tuition fees up to date': 1 if tuition_paid == "Ya" else 0,
    'Gender': 1 if gender == "Laki-laki" else 0,
    'Scholarship holder': 1 if scholarship == "Ya" else 0,
    'Age at enrollment': age,
    'Curricular units 1st sem (approved)': cu1_approved,
    'Curricular units 1st sem (grade)': cu1_grade,
    'Curricular units 2nd sem (approved)': cu2_approved,
    'Curricular units 2nd sem (grade)': cu2_grade,
}

# Buat DataFrame
input_df = pd.DataFrame([input_dict])

# Urutkan kolom sesuai model
input_df = input_df[selected_columns]

# Scaler
input_scaled = scaler.transform(input_df)

# Prediksi
pred = model.predict(input_scaled)

# Prediksi probabilitas (Dropout = 0)
pred_proba = model.predict_proba(input_scaled)[0]
dropout_proba = pred_proba[0]  

# Tampilkan berdasarkan probabilitas > 50%
if dropout_proba > 0.5:
    st.error("⚠️ Mahasiswa ini berpotensi *Dropout*")
else:
    st.success("✅ Mahasiswa ini *Tidak Dropout*")

# Pie Chart Probabilitas Dropout vs Tidak Dropout
labels = ['Dropout','Tidak Dropout']
fig, ax = plt.subplots()
explode = (0, 0.1)  
colors = ['#ef5350', '#66bb6a'] 
ax.pie(pred_proba, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
ax.axis('equal') 
ax.set_title("Hasil Probabilitas Dropout")
st.pyplot(fig)
