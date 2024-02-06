from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mis_name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promote():
    return '<br>Человечество вырастает из детства.</br>' \
           '<br>Человечеству мала одна планета.</br>' \
           '<br>Мы сделаем обитаемыми безжизненные пока планеты.</br>' \
           '<br>И начнем с Марса!</br>' \
           '<br>Присоединяйся!</br>'


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        <br>Вот она какая, красная планета.</br>
                      </body>
                    </html>'''


@app.route('/promotion_image')
def promo_image():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Привет, Марс!</title>
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                            <div class="alert alert-secondary" role="alert">
                            Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-light" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                            </div>
                            <div class="alert alert-danger" role="alert">
                            Присоединяйся!
                            </div>
                          </body>
                        </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее-профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <br>Каике у вас есть профессии?</br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option1", name="profession[]", value="Инженер-исследователь">
                                        <label class="form-check-label" for="prof_option1">Инженер-исследователь</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option2", name="profession[]", value="Пилот">
                                        <label class="form-check-label" for="prof_option2">Пилот</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option3", name="profession[]", value="Строитель">
                                        <label class="form-check-label" for="prof_option3">Строитель</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option4", name="profession[]", value="Экзобиолог">
                                        <label class="form-check-label" for="prof_option4">Экзобиолог</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option5", name="profession[]", value="Врач">
                                        <label class="form-check-label" for="prof_option5">Врач</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option6", name="profession[]", value="Климатолог">
                                        <label class="form-check-label" for="prof_option6">Климатолог</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option7", name="profession[]", value="Метеоролог">
                                        <label class="form-check-label" for="prof_option7">Метеоролог</label>
                                    </div> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof_option8", name="profession[]", value="Оператор марсохода">
                                        <label class="form-check-label" for="prof_option8">Оператор марсохода</label>
                                    </div> 
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">Мужской</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="5" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form.getlist('profession[]'))
        print(request.form['sex'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

