import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador de Autos México", page_icon="🚗", layout="wide")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #1E3A8A; text-align: center; font-weight: bold; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.1rem; color: #4B5563; text-align: center; margin-bottom: 2rem; }
    .stButton>button { width: 100%; background-color: #2563EB; color: white; font-weight: bold; border-radius: 8px; height: 3em; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🚗 Buscador de Autos México</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Encuentra tu auto ideal en los principales sitios de venta de México</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    presupuesto = st.number_input("💵 Presupuesto máximo (MXN)", value=300000, step=10000)

with col2:
    modelo = st.text_input("🚘 Marca o modelo (opcional)", placeholder="Ej: Toyota, Honda, Nissan")

with col3:
    ubicacion = st.text_input("📍 Ciudad o estado", placeholder="Ej: Ciudad de México, Monterrey")

if st.button("🔎 Buscar Autos"):
    st.success(f"Mostrando resultados para presupuesto hasta ${presupuesto:,.2f} MXN")
    
    # Base de datos simulada / borrador de scraping
    datos = [
        {"Auto": "Nissan Versa 2020", "Precio": 210000, "Ubicación": "Ciudad de México", "Sitio": "Kavak", "Link": "https://www.kavak.com/mx"},
        {"Auto": "Toyota Corolla 2019", "Precio": 285000, "Ubicación": "Monterrey", "Sitio": "MercadoLibre", "Link": "https://www.mercadolibre.com.mx"},
        {"Auto": "Honda Civic 2018", "Precio": 295000, "Ubicación": "Guadalajara", "Sitio": "AutosMéxico", "Link": "https://www.autosmexico.mx"},
        {"Auto": "Volkswagen Jetta 2021", "Precio": 320000, "Ubicación": "Ciudad de México", "Sitio": "Kavak", "Link": "https://www.kavak.com/mx"},
        {"Auto": "Mazda 3 2020", "Precio": 270000, "Ubicación": "Querétaro", "Sitio": "MercadoLibre", "Link": "https://www.mercadolibre.com.mx"},
    ]
    
    df = pd.DataFrame(datos)
    
    # Filtrar por presupuesto
    df_filtrado = df[df["Precio"] <= presupuesto]
    
    # Filtrar por modelo si escribió algo
    if modelo:
        df_filtrado = df_filtrado[df_filtrado["Auto"].str.contains(modelo, case=False)]
        
    if not df_filtrado.empty:
        # Formatear precio
        df_mostrar = df_filtrado.copy()
        df_mostrar["Precio"] = df_mostrar["Precio"].apply(lambda x: f"${x:,.2f} MXN")
        st.dataframe(df_mostrar, use_container_width=True)
    else:
        st.warning("No se encontraron autos con esos criterios de búsqueda.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF;'>Creado con Streamlit • Búsqueda de autos en México</div>", unsafe_allow_html=True)
