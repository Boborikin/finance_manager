# Менеджер учёта расходов

## Запуск
<details>
<summary>Локальный запуск</summary>

### Запуск API 

**Создание виртуального окружения**
```sh
python3 -m venv venv
```
**Активация виртуального окружения**
```sh
source venv/bin/activate
```
**Установка необходимых зависимостей**
```sh
pip install -r requirements.txt
```
**Инициализация необходимых переменных окружения(1)**
```shell
export DJANGO_ALLOWED_HOSTS="127.0.0.1"
export SECRET_KEY=foo
export DEBUG=1
```
**Запуск миграции**
```sh
python3 app/manage.py migrate
```
**Запуск проекта**
```shell
python3 app/manage.py runserver
```
**Проект доступен по ссылке ниже:**
```text
http://127.0.0.1:8000/
```
### Запуск рассылки
**В отдельном окне терминала запустите redis**
```shell
redis-server
```
**В другом окне терминала перейдите в папку app**
```shell
cd app
```
**Проведите инициализацию необходимых переменных окружения
1 и 2 и запустите celery worker**
```shell
celery -A mail worker -l info
```
**Создать другое новое окно, перейти в папку app выполнить
инициализацию переменных 1 и 2. Запустить celery beat**
```shell
celery -A mail beat -l info
```
**Инициализация необходимых 
переменных окружения(2)**
```shell
export EMAIL_HOST=""
export EMAIL_HOST_USER=""
export EMAIL_HOST_PASSWORD=""
export EMAIL_PORT=465
export CELERY_BROKER_URL=""
```

</details>
<details>
<summary>Docker контейнер</summary>

**Скопировать данные из файла <i>.env.example</i> в файл <i>.env</i> и изменить данные на ваши**

**Для сборки и запуска**
```shell
docker-compose up -d 
```

**Проект доступен по ссылке ниже:**
```text
http://localhost:8000/
```
</details>

---

## Методы API

**Регистрация пользователя**
```shell
curl -X POST 'http://127.0.0.1:8000/auth/register/'\
   -H 'Content-Type: application/json' \
   -d '{"username":"<username>","password":"<password>","password_again":"<password>",
"email":"<email>","first_name":"<first_name>","last_name":"<last_name>"}'
```
**Вход пользователя**
```shell
curl -X POST 'http://127.0.0.1:8000/auth/login/'\
   -H 'Content-Type: application/json' \
   -d '{"username":"<username>","password":"<password>"}'
```
**Вернется значение <i>access</i>**.
**Данное access значение используется для получения/изменения/создания данных**

**Получение текущего баланса**
```shell
curl -X GET 'http://127.0.0.1:8000/api/v1/balance/' -H 'Authorization: Bearer <access>'
```

**Получение статистики**
```shell
curl -X GET 'http://127.0.0.1:8000/api/v1/balance/' -H 'Authorization: Bearer <access>'
```

**Получение ваших категорий**
```shell
curl -X GET 'http://127.0.0.1:8000/api/v1/categories/' -H 'Authorization: Bearer <access>'
```
**Список транзакций с сортировкой по убыванию даты создания**
```shell
curl -X GET 'http://127.0.0.1:8000/api/v1/transactions/?ordering=-created' -H 'Authorization: Bearer <access>'
```
Доступные варианты сортировки:<br>
`ordering=created` - по возрастанию<br>
`ordering=-created` - по убыванию<br>
`ordering=amount` - сумма по возрастанию<br>
`ordering=-amount` - сумма по убыванию<br>
Доступные варианты фильтрации:<br>
`created=04.10.2022`  - дата создания<br>
`created_gte=04.10.2022 14:55:01` - дата создания больше или равно<br>
`created_lte=` - дата создания меньше или равно<br>
`created_gt=` - дата создания больше чем<br>
`created_lt=` - дата создания меньше чем<br>
`amount=1` - Сумма равная<br>
`amount_gte=` - Сумма больше или равна<br>
`amount_lte=` - Сумма меньше или равна<br>
`amount_gt=` - Сумма больше чем<br>
`amount_lt=` - Сумма меньше чем<br>

### Для удобства тестирования и просмотра всего перечня функций

---

Мною была добавление документация с помощью <a href="https://github.com/axnsan12/drf-yasg">drf-yasg</a>.

Доступно как <a href="http://127.0.0.1:8000/swagger"><b>Swagger</b></a>, так и <a href="http://127.0.0.1:8000/redoc"><b>Redoc</b></a> документация.