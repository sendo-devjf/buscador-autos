import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Buscador de Autos México", page_icon="🚗", layout="wide")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #1E3A8A; text-align: center; font-weight: bold; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.1rem; color: #4B5563; text-align: center; margin-bottom: 2rem; }
    .stButton>button { width: 100%; background-color: #2563EB; color: white; font-weight: bold; border-radius: 8px; height: 3em; }
</style>
""", unsafe_allow_html=True)

# --- Lógica de Scraping ---
def buscar_en_mercadolibre(modelo, presupuesto, ubicacion):
    # Formatear la búsqueda para la URL
    query = modelo.lower().replace(" ", "-") if modelo else "autos"
    if ubicacion:
        query += f"-{ubicacion.lower().replace(' ', '-')}"
        
    url = f"https://listado.mercadolibre.com.mx/vehiculos/{query}"
    
    # Simular ser un navegador real para que no nos bloqueen
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    resultados = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Encontrar todas las tarjetas de productos
            items = soup.find_all("li", class_="ui-search-layout__item")
            
            for item in items[:20]:  # Analizar los primeros 20 resultados
                try:
                    titulo = item.find("h2").text
                    precio_str = item.find("span", class_="andes-money-amount__fraction").text.replace(",", "")
                    precio = int(precio_str)
                    link_tag = item.find("a")
                    link = link_tag["href"] if link_tag else url
                    
                    # Filtrar estrictamente por presupuesto
                    if precio <= presupuesto:
                        resultados.append({
                            "Auto": titulo,
                            "Precio": precio,
                            "Sitio": "MercadoLibre",
                            "Link": link
                        })
                except Exception:
                    continue # Si falla un auto, pasa al siguiente
    except Exception as e:
        st.error(f"Error de conexión: {e}")
        
    return resultados

# --- Interfaz Gráfica ---
st.markdown('<div class="main-header">🚗 Buscador de Autos México</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Encuentra tu auto ideal en los principales sitios de venta de México</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    presupuesto = st.number_input("💵 Presupuesto máximo (MXN)", value=300000, step=10000)

with col2:
    modelo = st.text_input("🚘 Marca o modelo (opcional)", placeholder="Ej: Toyota Corolla")

with col3:
    ubicacion = st.text_input("📍 Ciudad o estado (opcional)", placeholder="Ej: Jalisco")

if st.button("🔎 Buscar Autos"):
    if not modelo and not ubicacion:
        st.warning("Por favor, ingresa al menos una marca/modelo o una ubicación para mejorar la búsqueda.")
    else:
        with st.spinner("Buscando en tiempo real en MercadoLibre México... 🕵️‍♂️"):
            datos_reales = buscar_en_mercadolibre(modelo, presupuesto, ubicacion)
            
            if datos_reales:
                st.success(f"¡Encontramos {len(datos_reales)} autos dentro de tu presupuesto!")
                df = pd.DataFrame(datos_reales)
                
                # Formatear el precio para que se vea bonito ($ XXX,XXX.00 MXN)
                df_mostrar = df.copy()
                df_mostrar["Precio"] = df_mostrar["Precio"].apply(lambda x: f"${x:,.2f} MXN")
                
                # Mostrar la tabla permitiendo hacer clic en los enlaces
                st.data_editor(
                    df_mostrar,
                    column_config={
                        "Link": st.column_config.LinkColumn("Ver publicación")
                    },
                    hide_index=True,
                    use_container_width=True
                )
            else:
                st.warning("No se encontraron autos con esos criterios o superan tu presupuesto.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #9CA3AF;'>Creado con Streamlit • Scraping en tiempo real</div>", unsafe_allow_html=True)
