import streamlit as st

# --- Konfiguracja Strony ---
st.set_page_config(
    page_title="Świąteczna Lista Magazynowa",
    layout="wide" # Używamy szerokiego układu, żeby kolumny miały miejsce
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

# 1. Tworzymy dwie kolumny: 60% szerokości dla aplikacji, 40% dla dekoracji
col_app, col_deco = st.columns([3, 2]) 

# =========================================================================
# === KOLUMNA LEWA: APLIKACJA MAGAZYNOWA (60%) =============================
# =========================================================================
with col_app:
    st.title("🎅 Lista Prezentów Mikołaja")
    st.markdown("Świąteczna edycja prostej listy magazynowej. Dane są tymczasowe.")

    # Sekcja Dodawania Produktu
    with st.container(border=True):
        st.subheader("🎁 Dodaj Prezent")
        
        product_to_add = st.text_input("Nazwa nowego produktu/prezentu", key="add_input")
        
        # Przycisk do dodawania
        st.button("Dodaj do Listy", on_click=add_product, args=(product_to_add,))

    st.markdown("---")

    # Sekcja Usuwania Produktu
    if st.session_state.inventory:
        with st.container(border=True):
            st.subheader("❌ Usuń Prezent")
            
            # Używamy selectbox do wyboru produktu do usunięcia
            product_to_remove = st.selectbox(
                "Wybierz prezent do usunięcia", 
                st.session_state.inventory,
                key="remove_select" # Dodanie klucza dla unikalności
            )
            
            # Przycisk do usuwania
            st.button("Usuń z Listy", on_click=remove_product, args=(product_to_remove,))
    else:
        st.info("Lista prezentów Mikołaja jest pusta.")

    st.markdown("---")

    # Sekcja Wyświetlania Magazynu
    st.subheader(f"📜 Aktualna Lista Prezentów ({len(st.session_state.inventory)})")

    if st.session_state.inventory:
        # Wyświetlenie listy produktów
        for i, item in enumerate(st.session_state.inventory, 1):
            st.markdown(f"**{i}.** {item}")
    else:
        st.info("Brak prezentów na liście. Dodaj pierwszy prezent powyżej.")

# =========================================================================
# === KOLUMNA PRAWA: DEKORACJE ŚWIĄTECZNE (40%) ============================
# =========================================================================
with col_deco:
    st.header(" ") # Pusty nagłówek dla wyrównania pionowego

    # 1. Święty Mikołaj
    st.markdown(
        """
        ### 🎅 Święty Mikołaj (Santa)
        
        Mikołaj sprawdza listę! 📝
        """,
        unsafe_allow_html=True
    )
    
    # Można tutaj użyć obrazu, jeśli masz go w pliku (np. 'santa.png'):
    # st.image("santa.png", caption="Kontrola Jakości Prezentów")
    
    # 2. Automaty do Gier (jako emotikony)
    st.markdown("---")
    st.markdown(
        """
        ### 🕹️ Automaty do Gier
        
        Prezenty z sekcji Gier i Rozrywki.
        """,
        unsafe_allow_html=True
    )
    
    # Symulacja Automatów (użycie emotikon i kolumn wewnątrz kolumny głównej)
    arcade_col1, arcade_col2, arcade_col3 = st.columns(3)
    
    with arcade_col1:
        st.metric(label="Pac-Man", value="👾", delta="Retro")
    with arcade_col2:
        st.metric(label="Tetris", value="🧱", delta="Logika")
    with arcade_col3:
        st.metric(label="Pinball", value="🔵", delta="Zręczność")
    
# --- Stopka ---
st.caption("Aplikacja działa w oparciu o pamięć sesji Streamlit.")
