# Менеджер учёта расходов

<details>
<summary>Задание</summary>
Минимальные требования:   
- Регистрация пользователя   
- Авторизация пользователя (по токену)   
- Транзакции пользователя - CRUD
С помощью транзакций происходит списание, начисление баланса пользователя.
Транзакция должна содержать в себе: сумму\*, время\*, категорию\*, организацию\*, описание.
Пользователь должен иметь возможность сортировать, фильтровать транзакции по времени, сумме, дате.
   
- Категории пользователя - CRUD
При регистрации пользователь получает набор стандартных категорий:
"Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование", "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд".
Пользователь может изменять/удалять стандартные категории как пожелает, а также создавать свои.   
- Просмотр профиля пользователя (информация о текущем балансе)   
- Статистика пользователя.
Реализовать отправку статистики на почту пользователя утром каждый день.
Объём получаемой статистики можете выбрать сами.   
</details>

# Проверка

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
EMAIL_HOST=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_PORT=465
CELERY_BROKER_URL=""
```

</details>
<details>
<summary>Docker контейнер</summary>

**Укажите необходимые переменные окружения в файле .env.dev**

**Запуск сборки docker контейнера**
```shell
docker-compose build
```
**По завершению сборки контейнера, нужно его запустить**
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
curl -X POST 'http://127.0.0.1/auth/register/' \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=<username>' \
--data-urlencode 'password=<password>' \
--data-urlencode 'password2=<password2>' \
--data-urlencode 'email=<email>' \
--data-urlencode 'first_name=<first_name>' \
--data-urlencode 'last_name=<last_name>'
```
**Вход пользователя**
```shell
curl -X POST 'https://shrouded-ravine-45950.herokuapp.com/auth/login/' \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=postman' \
--data-urlencode 'password=string123'
```
**Если все хорошо, вернется значение <i>access</i>**
**Данное access значение используется для получения/изменения/создания данных**

**Получение текущего баланса**
```shell
curl -X GET 'https://http://127.0.0.1/api/v1/balance/' -H 'Authorization: Bearer <access>'
```

**Получение статистики**
```shell
curl -X GET 'https://http://127.0.0.1/api/v1/balance/' -H 'Authorization: Bearer <access>'
```

**Получение ваших категорий**
```shell
curl -X GET 'https://http://127.0.0.1/api/v1/categories/' -H 'Authorization: Bearer <access>'
```
**Список транзакций с сортировкой по убыванию даты создания**
```shell
curl -X GET 'https://http://127.0.0.1/api/v1/categories/?ordering=-created' -H 'Authorization: Bearer <access>'
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