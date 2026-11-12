# API-тести геодезичного кабінету

Тести веб-застосунку Google Apps Script (pytest + requests).
Номери тестів T01–T12 збігаються з колонкою ID у `api_tests.xlsx`.
Потрібен Python 3.

## Запуск в один клік

Скрипт сам створює `.venv`, ставить залежності з `requirements.txt` і запускає всі тести.

- Windows: двічі клацнути `run.bat`
- Linux: у папці проєкту виконати

      chmod +x run.sh    # потрібно один раз
      ./run.sh

## Ручний запуск

Linux:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest -v

Windows (cmd):

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pytest -v

Windows (PowerShell):

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    pytest -v

Віртуальне середовище створюється один раз. Надалі достатньо активувати його і запускати `pytest -v`.

## Запуск окремих тестів

    pytest -m T04            # один тест за номером
    pytest -m "T04 or T05"   # кілька

З одним кліком: `./run.sh -m T04` або `run.bat -m T04`.

## Налаштування

URL веб-застосунку (`/exec`) задається в `config.py`.
