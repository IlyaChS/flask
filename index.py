from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_secret_key'


@app.route('/')
@app.route('/index')
def start_page():
    return render_template('index.html', title='Заготовка')


@app.route('/training/<prof>')
def trainings(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<t>')
def list_prof(t):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('professions.html', t=t, profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')