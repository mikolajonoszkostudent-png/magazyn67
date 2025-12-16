import streamlit as st

# --- Konfiguracja Strony ---
st.set_page_config(
    page_title="Prosta Aplikacja Magazynowa",
    layout="centered"
)

# --- Inicjalizacja Stanu Sesji ---
# Inicjalizuje listę 'inventory' (magazyn), jeśli jeszcze nie istnieje w bieżącej sesji.
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

# --- Funkcje Logiki Magazynowej ---

def add_product(product_name):
    """Dodaje produkt do magazynu."""
    # Upewnia się, że nazwa produktu nie jest pusta i dodaje ją.
    if product_name and product_name not in st.session_state.inventory:
        st.session_state.inventory.append(product_name)
        st.success(f"Dodano produkt: **{product_name}**")
    elif product_name in st.session_state.inventory:
        st.warning(f"Produkt **{product_name}** już jest w magazynie!")
    else:
        st.error("Wprowadź nazwę produktu.")

def remove_product(product_name):
    """Usuwa produkt z magazynu."""
    # Usuwa produkt z listy, jeśli istnieje.
    try:
        st.session_state.inventory.remove(product_name)
        st.success(f"Usunięto produkt: **{product_name}**")
    except ValueError:
        st.error(f"Produkt **{product_name}** nie został znaleziony w magazynie.")

# --- Interfejs Użytkownika Streamlit ---

st.title("🛒 Prosta Lista Magazynowa")
st.markdown("Dodawaj i usuwaj nazwy produktów. Dane nie są zapisywane.")

# Sekcja Dodawania Produktu
with st.container(border=True):
    st.subheader("➕ Dodaj Produkt")
    
    # Pole do wprowadzania nazwy produktu
    product_to_add = st.text_input("Nazwa nowego produktu", key="add_input")
    
    # Przycisk do dodawania, który wywołuje funkcję add_product
    # Używamy _product_to_add.strip() aby usunąć białe znaki i przekazać wartość
    st.button("Dodaj do Magazynu", on_click=add_product, args=(product_to_add.strip(),))

st.markdown("---")

# Sekcja Usuwania Produktu
if st.session_state.inventory:
    with st.container(border=True):
        st.subheader("➖ Usuń Produkt")
        
        # Używamy selectbox do wyboru produktu do usunięcia
        product_to_remove = st.selectbox(
            "Wybierz produkt do usunięcia", 
            st.session_state.inventory
        )
        
        # Przycisk do usuwania, który wywołuje funkcję remove_product
        st.button("Usuń z Magazynu", on_click=remove_product, args=(product_to_remove,))
else:
    st.info("Magazyn jest pusty.")

st.markdown("---")

# Sekcja Wyświetlania Magazynu
st.subheader(f"🗃️ Aktualny Magazyn ({len(st.session_state.inventory)})")

if st.session_state.inventory:
    # Wyświetlenie listy produktów jako lista punktowana
    for i, item in enumerate(st.session_state.inventory, 1):
        st.markdown(f"**{i}.** {item}")
else:
    st.info("Brak produktów w magazynie. Dodaj pierwszy produkt powyżej.")

# Stopka
st.caption("Aplikacja działa w oparciu o pamięć sesji Streamlit.")
