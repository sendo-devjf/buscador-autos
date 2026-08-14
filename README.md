# Buscador de Autos México

Una aplicación web interactiva desarrollada con Streamlit para buscar autos en los principales sitios de venta de México.

## Características

- ���� �� �� 💰 Ingresa tu presupuesto máximo en pesos MXN
- ���� �� �� 🏷������️ Especifica marca o modelo preferido (opcional)
- ���� �� �� 📍 Define ciudad o estado de búsqueda
- ���� �� �� 🔗 Genera enlaces directos de búsqueda filtrados para:
  - Mercado Libre Autos
  - Kavak
  - SoloAutos
  - Facebook Marketplace
- ���� �� �� 🎨 Interfaz moderna y profesional con tema azul oscuro/gris
- ���� �� �� 📊 Tarjetas de resultado y tabla interactiva para organizar resultados
- ���� �� �� 📱 Diseño responsive que funciona en móviles y escritorio

## Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) - Framework para crear aplicaciones web con Python
- Python 3.7+

## Instalación local

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/buscador-autos.git
   cd buscador-autos
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

5. Abre tu navegador en: http://localhost:8501

## Despliegue en Streamlit Community Cloud (gratuito)

Sigue estos pasos para desplegar tu aplicación gratis en [Streamlit Community Cloud](https://streamlit.io/cloud):

### Paso 1: Prepara tu repositorio de GitHub

1. Asegúrate de que tu repositorio tenga al menos estos archivos:
   - `app.py` - La aplicación principal
   - `requirements.txt` - Dependencias de Python
   - `.gitignore` - Archivos a excluir (opcional pero recomendado)

2. Tu `requirements.txt` debe contener:
   ```
   streamlit>=1.28.0
   ```

### Paso 2: Crea el repositorio en GitHub

1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón "+" → "New repository"
3. Nombre del repositorio: `buscador-autos` (o el nombre que prefieras)
4. Elige si será público o privado
5. Haz clic en "Create repository"
6. Sigue las instrucciones para subir tu código existente:
   ```bash
   git remote add origin https://github.com/tu-usuario/buscador-autos.git
   git branch -M main
   git push -u origin main
   ```

### Paso 3: Despliega en Streamlit Community Cloud

1. Ve a [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Haz clic en "Sign in with GitHub" y autoriza el acceso
3. Haz clic en "New app"
4. Selecciona:
   - **Repository**: Tu repositorio `buscador-autos`
   - **Branch**: `main` (o la rama que usarás)
   - **Main file path**: `app.py`
5. Haz clic en "Deploy!"
6. Espera unos minutos mientras Streamlit instala las dependencias y despliega tu app
7. ¡Listo! Tu aplicación estará disponible en una URL como: `https://tu-usuario-buscador-autos.streamlit.app`

### Paso 4: Personaliza tu despliegue (opcional)

- **Nombre de la app**: En la sección de settings de tu app en Streamlit Cloud, puedes cambiar el nombre público
- **Variables de entorno**: Si necesitas agregar secretos (como API keys), ve a Settings → Secrets
- **Dominio personalizado**: En planes pagos puedes conectar tu propio dominio

## Estructura del repositorio

```
buscador-autos/
├── app.py              # Aplicación principal de Streamlit
├── requirements.txt    # Dependencias de Python
├── README.md           # Este archivo
���└── .gitignore          # (Opcional) Archivos a excluir del versionado
```

Ejemplo de `.gitignore` recomendado:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## Uso de la aplicación

1. Abre la aplicación en tu navegador
2. Ingresa tu presupuesto máximo en pesos MXN
3. (Opcional) Especifica una marca o modelo preferido (ej: "Toyota Corolla")
4. Ingresa la ciudad o estado donde deseas buscar (ej: "Ciudad de México")
5. Haz clic en "Buscar Autos"
6. La aplicación generará enlaces directos de búsqueda para cada sitio
7. Hazclic en los botones "Ver resultados en [Sitio]" para abrir cada búsqueda

## Personalización

Puedes modificar el archivo `app.py` para:

- Cambiar el tema de colores editando las variables CSS en la sección `<style>`
- Agregar más sitios de búsqueda modificando la función `generate_search_urls`
- Mejorar los estilos o añadir nuevas funcionalidades
- Cambiar el texto de ayuda o placeholder en los campos de entrada

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación:

1. Haz un Fork del repositorio
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Haz tus cambios y haz commit: `git commit -m 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE] para más detalles.

## Créditos

Creado con ���� �� �� ❤������️ usando [Streamlit](https://streamlit.io/)

---
*¿Tienes preguntas o necesitas ayuda? Abre un issue en el repositorio o contacta al mantenedor.*