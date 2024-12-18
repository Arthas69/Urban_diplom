# Анализ и сравнение написания web-приложений с использованием разных фреймворков (Django, Flask и FastAPI) и их сравнение.
Любое web-приложение, создаваемое в настоящее время, состоит из множества технологий. Каждая из этих технологий реализует одну из частей проекта: frontend - внешняя(визуальная) оболочка приложения, backend - серверная часть и специальное api для взаимодействия между ними.
Так как backend часть является основным элементом, в котором реализуются все логические и бизнес процессы, выбор средства разработки является существенной частью web-разработки.
Для разработки backend составляющей приложений используются фреймворки - это специальные библиотеки, для реализации подобного рода задач.
Основными фреймворками на Python, используемыми сегодня, являются **Django**, **Flask** и **FastAPI**.
Их особенности, плюсы и минусы, а также сравним их по нескольким ключевым аспектам.


## Практическое задание
Нам предлагается сделать три проекта на трех разных фреймворках для их сравнения.
Мною были выбраны следующие варианты простых проектов на каждый из этих фреймворков:


### Приложение на Django
Приложение-библиотека. Пользователи могут найти интересующую их книгу или автора, почитать описание и оставить отзыв

#### Структура проекта
Структура проекта состоит из следующих элементов
#### Домашняя страница
Сюда выводится 4 случайных книги из базы данных На каждую книгу представлена своя карточка. Пользователь может зайти и подробнее посмотреть про книгу или автора, нажав на ссылки
![main.png](images%2Fdjango%2Fmain.png)

#### Страница авторизации
Здесь пользователи могут зайти в учётную запись. Если её нет – создать (Register – перенаправляет на форму регистрации).
![login.png](images%2Fdjango%2Flogin.png)
![register.png](images%2Fdjango%2Fregister.png)

#### Страница с информацией об авторе
На этой странице присутствует короткая информация об авторе, а также список его книг
![author.png](images%2Fdjango%2Fauthor.png)

#### Страница с информацией о книге
На этой странице есть короткая информация о книге, а также пользователь может посмотреть все отзывы, которые есть об этой книге или, авторизовавшись, оставить свой. 
![book.png](images%2Fdjango%2Fbook.png)

#### Шаблоны страниц
base.html – базовый шаблон, подключающий Bootstrap. Является основой для всех остальных страниц 
index.html – домашняя страница
book.html – Шаблон с информацией о книге
author.html – Шаблон с информацией об авторе
menu.html – Навигационная панель, подключается к базовому шаблону и появляется на всех страницах
login.html – вход в учётную запись
registration.html – создание учётной записи

#### Приложение: Файловая структура проекта
![tree.png](images%2Fdjango%2Ftree.png)

#### Приложение: Запуск проекта
1. Перейдите в директорию с проектом
![first.png](images%2Fdjango%2Ffirst.png)
2. Создайте виртуальное окружение
![second.png](images%2Fdjango%2Fsecond.png)
3. Запустите его
Для Linux:
![third.png](images%2Fdjango%2Fthird.png)
Для Windows:
![third_win.png](images%2Fdjango%2Fthird_win.png)
4. Установите зависимости
![fourth.png](images%2Fdjango%2Ffourth.png)
5. Сделайте миграцию базы данных
![mig_1.png](images%2Fdjango%2Fmig_1.png)
![mig_2.png](images%2Fdjango%2Fmig_2.png)
6. Запустите проект
![start.png](images%2Fdjango%2Fstart.png)
7. Перейдите на страницу по адресу внизу
![url.png](images%2Fdjango%2Furl.png)

#### Приложение: requirements.txt
```
asgiref==3.8.1
Django==5.1.3
psycopg2==2.9.10
sqlparse==0.5.2
```


### Приложение на Flask
Приложение для просмотра погоды. Пользователь может, введя название города в строке поиска, найти интересующий его город, и узнать в нем погоду. Так же может сохранить его, для того, чтобы в будущем узнать информацию, просто зайдя на свою страницу

#### Структура проекта
Структура проекта состоит из следующих элементов
#### Домашняя страница
Страница на которой есть возможность ввести название интересующего города, и увидеть все найденные города
![main.png](images%2Fflask%2Fmain.png)
![main_found.png](images%2Fflask%2Fmain_found.png)

#### Страница авторизации
Здесь пользователи могут зайти в учётную запись. Если её нет – создать (Register – перенаправляет на форму регистрации).
![login.png](images%2Fflask%2Flogin.png)
![register.png](images%2Fflask%2Fregister.png)

#### Страница с информацией о погоде в городе
Здесь есть основная информация о погоде в городе - температуре, влажности и облачности. Так же, пользователь может запомнить город, нажав на соответствующую кнопку
![city.png](images%2Fflask%2Fcity.png)
![city_2.png](images%2Fflask%2Fcity_2.png)

#### Страница с информацией о запомненных городах
На этой странице указаны все города сохраненные пользователем. Так же есть возможность перестать их отслеживать, просто нажав на соответствующую кнопку
![saved.png](images%2Fflask%2Fsaved.png)

#### Шаблоны страниц
base.html – базовый шаблон, подключающий Bootstrap. Является основой для всех остальных страниц 
all_cities.html - Домашняя страница
city.html – Шаблон с информацией о городе
my_cities.html – Шаблон с информацией городах сохраненных пользователем
menu.html – Навигационная панель, подключается к базовому шаблону и появляется на всех страницах
edit_profile.html - Шаблон для редактирования данных пользователя
users.html - Шаблон с информацией о пользователе
login.html – вход в учётную запись
registration.html – создание учётной записи

#### Приложение: Файловая структура проекта
![tree.png](images%2Fflask%2Ftree.png)

#### Приложение: Запуск проекта
1. Перейдите в директорию с проектом
![start.png](images%2Fflask%2Fstart.png)
2. Создайте виртуальное окружение
![second.png](images%2Fdjango%2Fsecond.png)
3. Запустите его
Для Linux:
![third.png](images%2Fdjango%2Fthird.png)
Для Windows:
![third_win.png](images%2Fdjango%2Fthird_win.png)
4. Установите зависимости
![fourth.png](images%2Fdjango%2Ffourth.png)
5. Сделайте миграцию базы данных
![mig_1.png](images%2Fflask%2Fmig_1.png)
![mig_2.png](images%2Fflask%2Fmig_2.png)
6. Запустите проект
![run.png](images%2Fflask%2Frun.png)

#### Приложение: requirements.txt
```
alembic==1.14.0
blinker==1.9.0
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
dnspython==2.7.0
email_validator==2.2.0
Flask==3.1.0
Flask-Login==0.6.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.6
MarkupSafe==3.0.2
psycopg2==2.9.10
requests==2.32.3
setuptools==75.6.0
SQLAlchemy==2.0.36
SQLAlchemy-Utils==0.41.2
typing_extensions==4.12.2
urllib3==2.2.3
Werkzeug==3.1.3
WTForms==3.2.1
```


### Приложение на FastAPI
Приложение по созданию и ведению заметок

#### Структура проекта
Структура проекта состоит из следующих элементов
#### Домашняя страница
Страница показывающая все возможные роуты
![main.png](images%2Ffastapi%2Fmain.png)
#### Страница авторизации
Регистрация:
![register.png](images%2Ffastapi%2Fregister.png)
Авторизация:
![login.png](images%2Ffastapi%2Flogin.png)
Авторизация с OAuth:
![authorization.png](images%2Ffastapi%2Fauthorization.png)
#### CRUD для событий
Создание события:
![event_create.png](images%2Ffastapi%2Fevent_create.png)
Список всех событий текущего пользователя:
![events_get.png](images%2Ffastapi%2Fevents_get.png)
Изменение события:
![event_update.png](images%2Ffastapi%2Fevent_update.png)
Удаление события:
![event_delete.png](images%2Ffastapi%2Fevent_delete.png)
#### Страница с информацией о пользователе
Вариант если авторизация пройдена успешно и пользователь запросил доступ к странице
![info_about_user_ok.png](images%2Ffastapi%2Finfo_about_user_ok.png)
Вариант без авторизации:
![info_about_user_fail.png](images%2Ffastapi%2Finfo_about_user_fail.png)

#### Приложение: Файловая структура проекта
![tree.png](images%2Ffastapi%2Ftree.png)

#### Приложение: Запуск проекта
1. Перейдите в директорию с проектом
![first.png](images%2Ffastapi%2Ffirst.png)
2. Создайте виртуальное окружение
![second.png](images%2Fdjango%2Fsecond.png)
3. Запустите его
Для Linux:
![third.png](images%2Fdjango%2Fthird.png)
Для Windows:
![third_win.png](images%2Fdjango%2Fthird_win.png)
4. Установите зависимости
![fourth.png](images%2Fdjango%2Ffourth.png)
5. Сделайте миграцию базы данных
![mig.png](images%2Ffastapi%2Fmig.png)
6. Запустите проект
![start.png](images%2Ffastapi%2Fstart.png)

#### Приложение: requirements.txt
```
alembic==1.14.0
annotated-types==0.7.0
anyio==4.6.2.post1
argon2-cffi==23.1.0
argon2-cffi-bindings==21.2.0
bcrypt==4.2.1
cffi==1.17.1
click==8.1.7
cryptography==44.0.0
dnspython==2.7.0
email_validator==2.2.0
fastapi==0.115.5
fastapi-users==14.0.0
fastapi-users-db-sqlalchemy==6.0.1
greenlet==3.1.1
h11==0.14.0
idna==3.10
Jinja2==3.1.4
makefun==1.15.6
Mako==1.3.6
MarkupSafe==3.0.2
passlib==1.7.4
psycopg2==2.9.10
pwdlib==0.2.1
pycparser==2.22
pydantic==2.10.2
pydantic_core==2.27.1
PyJWT==2.9.0
python-multipart==0.0.17
sniffio==1.3.1
SQLAlchemy==2.0.36
starlette==0.41.3
typing_extensions==4.12.2
uvicorn==0.32.1
```




### 1. **Django**

#### Описание:
[Django] – это мощный Python-фреймворк для разработки веб-приложений. Это бесплатная платформа веб-разработки с открытым исходным кодом. Он создан по шаблону Model-Template-View, и популярен благодаря своей надежности, хорошей документации и большому количеству обучающей информации. Джанго предоставляет разработчикам огромный выбор готовых модулей, надстроек и инструментов, которые значительно ускоряют и упрощают процесс создания сложных, многофункциональных веб-приложений. 



#### Преимущества:
- **Эффективная структура кода**: Позволяет разработчикам добавлять большое количество функций на свои веб-сайты
- **Масштабируемость и производительность**: Хотя Django ориентирован на более крупные проекты, его можно масштабировать и для больших приложений.
- **Безопасность**: Django предоставляет множество встроенных инструментов безопасности (например, защиту от Cross-Site Request Forgery (CSRF), Cross-Site Scripting (XSS), SQL-инъекций).
- **Много компонентов**: Аутентификация, авторизации, удобная админ панель, встроенный шаблонизатор и многое другое. В Django есть все необходимые компоненты для создания полноценного веб-приложения
- **Документация**: Django имеет отличную документацию, что облегчает обучение и решение проблем.

#### Недостатки:
- **Гибкость**: Django имеет жесткую архитектуру приложения, что может ограничить гибкость при разработке некоторых решений.
- **Производительность**: По сравнению с более легкими фреймворками, Django может быть менее производительным, особенно при работе с небольшими приложениями.
- **Скорость**: По сравнению с более легковесными фреймворками, Джанго может быть более медлительным из-за большого количества встроенных в него компонентов.

Используется зачастую для крупных и сложных проектов, таких как интернет-магазины, блоги, социальные сети.

---

### 2. **Flask**

#### Описание:
[Flask] — это минималистичный фреймворк, который предоставляет только основы для создания web-приложений. В нем нет такого количества встроенных компонентов, как в Django, но присутствует большое количество сторонних библиотек, что позволяет эффективно подключать необходимые инструменты, для каждого конкретного проекта.

#### Преимущества:
- **Гибкость**: Flask предоставляет гораздо больше свободы, чем Django. Выбор используемых компонентов остается за вами!
- **Легковесность**: Flask Легче в освоении и старте, имеет меньший объем кода, что делает его хорошим выбором для небольших проектов и API.
- **Простота**: Отлично подходит для небольших проектов или микросервисов, так как он не накладывает строгие ограничения на структуру приложения. Благодаря своей простоте, это идеальный фреймворк для начинающих.
- **Много сторонних расширений**: Хотя Flask сам по себе микро-фреймворком, объем компонентов доступных к подключению очень обширен (например, Flask-SQLAlchemy, Flask-WTF, Flask-Login), и позволяет покрыть большинство требований при создании проекта.

#### Недостатки:
- **Асинхронность**: Отсутствует асинхронная обработка запросов
- **Не подходит для больших проектов**: Flask не предоставляет столько инструментов для масштабируемых решений, как Django. Это может потребовать большего времени на разработку и поддержку в крупных проектах.
- **Безопасность**: Из-за того, что Flask включает в себя внешние модули, в перспективе возможно проблемы с обеспечением безопасности приложения.

Flask идеально подходит для небольших веб-приложений, API, микросервисов, сайтов-визиток.

---

### 3. **FastAPI**

#### Описание:
[FastAPI] — это современный, высокопроизводительный фреймворк для создания веб-API. Он использует асинхронные возможности Python (через `asyncio`).

#### Преимущества:
- **Производительность**: FastAPI очень быстрый благодаря использованию асинхронного программирования. Это один из самых быстрых фреймворков для Python.
- **Автоматическая генерация документации**: FastAPI автоматически генерирует документацию API с помощью OpenAPI и Swagger UI.
- **Асинхронность**: FastAPI отлично работает с асинхронными операциями, что делает его идеальным выбором для приложений, которые нуждаются в высоком уровне параллельности (например, чат-приложения или приложения для обработки большого количества запросов).
- **Типизация и проверка данных**: Благодаря использованию Pydantic для валидации и аннотации типов, FastAPI обеспечивает более строгую проверку данных и их автоматическую обработку, даже в глубоко вложенных запросах

#### Недостатки:
- **Менее подходящий для традиционных веб-приложений**: Хотя FastAPI идеально подходит для API, реализация инструментов для рендеринга HTML слабо развита, что делает его менее подходящим для стандартных веб-приложений.
- **Новизна**: Из-за того, что FastAPI является относительно новых фреймворком, им пользуются еще не такое большое количество разработчиков, и, несмотря на достаточно подробную документацию, внешних образовательных материалов не так много 

#### Применение:
- FastAPI идеально подходит для создания RESTful API, микросервисов, веб-сервисов с высокой нагрузкой.

---

### Сравнение фреймворков: Django, Flask, FastAPI

| Характеристика           | **Django**                                      | **Flask**                                  | **FastAPI**                               |
|--------------------------|-------------------------------------------------|--------------------------------------------|-------------------------------------------|
| **Тип**                  | Полноценный фреймворк для крупных и масштабируемых приложений | Легковесный фреймворк для API и микросервисов | API-фреймворк, ориентированный на скорость |
| **Производительность**    | Медленный, по сравнению с другими               | Средняя производительность                 | Очень высокая производительность          |
| **Гибкость**              | Менее гибкий, чем Flask и FastAPI               | Очень гибкий, подходит для небольших проектов | Очень гибкий, особенно для микросервисов  |
| **Документация и обучение** | Много материалов, но сложен в освоении          | Много информации, более прост в освоении   | Простой, но меньше доступных материалов   |
| **Работа**                | Больше вакансий, популярность среди работодателей | Меньше вакансий, но все еще актуален       | Наименьшее количество вакансий, но растет популярность |

### Заключение

- **Django** — лучший выбор для крупных, монолитных приложений, где важна скорость разработки и наличие множества встроенных функций. Он подходит для проектов с классической архитектурой, где необходима админка, система аутентификации и другие стандартные компоненты.
  
- **Flask** — идеален для небольших проектов или когда требуется полная гибкость. Он лучше всего подходит для микросервисов, прототипов и API, где важна минималистичность и скорость разработки.
  
- **FastAPI** — лучший выбор для создания высокопроизводительных API и микросервисов, особенно если в проекте используются асинхронные операции. FastAPI превосходит Flask и Django по производительности при работе с API.





[Django]: <https://www.djangoproject.com/>
[Flask]: <https://flask.palletsprojects.com/en/stable/>
[FastAPI]: <https://fastapi.tiangolo.com/>

