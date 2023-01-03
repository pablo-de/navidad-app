from flask import Flask, render_template, request, flash
import datetime

app = Flask(__name__)
app.secret_key = "JY&7HtLmVTugs#iW4ZRzfqh4"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    # Si el método de la solicitud es POST, procesar el formulario
    if request.method == "POST":
        # Obtener el día de la semana seleccionado del formulario
        dia_semana = request.form['dia_semana']
        
        dia_semana = dia_semana.lower()

        # Convertir el día de la semana a un número (lunes es 0, martes es 1, etc.)
        dias_semana = {
            "lunes": 0,
            "martes": 1,
            "miercoles": 2,
            "miércoles": 2,
            "jueves": 3,
            "viernes": 4,
            "sabado": 5,
            "sábado": 5,
            "domingo": 6
        }

        # Si el día de la semana es inválido, mostrar un mensaje de error
        if dia_semana not in dias_semana:
            flash(f'El día de la semana ingresado es inválido. Por favor ingrese un día válido.', category='warning')
        else:
            # Obtener el número del día de la semana seleccionado
            dia_semana_num = dias_semana[dia_semana]

            # Obtener la fecha actual
            hoy = datetime.date.today()

            # Calcular la fecha de Navidad del año actual
            navidad = hoy.replace(month=12, day=24)
            prox_navidad = hoy.replace(month=12, day=24)

            # Si el día de la semana de Navidad es diferente del día de la semana seleccionado, aún no ha pasado este año
            while navidad.weekday() != dia_semana_num:
                # Calcular la fecha de Navidad del año anterior
                navidad = navidad.replace(year=navidad.year - 1)

            while prox_navidad.weekday() != dia_semana_num:
                prox_navidad = prox_navidad.replace(year=prox_navidad.year + 1)

            return render_template('index.html', navidad=navidad.year, prox_navidad=prox_navidad.year, dia_semana=dia_semana)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
