import streamlit as st

# --- Konfiguracja Strony ---
st.set_page_config(
    page_title="Lista Magazynowa (Mikołaj)",
    layout="wide" # Używamy szerokiego układu
)

# --- Inicjalizacja Stanu Sesji ---
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

# --- Funkcje Logiki Magazynowej ---

def add_product(product_name):
    """Dodaje produkt do magazynu."""
    product_name = product_name.strip()
    if product_name and product_name not in st.session_state.inventory:
        st.session_state.inventory.append(product_name)
        st.success(f"Dodano produkt: **{product_name}**")
    elif product_name in st.session_state.inventory:
        st.warning(f"Produkt **{product_name}** już jest w magazynie!")
    else:
        st.error("Wprowadź nazwę produktu.")

def remove_product(product_name):
    """Usuwa produkt z magazynu."""
    try:
        st.session_state.inventory.remove(product_name)
        st.success(f"Usunięto produkt: **{product_name}**")
    except ValueError:
        st.error(f"Produkt **{product_name}** nie został znaleziony w magazynie.")


# --- INTERFEJS UŻYTKOWNIKA Z KOLUMNAMI ---

# 1. Tworzymy dwie kolumny: Lewa (70%) dla aplikacji, Prawa (30%) dla Mikołaja
col_app, col_deco = st.columns([7, 3]) 

# =========================================================================
# === KOLUMNA LEWA: APLIKACJA MAGAZYNOWA (70%) =============================
# =========================================================================
with col_app:
    st.title("🎁 Prosta Lista Magazynowa")
    st.markdown("Dodawaj i usuwaj nazwy produktów. Dane są tymczasowe.")

    # Sekcja Dodawania Produktu
    with st.container(border=True):
        st.subheader("➕ Dodaj Produkt")
        
        product_to_add = st.text_input("Nazwa nowego produktu", key="add_input")
        
        # Przycisk do dodawania
        st.button("Dodaj do Magazynu", on_click=add_product, args=(product_to_add,))

    st.markdown("---")

    # Sekcja Usuwania Produktu
    if st.session_state.inventory:
        with st.container(border=True):
            st.subheader("➖ Usuń Produkt")
            
            # Używamy selectbox do wyboru produktu do usunięcia
            product_to_remove = st.selectbox(
                "Wybierz produkt do usunięcia", 
                st.session_state.inventory,
                key="remove_select" 
            )
            
            # Przycisk do usuwania
            st.button("Usuń z Magazynu", on_click=remove_product, args=(product_to_remove,))
    else:
        st.info("Magazyn jest pusty.")

    st.markdown("---")

    # Sekcja Wyświetlania Magazynu
    st.subheader(f"🗃️ Aktualny Magazyn ({len(st.session_state.inventory)})")

    if st.session_state.inventory:
        for i, item in enumerate(st.session_state.inventory, 1):
            st.markdown(f"**{i}.** {item}")
    else:
        st.info("Brak produktów w magazynie. Dodaj pierwszy produkt powyżej.")

# =========================================================================
# === KOLUMNA PRAWA: ŚWIĘTY MIKOŁAJ (30%) ==================================
# =========================================================================
with col_deco:
    st.header(" ") # Pusty nagłówek dla wyrównania

    # Symulacja Mikołaja z liczbą 67 na brzuchu
    st.markdown(
        """
        <style>
        .santa-box {
            background-color: #F0F2F6; /* Lekkie tło */
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .santa-icon {
            font-size: 80px;
            margin-bottom: -15px;
        }
        .santa-number {
            font-size: 72px;
            font-weight: bold;
            color: white; /* Kolor liczby na "brzuchu" */
            background-color: red; /* "Pas/Brzuch" Mikołaja */
            padding: 10px 20px;
            border-radius: 15px;
            display: inline-block;
            border: 5px solid white;
        }
        </style>
        
        <div class="santa-box">
            <span class="santa-icon">🎅</span>
            <h3>Mikołaj Patroluje!</h3>
            <span class="santa-number">67</span>
            <p style='margin-top: 10px;'>Numer identyfikacyjny</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Stopka ---
st.caption("Aplikacja działa w oparciu o pamięć sesji Streamlit. Użyto HTML/CSS dla stylizacji Mikołaja.")
