# ShopAPI

[![N|Solid](https://netology.ru/images2/logo_b.png)](https://netology.ru/)

### Установка
 - Скопировать репозиторий
 - Установить библиотеки из requirements.txt
 - Задать переменные окружения

### Переменные окружения
- Создайте в папке .../api файл .env
В файле укажите настройки сетевого окружения для доступа к конфиденциальной информации:
- EMAIL_HOST = {адрес smtp-сервера}
- EMAIL_HOST_USER = {логин}
- EMAIL_HOST_PASSWORD = {пароль}
Убедитесь, что в settings.py прописаны следующие настройки
- EMAIL_HOST = os.getenv('EMAIL_HOST')
- EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
- EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

### Доступ к панели администратора
http://{your_host}/admin/

### Описание методов
Доступно в приложенной коллекции Postman