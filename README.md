# SBER NER Pipeline

**Описание проекта**

Этот репозиторий содержит реализацию конвейера для задачи извлечения именованных сущностей (NER) на русском языке с использованием LLM (GigaChat) и собственных скриптов оценки качества.

**Основные шаги**

1. **Загрузка данных**

   * Аннотации (\*.out) загружаются функцией `load_annotations` из `src/data_loader.py`.
   * Тексты (\*.txt) загружаются функцией `load_texts`.
2. **Генерация предсказаний**

   * Сформированы промпты в `src/prompt.py`.
   * Ручной прогон через GigaChat, ответы собираются в `data/predictions/predictions.csv`.
3. **Оценка качества**

   * Метрика F1 реализована в `src/metrics.py`, покрыта unit‑тестами `tests/test_metrics.py`.
   * Слияние `gold.csv` и `predictions.csv` и расчёт F1 в ноутбуке `notebooks/solution.ipynb`.
4. **Анализ**

   * Группировка результатов по типам сущностей и документам.
   * Зависимость качества от длины документа.
   * Ошибки FP/FN и рекомендации по их сокращению.

**Структура репозитория**

```
├── data/
│   ├── annotations/
│   │   └── gold.csv         # золотая разметка
│   ├── raw/                # исходные тексты и .out файлы
│   └── predictions/        # результаты GigaChat
│       └── predictions.csv
├── notebooks/
│   └── solution.ipynb      # аналитический ноутбук
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # загрузка данных
│   ├── prompt.py           # генерация промптов
│   └── metrics.py          # реализация F1
├── tests/
│   └── test_metrics.py     # unit‑тесты метрики
│   └── conftest.py         # для import functions
├── .gitignore
├── requirements.txt
└── README.md
```

**Установка**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**Использование**

1. Запустить загрузку и сохранение gold.csv:

   ```bash
   jupyter notebook notebooks/solution.ipynb
   ```
2. Сформировать promts и вручную получить `predictions.csv`.
3. Выполнить ячейки в ноутбуке для расчёта F1 и анализа.

---

