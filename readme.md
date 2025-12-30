# 🛡️ DFA Sentinel Pro - Email DFA Analyzer

**DFA Sentinel Pro** adalah aplikasi simulator berbasis web yang mengimplementasikan teori **Deterministic Finite Automata (DFA)** untuk melakukan validasi format alamat email. Proyek ini dibangun menggunakan Python dan Streamlit sebagai bagian dari tugas besar/UAS mata kuliah Teori Bahasa dan Automata.

## 🚀 Fitur Utama
* **Visualisasi Transisi State**: Menampilkan perpindahan *state* (q0 hingga q5) secara interaktif dengan animasi.
* **Analisis Teknis Mendalam**: Memberikan penjelasan logis mengapa sebuah email diterima atau ditolak (berhenti di *non-final state* atau masuk ke *trap state*).
* **Tabel Riwayat (Log)**: Mencatat setiap langkah transisi karakter demi karakter untuk kebutuhan audit logika.
* **Uji Akurasi Otomatis**: Fitur untuk menguji performa mesin DFA terhadap dataset email valid dan invalid.
* **Antarmuka Profesional**: Desain bersih tanpa animasi berlebihan, cocok untuk presentasi akademis.

## ⚙️ Persyaratan Sistem
Pastikan Anda telah menginstal Python di komputer Anda. Library yang dibutuhkan:
* `streamlit`
* `pandas`

## 📥 Instalasi
1. Clone atau download repositori ini.
2. Masuk ke direktori proyek:
   ```powershell
   cd D:\ProyekUAS_DFA_Email\ProyekUAS_DFA_Email

## Instal Dependensi
pip install streamlit pandas

## Jalankan Perintah berikut di terminal/PowerShell Anda:
python -m streamlit run app.py

## Struktur Proyek
ProyekUAS_DFA_Email/
├── app.py              
├── dfa_email_validator.py              
├── style.css          
└── README.md
           