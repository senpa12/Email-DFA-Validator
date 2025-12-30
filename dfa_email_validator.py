# =======================================================
# Proyek UAS Teori Graf & Automata: Validasi Email Sederhana
# File: dfa_email_validator.py
# =======================================================

# BAGIAN 1: DEFINISI STRUKTUR DFA (Q, q0, F, Delta)

FINAL_STATES = {'q5'}

# Fungsi Transisi (Delta)
TRANSITIONS = {
    # State q0 hingga q5 dan state 'reject'
    'q0': {'char': 'q1', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'q1': {'char': 'q1', '@': 'q2', '.': 'reject', 'other': 'reject'},
    'q2': {'char': 'q3', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'q3': {'char': 'q3', '@': 'reject', '.': 'q4', 'other': 'reject'},
    'q4': {'char': 'q5', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'q5': {'char': 'q5', '@': 'reject', '.': 'reject', 'other': 'reject'},
    'reject': {'char': 'reject', '@': 'reject', '.': 'reject', 'other': 'reject'}
}

# BAGIAN 2: FUNGSI KLASIFIKASI INPUT

def get_char_type(char):
    """Mengklasifikasikan karakter input untuk DFA."""
    if 'a' <= char.lower() <= 'z' or '0' <= char <= '9':
        return 'char'
    elif char == '@':
        return '@'
    elif char == '.':
        return '.'
    else:
        return 'other'

# BAGIAN 3: FUNGSI UTAMA SIMULASI DFA

def validate_email_dfa(email_string):
    """
    Simulasi logika DFA untuk memvalidasi format email sederhana.
    """
    current_state = 'q0'

    # Menampilkan tracing pergerakan state
    print(f"\n--- Tracing: {email_string} ---")
    
    for char in email_string:
        input_type = get_char_type(char)
        
        if current_state in TRANSITIONS and input_type in TRANSITIONS[current_state]:
            next_state = TRANSITIONS[current_state][input_type]
            print(f"[{current_state}] --({char}/{input_type})--> [{next_state}]")
            current_state = next_state
        else:
            current_state = 'reject'
            print(f"[{current_state}] --({char}/{input_type})--> [reject] (Transisi tidak valid)")
            break
            
        if current_state == 'reject':
            break

    # Keputusan Akhir
    print(f"\nState Akhir: {current_state}")
    if current_state in FINAL_STATES:
        print(f"HASIL: '{email_string}' DITERIMA.")
        return True
    else:
        print(f"HASIL: '{email_string}' DITOLAK. (Tidak berakhir di Final State)")
        return False

# BAGIAN 4: PENGUJIAN (Main Execution Block)

if __name__ == "__main__":
    # Daftar email yang akan diuji
    test_emails = [
        "valid123@mail.com",
        "user_dua@domain.net",
        "@awal.salah.com",
        "emailtanpatitik@domain",
        "email#@domain.com",
        "titik@awal.salah",
        "user@mail..com"
    ]

    print("=== PROYEK VALIDASI EMAIL DFA ===")
    
    for email in test_emails:
        validate_email_dfa(email)