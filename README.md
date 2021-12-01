# Тестовое задание для Fabrique V

## Быстрый запуск:
```
pip install -r requirements.txt
cd fabrique_v_test_task
python manage.pu runserver
```

API можно использовать через Swagger UI (http://127.0.0.1:8000/swagger/). Некоторые ручки имеют описание + к тому, что
автосгенерил Swagger. Ручки, связанные с юзером пытаются найти такого в БД, и, если неудачно, создают нового.

## TODO:
- не прикручены пермишны
- больше статистик в /user-stats подобавлять
- вынести settings в env vars
- прикрутить БД не sqlite