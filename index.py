from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_secret_key'


@app.route('/')
@app.route('/index')
def start_page():
    return render_template('index.html', title='Заготовка')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')