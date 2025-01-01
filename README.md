# Calculadora de Boleta de Honorarios 2025 🧾

¡Bienvenido! Este es un proyecto desarrollado en **Python** utilizando **Flask** para calcular la retención de la Boleta de Honorarios en Chile, basado en las tasas actualizadas de los años 2023 a 2028.

## 🎯 Funcionalidades

- Calcula el **monto líquido**, **retención** y **monto bruto** a partir del valor ingresado.
- Incluye las tasas estándar y las asociadas al **Préstamo Solidario (Ley 21.323, Art. 12)**.
- Muestra el porcentaje de retención aplicado y el tipo de retención seleccionado.
- Interfaz moderna, profesional y **responsiva** gracias a **Bootstrap**.

---

## 📸 Vista Previa

### Formulario Principal
![Formulario Principal](https://via.placeholder.com/800x400.png?text=Formulario+Principal)

### Resultados
![Resultados](https://via.placeholder.com/800x400.png?text=Resultados)

---

## 🚀 Tecnologías Utilizadas

- **Python 3.8+**
- **Flask** (Framework web)
- **Bootstrap 5** (Estilo y diseño responsivo)

---

## 📂 Estructura del Proyecto

```plaintext
.
├── app.py                 # Archivo principal de la aplicación Flask
├── templates/
│   └── index.html         # Plantilla HTML con el diseño del formulario y resultados
├── static/                # (Opcional) Archivos CSS o JS adicionales
└── README.md              # Este archivo

🛠️ Instalación y Configuración
1. Requisitos Previos

    Python 3.8 o superior
    Gestor de paquetes pip

2. Clonar el Repositorio

git clone https://github.com/israelubeda/calculadora-honorarios.git
cd calculadora-honorarios

3. Instalar Dependencias

pip install flask

4. Ejecutar la Aplicación

python app.py

5. Abrir en el Navegador

Accede a la aplicación en: http://127.0.0.1:5000/
🎨 Personalización
Cambiar las Tasas de Retención

Las tasas de retención están definidas en el archivo app.py. Puedes actualizarlas en el diccionario RETENCIONES:

RETENCIONES = {
    "Retención 2023": 0.13,
    "Préstamo Solidario 2023": 0.16,
    ...
}

Diseño

El diseño utiliza Bootstrap 5, y puedes modificar el archivo templates/index.html para cambiar los estilos o agregar nuevas secciones.
🖼️ Ejemplo de Uso
Paso 1: Selecciona el tipo de cálculo

Elige si tienes el valor Líquido o el Bruto.
Paso 2: Selecciona la retención

Escoge la tasa de retención correspondiente al año y tipo de boleta.
Paso 3: Ingresa el monto

Introduce el valor (líquido o bruto) según el tipo de cálculo seleccionado.
Paso 4: Presiona "Calcular"

Se mostrarán los resultados con los valores calculados y detalles adicionales.
🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

    Haz un fork del repositorio.
    Crea una rama con tu funcionalidad: git checkout -b mi-nueva-funcionalidad.
    Realiza los cambios y haz un commit: git commit -m 'Añadí nueva funcionalidad'.
    Sube los cambios: git push origin mi-nueva-funcionalidad.
    Crea un pull request.

📝 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente, siempre dando el crédito correspondiente. 🧑‍💻
✨ Autor

Desarrollado por Israel Ubeda
📧 Contacto: israel.ubedabravo@gmail.com

¡Gracias por usar esta calculadora! 🎉