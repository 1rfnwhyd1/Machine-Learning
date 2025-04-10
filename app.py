import streamlit as st
import pickle
import numpy as np

# Judul Aplikasi
st.title('Aplikasi Prediksi Spesies Ikan SVM by IrfnwhydI_')

# Dropdown untuk memilih model
model_choice = st.selectbox(
    'Pilih Model untuk Prediksi:',
    ('SVM')  # Menyediakan pilihan model sesuai kebutuhan, Anda bisa menambahkan model lain di sini
)

# Memuat semua model
try:
    with open('model_svm_ikan.pkl', 'rb') as f:
        model_SVM = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Input untuk setiap fitur ikan
length = st.number_input('Panjang Ikan (length):', min_value=0.0)
weight = st.number_input('Berat Ikan (weight):', min_value=0.0)
w_l_ratio = st.number_input('Rasio Berat ke Panjang (w_l_ratio):', min_value=0.0)

# Tombol untuk memprediksi spesies ikan
if st.button('Prediksi Spesies'):
    features = np.array([[length, weight, w_l_ratio]])
    
    # Memilih model berdasarkan pilihan pengguna
    if model_choice == 'SVM':
        model = model_SVM
    
    
    prediction = model.predict(features)[0]
    st.success(f'Spesies yang Diprediksi: {prediction}')
