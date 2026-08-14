import streamlit as st

st.set_page_config(page_title="Buscador de Autos México", layout="wide")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #1E3A8A; text-align: center; font-weight: bold; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.1rem; color: #4B5563; text-align: center; margin-bottom: 2rem; }
    .stButton>button { width: 100%; background-color: #2563EB; color: white; font-weight: bold; border-radius: 8px; height: 3em; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Buscador de Autos México</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Encuentra tu auto ideal en los principales sitios de venta de México</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    presupuesto = st.number_input("Presupuesto máximo (MXN)", value=300000, step=10000)

with col2:
    modelo = st.text_input("Marca o modelo (opcional)", placeholder="Ej: Toyota Corolla, Honda Civic")

with col3:
    ubicacion = st.text_input("Ciudad o estado", placeholder="Ej: Ciudad de México, Monterrey")

if st.button("Buscar Autos"):
    st.info("Iniciando búsqueda...")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF;'>Creado con Streamlit • Búsqueda de autos en México</div>", unsafe_allow_html=True)
