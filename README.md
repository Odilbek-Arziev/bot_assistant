# Телеграм-бот на Python

Зависимости
-----------
1.	Python 3 
2.	Django последней версии
3.	Ngrok – можете установить и почитать документацию по [ссылке](https://ngrok.com/download) 
4. 	Psycopg2 (2.8.6)


Установка
-----------
 1. Запустите команду:
 * http - `pip install git+https://github.com/mondaylabs/botmother.git@v1.2.2`
 * ssh  - `pip install git+ssh://git@github.com/mondaylabs/botmother.git@v1.2.2`

Библиотека установлена, идем дальше.

2. Откройте файл `settings.py` и добавьте в `INSTALLED_APPS` название библиотеки и вашего приложения:
```python
INSTALLED_APPS = [
    ...
    'botmother',
    'имя_вашего_приложения'
]
```

3. Создайте нового бота с помощью [BotFather]( @BotFather). Скопируйте токен созданного бота и задайте его в переменной `BOT_TOKEN` в том же `settings.py`: 
```python
BOT_TOKEN = '1619688226:AAFa1v1nPZXWG97wFdu4W**************'
```
4. Также, добавьте следующее:

```python
	import sys
	...	
	BOTMOTHER_CHAT_MODEL = 'botmother.Chat'
	TESTING = ('test' == sys.argv[1]) if sys.argv else False
```
5.  Далее, для того, чтобы ваш бот правильно работал, вам следует создать модель `Chat` в `models.py`. 
```python
from botmother.models import AbstractChat

class Chat(AbstractChat):
    class Meta(AbstractChat.Meta):
        db_table = '<имя_вашего_приложения>_chats'
```

6. Перейдя в командную строку, пропишите команду `python manage.py makemigrations` и `python manage.py migrate`.
После этого, просто поменяйте `BOTMOTHER_CHAT_MODEL = 'botmother.Chat'` на `BOTMOTHER_CHAT_MODEL = '<название_вашего_приложения>.Chat'`

7. Создайте файл `handlers.py` в папке приложения и напишите свою первую функцию `start`:
```python
def start(chat, *args, **kwargs):
    chat.send_message('Hello, world!')
```

8. Создайте файл `urls.py` в папке вашего приложения так, чтобы у вас получился путь `<имя_вашего_проекта >/<имя_вашего_приложения>/urls.py`, и добавьте функцию `dispatch()`, как показано ниже:
```python
from botmother.webhook import webhook
from django.urls import path
from example.handlers.main import *


def dispatch(router):
    router.command('/start', start),

urlpatterns = [
    path('', webhook(dispatch)),
]
```
Теперь, перейдите в корневой файл urls.py и выполните следующие действия:
```python
urlpatterns = [
    ...
    path('example/', include(('example.urls', 'example'), namespace='example')),
]
```
Вместо `example` вы должны подставить имя своего приложения.

9.	Так же добавьте `ngrok` в `ALLOWED_HOSTS` следующим образом:
```python
ALLOWED_HOSTS = (
    ...
    '.ngrok.io',
)
```

10.	Запустите ngrok командой `ngrok http 8000`.
Но прежде, если у вас Windows, то укажите где находится файл `ngrok.exe` в командной строке. Затем, скопируйте появившуюся ссылку, показанную ниже:

    `Forwarding                    https://82691332ba1f.ngrok.io -> http://localhost:8000`

11. Добавив `/example/webhook` в конец ссылки, запустите `webhook` командой:

    `py manage.py setwebhook https://82691332ba1f.ngrok.io/example/webhook`

12.	Запустите бота командой `py manage.py runserver`.

13.	Проверьте работоспособность своего бота!
