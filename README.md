# Proyecto Final – Automation Testing (UI + API)

## 📌 Propósito del Proyecto
Este proyecto tiene como objetivo demostrar la implementación de pruebas automatizadas
de **UI y API** utilizando buenas prácticas de automation testing como:

- Page Object Model (POM)
- Parametrización de datos
- Separación de responsabilidades
- Reportes automáticos
- Logging y screenshots en fallos
- Integración con CI/CD (GitHub Actions)

---

## 🛠 Tecnologías Utilizadas

- Python 3.13
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Requests
- WebDriver Manager
- GitHub Actions (CI/CD)

---




## 📦 Instalación de Dependencias

1. Crear entorno virtual:
```bash
python -m venv .venv
Activar entorno virtual:

Windows:

bash
Copiar código
.venv\Scripts\activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
▶️ Ejecución de las Pruebas
Ejecutar todos los tests:
bash
Copiar código
pytest -v
Ejecutar con reporte HTML:
bash
Copiar código
pytest -v --html=reports/reporte.html --self-contained-html
📊 Reportes
El reporte HTML se genera en:

bash
Copiar código
reports/reporte.html
Incluye:

Tests ejecutados

Estado (PASSED / FAILED)

Duración

Evidencias (screenshots en fallos)

🔄 CI/CD – GitHub Actions
El proyecto cuenta con integración continua mediante GitHub Actions.

Cada push o pull request:

Ejecuta automáticamente todas las pruebas

Genera el reporte HTML

Guarda el reporte como artefacto descargable

Ruta del workflow:

bash
Copiar código
.github/workflows/ci.yml

🚀 Cómo ejecutar los tests

Abrir terminal en la raíz del proyecto:

cd D:\git-repositorio\proyecto-final-automation-testing-juan-ruiz


Ejecutar todos los tests de UI:

pytest test/ui/ -v --html=reports/reporte.html --self-contained-html


Ejecutar un test específico:

pytest test/ui/test_login.py -v --html=reports/reporte.html --self-contained-html


🛠️ Contacto

Juan Ruiz
Email: juane.ruiz97@gmail.com

LinkedIn: https://www.linkedin.com/in/juanruiz97/
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
Los test con pytest corren 12/12
Fallo la integracion CI y CD
Da errores de versiones con selenium,
webdriver en github/workflow actions

## 📂 Reportes
El reporte HTML se genera automáticamente en `reports/reporte.html`.  
En caso de error, se guarda una captura en `reports/`.
