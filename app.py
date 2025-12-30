import streamlit as st
import pandas as pd
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="DFA Sentinel Pro", page_icon="🛡️", layout="wide")

# --- 2. FUNGSI UNTUK MEMBACA CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Memanggil file CSS eksternal
try:
    local_css("style.css")
except FileNotFoundError:
    st.error("File style.css tidak ditemukan! Pastikan file berada di folder yang sama.")

# --- 3. LOGIKA DFA ---
TRANSITIONS = {
    'q0': {'char': 'q1', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'q1': {'char': 'q1', '@': 'q2', '.': 'reject', 'other': 'reject'},
    'q2': {'char': 'q3', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'q3': {'char': 'q3', '@': 'reject', '.': 'q4', 'other': 'reject'},
    'q4': {'char': 'q5', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'q5': {'char': 'q5', '@': 'reject', '.': 'reject', 'other': 'reject'},
}

def get_type(c):
    if c.isalnum() or c == '_': return 'char'
    if c == '@': return '@'
    if c == '.': return '.'
    return 'other'

# --- 4. TAMPILAN UTAMA ---
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>VERIFIKASI EMAIL</h1>", unsafe_allow_html=True)

email_input = st.text_input("📡 Scan Stream Email:", placeholder="user@gmail.com")

if email_input:
    current = 'q0'
    history = [('START', 'q0')]
    
    # Jalankan Logika DFA
    for char in email_input:
        type_ = get_type(char)
        current = TRANSITIONS.get(current, {}).get(type_, 'reject')
        history.append((char, current))
        if current == 'reject': break

    st.subheader("Visualisasi Transisi")
    
    # Visualizer Container
    display_area = st.empty()
    html_content = '<div class="animation-wrapper">'

    for i, (char, state) in enumerate(history):
        color = "#3b82f6" 
        if state in {'q5'}: color = "#10b981" 
        if state == 'reject': color = "#ef4444" 

        html_content += f'''
            <div class="node">
                <div class="circle-glow" style="background: {color};">{state}</div>
                <div style="margin-top: 8px; font-size: 12px; font-weight: bold; color: #94a3b8;">{char}</div>
            </div>
        '''
        
        if i < len(history) - 1:
            html_content += '<div class="arrow-icon">➜</div>'
        
        display_area.markdown(html_content + '</div>', unsafe_allow_html=True)
        time.sleep(0.05)

    # --- BAGIAN ANALISIS DINAMIS (BERHASIL / GAGAL) ---
    st.write("---")
    
    if current == 'q5':
        # KONDISI BERHASIL
        st.success("### ✅ VERIFIKASI BERHASIL")
        st.balloons()
        st.markdown(f"""
        **Analisis DFA:**
        * String **'{email_input}'** diterima sepenuhnya oleh mesin.
        * Jalur transisi berakhir di **Final State (q5)**.
        * **Kesimpulan:** Struktur email valid (Username, Symbol @, Domain, dan Ekstensi ditemukan).
        """)
    else:
        # KONDISI GAGAL
        st.error(f"### ❌ VERIFIKASI GAGAL")
        
        if current == 'reject':
            st.warning("**Analisis Kesalahan (Trap State):**")
            st.write("Mesin memasuki 'Reject State' karena menemukan karakter yang melanggar aturan transisi (seperti simbol ganda atau karakter ilegal).")
        else:
            st.info(f"**Analisis Kesalahan (Dead-end):**")
            st.write(f"Proses pembacaan selesai, namun mesin berhenti di state **{current}** yang bukan merupakan Final State.")
            
        st.markdown(f"""
        **Kenapa gagal?**
        * String **'{email_input}'** ditolak oleh mesin DFA.
        * Mesin gagal mencapai **Final State (q5)**.
        * **Saran:** Pastikan format email lengkap (contoh: nama@domain.com).
        """)

    # --- 5. TABEL RIWAYAT TRANSISI ---
    st.write("---")
    st.subheader("📋 Tabel Riwayat Transisi Detail")
    
    df_data = []
    for i, (char, next_state) in enumerate(history):
        if i == 0: continue 
        prev_state = history[i-1][1]
        df_data.append({
            "Langkah": i,
            "Karakter Input": f"'{char}'",
            "Dari State": prev_state,
            "Ke State": next_state,
            "Status": "✅ Terlalui" if next_state != 'reject' else "❌ Reject"
        })

    df = pd.DataFrame(df_data)
    st.dataframe(
        df,
        column_config={
            "Langkah": st.column_config.NumberColumn(width="small"),
            "Status": st.column_config.TextColumn(width="small"),
        },
        hide_index=True,
        use_container_width=True
    )

    # --- 6. INFORMASI TAMBAHAN ---
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Total Karakter:** {len(email_input)}")
    with col2:
        st.info(f"**State Akhir:** {current}")