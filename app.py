import streamlit as st
import pickle
import numpy as np

# Judul Aplikasi
st.title('Aplikasi Prediksi Spesies Ikan SVM by IrfnwhydI_')

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
    
    
    prediction = model.predict(features)[0]
    st.success(f'Spesies yang Diprediksi: {prediction}')
