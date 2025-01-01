"""
Calculadora de Boleta de Honorarios - Actualizada 2025
------------------------------------------------------
Este proyecto es una aplicación web desarrollada en Python usando Flask. 
Permite calcular los valores correspondientes a boletas de honorarios en Chile 
con base en las tasas de retención de los años 2023 al 2028.

Características:
- Permite calcular desde el valor líquido o bruto de la boleta.
- Muestra la retención, el monto líquido y el monto bruto.
- Incluye tasas de retención estándar y asociadas al Préstamo Solidario (Ley 21.323, Art. 12).

Componentes:
- Backend: Flask, encargado de manejar las solicitudes y cálculos.
- Frontend: HTML simple, dinámicamente renderizado con Jinja2.
- Tasas de retención configurables para actualizaciones futuras.

Requisitos:
- Python 3.8 o superior
- Flask (instalación con `pip install flask`)

Instrucciones:
1. Clona o descarga este repositorio.
2. Ejecuta `python app.py` para iniciar el servidor.
3. Accede a `http://127.0.0.1:5000/` desde tu navegador.

Desarrollado por:
Israel Ubeda
--------------------------------
¡Calcula fácilmente tus boletas de honorarios y cumple con tus obligaciones tributarias!

"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Tasas de retención
RETENCIONES = {
    "Retención 2023": 0.13,  # 2023
    "Préstamo Solidario 2023": 0.16,  # Préstamo Solidario 2023
    "Retención 2024": 0.1375,  # 2024
    "Préstamo Solidario 2024": 0.1675,  # Préstamo Solidario 2024
    "Retención 2025": 0.145,  # 2025
    "Préstamo Solidario 2025": 0.175,  # Préstamo Solidario 2025
    "Retención 2026": 0.1525,  # 2026
    "Préstamo Solidario 2026": 0.1825,  # Préstamo Solidario 2026
    "Retención 2027": 0.16,  # 2027
    "Préstamo Solidario 2027": 0.19,  # Préstamo Solidario 2027
    "Retención 2028": 0.17,  # 2028
    "Préstamo Solidario 2028": 0.20,  # Préstamo Solidario 2028
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        try:
            calculation_type = request.form.get('calculation_type')
            retention_label = request.form.get('retention')
            rate = RETENCIONES.get(retention_label, 0)

            # Obtener el monto ingresado
            amount = float(request.form.get('amount'))

            # Cálculos según el tipo de boleta
            if calculation_type == 'liquid':
                # Cálculo a partir del valor líquido
                gross_amount = round(amount / (1 - rate))
                retention_amount = round(gross_amount - amount)
                liquid_amount = round(amount)
            elif calculation_type == 'gross':
                # Cálculo a partir del valor bruto
                gross_amount = round(amount)
                retention_amount = round(gross_amount * rate)
                liquid_amount = round(gross_amount - retention_amount)
            else:
                raise ValueError("Tipo de cálculo no válido")

            # Resultado
            result = {
                'liquid_amount': liquid_amount,
                'retention_amount': round(retention_amount, 2),
                'gross_amount': gross_amount,
                'rate': round(rate * 100, 2),
                'retention_label': retention_label
            }
        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result, retentions=RETENCIONES)

if __name__ == '__main__':
    app.run(debug=True)
