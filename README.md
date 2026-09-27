# Bike Sharing Data Pipeline

Учебный проект по построению простого data pipeline:

**CSV → Python/Pandas → PostgreSQL → SQL/Pandas analysis → Plotly**

Проект использует датасет Bike Sharing с почасовыми данными об аренде велосипедов.

## Стек

- Python
- Pandas
- PostgreSQL
- psycopg
- Jupyter Notebook
- Plotly
- Docker

## Структура проекта

```text
day14_project/
├── data/
│   └── hour.csv
├── src/
│   └── load_to_postgres.py
├── notebooks/
│   └── analysis.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

`data/` не хранится в Git-репозитории. Датасет необходимо скачать отдельно.

## Pipeline

1. CSV загружается через Pandas.
2. Колонка `dteday` преобразуется в datetime.
3. Данные загружаются в PostgreSQL через `psycopg`.
4. Аналитические задачи выполняются параллельно через Pandas и SQL.
5. Основные результаты визуализируются через Plotly.

Исходный датасет содержит **17 379 строк и 17 колонок**.

## PostgreSQL schema

Таблица:

`bicycle_rental`

| Column | PostgreSQL type | Description |
|---|---|---|
| `instant` | `INTEGER PRIMARY KEY` | ID записи |
| `dteday` | `DATE` | Дата |
| `season` | `INTEGER` | Сезон |
| `yr` | `INTEGER` | Год |
| `mnth` | `INTEGER` | Месяц |
| `hr` | `INTEGER` | Час суток |
| `holiday` | `INTEGER` | Праздничный день |
| `weekday` | `INTEGER` | День недели |
| `workingday` | `INTEGER` | Рабочий день |
| `weathersit` | `INTEGER` | Категория погоды |
| `temp` | `DOUBLE PRECISION` | Нормализованная температура |
| `atemp` | `DOUBLE PRECISION` | Нормализованная ощущаемая температура |
| `hum` | `DOUBLE PRECISION` | Нормализованная влажность |
| `windspeed` | `DOUBLE PRECISION` | Нормализованная скорость ветра |
| `casual` | `INTEGER` | Аренды незарегистрированных пользователей |
| `registered` | `INTEGER` | Аренды зарегистрированных пользователей |
| `cnt` | `INTEGER` | Общее количество аренд |

`cnt = casual + registered`.

## Анализ

В проекте исследуются:

- среднее количество аренд по часам суток;
- различия между рабочими и нерабочими днями;
- среднее количество аренд по сезонам;
- топ-5 дат по общему количеству аренд;
- пиковый час для каждого сезона;
- день недели с максимальным средним количеством аренд для каждого сезона среди рабочих дней.

Более сложные SQL-запросы используют CTE и оконную функцию `ROW_NUMBER()`.

Аналогичные задачи выполняются через Pandas с использованием `groupby`, агрегатных функций, сортировки и `idxmax()`.

## Визуализация

Через Plotly построены графики:

- среднего количества аренд по часам суток;
- среднего количества аренд по сезонам;
- топ-5 дат по общему количеству аренд.

## Запуск

Создать виртуальное окружение и установить зависимости:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Запустить PostgreSQL и создать базу данных и таблицу `bicycle_rental`.

После настройки подключения выполнить загрузку данных:

```bash
python src/load_to_postgres.py
```

Анализ находится в:

```text
notebooks/analysis.ipynb
```

## Dataset

Bike Sharing Dataset:

https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset

Для проекта используется файл `hour.csv`.
```
