# Тестирование калькулятора с задержкой

Проект содержит автоматизированные тесты для веб-калькулятора с задержкой выполнения операций.

## Зависимости
- Python 3.8+
- pip
- Chrome браузер

## Установка
1. Клонировать репозиторий
2. Установить зависимости:
```bash
pip install -r requirements.txt
```

## Запуск тестов
Для запуска тестов с генерацией Allure отчета:
```bash
pytest --alluredir=allure-results
```

## Просмотр отчета
1. Установить Allure: https://docs.qameta.io/allure/#_installing_a_commandline
2. Запустить сервер отчетов:
```bash
allure serve allure-results
```

## Структура проекта
- `Calculator/CalculatorPage.py` - Page Object модель калькулятора
- `Calculator/test_calculator.py` - тесты калькулятора
- `allure-results/` - директория с результатами тестов (не включена в репозиторий)
