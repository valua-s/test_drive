<h1>Приложение по тестовому задaнию от компании KODE<br>JUST DO IT!</h1>

Данное проложение было разработано с целью выполнения тестового задания и для помощи доктору Айболиту, очень меня заинтересовало и будет развиваться в ближайщем будущем.

Для локального запуска необходимо:<br>
<code>python -m venv venv</code> - создаем вируальную среду<br>
<code>source venv/Scripts/activate</code> - активируем среду<br><br>
<code>pip install --upgrade pip</code><br>
<code>pip install -r requirements.txt</code> - устанавливаем зависимости<br><br>
<code>cd app/</code> - переходим в папку проекта
<code>python main.py</code> - запускаем сервер
<br>
<br>
Теперь приложение доступно по адресу:<br><br>
<code>http://localhost:8000/</code> - само приложение <br>
<code>http://localhost:8000/docs</code> - ссылка на документацию <br>

Дополнительно в файле <code>constants.py</code> можно установить время начала и завершения дня, а также интервал для <code>/next_taking</code>