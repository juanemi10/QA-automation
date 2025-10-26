# Pre-Entrega: Automation Testing - Juan Ruiz

## 🧠 Propósito
Automatizar los flujos principales de **SauceDemo**:
- Login
- Navegación del catálogo
- Interacción con productos (carrito)

## 🛠️ Tecnologías
- Python 
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Git / GitHub

## 📦 Instalación
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución de pruebas
```bash
pytest -v --html=reports/reporte.html
```

## 📋 Casos de prueba implementados
1. **Login:** Verifica acceso con credenciales válidas.  
2. **Inventario:** Verifica título, productos visibles y presencia de interfaz.  
3. **Carrito:** Añade producto, valida contador y producto en carrito.  

## 📂 Reportes
El reporte HTML se genera automáticamente en `reports/reporte.html`.  
En caso de error, se guarda una captura en `reports/`.
