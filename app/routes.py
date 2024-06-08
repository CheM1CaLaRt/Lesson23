from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route("/", methods=["GET", "POST"])
def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
    #функция request.form извлекает значение из соответствующих полей
        title = request.form.get('title')
        city = request.form.get('city')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        #создаёт условие для проверки наличия данных в полях title и content
        if title and city and age and hobby:
            posts.append({'title': title, 'city': city, 'age': age, 'hobby': hobby})
        #использует для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))
        #возвращает отрендеренный шаблон с переданными данными постов
    return render_template('blog.html', posts=posts)