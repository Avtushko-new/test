# Тестирование интернет-магазина

Проект содержит автоматизированные тесты для интернет-магазина.

## Зависимости
- Python 3.8+
- pip
- Chrome браузер

## Установка
```bash
pip install -r requirements.txt
```

## Запуск тестов
Для запуска тестов с генерацией Allure отчета:
```bash
pytest InternetShop/test_shopping.py --alluredir=allure-results
```

## Просмотр отчета
1. Установите Allure: https://docs.qameta.io/allure/#_installing_a_commandline
2. Запустите сервер отчетов:
```bash
allure serve allure-results
```

## Структура проекта
- `InternetShop/pages/` - Page Object модели
- `InternetShop/test_shopping.py` - тесты
- `allure-results/` - результаты тестов (не включено в репозиторий)
